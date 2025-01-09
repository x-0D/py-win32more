import importlib
import weakref
import xml.etree.ElementTree as ET
from functools import partial
from pathlib import Path
from tempfile import NamedTemporaryFile

from win32more import FAILED, WinError, asyncui
from win32more._winrt import ComClass, WinRT_String, event_setter
from win32more.mddbootstrap import (
    WINDOWSAPPSDK_RELEASE_MAJORMINOR,
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64,
    MddBootstrapInitialize2,
    MddBootstrapInitializeOptions_OnNoMatch_ShowUI,
    MddBootstrapShutdown,
)
from win32more.Microsoft.UI.Xaml import Application, FrameworkElement, IApplicationOverrides, Window
from win32more.Microsoft.UI.Xaml.Markup import IComponentConnector, IXamlMetadataProvider, IXamlType, XamlReader
from win32more.Microsoft.UI.Xaml.XamlTypeInfo import XamlControlsXamlMetaDataProvider
from win32more.Windows.Foundation import Uri
from win32more.Windows.UI.Xaml.Interop import TypeName
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.Com import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize
from win32more.Windows.Win32.UI.HiDpi import DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2, SetProcessDpiAwarenessContext
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer

XMLNS_XAML = "http://schemas.microsoft.com/winfx/2006/xaml"
XMLNS_XAML_PRESENTATION = "http://schemas.microsoft.com/winfx/2006/xaml/presentation"

# FIXME: register_namespace() is global.
# This is required to prevent "ns0:" prefix for default namespace.
ET.register_namespace("", XMLNS_XAML_PRESENTATION)


class XamlApplication(ComClass, Application, IApplicationOverrides, IXamlMetadataProvider):
    def __init__(self):
        XamlApplication.__current = self
        self._provider = None
        super().__init__(own=True)
        self.InitializeComponent()

    def InitializeComponent(self):
        xaml_path = Path(__file__).with_name("app.xaml").as_posix()
        resource_locator = Uri(f"ms-appx:///{xaml_path}")
        Application.LoadComponent(self, resource_locator)

    def OnLaunched(self, args):
        # You should override this in your derived class
        ...

    def GetXamlType(self, type):
        return self.AppProvider().GetXamlType(type)

    # TODO: Is it needed to provide information for primitive or winui type?
    def GetXamlTypeByFullName(self, fullName):
        return self.AppProvider().GetXamlTypeByFullName(fullName)

    def GetXmlnsDefinitions(self):
        return self.AppProvider().GetXmlnsDefinitions()

    def AppProvider(self):
        if self._provider is None:
            self._provider = XamlControlsXamlMetaDataProvider()
        return self._provider

    __current = None

    @classmethod
    def Start(cls, init):
        r = SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)
        if not r:
            raise WinError()

        hr = CoInitializeEx(None, COINIT_APARTMENTTHREADED)
        if FAILED(hr):
            raise WinError(hr)

        hr = MddBootstrapInitialize2(
            WINDOWSAPPSDK_RELEASE_MAJORMINOR,
            WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
            PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64),
            MddBootstrapInitializeOptions_OnNoMatch_ShowUI,
        )
        if FAILED(hr):
            raise WinError(hr)

        with asyncui.HandCrankRunner() as runner:
            SetTimer(0, 0, 100, lambda *_: runner.update())
            Application.Start(lambda params: init())

        # FIXME: force Release() to avoid exit with error code.
        if XamlApplication.__current is not None:
            XamlApplication.__current.Release()

        MddBootstrapShutdown()

        CoUninitialize()


class XamlClass(ComClass, IComponentConnector):
    def __init__(self, *args, own=True, **kwargs):
        super().__init__(*args, own=own, **kwargs)
        self.__component_connector = None

    def Connect(self, connectionId, target):
        self.__component_connector.Connect(connectionId, target)

    def GetBindingConnector(self, connectionId, target):
        return self.__component_connector.GetBindingConnector(connectionId, target)

    def LoadComponentFromFile(self, xaml_path):
        self.LoadComponentFromString(Path(xaml_path).read_text())

    def LoadComponentFromString(self, xaml_str):
        self.__component_connector = XamlComponentConnector(self)
        self.__component_connector.Load(xaml_str)


class XamlComponentConnector:
    def __init__(self, component):
        self._component = component
        self._connectors = {}

    def Connect(self, connectionId, target):
        for connect in self._connectors[connectionId]:
            connect(target)

    def GetBindingConnector(self, connectionId, target):
        return None

    def Load(self, xaml_str):
        xaml_preprocessed = self._preprocess(xaml_str)
        with NamedTemporaryFile(delete_on_close=False) as f:
            f.write(xaml_preprocessed.encode("utf-8"))
            f.close()
            xaml_path = Path(f.name).as_posix()
            resource_locator = Uri(f"ms-appx:///{xaml_path}")
            Application.LoadComponent(self._component, resource_locator)

    def _preprocess(self, xaml_str):
        root = ET.fromstring(xaml_str)
        for i, e in enumerate(root.iter()):
            self._connectors[i] = []
            for k, v in list(e.attrib.items()):
                if k == f"{{{XMLNS_XAML}}}Name":
                    self._connectors[i].append(partial(self._connect_name, v))
                    del e.attrib[k]
                elif hasattr(self._component, v):
                    self._connectors[i].append(partial(self._connect_event, k, v))
                    del e.attrib[k]
            if self._connectors[i]:
                e.attrib[f"{{{XMLNS_XAML}}}ConnectionId"] = str(i)
        return ET.tostring(root, encoding="unicode")

    def _connect_name(self, bind_name, target):
        setattr(self._component, bind_name, as_runtime_class(target))

    def _connect_event(self, event_name, method_name, target):
        event_setter = getattr(as_runtime_class(target), event_name)
        event_setter += getattr(self._component, method_name)


