from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.Mmc
import Windows.Win32.UI.Controls
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
MMC_VER: UInt32 = 512
MMC_PROP_CHANGEAFFECTSUI: UInt32 = 1
MMC_PROP_MODIFIABLE: UInt32 = 2
MMC_PROP_REMOVABLE: UInt32 = 4
MMC_PROP_PERSIST: UInt32 = 8
MMCLV_AUTO: Int32 = -1
MMCLV_NOPARAM: Int32 = -2
MMCLV_NOICON: Int32 = -1
MMCLV_VIEWSTYLE_ICON: UInt32 = 0
MMCLV_VIEWSTYLE_SMALLICON: UInt32 = 2
MMCLV_VIEWSTYLE_LIST: UInt32 = 3
MMCLV_VIEWSTYLE_REPORT: UInt32 = 1
MMCLV_VIEWSTYLE_FILTERED: UInt32 = 4
MMCLV_NOPTR: UInt32 = 0
MMCLV_UPDATE_NOINVALIDATEALL: UInt32 = 1
MMCLV_UPDATE_NOSCROLL: UInt32 = 2
MMC_IMAGECALLBACK: Int32 = -1
RDI_STR: UInt32 = 2
RDI_IMAGE: UInt32 = 4
RDI_STATE: UInt32 = 8
RDI_PARAM: UInt32 = 16
RDI_INDEX: UInt32 = 32
RDI_INDENT: UInt32 = 64
MMC_VIEW_OPTIONS_NONE: UInt32 = 0
MMC_VIEW_OPTIONS_NOLISTVIEWS: UInt32 = 1
MMC_VIEW_OPTIONS_MULTISELECT: UInt32 = 2
MMC_VIEW_OPTIONS_OWNERDATALIST: UInt32 = 4
MMC_VIEW_OPTIONS_FILTERED: UInt32 = 8
MMC_VIEW_OPTIONS_CREATENEW: UInt32 = 16
MMC_VIEW_OPTIONS_USEFONTLINKING: UInt32 = 32
MMC_VIEW_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST: UInt32 = 64
MMC_VIEW_OPTIONS_LEXICAL_SORT: UInt32 = 128
MMC_PSO_NOAPPLYNOW: UInt32 = 1
MMC_PSO_HASHELP: UInt32 = 2
MMC_PSO_NEWWIZARDTYPE: UInt32 = 4
MMC_PSO_NO_PROPTITLE: UInt32 = 8
RFI_PARTIAL: UInt32 = 1
RFI_WRAP: UInt32 = 2
RSI_DESCENDING: UInt32 = 1
RSI_NOSORTICON: UInt32 = 2
SDI_STR: UInt32 = 2
SDI_IMAGE: UInt32 = 4
SDI_OPENIMAGE: UInt32 = 8
SDI_STATE: UInt32 = 16
SDI_PARAM: UInt32 = 32
SDI_CHILDREN: UInt32 = 64
SDI_PARENT: UInt32 = 0
SDI_PREVIOUS: UInt32 = 268435456
SDI_NEXT: UInt32 = 536870912
SDI_FIRST: UInt32 = 134217728
MMC_MULTI_SELECT_COOKIE: Int32 = -2
MMC_WINDOW_COOKIE: Int32 = -3
SPECIAL_COOKIE_MIN: Int32 = -10
SPECIAL_COOKIE_MAX: Int32 = -1
MMC_NW_OPTION_NONE: UInt32 = 0
MMC_NW_OPTION_NOSCOPEPANE: UInt32 = 1
MMC_NW_OPTION_NOTOOLBARS: UInt32 = 2
MMC_NW_OPTION_SHORTTITLE: UInt32 = 4
MMC_NW_OPTION_CUSTOMTITLE: UInt32 = 8
MMC_NW_OPTION_NOPERSIST: UInt32 = 16
MMC_NW_OPTION_NOACTIONPANE: UInt32 = 32
MMC_NODEID_SLOW_RETRIEVAL: UInt32 = 1
SPECIAL_DOBJ_MIN: Int32 = -10
SPECIAL_DOBJ_MAX: UInt32 = 0
AUTO_WIDTH: Int32 = -1
HIDE_COLUMN: Int32 = -4
ILSIF_LEAVE_LARGE_ICON: UInt32 = 1073741824
ILSIF_LEAVE_SMALL_ICON: UInt32 = 536870912
HDI_HIDDEN: UInt32 = 1
RDCI_ScopeItem: UInt32 = 2147483648
RVTI_MISC_OPTIONS_NOLISTVIEWS: UInt32 = 1
RVTI_LIST_OPTIONS_NONE: UInt32 = 0
RVTI_LIST_OPTIONS_OWNERDATALIST: UInt32 = 2
RVTI_LIST_OPTIONS_MULTISELECT: UInt32 = 4
RVTI_LIST_OPTIONS_FILTERED: UInt32 = 8
RVTI_LIST_OPTIONS_USEFONTLINKING: UInt32 = 32
RVTI_LIST_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST: UInt32 = 64
RVTI_LIST_OPTIONS_LEXICAL_SORT: UInt32 = 128
RVTI_LIST_OPTIONS_ALLOWPASTE: UInt32 = 256
RVTI_HTML_OPTIONS_NONE: UInt32 = 0
RVTI_HTML_OPTIONS_NOLISTVIEW: UInt32 = 1
RVTI_OCX_OPTIONS_NONE: UInt32 = 0
RVTI_OCX_OPTIONS_NOLISTVIEW: UInt32 = 1
RVTI_OCX_OPTIONS_CACHE_OCX: UInt32 = 2
MMC_DEFAULT_OPERATION_COPY: UInt32 = 1
MMC_ITEM_OVERLAY_STATE_MASK: UInt32 = 3840
MMC_ITEM_OVERLAY_STATE_SHIFT: UInt32 = 8
MMC_ITEM_STATE_MASK: UInt32 = 255
class AppEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fc7a4252-78ac-4532-8c-5a-56-3c-fe-13-88-63')
AppEventsDHTMLConnector = Guid('ade6444b-c91f-4e37-92-a4-5b-b4-30-a3-33-40')
Application = Guid('49b2791a-b1ae-4c90-9b-8e-e8-60-ba-07-f8-89')
CCM_COMMANDID_MASK_CONSTANTS = UInt32
CCM_COMMANDID_MASK_RESERVED: CCM_COMMANDID_MASK_CONSTANTS = 4294901760
CCM_INSERTIONALLOWED = Int32
CCM_INSERTIONALLOWED_TOP: CCM_INSERTIONALLOWED = 1
CCM_INSERTIONALLOWED_NEW: CCM_INSERTIONALLOWED = 2
CCM_INSERTIONALLOWED_TASK: CCM_INSERTIONALLOWED = 4
CCM_INSERTIONALLOWED_VIEW: CCM_INSERTIONALLOWED = 8
CCM_INSERTIONPOINTID = Int32
CCM_INSERTIONPOINTID_MASK_SPECIAL: CCM_INSERTIONPOINTID = -65536
CCM_INSERTIONPOINTID_MASK_SHARED: CCM_INSERTIONPOINTID = -2147483648
CCM_INSERTIONPOINTID_MASK_CREATE_PRIMARY: CCM_INSERTIONPOINTID = 1073741824
CCM_INSERTIONPOINTID_MASK_ADD_PRIMARY: CCM_INSERTIONPOINTID = 536870912
CCM_INSERTIONPOINTID_MASK_ADD_3RDPARTY: CCM_INSERTIONPOINTID = 268435456
CCM_INSERTIONPOINTID_MASK_RESERVED: CCM_INSERTIONPOINTID = 268369920
CCM_INSERTIONPOINTID_MASK_FLAGINDEX: CCM_INSERTIONPOINTID = 31
CCM_INSERTIONPOINTID_PRIMARY_TOP: CCM_INSERTIONPOINTID = -1610612736
CCM_INSERTIONPOINTID_PRIMARY_NEW: CCM_INSERTIONPOINTID = -1610612735
CCM_INSERTIONPOINTID_PRIMARY_TASK: CCM_INSERTIONPOINTID = -1610612734
CCM_INSERTIONPOINTID_PRIMARY_VIEW: CCM_INSERTIONPOINTID = -1610612733
CCM_INSERTIONPOINTID_PRIMARY_HELP: CCM_INSERTIONPOINTID = -1610612732
CCM_INSERTIONPOINTID_3RDPARTY_NEW: CCM_INSERTIONPOINTID = -1879048191
CCM_INSERTIONPOINTID_3RDPARTY_TASK: CCM_INSERTIONPOINTID = -1879048190
CCM_INSERTIONPOINTID_ROOT_MENU: CCM_INSERTIONPOINTID = -2147483648
CCM_SPECIAL = Int32
CCM_SPECIAL_SEPARATOR: CCM_SPECIAL = 1
CCM_SPECIAL_SUBMENU: CCM_SPECIAL = 2
CCM_SPECIAL_DEFAULT_ITEM: CCM_SPECIAL = 4
CCM_SPECIAL_INSERTION_POINT: CCM_SPECIAL = 8
CCM_SPECIAL_TESTONLY: CCM_SPECIAL = 16
class CONTEXTMENUITEM(Structure):
    strName: Windows.Win32.Foundation.PWSTR
    strStatusBarText: Windows.Win32.Foundation.PWSTR
    lCommandID: Int32
    lInsertionPointID: Int32
    fFlags: Int32
    fSpecialFlags: Int32
