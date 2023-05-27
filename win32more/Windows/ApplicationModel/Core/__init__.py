from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.UI.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AppListEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Core.IAppListEntry
    _classid_ = 'Windows.ApplicationModel.Core.AppListEntry'
    @winrt_mixinmethod
    def get_DisplayInfo(self: win32more.Windows.ApplicationModel.Core.IAppListEntry) -> win32more.Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_mixinmethod
    def LaunchAsync(self: win32more.Windows.ApplicationModel.Core.IAppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.ApplicationModel.Core.IAppListEntry2) -> WinRT_String: ...
    @winrt_mixinmethod
    def LaunchForUserAsync(self: win32more.Windows.ApplicationModel.Core.IAppListEntry3, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AppInfo(self: win32more.Windows.ApplicationModel.Core.IAppListEntry4) -> win32more.Windows.ApplicationModel.AppInfo: ...
    DisplayInfo = property(get_DisplayInfo, None)
    AppUserModelId = property(get_AppUserModelId, None)
    AppInfo = property(get_AppInfo, None)
AppRestartFailureReason = Int32
AppRestartFailureReason_RestartPending: AppRestartFailureReason = 0
AppRestartFailureReason_NotInForeground: AppRestartFailureReason = 1
AppRestartFailureReason_InvalidUser: AppRestartFailureReason = 2
AppRestartFailureReason_Other: AppRestartFailureReason = 3
class _CoreApplication_Meta_(ComPtr.__class__):
    pass
class CoreApplication(ComPtr, metaclass=_CoreApplication_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.CoreApplication'
    @winrt_classmethod
    def CreateNewViewWithViewSource(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication3, viewSource: win32more.Windows.ApplicationModel.Core.IFrameworkViewSource) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def CreateNewViewFromMainView(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication2) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def add_UnhandledErrorDetected(cls: Windows.ApplicationModel.Core.ICoreApplicationUnhandledError, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Core.UnhandledErrorDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UnhandledErrorDetected(cls: Windows.ApplicationModel.Core.ICoreApplicationUnhandledError, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IncrementApplicationUseCount(cls: Windows.ApplicationModel.Core.ICoreApplicationUseCount) -> Void: ...
    @winrt_classmethod
    def DecrementApplicationUseCount(cls: Windows.ApplicationModel.Core.ICoreApplicationUseCount) -> Void: ...
    @winrt_classmethod
    def get_Views(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Core.CoreApplicationView]: ...
    @winrt_classmethod
    def CreateNewView(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication, runtimeType: WinRT_String, entryPoint: WinRT_String) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def get_MainView(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def Exit(cls: Windows.ApplicationModel.Core.ICoreApplicationExit) -> Void: ...
    @winrt_classmethod
    def add_Exiting(cls: Windows.ApplicationModel.Core.ICoreApplicationExit, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Exiting(cls: Windows.ApplicationModel.Core.ICoreApplicationExit, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestRestartAsync(cls: Windows.ApplicationModel.Core.ICoreApplication3, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def RequestRestartForUserAsync(cls: Windows.ApplicationModel.Core.ICoreApplication3, user: win32more.Windows.System.User, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def add_BackgroundActivated(cls: Windows.ApplicationModel.Core.ICoreApplication2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BackgroundActivated(cls: Windows.ApplicationModel.Core.ICoreApplication2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LeavingBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.LeavingBackgroundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LeavingBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_EnteredBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.EnteredBackgroundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EnteredBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def EnablePrelaunch(cls: Windows.ApplicationModel.Core.ICoreApplication2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_Id(cls: Windows.ApplicationModel.Core.ICoreApplication) -> WinRT_String: ...
    @winrt_classmethod
    def add_Suspending(cls: Windows.ApplicationModel.Core.ICoreApplication, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.SuspendingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Suspending(cls: Windows.ApplicationModel.Core.ICoreApplication, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Resuming(cls: Windows.ApplicationModel.Core.ICoreApplication, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Resuming(cls: Windows.ApplicationModel.Core.ICoreApplication, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Properties(cls: Windows.ApplicationModel.Core.ICoreApplication) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_classmethod
    def GetCurrentView(cls: Windows.ApplicationModel.Core.ICoreApplication) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def Run(cls: Windows.ApplicationModel.Core.ICoreApplication, viewSource: win32more.Windows.ApplicationModel.Core.IFrameworkViewSource) -> Void: ...
    @winrt_classmethod
    def RunWithActivationFactories(cls: Windows.ApplicationModel.Core.ICoreApplication, activationFactoryCallback: win32more.Windows.Foundation.IGetActivationFactory) -> Void: ...
    _CoreApplication_Meta_.Views = property(get_Views.__wrapped__, None)
    _CoreApplication_Meta_.MainView = property(get_MainView.__wrapped__, None)
    _CoreApplication_Meta_.Id = property(get_Id.__wrapped__, None)
    _CoreApplication_Meta_.Properties = property(get_Properties.__wrapped__, None)
class CoreApplicationView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Core.ICoreApplicationView
    _classid_ = 'Windows.ApplicationModel.Core.CoreApplicationView'
    @winrt_mixinmethod
    def get_CoreWindow(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView) -> win32more.Windows.UI.Core.CoreWindow: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationView, win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsMain(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHosted(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView2) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_IsComponent(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView3) -> Boolean: ...
    @winrt_mixinmethod
    def get_TitleBar(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView3) -> win32more.Windows.ApplicationModel.Core.CoreApplicationViewTitleBar: ...
    @winrt_mixinmethod
    def add_HostedViewClosing(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationView, win32more.Windows.ApplicationModel.Core.HostedViewClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HostedViewClosing(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView5) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationView6) -> win32more.Windows.System.DispatcherQueue: ...
    CoreWindow = property(get_CoreWindow, None)
    IsMain = property(get_IsMain, None)
    IsHosted = property(get_IsHosted, None)
    Dispatcher = property(get_Dispatcher, None)
    IsComponent = property(get_IsComponent, None)
    TitleBar = property(get_TitleBar, None)
    Properties = property(get_Properties, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
class CoreApplicationViewTitleBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar
    _classid_ = 'Windows.ApplicationModel.Core.CoreApplicationViewTitleBar'
    @winrt_mixinmethod
    def put_ExtendViewIntoTitleBar(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExtendViewIntoTitleBar(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Boolean: ...
    @winrt_mixinmethod
    def get_SystemOverlayLeftInset(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Double: ...
    @winrt_mixinmethod
    def get_SystemOverlayRightInset(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Double: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Double: ...
    @winrt_mixinmethod
    def add_LayoutMetricsChanged(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LayoutMetricsChanged(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsVisible(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsVisibleChanged(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsVisibleChanged(self: win32more.Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExtendViewIntoTitleBar = property(get_ExtendViewIntoTitleBar, put_ExtendViewIntoTitleBar)
    SystemOverlayLeftInset = property(get_SystemOverlayLeftInset, None)
    SystemOverlayRightInset = property(get_SystemOverlayRightInset, None)
    Height = property(get_Height, None)
    IsVisible = property(get_IsVisible, None)
class HostedViewClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Core.IHostedViewClosingEventArgs
    _classid_ = 'Windows.ApplicationModel.Core.HostedViewClosingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Core.IHostedViewClosingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class IAppListEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IAppListEntry'
    _iid_ = Guid('{ef00f07f-2108-490a-877a-8a9f17c25fad}')
    @winrt_commethod(6)
    def get_DisplayInfo(self) -> win32more.Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_commethod(7)
    def LaunchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    DisplayInfo = property(get_DisplayInfo, None)
class IAppListEntry2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IAppListEntry2'
    _iid_ = Guid('{d0a618ad-bf35-42ac-ac06-86eeeb41d04b}')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    AppUserModelId = property(get_AppUserModelId, None)
class IAppListEntry3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IAppListEntry3'
    _iid_ = Guid('{6099f28d-fc32-470a-bc69-4b061a76ef2e}')
    @winrt_commethod(6)
    def LaunchForUserAsync(self, user: win32more.Windows.System.User) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IAppListEntry4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IAppListEntry4'
    _iid_ = Guid('{2a131ed2-56f5-487c-8697-5166f3b33da0}')
    @winrt_commethod(6)
    def get_AppInfo(self) -> win32more.Windows.ApplicationModel.AppInfo: ...
    AppInfo = property(get_AppInfo, None)
class ICoreApplication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplication'
    _iid_ = Guid('{0aacf7a4-5e1d-49df-8034-fb6a68bc5ed1}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_Suspending(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.SuspendingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Suspending(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Resuming(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Resuming(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(12)
    def GetCurrentView(self) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_commethod(13)
    def Run(self, viewSource: win32more.Windows.ApplicationModel.Core.IFrameworkViewSource) -> Void: ...
    @winrt_commethod(14)
    def RunWithActivationFactories(self, activationFactoryCallback: win32more.Windows.Foundation.IGetActivationFactory) -> Void: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class ICoreApplication2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplication2'
    _iid_ = Guid('{998681fb-1ab6-4b7f-be4a-9a0645224c04}')
    @winrt_commethod(6)
    def add_BackgroundActivated(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BackgroundActivated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_LeavingBackground(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.LeavingBackgroundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LeavingBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_EnteredBackground(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.EnteredBackgroundEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_EnteredBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def EnablePrelaunch(self, value: Boolean) -> Void: ...
class ICoreApplication3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplication3'
    _iid_ = Guid('{feec0d39-598b-4507-8a67-772632580a57}')
    @winrt_commethod(6)
    def RequestRestartAsync(self, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_commethod(7)
    def RequestRestartForUserAsync(self, user: win32more.Windows.System.User, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
class ICoreApplicationExit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationExit'
    _iid_ = Guid('{cf86461d-261e-4b72-9acd-44ed2ace6a29}')
    @winrt_commethod(6)
    def Exit(self) -> Void: ...
    @winrt_commethod(7)
    def add_Exiting(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Exiting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreApplicationUnhandledError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationUnhandledError'
    _iid_ = Guid('{f0e24ab0-dd09-42e1-b0bc-e0e131f78d7e}')
    @winrt_commethod(6)
    def add_UnhandledErrorDetected(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Core.UnhandledErrorDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UnhandledErrorDetected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreApplicationUseCount(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationUseCount'
    _iid_ = Guid('{518dc408-c077-475b-809e-0bc0c57e4b74}')
    @winrt_commethod(6)
    def IncrementApplicationUseCount(self) -> Void: ...
    @winrt_commethod(7)
    def DecrementApplicationUseCount(self) -> Void: ...
class ICoreApplicationView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationView'
    _iid_ = Guid('{638bb2db-451d-4661-b099-414f34ffb9f1}')
    @winrt_commethod(6)
    def get_CoreWindow(self) -> win32more.Windows.UI.Core.CoreWindow: ...
    @winrt_commethod(7)
    def add_Activated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationView, win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_IsMain(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsHosted(self) -> Boolean: ...
    CoreWindow = property(get_CoreWindow, None)
    IsMain = property(get_IsMain, None)
    IsHosted = property(get_IsHosted, None)
class ICoreApplicationView2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationView2'
    _iid_ = Guid('{68eb7adf-917f-48eb-9aeb-7de53e086ab1}')
    @winrt_commethod(6)
    def get_Dispatcher(self) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    Dispatcher = property(get_Dispatcher, None)
class ICoreApplicationView3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationView3'
    _iid_ = Guid('{07ebe1b3-a4cf-4550-ab70-b07e85330bc8}')
    @winrt_commethod(6)
    def get_IsComponent(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TitleBar(self) -> win32more.Windows.ApplicationModel.Core.CoreApplicationViewTitleBar: ...
    @winrt_commethod(8)
    def add_HostedViewClosing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationView, win32more.Windows.ApplicationModel.Core.HostedViewClosingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HostedViewClosing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsComponent = property(get_IsComponent, None)
    TitleBar = property(get_TitleBar, None)
class ICoreApplicationView5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationView5'
    _iid_ = Guid('{2bc095a8-8ef0-446d-9e60-3a3e0428c671}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Properties = property(get_Properties, None)
class ICoreApplicationView6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationView6'
    _iid_ = Guid('{c119d49a-0679-49ba-803f-b79c5cf34cca}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class ICoreApplicationViewTitleBar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar'
    _iid_ = Guid('{006d35e3-e1f1-431b-9508-29b96926ac53}')
    @winrt_commethod(6)
    def put_ExtendViewIntoTitleBar(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_ExtendViewIntoTitleBar(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SystemOverlayLeftInset(self) -> Double: ...
    @winrt_commethod(9)
    def get_SystemOverlayRightInset(self) -> Double: ...
    @winrt_commethod(10)
    def get_Height(self) -> Double: ...
    @winrt_commethod(11)
    def add_LayoutMetricsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_LayoutMetricsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(14)
    def add_IsVisibleChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_IsVisibleChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExtendViewIntoTitleBar = property(get_ExtendViewIntoTitleBar, put_ExtendViewIntoTitleBar)
    SystemOverlayLeftInset = property(get_SystemOverlayLeftInset, None)
    SystemOverlayRightInset = property(get_SystemOverlayRightInset, None)
    Height = property(get_Height, None)
    IsVisible = property(get_IsVisible, None)
class ICoreImmersiveApplication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreImmersiveApplication'
    _iid_ = Guid('{1ada0e3e-e4a2-4123-b451-dc96bf800419}')
    @winrt_commethod(6)
    def get_Views(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Core.CoreApplicationView]: ...
    @winrt_commethod(7)
    def CreateNewView(self, runtimeType: WinRT_String, entryPoint: WinRT_String) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_commethod(8)
    def get_MainView(self) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
    Views = property(get_Views, None)
    MainView = property(get_MainView, None)
class ICoreImmersiveApplication2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreImmersiveApplication2'
    _iid_ = Guid('{828e1e36-e9e3-4cfc-9b66-48b78ea9bb2c}')
    @winrt_commethod(6)
    def CreateNewViewFromMainView(self) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
class ICoreImmersiveApplication3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.ICoreImmersiveApplication3'
    _iid_ = Guid('{34a05b2f-ee0d-41e5-8314-cf10c91bf0af}')
    @winrt_commethod(6)
    def CreateNewViewWithViewSource(self, viewSource: win32more.Windows.ApplicationModel.Core.IFrameworkViewSource) -> win32more.Windows.ApplicationModel.Core.CoreApplicationView: ...
class IFrameworkView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IFrameworkView'
    _iid_ = Guid('{faab5cd0-8924-45ac-ad0f-a08fae5d0324}')
    @winrt_commethod(6)
    def Initialize(self, applicationView: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> Void: ...
    @winrt_commethod(7)
    def SetWindow(self, window: win32more.Windows.UI.Core.CoreWindow) -> Void: ...
    @winrt_commethod(8)
    def Load(self, entryPoint: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def Run(self) -> Void: ...
    @winrt_commethod(10)
    def Uninitialize(self) -> Void: ...
class IFrameworkViewSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IFrameworkViewSource'
    _iid_ = Guid('{cd770614-65c4-426c-9494-34fc43554862}')
    @winrt_commethod(6)
    def CreateView(self) -> win32more.Windows.ApplicationModel.Core.IFrameworkView: ...
class IHostedViewClosingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IHostedViewClosingEventArgs'
    _iid_ = Guid('{d238943c-b24e-4790-acb5-3e4243c4ff87}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IUnhandledError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IUnhandledError'
    _iid_ = Guid('{9459b726-53b5-4686-9eaf-fa8162dc3980}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def Propagate(self) -> Void: ...
    Handled = property(get_Handled, None)
class IUnhandledErrorDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Core.IUnhandledErrorDetectedEventArgs'
    _iid_ = Guid('{679ab78b-b336-4822-ac40-0d750f0b7a2b}')
    @winrt_commethod(6)
    def get_UnhandledError(self) -> win32more.Windows.ApplicationModel.Core.UnhandledError: ...
    UnhandledError = property(get_UnhandledError, None)
class UnhandledError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Core.IUnhandledError
    _classid_ = 'Windows.ApplicationModel.Core.UnhandledError'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.ApplicationModel.Core.IUnhandledError) -> Boolean: ...
    @winrt_mixinmethod
    def Propagate(self: win32more.Windows.ApplicationModel.Core.IUnhandledError) -> Void: ...
    Handled = property(get_Handled, None)
class UnhandledErrorDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Core.IUnhandledErrorDetectedEventArgs
    _classid_ = 'Windows.ApplicationModel.Core.UnhandledErrorDetectedEventArgs'
    @winrt_mixinmethod
    def get_UnhandledError(self: win32more.Windows.ApplicationModel.Core.IUnhandledErrorDetectedEventArgs) -> win32more.Windows.ApplicationModel.Core.UnhandledError: ...
    UnhandledError = property(get_UnhandledError, None)
make_head(_module, 'AppListEntry')
make_head(_module, 'CoreApplication')
make_head(_module, 'CoreApplicationView')
make_head(_module, 'CoreApplicationViewTitleBar')
make_head(_module, 'HostedViewClosingEventArgs')
make_head(_module, 'IAppListEntry')
make_head(_module, 'IAppListEntry2')
make_head(_module, 'IAppListEntry3')
make_head(_module, 'IAppListEntry4')
make_head(_module, 'ICoreApplication')
make_head(_module, 'ICoreApplication2')
make_head(_module, 'ICoreApplication3')
make_head(_module, 'ICoreApplicationExit')
make_head(_module, 'ICoreApplicationUnhandledError')
make_head(_module, 'ICoreApplicationUseCount')
make_head(_module, 'ICoreApplicationView')
make_head(_module, 'ICoreApplicationView2')
make_head(_module, 'ICoreApplicationView3')
make_head(_module, 'ICoreApplicationView5')
make_head(_module, 'ICoreApplicationView6')
make_head(_module, 'ICoreApplicationViewTitleBar')
make_head(_module, 'ICoreImmersiveApplication')
make_head(_module, 'ICoreImmersiveApplication2')
make_head(_module, 'ICoreImmersiveApplication3')
make_head(_module, 'IFrameworkView')
make_head(_module, 'IFrameworkViewSource')
make_head(_module, 'IHostedViewClosingEventArgs')
make_head(_module, 'IUnhandledError')
make_head(_module, 'IUnhandledErrorDetectedEventArgs')
make_head(_module, 'UnhandledError')
make_head(_module, 'UnhandledErrorDetectedEventArgs')