# Load xaml and connect element and event handler to view object.
#
# <Element x:Name="Element1" Clicked="Element1_Clicked" />
#
# to be
#
# view.Element1 = loaded element
# view.Clicked += view.Element1_Clicked
class XamlLoader:
    @classmethod
    def load(cls, view: object, xaml: str) -> object:
        return cls().execute(view, xaml)

    def execute(self, view, xaml):
        xaml = self.preprocess(view, xaml)
        uiroot = as_runtime_class(XamlReader.Load(xaml))

        if isinstance(uiroot, Window):
            framework_element = uiroot.Content.as_(FrameworkElement)
        else:
            framework_element = uiroot.as_(FrameworkElement)

        xmlroot = ET.fromstring(xaml)
        for xmlelement in xmlroot.iter():
            try:
                name = xmlelement.attrib[f"{{{XMLNS_XAML}}}Name"]
            except KeyError:
                name = None

            if xmlelement is xmlroot:
                self.wire_event(view, uiroot, xmlelement)
                if name is not None:
                    setattr(view, name, uiroot)
                continue

            if name is None:
                continue

            uielement = as_runtime_class(framework_element.FindName(name))
            self.wire_event(view, uielement, xmlelement)
            if not name.startswith("__dummy"):
                setattr(view, name, uielement)

        return uiroot

    def preprocess(self, view, xaml):
        xmlroot = ET.fromstring(xaml)
        for i, xmlelement in enumerate(xmlroot.iter()):
            if xmlelement is xmlroot:
                continue
            if f"{{{XMLNS_XAML}}}Name" in xmlelement.attrib:
                continue
            has_event = any(hasattr(view, v) for v in xmlelement.attrib.values())
            if has_event:
                # It seems that xmlelement has event handler without x:Name.
                # Add temporary name.
                xmlelement.attrib[f"{{{XMLNS_XAML}}}Name"] = f"__dummy{i}"
        return ET.tostring(xmlroot, encoding="unicode")

    def wire_event(self, view, uielement, xmlelement):
        for k, v in xmlelement.items():
            if isinstance(getattr(uielement, k, None), event_setter):
                setter = getattr(uielement, k)
                setter += getattr(view, v)


class XamlType(ComClass, IXamlType):
    def __init__(
        self,
        full_name,
        type_kind,
        *,
        base_type=None,
        boxed_type=None,
        content_property=None,
        is_array=False,
        is_bindable=False,
        is_collection=False,
        is_dictionary=False,
        is_markup_extension=False,
        item_type=None,
        key_type=None,
        activate_instance=None,
        add_to_map=None,
        add_to_vector=None,
        create_from_string=None,
    ):
        super().__init__(own=True)
        self._full_name = full_name
        self._type_kind = type_kind
        self._base_type = base_type
        self._boxed_type = boxed_type
        self._content_property = content_property
        self._is_array = is_array
        self._is_bindable = is_bindable
        self._is_collection = is_collection
        self._is_constructible = bool(activate_instance)
        self._is_dictionary = is_dictionary
        self._is_markup_extension = is_markup_extension
        self._item_type = item_type
        self._key_type = key_type
        self._activate_instance = activate_instance
        self._add_to_map = add_to_map
        self._add_to_vector = add_to_vector
        self._create_from_string = create_from_string

    def get_BaseType(self):
        return self._base_type

    def get_BoxedType(self):
        return self._boxed_type

    def get_ContentProperty(self):
        return self._content_property

    def get_FullName(self):
        return self._full_name

    def get_IsArray(self):
        return self._is_array

    def get_IsBindable(self):
        return self._is_bindable

    def get_IsCollection(self):
        return self._is_collection

    def get_IsConstructible(self):
        return self._is_constructible

    def get_IsDictionary(self):
        return self._is_dictionary

    def get_IsMarkupExtension(self):
        return self._is_markup_extension

    def get_ItemType(self):
        return self._item_type

    def get_KeyType(self):
        return self._key_type

    def get_UnderlyingType(self):
        return TypeName(WinRT_String(self._full_name), self._type_kind)

    def ActivateInstance(self):
        if self._activate_instance is None:
            raise NotImplementedError()
        return self._activate_instance()

    def AddToMap(self, instance, key, value):
        if self._add_to_map is None:
            raise NotImplementedError()
        self._add_to_map(instance, key, value)

    def AddToVector(self, instance, value):
        if self._add_to_vector is None:
            raise NotImplementedError()
        self._add_to_vector(instance, value)

    def CreateFromString(self, value):
        if self._boxed_type is not None:
            return self._boxed_type.CreateFromString(value)
        if self._create_from_string is not None:
            return self._create_from_string(value)
        # TODO:
        # return fromStringConverter()
        raise NotImplementedError()

    def GetMember(self, name):
        # TODO:
        raise NotImplementedError()

    def RunInitializer(self):
        pass


def xaml_typename(name, kind):
    hs = WinRT_String(name)
    tn = TypeName(hs, kind)
    weakref.finalize(tn, hs.clear)
    return tn


def as_runtime_class(uielement):
    return uielement.as_(_get_runtime_class(uielement))


def _get_runtime_class(uielement):
    namespace, name = _get_runtime_class_name(uielement).rsplit(".", 1)
    module = importlib.import_module(f"win32more.{namespace}")
    return getattr(module, name)


def _get_runtime_class_name(uielement):
    s = WinRT_String(own=True)
    hr = uielement.GetRuntimeClassName(s)
    if FAILED(hr):
        raise WinError(hr)
    return s.strvalue