class CONTEXTMENUITEM2(Structure):
    strName: Windows.Win32.Foundation.PWSTR
    strStatusBarText: Windows.Win32.Foundation.PWSTR
    lCommandID: Int32
    lInsertionPointID: Int32
    fFlags: Int32
    fSpecialFlags: Int32
    strLanguageIndependentName: Windows.Win32.Foundation.PWSTR
class Column(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fd1c5f63-2b16-4d06-9a-b3-f4-53-50-b9-40-ab')
    @commethod(7)
    def Name(Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Width(Width: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Width(Width: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DisplayPosition(DisplayPosition: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_DisplayPosition(Index: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Hidden(Hidden: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Hidden(Hidden: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetAsSortColumn(SortOrder: Windows.Win32.System.Mmc._ColumnSortOrder) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsSortColumn(IsSortColumn: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class Columns(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('383d4d97-fc44-478b-b1-39-63-23-dc-48-61-1c')
    @commethod(7)
    def Item(Index: Int32, Column: POINTER(Windows.Win32.System.Mmc.Column_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
ConsolePower = Guid('f0285374-dff1-11d3-b4-33-00-c0-4f-8e-cd-78')
class ContextMenu(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('dab39ce0-25e6-4e07-83-62-ba-9c-95-70-65-45')
    @commethod(7)
    def get__NewEnum(retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(IndexOrPath: Windows.Win32.System.Com.VARIANT, MenuItem: POINTER(Windows.Win32.System.Mmc.MenuItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
DATA_OBJECT_TYPES = Int32
CCT_SCOPE: DATA_OBJECT_TYPES = 32768
CCT_RESULT: DATA_OBJECT_TYPES = 32769
CCT_SNAPIN_MANAGER: DATA_OBJECT_TYPES = 32770
CCT_UNINITIALIZED: DATA_OBJECT_TYPES = 65535
class Document(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('225120d6-1e0f-40a3-93-fe-10-79-e6-a8-01-7b')
    @commethod(7)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SaveAs(Filename: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Close(SaveChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Views(Views: POINTER(Windows.Win32.System.Mmc.Views_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SnapIns(SnapIns: POINTER(Windows.Win32.System.Mmc.SnapIns_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ActiveView(View: POINTER(Windows.Win32.System.Mmc.View_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Name(Name: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Name(Name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Location(Location: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsSaved(IsSaved: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Mode(Mode: POINTER(Windows.Win32.System.Mmc._DocumentMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Mode(Mode: Windows.Win32.System.Mmc._DocumentMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_RootNode(Node: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ScopeNamespace(ScopeNamespace: POINTER(Windows.Win32.System.Mmc.ScopeNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateProperties(Properties: POINTER(Windows.Win32.System.Mmc.Properties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Application(Application: POINTER(Windows.Win32.System.Mmc._Application_head)) -> Windows.Win32.Foundation.HRESULT: ...
class Extension(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ad4d6ca6-912f-409b-a2-6e-7f-d2-34-ae-f5-42')
    @commethod(7)
    def get_Name(Name: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Vendor(Vendor: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Version(Version: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Extensions(Extensions: POINTER(Windows.Win32.System.Mmc.Extensions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SnapinCLSID(SnapinCLSID: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnableAllExtensions(Enable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Enable(Enable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class Extensions(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('82dbea43-8ca4-44bc-a2-ca-d1-87-41-05-9e-c8')
    @commethod(7)
    def get__NewEnum(retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Extension: POINTER(Windows.Win32.System.Mmc.Extension_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class Frame(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e5e2d970-5bb3-4306-88-04-b0-96-8a-31-c8-e6')
    @commethod(7)
    def Maximize() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Minimize() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Restore() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Top(Top: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Top(top: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Bottom(Bottom: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Bottom(bottom: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Left(Left: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Left(left: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Right(Right: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Right(right: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IColumnData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('547c1354-024d-11d3-a7-07-00-c0-4f-8e-f4-cb')
    @commethod(3)
    def SetColumnConfigData(pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), pColSetData: POINTER(Windows.Win32.System.Mmc.MMC_COLUMN_SET_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnConfigData(pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), ppColSetData: POINTER(POINTER(Windows.Win32.System.Mmc.MMC_COLUMN_SET_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetColumnSortData(pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), pColSortData: POINTER(Windows.Win32.System.Mmc.MMC_SORT_SET_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnSortData(pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), ppColSortData: POINTER(POINTER(Windows.Win32.System.Mmc.MMC_SORT_SET_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IComponent(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43136eb2-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def Initialize(lpConsole: Windows.Win32.System.Mmc.IConsole_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Notify(lpDataObject: Windows.Win32.System.Com.IDataObject_head, event: Windows.Win32.System.Mmc.MMC_NOTIFY_TYPE, arg: Windows.Win32.Foundation.LPARAM, param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Destroy(cookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryDataObject(cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDataObject: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResultViewType(cookie: IntPtr, ppViewType: POINTER(Windows.Win32.Foundation.PWSTR), pViewOptions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayInfo(pResultDataItem: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CompareObjects(lpDataObjectA: Windows.Win32.System.Com.IDataObject_head, lpDataObjectB: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IComponent2(c_void_p):
    extends: Windows.Win32.System.Mmc.IComponent
    Guid = Guid('79a2d615-4a10-4ed4-8c-65-86-33-f9-33-50-95')
    @commethod(10)
    def QueryDispatch(cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetResultViewType2(cookie: IntPtr, pResultViewType: POINTER(Windows.Win32.System.Mmc.RESULT_VIEW_TYPE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RestoreResultView(cookie: IntPtr, pResultViewType: POINTER(Windows.Win32.System.Mmc.RESULT_VIEW_TYPE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('955ab28a-5218-11d0-a9-85-00-c0-4f-d8-d5-65')
    @commethod(3)
    def Initialize(pUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateComponent(ppComponent: POINTER(Windows.Win32.System.Mmc.IComponent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Notify(lpDataObject: Windows.Win32.System.Com.IDataObject_head, event: Windows.Win32.System.Mmc.MMC_NOTIFY_TYPE, arg: Windows.Win32.Foundation.LPARAM, param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Destroy() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryDataObject(cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDataObject: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayInfo(pScopeDataItem: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CompareObjects(lpDataObjectA: Windows.Win32.System.Com.IDataObject_head, lpDataObjectB: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentData2(c_void_p):
    extends: Windows.Win32.System.Mmc.IComponentData
    Guid = Guid('cca0f2d2-82de-41b5-bf-47-3b-20-76-27-3d-5c')
    @commethod(10)
    def QueryDispatch(cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsole(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43136eb1-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def SetHeader(pHeader: Windows.Win32.System.Mmc.IHeaderCtrl_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetToolbar(pToolbar: Windows.Win32.System.Mmc.IToolbar_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryResultView(pUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryScopeImageList(ppImageList: POINTER(Windows.Win32.System.Mmc.IImageList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryResultImageList(ppImageList: POINTER(Windows.Win32.System.Mmc.IImageList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdateAllViews(lpDataObject: Windows.Win32.System.Com.IDataObject_head, data: Windows.Win32.Foundation.LPARAM, hint: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MessageBox(lpszText: Windows.Win32.Foundation.PWSTR, lpszTitle: Windows.Win32.Foundation.PWSTR, fuStyle: UInt32, piRetval: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def QueryConsoleVerb(ppConsoleVerb: POINTER(Windows.Win32.System.Mmc.IConsoleVerb_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectScopeItem(hScopeItem: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMainWindow(phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def NewWindow(hScopeItem: IntPtr, lOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IConsole2(c_void_p):
    extends: Windows.Win32.System.Mmc.IConsole
    Guid = Guid('103d842a-aa63-11d1-a7-e1-00-c0-4f-d8-d5-65')
    @commethod(14)
    def Expand(hItem: IntPtr, bExpand: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsTaskpadViewPreferred() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStatusText(pszStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IConsole3(c_void_p):
    extends: Windows.Win32.System.Mmc.IConsole2
    Guid = Guid('4f85efdb-d0e1-498c-8d-4a-d0-10-df-dd-40-4f')
    @commethod(17)
    def RenameScopeItem(hScopeItem: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IConsoleNameSpace(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bedeb620-f24d-11cf-8a-fc-00-aa-00-3c-a9-f6')
    @commethod(3)
    def InsertItem(item: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteItem(hItem: IntPtr, fDeleteThis: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetItem(item: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItem(item: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetChildItem(item: IntPtr, pItemChild: POINTER(IntPtr), pCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNextItem(item: IntPtr, pItemNext: POINTER(IntPtr), pCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetParentItem(item: IntPtr, pItemParent: POINTER(IntPtr), pCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsoleNameSpace2(c_void_p):
    extends: Windows.Win32.System.Mmc.IConsoleNameSpace
    Guid = Guid('255f18cc-65db-11d1-a7-dc-00-c0-4f-d8-d5-65')
    @commethod(10)
    def Expand(hItem: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddExtension(hItem: IntPtr, lpClsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsolePower(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1cfbdd0e-62ca-49ce-a3-af-db-b2-de-61-b0-68')
    @commethod(3)
    def SetExecutionState(dwAdd: UInt32, dwRemove: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResetIdleTimer(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IConsolePowerSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3333759f-fe4f-4975-b1-43-fe-c0-a5-dd-6d-65')
    @commethod(3)
    def OnPowerBroadcast(nEvent: UInt32, lParam: Windows.Win32.Foundation.LPARAM, plReturn: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsoleVerb(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e49f7a60-74af-11d0-a2-86-00-c0-4f-d8-fe-93')
    @commethod(3)
    def GetVerbState(eCmdID: Windows.Win32.System.Mmc.MMC_CONSOLE_VERB, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, pState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetVerbState(eCmdID: Windows.Win32.System.Mmc.MMC_CONSOLE_VERB, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, bState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultVerb(eCmdID: Windows.Win32.System.Mmc.MMC_CONSOLE_VERB) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDefaultVerb(peCmdID: POINTER(Windows.Win32.System.Mmc.MMC_CONSOLE_VERB)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43136eb7-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def AddItem(pItem: POINTER(Windows.Win32.System.Mmc.CONTEXTMENUITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuCallback2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e178bc0e-2ed0-4b5e-80-97-42-c9-08-7e-8b-33')
    @commethod(3)
    def AddItem(pItem: POINTER(Windows.Win32.System.Mmc.CONTEXTMENUITEM2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuProvider(c_void_p):
    extends: Windows.Win32.System.Mmc.IContextMenuCallback
    Guid = Guid('43136eb6-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(4)
    def EmptyMenuList() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPrimaryExtensionItems(piExtension: Windows.Win32.System.Com.IUnknown_head, piDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddThirdPartyExtensionItems(piDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowContextMenu(hwndParent: Windows.Win32.Foundation.HWND, xPos: Int32, yPos: Int32, plSelected: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IControlbar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('69fb811e-6c1c-11d0-a2-cb-00-c0-4f-d9-09-dd')
    @commethod(3)
    def Create(nType: Windows.Win32.System.Mmc.MMC_CONTROL_TYPE, pExtendControlbar: Windows.Win32.System.Mmc.IExtendControlbar_head, ppUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Attach(nType: Windows.Win32.System.Mmc.MMC_CONTROL_TYPE, lpUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach(lpUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDisplayHelp(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cc593830-b926-11d1-80-63-00-00-f8-75-a9-ce')
    @commethod(3)
    def ShowTopic(pszHelpTopic: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumTASK(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('338698b1-5a02-11d1-9f-ec-00-60-08-32-db-4a')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.System.Mmc.MMC_TASK_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.System.Mmc.IEnumTASK_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendContextMenu(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4f3b7a4f-cfac-11cf-b8-e3-00-c0-4f-d8-d5-b0')
    @commethod(3)
    def AddMenuItems(piDataObject: Windows.Win32.System.Com.IDataObject_head, piCallback: Windows.Win32.System.Mmc.IContextMenuCallback_head, pInsertionAllowed: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Command(lCommandID: Int32, piDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendControlbar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('49506520-6f40-11d0-a9-8b-00-c0-4f-d8-d5-65')
    @commethod(3)
    def SetControlbar(pControlbar: Windows.Win32.System.Mmc.IControlbar_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ControlbarNotify(event: Windows.Win32.System.Mmc.MMC_NOTIFY_TYPE, arg: Windows.Win32.Foundation.LPARAM, param2: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendPropertySheet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85de64dc-ef21-11cf-a2-85-00-c0-4f-d8-db-e6')
    @commethod(3)
    def CreatePropertyPages(lpProvider: Windows.Win32.System.Mmc.IPropertySheetCallback_head, handle: IntPtr, lpIDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryPagesFor(lpDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendPropertySheet2(c_void_p):
    extends: Windows.Win32.System.Mmc.IExtendPropertySheet
    Guid = Guid('b7a87232-4a51-11d1-a7-ea-00-c0-4f-d9-09-dd')
    @commethod(5)
    def GetWatermarks(lpIDataObject: Windows.Win32.System.Com.IDataObject_head, lphWatermark: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), lphHeader: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), lphPalette: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE), bStretch: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendTaskPad(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8dee6511-554d-11d1-9f-ea-00-60-08-32-db-4a')
    @commethod(3)
    def TaskNotify(pdo: Windows.Win32.System.Com.IDataObject_head, arg: POINTER(Windows.Win32.System.Com.VARIANT_head), param2: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumTasks(pdo: Windows.Win32.System.Com.IDataObject_head, szTaskGroup: Windows.Win32.Foundation.PWSTR, ppEnumTASK: POINTER(Windows.Win32.System.Mmc.IEnumTASK_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTitle(pszGroup: Windows.Win32.Foundation.PWSTR, pszTitle: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescriptiveText(pszGroup: Windows.Win32.Foundation.PWSTR, pszDescriptiveText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBackground(pszGroup: Windows.Win32.Foundation.PWSTR, pTDO: POINTER(Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_OBJECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetListPadInfo(pszGroup: Windows.Win32.Foundation.PWSTR, lpListPadInfo: POINTER(Windows.Win32.System.Mmc.MMC_LISTPAD_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendView(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('89995cee-d2ed-4c0e-ae-5e-df-7e-76-f3-fa-53')
    @commethod(3)
    def GetViews(pDataObject: Windows.Win32.System.Com.IDataObject_head, pViewExtensionCallback: Windows.Win32.System.Mmc.IViewExtensionCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderCtrl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43136eb3-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def InsertColumn(nCol: Int32, title: Windows.Win32.Foundation.PWSTR, nFormat: Int32, nWidth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteColumn(nCol: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetColumnText(nCol: Int32, title: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnText(nCol: Int32, pText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColumnWidth(nCol: Int32, nWidth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetColumnWidth(nCol: Int32, pWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderCtrl2(c_void_p):
    extends: Windows.Win32.System.Mmc.IHeaderCtrl
    Guid = Guid('9757abb8-1b32-11d1-a7-ce-00-c0-4f-d8-d5-65')
    @commethod(9)
    def SetChangeTimeOut(uTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetColumnFilter(nColumn: UInt32, dwType: UInt32, pFilterData: POINTER(Windows.Win32.System.Mmc.MMC_FILTERDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetColumnFilter(nColumn: UInt32, pdwType: POINTER(UInt32), pFilterData: POINTER(Windows.Win32.System.Mmc.MMC_FILTERDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IImageList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43136eb8-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def ImageListSetIcon(pIcon: POINTER(IntPtr), nLoc: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ImageListSetStrip(pBMapSm: POINTER(IntPtr), pBMapLg: POINTER(IntPtr), nStartLoc: Int32, cMask: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
class IMMCVersionInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a8d2c5fe-cdcb-4b9d-bd-e5-a2-73-43-ff-54-bc')
    @commethod(3)
    def GetMMCVersion(pVersionMajor: POINTER(Int32), pVersionMinor: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMenuButton(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('951ed750-d080-11d0-b1-97-00-00-00-00-00-00')
    @commethod(3)
    def AddButton(idCommand: Int32, lpButtonText: Windows.Win32.Foundation.PWSTR, lpTooltipText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetButton(idCommand: Int32, lpButtonText: Windows.Win32.Foundation.PWSTR, lpTooltipText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetButtonState(idCommand: Int32, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, bState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMessageView(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('80f94174-fccc-11d2-b9-91-00-c0-4f-8e-cd-78')
    @commethod(3)
    def SetTitleText(pszTitleText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBodyText(pszBodyText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIcon(id: Windows.Win32.System.Mmc.IconIdentifier) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clear() -> Windows.Win32.Foundation.HRESULT: ...
class INodeProperties(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('15bc4d24-a522-4406-aa-55-07-49-53-7a-68-65')
    @commethod(3)
    def GetProperty(pDataObject: Windows.Win32.System.Com.IDataObject_head, szPropertyName: Windows.Win32.Foundation.BSTR, pbstrProperty: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySheetCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85de64dd-ef21-11cf-a2-85-00-c0-4f-d8-db-e6')
    @commethod(3)
    def AddPage(hPage: Windows.Win32.UI.Controls.HPROPSHEETPAGE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemovePage(hPage: Windows.Win32.UI.Controls.HPROPSHEETPAGE) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySheetProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85de64de-ef21-11cf-a2-85-00-c0-4f-d8-db-e6')
    @commethod(3)
    def CreatePropertySheet(title: Windows.Win32.Foundation.PWSTR, type: Byte, cookie: IntPtr, pIDataObjectm: Windows.Win32.System.Com.IDataObject_head, dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindPropertySheet(hItem: IntPtr, lpComponent: Windows.Win32.System.Mmc.IComponent_head, lpDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPrimaryPages(lpUnknown: Windows.Win32.System.Com.IUnknown_head, bCreateHandle: Windows.Win32.Foundation.BOOL, hNotifyWindow: Windows.Win32.Foundation.HWND, bScopePane: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddExtensionPages() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Show(window: IntPtr, page: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IRequiredExtensions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('72782d7a-a4a0-11d1-af-0f-00-c0-4f-b6-dd-2c')
    @commethod(3)
    def EnableAllExtensions() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstExtension(pExtCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextExtension(pExtCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IResultData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('31da5fa0-e0eb-11cf-9f-21-00-aa-00-3c-a9-f6')
    @commethod(3)
    def InsertItem(item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteItem(itemID: IntPtr, nCol: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindItemByLParam(lParam: Windows.Win32.Foundation.LPARAM, pItemID: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteAllRsltItems() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetItem(item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetItem(item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextItem(item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ModifyItemState(nIndex: Int32, itemID: IntPtr, uAdd: UInt32, uRemove: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ModifyViewStyle(add: Windows.Win32.System.Mmc.MMC_RESULT_VIEW_STYLE, remove: Windows.Win32.System.Mmc.MMC_RESULT_VIEW_STYLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetViewMode(lViewMode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetViewMode(lViewMode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UpdateItem(itemID: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Sort(nColumn: Int32, dwSortOptions: UInt32, lUserParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetDescBarText(DescText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetItemCount(nItemCount: Int32, dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IResultData2(c_void_p):
    extends: Windows.Win32.System.Mmc.IResultData
    Guid = Guid('0f36e0eb-a7f1-4a81-be-5a-92-47-f7-de-4b-1b')
    @commethod(18)
    def RenameResultItem(itemID: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IResultDataCompare(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e8315a52-7a1a-11d0-a2-d2-00-c0-4f-d9-09-dd')
    @commethod(3)
    def Compare(lUserParam: Windows.Win32.Foundation.LPARAM, cookieA: IntPtr, cookieB: IntPtr, pnResult: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IResultDataCompareEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('96933476-0251-11d3-ae-b0-00-c0-4f-8e-cd-78')
    @commethod(3)
    def Compare(prdc: POINTER(Windows.Win32.System.Mmc.RDCOMPARE_head), pnResult: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IResultOwnerData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9cb396d8-ea83-11d0-ae-f1-00-c0-4f-b6-dd-2c')
    @commethod(3)
    def FindItem(pFindInfo: POINTER(Windows.Win32.System.Mmc.RESULTFINDINFO_head), pnFoundIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CacheHint(nStartIndex: Int32, nEndIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SortItems(nColumn: Int32, dwSortOptions: UInt32, lUserParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinAbout(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1245208c-a151-11d0-a7-d7-00-c0-4f-d9-09-dd')
    @commethod(3)
    def GetSnapinDescription(lpDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProvider(lpName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSnapinVersion(lpVersion: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSnapinImage(hAppIcon: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStaticFolderImage(hSmallImage: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), hSmallImageOpen: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), hLargeImage: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), cMask: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinHelp(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a6b15ace-df59-11d0-a7-dd-00-c0-4f-d9-09-dd')
    @commethod(3)
    def GetHelpTopic(lpCompiledHelpFile: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinHelp2(c_void_p):
    extends: Windows.Win32.System.Mmc.ISnapinHelp
    Guid = Guid('4861a010-20f9-11d2-a5-10-00-c0-4f-b6-dd-2c')
    @commethod(4)
    def GetLinkedTopics(lpCompiledHelpFiles: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinProperties(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f7889da9-4a02-4837-bf-89-1a-6f-2a-02-10-10')
    @commethod(3)
    def Initialize(pProperties: Windows.Win32.System.Mmc.Properties_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryPropertyNames(pCallback: Windows.Win32.System.Mmc.ISnapinPropertiesCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PropertiesChanged(cProperties: Int32, pProperties: POINTER(Windows.Win32.System.Mmc.MMC_SNAPIN_PROPERTY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinPropertiesCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a50fa2e5-7e61-45eb-a8-d4-9a-07-b3-e8-51-a8')
    @commethod(3)
    def AddPropertyName(pszPropName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IStringTable(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('de40b7a4-0f65-11d2-8e-25-00-c0-4f-8e-cd-78')
    @commethod(3)
    def AddString(pszAdd: Windows.Win32.Foundation.PWSTR, pStringID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(StringID: UInt32, cchBuffer: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringLength(StringID: UInt32, pcchString: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteString(StringID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteAllStrings() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindString(pszFind: Windows.Win32.Foundation.PWSTR, pStringID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Enumerate(ppEnum: POINTER(Windows.Win32.System.Com.IEnumString_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IToolbar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43136eb9-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def AddBitmap(nImages: Int32, hbmp: Windows.Win32.Graphics.Gdi.HBITMAP, cxSize: Int32, cySize: Int32, crMask: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddButtons(nButtons: Int32, lpButtons: POINTER(Windows.Win32.System.Mmc.MMCBUTTON_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertButton(nIndex: Int32, lpButton: POINTER(Windows.Win32.System.Mmc.MMCBUTTON_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteButton(nIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetButtonState(idCommand: Int32, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, pState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetButtonState(idCommand: Int32, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, bState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IViewExtensionCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('34dd928a-7599-41e5-9f-5e-d6-bc-30-62-c2-da')
    @commethod(3)
    def AddView(pExtViewData: POINTER(Windows.Win32.System.Mmc.MMC_EXT_VIEW_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
IconIdentifier = Int32
Icon_None: IconIdentifier = 0
Icon_Error: IconIdentifier = 32513
Icon_Question: IconIdentifier = 32514
Icon_Warning: IconIdentifier = 32515
Icon_Information: IconIdentifier = 32516
Icon_First: IconIdentifier = 32513
Icon_Last: IconIdentifier = 32516
class MENUBUTTONDATA(Structure):
    idCommand: Int32
    x: Int32
    y: Int32
class MMCBUTTON(Structure):
    nBitmap: Int32
    idCommand: Int32
    fsState: Byte
    fsType: Byte
    lpButtonText: Windows.Win32.Foundation.PWSTR
    lpTooltipText: Windows.Win32.Foundation.PWSTR
MMCVersionInfo = Guid('d6fedb1d-cf21-4bd9-af-3b-c5-46-8e-9c-66-84')
MMC_ACTION_TYPE = Int32
MMC_ACTION_UNINITIALIZED: MMC_ACTION_TYPE = -1
MMC_ACTION_ID: MMC_ACTION_TYPE = 0
MMC_ACTION_LINK: MMC_ACTION_TYPE = 1
MMC_ACTION_SCRIPT: MMC_ACTION_TYPE = 2
MMC_BUTTON_STATE = Int32
ENABLED: MMC_BUTTON_STATE = 1
CHECKED: MMC_BUTTON_STATE = 2
HIDDEN: MMC_BUTTON_STATE = 4
INDETERMINATE: MMC_BUTTON_STATE = 8
BUTTONPRESSED: MMC_BUTTON_STATE = 16
class MMC_COLUMN_DATA(Structure):
    nColIndex: Int32
    dwFlags: UInt32
    nWidth: Int32
    ulReserved: UIntPtr
class MMC_COLUMN_SET_DATA(Structure):
    cbSize: Int32
    nNumCols: Int32
    pColData: POINTER(Windows.Win32.System.Mmc.MMC_COLUMN_DATA_head)
MMC_CONSOLE_VERB = Int32
MMC_VERB_NONE: MMC_CONSOLE_VERB = 0
MMC_VERB_OPEN: MMC_CONSOLE_VERB = 32768
MMC_VERB_COPY: MMC_CONSOLE_VERB = 32769
MMC_VERB_PASTE: MMC_CONSOLE_VERB = 32770
MMC_VERB_DELETE: MMC_CONSOLE_VERB = 32771
MMC_VERB_PROPERTIES: MMC_CONSOLE_VERB = 32772
MMC_VERB_RENAME: MMC_CONSOLE_VERB = 32773
MMC_VERB_REFRESH: MMC_CONSOLE_VERB = 32774
MMC_VERB_PRINT: MMC_CONSOLE_VERB = 32775
MMC_VERB_CUT: MMC_CONSOLE_VERB = 32776
MMC_VERB_MAX: MMC_CONSOLE_VERB = 32777
MMC_VERB_FIRST: MMC_CONSOLE_VERB = 32768
MMC_VERB_LAST: MMC_CONSOLE_VERB = 32776
MMC_CONTROL_TYPE = Int32
TOOLBAR: MMC_CONTROL_TYPE = 0
MENUBUTTON: MMC_CONTROL_TYPE = 1
COMBOBOXBAR: MMC_CONTROL_TYPE = 2
class MMC_EXPANDSYNC_STRUCT(Structure):
    bHandled: Windows.Win32.Foundation.BOOL
    bExpanding: Windows.Win32.Foundation.BOOL
    hItem: IntPtr
class MMC_EXT_VIEW_DATA(Structure):
    viewID: Guid
    pszURL: Windows.Win32.Foundation.PWSTR
    pszViewTitle: Windows.Win32.Foundation.PWSTR
    pszTooltipText: Windows.Win32.Foundation.PWSTR
    bReplacesDefaultView: Windows.Win32.Foundation.BOOL
class MMC_FILTERDATA(Structure):
    pszText: Windows.Win32.Foundation.PWSTR
    cchTextMax: Int32
    lValue: Int32
MMC_FILTER_CHANGE_CODE = Int32
MFCC_DISABLE: MMC_FILTER_CHANGE_CODE = 0
MFCC_ENABLE: MMC_FILTER_CHANGE_CODE = 1
MFCC_VALUE_CHANGE: MMC_FILTER_CHANGE_CODE = 2
MMC_FILTER_TYPE = Int32
MMC_STRING_FILTER: MMC_FILTER_TYPE = 0
MMC_INT_FILTER: MMC_FILTER_TYPE = 1
MMC_FILTER_NOVALUE: MMC_FILTER_TYPE = 32768
class MMC_LISTPAD_INFO(Structure):
    szTitle: Windows.Win32.Foundation.PWSTR
    szButtonText: Windows.Win32.Foundation.PWSTR
    nCommandID: IntPtr
MMC_MENU_COMMAND_IDS = Int32
MMCC_STANDARD_VIEW_SELECT: MMC_MENU_COMMAND_IDS = -1
MMC_NOTIFY_TYPE = Int32
MMCN_ACTIVATE: MMC_NOTIFY_TYPE = 32769
MMCN_ADD_IMAGES: MMC_NOTIFY_TYPE = 32770
MMCN_BTN_CLICK: MMC_NOTIFY_TYPE = 32771
MMCN_CLICK: MMC_NOTIFY_TYPE = 32772
MMCN_COLUMN_CLICK: MMC_NOTIFY_TYPE = 32773
MMCN_CONTEXTMENU: MMC_NOTIFY_TYPE = 32774
MMCN_CUTORMOVE: MMC_NOTIFY_TYPE = 32775
MMCN_DBLCLICK: MMC_NOTIFY_TYPE = 32776
MMCN_DELETE: MMC_NOTIFY_TYPE = 32777
MMCN_DESELECT_ALL: MMC_NOTIFY_TYPE = 32778
MMCN_EXPAND: MMC_NOTIFY_TYPE = 32779
MMCN_HELP: MMC_NOTIFY_TYPE = 32780
MMCN_MENU_BTNCLICK: MMC_NOTIFY_TYPE = 32781
MMCN_MINIMIZED: MMC_NOTIFY_TYPE = 32782
MMCN_PASTE: MMC_NOTIFY_TYPE = 32783
MMCN_PROPERTY_CHANGE: MMC_NOTIFY_TYPE = 32784
MMCN_QUERY_PASTE: MMC_NOTIFY_TYPE = 32785
MMCN_REFRESH: MMC_NOTIFY_TYPE = 32786
MMCN_REMOVE_CHILDREN: MMC_NOTIFY_TYPE = 32787
MMCN_RENAME: MMC_NOTIFY_TYPE = 32788
MMCN_SELECT: MMC_NOTIFY_TYPE = 32789
MMCN_SHOW: MMC_NOTIFY_TYPE = 32790
MMCN_VIEW_CHANGE: MMC_NOTIFY_TYPE = 32791
MMCN_SNAPINHELP: MMC_NOTIFY_TYPE = 32792
MMCN_CONTEXTHELP: MMC_NOTIFY_TYPE = 32793
MMCN_INITOCX: MMC_NOTIFY_TYPE = 32794
MMCN_FILTER_CHANGE: MMC_NOTIFY_TYPE = 32795
MMCN_FILTERBTN_CLICK: MMC_NOTIFY_TYPE = 32796
MMCN_RESTORE_VIEW: MMC_NOTIFY_TYPE = 32797
MMCN_PRINT: MMC_NOTIFY_TYPE = 32798
MMCN_PRELOAD: MMC_NOTIFY_TYPE = 32799
MMCN_LISTPAD: MMC_NOTIFY_TYPE = 32800
MMCN_EXPANDSYNC: MMC_NOTIFY_TYPE = 32801
MMCN_COLUMNS_CHANGED: MMC_NOTIFY_TYPE = 32802
MMCN_CANPASTE_OUTOFPROC: MMC_NOTIFY_TYPE = 32803
MMC_PROPERTY_ACTION = Int32
MMC_PROPACT_DELETING: MMC_PROPERTY_ACTION = 1
MMC_PROPACT_CHANGING: MMC_PROPERTY_ACTION = 2
MMC_PROPACT_INITIALIZED: MMC_PROPERTY_ACTION = 3
class MMC_RESTORE_VIEW(Structure):
    dwSize: UInt32
    cookie: IntPtr
    pViewType: Windows.Win32.Foundation.PWSTR
    lViewOptions: Int32
MMC_RESULT_VIEW_STYLE = Int32
MMC_SINGLESEL: MMC_RESULT_VIEW_STYLE = 1
MMC_SHOWSELALWAYS: MMC_RESULT_VIEW_STYLE = 2
MMC_NOSORTHEADER: MMC_RESULT_VIEW_STYLE = 4
MMC_ENSUREFOCUSVISIBLE: MMC_RESULT_VIEW_STYLE = 8
MMC_SCOPE_ITEM_STATE = Int32
MMC_SCOPE_ITEM_STATE_NORMAL: MMC_SCOPE_ITEM_STATE = 1
MMC_SCOPE_ITEM_STATE_BOLD: MMC_SCOPE_ITEM_STATE = 2
MMC_SCOPE_ITEM_STATE_EXPANDEDONCE: MMC_SCOPE_ITEM_STATE = 3
class MMC_SNAPIN_PROPERTY(Structure):
    pszPropName: Windows.Win32.Foundation.PWSTR
    varValue: Windows.Win32.System.Com.VARIANT
    eAction: Windows.Win32.System.Mmc.MMC_PROPERTY_ACTION
class MMC_SORT_DATA(Structure):
    nColIndex: Int32
    dwSortOptions: UInt32
    ulReserved: UIntPtr
class MMC_SORT_SET_DATA(Structure):
    cbSize: Int32
    nNumItems: Int32
    pSortData: POINTER(Windows.Win32.System.Mmc.MMC_SORT_DATA_head)
class MMC_TASK(Structure):
    sDisplayObject: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_OBJECT
    szText: Windows.Win32.Foundation.PWSTR
    szHelpString: Windows.Win32.Foundation.PWSTR
    eActionType: Windows.Win32.System.Mmc.MMC_ACTION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        nCommandID: IntPtr
        szActionURL: Windows.Win32.Foundation.PWSTR
        szScript: Windows.Win32.Foundation.PWSTR
class MMC_TASK_DISPLAY_BITMAP(Structure):
    szMouseOverBitmap: Windows.Win32.Foundation.PWSTR
    szMouseOffBitmap: Windows.Win32.Foundation.PWSTR
class MMC_TASK_DISPLAY_OBJECT(Structure):
    eDisplayType: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        uBitmap: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_BITMAP
        uSymbol: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_SYMBOL
class MMC_TASK_DISPLAY_SYMBOL(Structure):
    szFontFamilyName: Windows.Win32.Foundation.PWSTR
    szURLtoEOT: Windows.Win32.Foundation.PWSTR
    szSymbolString: Windows.Win32.Foundation.PWSTR
MMC_TASK_DISPLAY_TYPE = Int32
MMC_TASK_DISPLAY_UNINITIALIZED: MMC_TASK_DISPLAY_TYPE = 0
MMC_TASK_DISPLAY_TYPE_SYMBOL: MMC_TASK_DISPLAY_TYPE = 1
MMC_TASK_DISPLAY_TYPE_VANILLA_GIF: MMC_TASK_DISPLAY_TYPE = 2
MMC_TASK_DISPLAY_TYPE_CHOCOLATE_GIF: MMC_TASK_DISPLAY_TYPE = 3
MMC_TASK_DISPLAY_TYPE_BITMAP: MMC_TASK_DISPLAY_TYPE = 4
MMC_VIEW_TYPE = Int32
MMC_VIEW_TYPE_LIST: MMC_VIEW_TYPE = 0
MMC_VIEW_TYPE_HTML: MMC_VIEW_TYPE = 1
MMC_VIEW_TYPE_OCX: MMC_VIEW_TYPE = 2
class MMC_VISIBLE_COLUMNS(Structure):
    nVisibleColumns: Int32
    rgVisibleCols: Int32 * 1
class MenuItem(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0178fad1-b361-4b27-96-ad-67-c5-7e-bf-2e-1d')
    @commethod(7)
    def get_DisplayName(DisplayName: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LanguageIndependentName(LanguageIndependentName: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Path(Path: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_LanguageIndependentPath(LanguageIndependentPath: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Execute() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Enabled(Enabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class Node(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f81ed800-7839-4447-94-5d-8e-15-da-59-ca-55')
    @commethod(7)
    def get_Name(Name: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Property(PropertyName: Windows.Win32.Foundation.BSTR, PropertyValue: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Bookmark(Bookmark: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsScopeNode(IsScopeNode: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Nodetype(Nodetype: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
class Nodes(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('313b01df-b22f-4d42-b1-b8-48-3c-dc-f5-1d-35')
    @commethod(7)
    def get__NewEnum(retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, Node: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class Properties(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2886abc2-a425-42b2-91-c6-e2-5c-0e-04-58-1c')
    @commethod(7)
    def get__NewEnum(retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Name: Windows.Win32.Foundation.BSTR, Property: POINTER(Windows.Win32.System.Mmc.Property_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(Name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class Property(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4600c3a5-e301-41d8-b6-d0-ef-2e-42-12-e0-ca')
    @commethod(7)
    def get_Value(Value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(Value: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(Name: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
class RDCOMPARE(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    nColumn: Int32
    lUserParam: Windows.Win32.Foundation.LPARAM
    prdch1: POINTER(Windows.Win32.System.Mmc.RDITEMHDR_head)
    prdch2: POINTER(Windows.Win32.System.Mmc.RDITEMHDR_head)
class RDITEMHDR(Structure):
    dwFlags: UInt32
    cookie: IntPtr
    lpReserved: Windows.Win32.Foundation.LPARAM
class RESULTDATAITEM(Structure):
    mask: UInt32
    bScopeItem: Windows.Win32.Foundation.BOOL
    itemID: IntPtr
    nIndex: Int32
    nCol: Int32
    str: Windows.Win32.Foundation.PWSTR
    nImage: Int32
    nState: UInt32
    lParam: Windows.Win32.Foundation.LPARAM
    iIndent: Int32
class RESULTFINDINFO(Structure):
    psz: Windows.Win32.Foundation.PWSTR
    nStart: Int32
    dwOptions: UInt32
class RESULT_VIEW_TYPE_INFO(Structure):
    pstrPersistableViewDescription: Windows.Win32.Foundation.PWSTR
    eViewType: Windows.Win32.System.Mmc.MMC_VIEW_TYPE
    dwMiscOptions: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        dwListOptions: UInt32
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            dwHTMLOptions: UInt32
            pstrURL: Windows.Win32.Foundation.PWSTR
        class _Anonymous2_e__Struct(Structure):
            dwOCXOptions: UInt32
            pUnkControl: Windows.Win32.System.Com.IUnknown_head
class SCOPEDATAITEM(Structure):
    mask: UInt32
    displayname: Windows.Win32.Foundation.PWSTR
    nImage: Int32
    nOpenImage: Int32
    nState: UInt32
    cChildren: Int32
    lParam: Windows.Win32.Foundation.LPARAM
    relativeID: IntPtr
    ID: IntPtr
class SColumnSetID(Structure):
    dwFlags: UInt32
    cBytes: UInt32
    id: Byte * 1
class SMMCDataObjects(Structure):
    count: UInt32
    lpDataObject: Windows.Win32.System.Com.IDataObject_head * 1
class SMMCObjectTypes(Structure):
    count: UInt32
    guid: Guid * 1
class SNodeID(Structure):
    cBytes: UInt32
    id: Byte * 1
class SNodeID2(Structure):
    dwFlags: UInt32
    cBytes: UInt32
    id: Byte * 1
class ScopeNamespace(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ebbb48dc-1a3b-4d86-b7-86-c2-1b-28-38-90-12')
    @commethod(7)
    def GetParent(Node: Windows.Win32.System.Mmc.Node_head, Parent: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetChild(Node: Windows.Win32.System.Mmc.Node_head, Child: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNext(Node: Windows.Win32.System.Mmc.Node_head, Next: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRoot(Root: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Expand(Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
class SnapIn(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3be910f6-3459-49c6-a1-bb-41-e6-be-9d-f3-ea')
    @commethod(7)
    def get_Name(Name: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Vendor(Vendor: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Version(Version: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Extensions(Extensions: POINTER(Windows.Win32.System.Mmc.Extensions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SnapinCLSID(SnapinCLSID: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Properties(Properties: POINTER(Windows.Win32.System.Mmc.Properties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableAllExtensions(Enable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class SnapIns(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2ef3de1d-b12a-49d1-92-c5-0b-00-79-87-68-f1')
    @commethod(7)
    def get__NewEnum(retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, SnapIn: POINTER(Windows.Win32.System.Mmc.SnapIn_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(SnapinNameOrCLSID: Windows.Win32.Foundation.BSTR, ParentSnapin: Windows.Win32.System.Com.VARIANT, Properties: Windows.Win32.System.Com.VARIANT, SnapIn: POINTER(Windows.Win32.System.Mmc.SnapIn_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(SnapIn: Windows.Win32.System.Mmc.SnapIn_head) -> Windows.Win32.Foundation.HRESULT: ...
class View(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('6efc2da2-b38c-457e-9a-bb-ed-2d-18-9b-8c-38')
    @commethod(7)
    def get_ActiveScopeNode(Node: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ActiveScopeNode(Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Selection(Nodes: POINTER(Windows.Win32.System.Mmc.Nodes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ListItems(Nodes: POINTER(Windows.Win32.System.Mmc.Nodes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SnapinScopeObject(ScopeNode: Windows.Win32.System.Com.VARIANT, ScopeNodeObject: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SnapinSelectionObject(SelectionObject: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Is(View: Windows.Win32.System.Mmc.View_head, TheSame: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Document(Document: POINTER(Windows.Win32.System.Mmc.Document_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SelectAll() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Select(Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Deselect(Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def IsSelected(Node: Windows.Win32.System.Mmc.Node_head, IsSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DisplayScopeNodePropertySheet(ScopeNode: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DisplaySelectionPropertySheet() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CopyScopeNode(ScopeNode: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CopySelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DeleteScopeNode(ScopeNode: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def RenameScopeNode(NewName: Windows.Win32.Foundation.BSTR, ScopeNode: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RenameSelectedItem(NewName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ScopeNodeContextMenu(ScopeNode: Windows.Win32.System.Com.VARIANT, ContextMenu: POINTER(Windows.Win32.System.Mmc.ContextMenu_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_SelectionContextMenu(ContextMenu: POINTER(Windows.Win32.System.Mmc.ContextMenu_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def RefreshScopeNode(ScopeNode: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def RefreshSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ExecuteSelectionMenuItem(MenuItemPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def ExecuteScopeNodeMenuItem(MenuItemPath: Windows.Win32.Foundation.BSTR, ScopeNode: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ExecuteShellCommand(Command: Windows.Win32.Foundation.BSTR, Directory: Windows.Win32.Foundation.BSTR, Parameters: Windows.Win32.Foundation.BSTR, WindowState: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Frame(Frame: POINTER(Windows.Win32.System.Mmc.Frame_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_ScopeTreeVisible(Visible: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_ScopeTreeVisible(Visible: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def Back() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def Forward() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_StatusBarText(StatusBarText: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_Memento(Memento: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def ViewMemento(Memento: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_Columns(Columns: POINTER(Windows.Win32.System.Mmc.Columns_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_CellContents(Node: Windows.Win32.System.Mmc.Node_head, Column: Int32, CellContents: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def ExportList(File: Windows.Win32.Foundation.BSTR, exportoptions: Windows.Win32.System.Mmc._ExportListOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_ListViewMode(Mode: POINTER(Windows.Win32.System.Mmc._ListViewMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_ListViewMode(mode: Windows.Win32.System.Mmc._ListViewMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_ControlObject(Control: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class Views(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d6b8c29d-a1ff-4d72-aa-b0-e3-81-e9-b9-33-8d')
    @commethod(7)
    def Item(Index: Int32, View: POINTER(Windows.Win32.System.Mmc.View_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Add(Node: Windows.Win32.System.Mmc.Node_head, viewOptions: Windows.Win32.System.Mmc._ViewOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get__NewEnum(retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class _AppEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('de46cbdd-53f5-4635-af-54-4f-e7-1e-92-3d-3f')
    @commethod(7)
    def OnQuit(Application: Windows.Win32.System.Mmc._Application_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnDocumentOpen(Document: Windows.Win32.System.Mmc.Document_head, New: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnDocumentClose(Document: Windows.Win32.System.Mmc.Document_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnSnapInAdded(Document: Windows.Win32.System.Mmc.Document_head, SnapIn: Windows.Win32.System.Mmc.SnapIn_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnSnapInRemoved(Document: Windows.Win32.System.Mmc.Document_head, SnapIn: Windows.Win32.System.Mmc.SnapIn_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnNewView(View: Windows.Win32.System.Mmc.View_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnViewClose(View: Windows.Win32.System.Mmc.View_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnViewChange(View: Windows.Win32.System.Mmc.View_head, NewOwnerNode: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnSelectionChange(View: Windows.Win32.System.Mmc.View_head, NewNodes: Windows.Win32.System.Mmc.Nodes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnContextMenuExecuted(MenuItem: Windows.Win32.System.Mmc.MenuItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnToolbarButtonClicked() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def OnListUpdated(View: Windows.Win32.System.Mmc.View_head) -> Windows.Win32.Foundation.HRESULT: ...
class _Application(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('a3afb9cc-b653-4741-86-ab-f0-47-0e-c1-38-4c')
    @commethod(7)
    def Help() -> Void: ...
    @commethod(8)
    def Quit() -> Void: ...
    @commethod(9)
    def get_Document(Document: POINTER(Windows.Win32.System.Mmc.Document_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Load(Filename: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Frame(Frame: POINTER(Windows.Win32.System.Mmc.Frame_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Visible(Visible: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Show() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Hide() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_UserControl(UserControl: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_UserControl(UserControl: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_VersionMajor(VersionMajor: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_VersionMinor(VersionMinor: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
_ColumnSortOrder = Int32
SortOrder_Ascending: _ColumnSortOrder = 0
SortOrder_Descending: _ColumnSortOrder = 1
_DocumentMode = Int32
DocumentMode_Author: _DocumentMode = 0
DocumentMode_User: _DocumentMode = 1
DocumentMode_User_MDI: _DocumentMode = 2
DocumentMode_User_SDI: _DocumentMode = 3
class _EventConnector(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c0bccd30-de44-4528-84-03-a0-5a-6a-1c-c8-ea')
    @commethod(7)
    def ConnectTo(Application: Windows.Win32.System.Mmc._Application_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Disconnect() -> Windows.Win32.Foundation.HRESULT: ...
_ExportListOptions = Int32
ExportListOptions_Default: _ExportListOptions = 0
ExportListOptions_Unicode: _ExportListOptions = 1
ExportListOptions_TabDelimited: _ExportListOptions = 2
ExportListOptions_SelectedItemsOnly: _ExportListOptions = 4
_ListViewMode = Int32
ListMode_Small_Icons: _ListViewMode = 0
ListMode_Large_Icons: _ListViewMode = 1
ListMode_List: _ListViewMode = 2
ListMode_Detail: _ListViewMode = 3
ListMode_Filtered: _ListViewMode = 4
_ViewOptions = Int32
ViewOption_Default: _ViewOptions = 0
ViewOption_ScopeTreeHidden: _ViewOptions = 1
ViewOption_NoToolBars: _ViewOptions = 2
ViewOption_NotPersistable: _ViewOptions = 4
ViewOption_ActionPaneHidden: _ViewOptions = 8
make_head(_module, 'AppEvents')
make_head(_module, 'CONTEXTMENUITEM')
make_head(_module, 'CONTEXTMENUITEM2')
make_head(_module, 'Column')
make_head(_module, 'Columns')
make_head(_module, 'ContextMenu')
make_head(_module, 'Document')
make_head(_module, 'Extension')
make_head(_module, 'Extensions')
make_head(_module, 'Frame')
make_head(_module, 'IColumnData')
make_head(_module, 'IComponent')
make_head(_module, 'IComponent2')
make_head(_module, 'IComponentData')
make_head(_module, 'IComponentData2')
make_head(_module, 'IConsole')
make_head(_module, 'IConsole2')
make_head(_module, 'IConsole3')
make_head(_module, 'IConsoleNameSpace')
make_head(_module, 'IConsoleNameSpace2')
make_head(_module, 'IConsolePower')
make_head(_module, 'IConsolePowerSink')
make_head(_module, 'IConsoleVerb')
make_head(_module, 'IContextMenuCallback')
make_head(_module, 'IContextMenuCallback2')
make_head(_module, 'IContextMenuProvider')
make_head(_module, 'IControlbar')
make_head(_module, 'IDisplayHelp')
make_head(_module, 'IEnumTASK')
make_head(_module, 'IExtendContextMenu')
make_head(_module, 'IExtendControlbar')
make_head(_module, 'IExtendPropertySheet')
make_head(_module, 'IExtendPropertySheet2')
make_head(_module, 'IExtendTaskPad')
make_head(_module, 'IExtendView')
make_head(_module, 'IHeaderCtrl')
make_head(_module, 'IHeaderCtrl2')
make_head(_module, 'IImageList')
make_head(_module, 'IMMCVersionInfo')
make_head(_module, 'IMenuButton')
make_head(_module, 'IMessageView')
make_head(_module, 'INodeProperties')
make_head(_module, 'IPropertySheetCallback')
make_head(_module, 'IPropertySheetProvider')
make_head(_module, 'IRequiredExtensions')
make_head(_module, 'IResultData')
make_head(_module, 'IResultData2')
make_head(_module, 'IResultDataCompare')
make_head(_module, 'IResultDataCompareEx')
make_head(_module, 'IResultOwnerData')
make_head(_module, 'ISnapinAbout')
make_head(_module, 'ISnapinHelp')
make_head(_module, 'ISnapinHelp2')
make_head(_module, 'ISnapinProperties')
make_head(_module, 'ISnapinPropertiesCallback')
make_head(_module, 'IStringTable')
make_head(_module, 'IToolbar')
make_head(_module, 'IViewExtensionCallback')
make_head(_module, 'MENUBUTTONDATA')
make_head(_module, 'MMCBUTTON')
make_head(_module, 'MMC_COLUMN_DATA')
make_head(_module, 'MMC_COLUMN_SET_DATA')
make_head(_module, 'MMC_EXPANDSYNC_STRUCT')
make_head(_module, 'MMC_EXT_VIEW_DATA')
make_head(_module, 'MMC_FILTERDATA')
make_head(_module, 'MMC_LISTPAD_INFO')
make_head(_module, 'MMC_RESTORE_VIEW')
make_head(_module, 'MMC_SNAPIN_PROPERTY')
make_head(_module, 'MMC_SORT_DATA')
make_head(_module, 'MMC_SORT_SET_DATA')
make_head(_module, 'MMC_TASK')
make_head(_module, 'MMC_TASK_DISPLAY_BITMAP')
make_head(_module, 'MMC_TASK_DISPLAY_OBJECT')
make_head(_module, 'MMC_TASK_DISPLAY_SYMBOL')
make_head(_module, 'MMC_VISIBLE_COLUMNS')
make_head(_module, 'MenuItem')
make_head(_module, 'Node')
make_head(_module, 'Nodes')
make_head(_module, 'Properties')
make_head(_module, 'Property')
make_head(_module, 'RDCOMPARE')
make_head(_module, 'RDITEMHDR')
make_head(_module, 'RESULTDATAITEM')
make_head(_module, 'RESULTFINDINFO')
make_head(_module, 'RESULT_VIEW_TYPE_INFO')
make_head(_module, 'SCOPEDATAITEM')
make_head(_module, 'SColumnSetID')
make_head(_module, 'SMMCDataObjects')
make_head(_module, 'SMMCObjectTypes')
make_head(_module, 'SNodeID')
make_head(_module, 'SNodeID2')
make_head(_module, 'ScopeNamespace')
make_head(_module, 'SnapIn')
make_head(_module, 'SnapIns')
make_head(_module, 'View')
make_head(_module, 'Views')
make_head(_module, '_AppEvents')
make_head(_module, '_Application')
make_head(_module, '_EventConnector')
__all__ = [
    "AUTO_WIDTH",
    "AppEvents",
    "AppEventsDHTMLConnector",
    "Application",
    "BUTTONPRESSED",
    "CCM_COMMANDID_MASK_CONSTANTS",
    "CCM_COMMANDID_MASK_RESERVED",
    "CCM_INSERTIONALLOWED",
    "CCM_INSERTIONALLOWED_NEW",
    "CCM_INSERTIONALLOWED_TASK",
    "CCM_INSERTIONALLOWED_TOP",
    "CCM_INSERTIONALLOWED_VIEW",
    "CCM_INSERTIONPOINTID",
    "CCM_INSERTIONPOINTID_3RDPARTY_NEW",
    "CCM_INSERTIONPOINTID_3RDPARTY_TASK",
    "CCM_INSERTIONPOINTID_MASK_ADD_3RDPARTY",
    "CCM_INSERTIONPOINTID_MASK_ADD_PRIMARY",
    "CCM_INSERTIONPOINTID_MASK_CREATE_PRIMARY",
    "CCM_INSERTIONPOINTID_MASK_FLAGINDEX",
    "CCM_INSERTIONPOINTID_MASK_RESERVED",
    "CCM_INSERTIONPOINTID_MASK_SHARED",
    "CCM_INSERTIONPOINTID_MASK_SPECIAL",
    "CCM_INSERTIONPOINTID_PRIMARY_HELP",
    "CCM_INSERTIONPOINTID_PRIMARY_NEW",
    "CCM_INSERTIONPOINTID_PRIMARY_TASK",
    "CCM_INSERTIONPOINTID_PRIMARY_TOP",
    "CCM_INSERTIONPOINTID_PRIMARY_VIEW",
    "CCM_INSERTIONPOINTID_ROOT_MENU",
    "CCM_SPECIAL",
    "CCM_SPECIAL_DEFAULT_ITEM",
    "CCM_SPECIAL_INSERTION_POINT",
    "CCM_SPECIAL_SEPARATOR",
    "CCM_SPECIAL_SUBMENU",
    "CCM_SPECIAL_TESTONLY",
    "CCT_RESULT",
    "CCT_SCOPE",
    "CCT_SNAPIN_MANAGER",
    "CCT_UNINITIALIZED",
    "CHECKED",
    "COMBOBOXBAR",
    "CONTEXTMENUITEM",
    "CONTEXTMENUITEM2",
    "Column",
    "Columns",
    "ConsolePower",
    "ContextMenu",
    "DATA_OBJECT_TYPES",
    "Document",
    "DocumentMode_Author",
    "DocumentMode_User",
    "DocumentMode_User_MDI",
    "DocumentMode_User_SDI",
    "ENABLED",
    "ExportListOptions_Default",
    "ExportListOptions_SelectedItemsOnly",
    "ExportListOptions_TabDelimited",
    "ExportListOptions_Unicode",
    "Extension",
    "Extensions",
    "Frame",
    "HDI_HIDDEN",
    "HIDDEN",
    "HIDE_COLUMN",
    "IColumnData",
    "IComponent",
    "IComponent2",
    "IComponentData",
    "IComponentData2",
    "IConsole",
    "IConsole2",
    "IConsole3",
    "IConsoleNameSpace",
    "IConsoleNameSpace2",
    "IConsolePower",
    "IConsolePowerSink",
    "IConsoleVerb",
    "IContextMenuCallback",
    "IContextMenuCallback2",
    "IContextMenuProvider",
    "IControlbar",
    "IDisplayHelp",
    "IEnumTASK",
    "IExtendContextMenu",
    "IExtendControlbar",
    "IExtendPropertySheet",
    "IExtendPropertySheet2",
    "IExtendTaskPad",
    "IExtendView",
    "IHeaderCtrl",
    "IHeaderCtrl2",
    "IImageList",
    "ILSIF_LEAVE_LARGE_ICON",
    "ILSIF_LEAVE_SMALL_ICON",
    "IMMCVersionInfo",
    "IMenuButton",
    "IMessageView",
    "INDETERMINATE",
    "INodeProperties",
    "IPropertySheetCallback",
    "IPropertySheetProvider",
    "IRequiredExtensions",
    "IResultData",
    "IResultData2",
    "IResultDataCompare",
    "IResultDataCompareEx",
    "IResultOwnerData",
    "ISnapinAbout",
    "ISnapinHelp",
    "ISnapinHelp2",
    "ISnapinProperties",
    "ISnapinPropertiesCallback",
    "IStringTable",
    "IToolbar",
    "IViewExtensionCallback",
    "IconIdentifier",
    "Icon_Error",
    "Icon_First",
    "Icon_Information",
    "Icon_Last",
    "Icon_None",
    "Icon_Question",
    "Icon_Warning",
    "ListMode_Detail",
    "ListMode_Filtered",
    "ListMode_Large_Icons",
    "ListMode_List",
    "ListMode_Small_Icons",
    "MENUBUTTON",
    "MENUBUTTONDATA",
    "MFCC_DISABLE",
    "MFCC_ENABLE",
    "MFCC_VALUE_CHANGE",
    "MMCBUTTON",
    "MMCC_STANDARD_VIEW_SELECT",
    "MMCLV_AUTO",
    "MMCLV_NOICON",
    "MMCLV_NOPARAM",
    "MMCLV_NOPTR",
    "MMCLV_UPDATE_NOINVALIDATEALL",
    "MMCLV_UPDATE_NOSCROLL",
    "MMCLV_VIEWSTYLE_FILTERED",
    "MMCLV_VIEWSTYLE_ICON",
    "MMCLV_VIEWSTYLE_LIST",
    "MMCLV_VIEWSTYLE_REPORT",
    "MMCLV_VIEWSTYLE_SMALLICON",
    "MMCN_ACTIVATE",
    "MMCN_ADD_IMAGES",
    "MMCN_BTN_CLICK",
    "MMCN_CANPASTE_OUTOFPROC",
    "MMCN_CLICK",
    "MMCN_COLUMNS_CHANGED",
    "MMCN_COLUMN_CLICK",
    "MMCN_CONTEXTHELP",
    "MMCN_CONTEXTMENU",
    "MMCN_CUTORMOVE",
    "MMCN_DBLCLICK",
    "MMCN_DELETE",
    "MMCN_DESELECT_ALL",
    "MMCN_EXPAND",
    "MMCN_EXPANDSYNC",
    "MMCN_FILTERBTN_CLICK",
    "MMCN_FILTER_CHANGE",
    "MMCN_HELP",
    "MMCN_INITOCX",
    "MMCN_LISTPAD",
    "MMCN_MENU_BTNCLICK",
    "MMCN_MINIMIZED",
    "MMCN_PASTE",
    "MMCN_PRELOAD",
    "MMCN_PRINT",
    "MMCN_PROPERTY_CHANGE",
    "MMCN_QUERY_PASTE",
    "MMCN_REFRESH",
    "MMCN_REMOVE_CHILDREN",
    "MMCN_RENAME",
    "MMCN_RESTORE_VIEW",
    "MMCN_SELECT",
    "MMCN_SHOW",
    "MMCN_SNAPINHELP",
    "MMCN_VIEW_CHANGE",
    "MMCVersionInfo",
    "MMC_ACTION_ID",
    "MMC_ACTION_LINK",
    "MMC_ACTION_SCRIPT",
    "MMC_ACTION_TYPE",
    "MMC_ACTION_UNINITIALIZED",
    "MMC_BUTTON_STATE",
    "MMC_COLUMN_DATA",
    "MMC_COLUMN_SET_DATA",
    "MMC_CONSOLE_VERB",
    "MMC_CONTROL_TYPE",
    "MMC_DEFAULT_OPERATION_COPY",
    "MMC_ENSUREFOCUSVISIBLE",
    "MMC_EXPANDSYNC_STRUCT",
    "MMC_EXT_VIEW_DATA",
    "MMC_FILTERDATA",
    "MMC_FILTER_CHANGE_CODE",
    "MMC_FILTER_NOVALUE",
    "MMC_FILTER_TYPE",
    "MMC_IMAGECALLBACK",
    "MMC_INT_FILTER",
    "MMC_ITEM_OVERLAY_STATE_MASK",
    "MMC_ITEM_OVERLAY_STATE_SHIFT",
    "MMC_ITEM_STATE_MASK",
    "MMC_LISTPAD_INFO",
    "MMC_MENU_COMMAND_IDS",
    "MMC_MULTI_SELECT_COOKIE",
    "MMC_NODEID_SLOW_RETRIEVAL",
    "MMC_NOSORTHEADER",
    "MMC_NOTIFY_TYPE",
    "MMC_NW_OPTION_CUSTOMTITLE",
    "MMC_NW_OPTION_NOACTIONPANE",
    "MMC_NW_OPTION_NONE",
    "MMC_NW_OPTION_NOPERSIST",
    "MMC_NW_OPTION_NOSCOPEPANE",
    "MMC_NW_OPTION_NOTOOLBARS",
    "MMC_NW_OPTION_SHORTTITLE",
    "MMC_PROPACT_CHANGING",
    "MMC_PROPACT_DELETING",
    "MMC_PROPACT_INITIALIZED",
    "MMC_PROPERTY_ACTION",
    "MMC_PROP_CHANGEAFFECTSUI",
    "MMC_PROP_MODIFIABLE",
    "MMC_PROP_PERSIST",
    "MMC_PROP_REMOVABLE",
    "MMC_PSO_HASHELP",
    "MMC_PSO_NEWWIZARDTYPE",
    "MMC_PSO_NOAPPLYNOW",
    "MMC_PSO_NO_PROPTITLE",
    "MMC_RESTORE_VIEW",
    "MMC_RESULT_VIEW_STYLE",
    "MMC_SCOPE_ITEM_STATE",
    "MMC_SCOPE_ITEM_STATE_BOLD",
    "MMC_SCOPE_ITEM_STATE_EXPANDEDONCE",
    "MMC_SCOPE_ITEM_STATE_NORMAL",
    "MMC_SHOWSELALWAYS",
    "MMC_SINGLESEL",
    "MMC_SNAPIN_PROPERTY",
    "MMC_SORT_DATA",
    "MMC_SORT_SET_DATA",
    "MMC_STRING_FILTER",
    "MMC_TASK",
    "MMC_TASK_DISPLAY_BITMAP",
    "MMC_TASK_DISPLAY_OBJECT",
    "MMC_TASK_DISPLAY_SYMBOL",
    "MMC_TASK_DISPLAY_TYPE",
    "MMC_TASK_DISPLAY_TYPE_BITMAP",
    "MMC_TASK_DISPLAY_TYPE_CHOCOLATE_GIF",
    "MMC_TASK_DISPLAY_TYPE_SYMBOL",
    "MMC_TASK_DISPLAY_TYPE_VANILLA_GIF",
    "MMC_TASK_DISPLAY_UNINITIALIZED",
    "MMC_VER",
    "MMC_VERB_COPY",
    "MMC_VERB_CUT",
    "MMC_VERB_DELETE",
    "MMC_VERB_FIRST",
    "MMC_VERB_LAST",
    "MMC_VERB_MAX",
    "MMC_VERB_NONE",
    "MMC_VERB_OPEN",
    "MMC_VERB_PASTE",
    "MMC_VERB_PRINT",
    "MMC_VERB_PROPERTIES",
    "MMC_VERB_REFRESH",
    "MMC_VERB_RENAME",
    "MMC_VIEW_OPTIONS_CREATENEW",
    "MMC_VIEW_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST",
    "MMC_VIEW_OPTIONS_FILTERED",
    "MMC_VIEW_OPTIONS_LEXICAL_SORT",
    "MMC_VIEW_OPTIONS_MULTISELECT",
    "MMC_VIEW_OPTIONS_NOLISTVIEWS",
    "MMC_VIEW_OPTIONS_NONE",
    "MMC_VIEW_OPTIONS_OWNERDATALIST",
    "MMC_VIEW_OPTIONS_USEFONTLINKING",
    "MMC_VIEW_TYPE",
    "MMC_VIEW_TYPE_HTML",
    "MMC_VIEW_TYPE_LIST",
    "MMC_VIEW_TYPE_OCX",
    "MMC_VISIBLE_COLUMNS",
    "MMC_WINDOW_COOKIE",
    "MenuItem",
    "Node",
    "Nodes",
    "Properties",
    "Property",
    "RDCI_ScopeItem",
    "RDCOMPARE",
    "RDITEMHDR",
    "RDI_IMAGE",
    "RDI_INDENT",
    "RDI_INDEX",
    "RDI_PARAM",
    "RDI_STATE",
    "RDI_STR",
    "RESULTDATAITEM",
    "RESULTFINDINFO",
    "RESULT_VIEW_TYPE_INFO",
    "RFI_PARTIAL",
    "RFI_WRAP",
    "RSI_DESCENDING",
    "RSI_NOSORTICON",
    "RVTI_HTML_OPTIONS_NOLISTVIEW",
    "RVTI_HTML_OPTIONS_NONE",
    "RVTI_LIST_OPTIONS_ALLOWPASTE",
    "RVTI_LIST_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST",
    "RVTI_LIST_OPTIONS_FILTERED",
    "RVTI_LIST_OPTIONS_LEXICAL_SORT",
    "RVTI_LIST_OPTIONS_MULTISELECT",
    "RVTI_LIST_OPTIONS_NONE",
    "RVTI_LIST_OPTIONS_OWNERDATALIST",
    "RVTI_LIST_OPTIONS_USEFONTLINKING",
    "RVTI_MISC_OPTIONS_NOLISTVIEWS",
    "RVTI_OCX_OPTIONS_CACHE_OCX",
    "RVTI_OCX_OPTIONS_NOLISTVIEW",
    "RVTI_OCX_OPTIONS_NONE",
    "SCOPEDATAITEM",
    "SColumnSetID",
    "SDI_CHILDREN",
    "SDI_FIRST",
    "SDI_IMAGE",
    "SDI_NEXT",
    "SDI_OPENIMAGE",
    "SDI_PARAM",
    "SDI_PARENT",
    "SDI_PREVIOUS",
    "SDI_STATE",
    "SDI_STR",
    "SMMCDataObjects",
    "SMMCObjectTypes",
    "SNodeID",
    "SNodeID2",
    "SPECIAL_COOKIE_MAX",
    "SPECIAL_COOKIE_MIN",
    "SPECIAL_DOBJ_MAX",
    "SPECIAL_DOBJ_MIN",
    "ScopeNamespace",
    "SnapIn",
    "SnapIns",
    "SortOrder_Ascending",
    "SortOrder_Descending",
    "TOOLBAR",
    "View",
    "ViewOption_ActionPaneHidden",
    "ViewOption_Default",
    "ViewOption_NoToolBars",
    "ViewOption_NotPersistable",
    "ViewOption_ScopeTreeHidden",
    "Views",
    "_AppEvents",
    "_Application",
    "_ColumnSortOrder",
    "_DocumentMode",
    "_EventConnector",
    "_ExportListOptions",
    "_ListViewMode",
    "_ViewOptions",
]
_arch_optional = [
]