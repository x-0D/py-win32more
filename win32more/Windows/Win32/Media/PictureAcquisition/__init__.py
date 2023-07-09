from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Media.PictureAcquisition
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
import win32more.Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def PKEY_PhotoAcquire_RelativePathname():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=2)
def PKEY_PhotoAcquire_FinalFilename():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=3)
def PKEY_PhotoAcquire_GroupTag():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=4)
def PKEY_PhotoAcquire_TransferResult():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=5)
def PKEY_PhotoAcquire_OriginalFilename():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=6)
def PKEY_PhotoAcquire_CameraSequenceNumber():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=7)
def PKEY_PhotoAcquire_IntermediateFile():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=8)
def PKEY_PhotoAcquire_SkipImport():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=9)
def PKEY_PhotoAcquire_DuplicateDetectionID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{00f23377-7ac6-4b7a-8443-345e731fa57a}'), pid=10)
PROGRESS_INDETERMINATE: Int32 = -1
PHOTOACQ_ERROR_RESTART_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -2147180543
PHOTOACQ_RUN_DEFAULT: UInt32 = 0
PHOTOACQ_NO_GALLERY_LAUNCH: UInt32 = 1
PHOTOACQ_DISABLE_AUTO_ROTATE: UInt32 = 2
PHOTOACQ_DISABLE_PLUGINS: UInt32 = 4
PHOTOACQ_DISABLE_GROUP_TAG_PROMPT: UInt32 = 8
PHOTOACQ_DISABLE_DB_INTEGRATION: UInt32 = 16
PHOTOACQ_DELETE_AFTER_ACQUIRE: UInt32 = 32
PHOTOACQ_DISABLE_DUPLICATE_DETECTION: UInt32 = 64
PHOTOACQ_ENABLE_THUMBNAIL_CACHING: UInt32 = 128
PHOTOACQ_DISABLE_METADATA_WRITE: UInt32 = 256
PHOTOACQ_DISABLE_THUMBNAIL_PROGRESS: UInt32 = 512
PHOTOACQ_DISABLE_SETTINGS_LINK: UInt32 = 1024
PHOTOACQ_ABORT_ON_SETTINGS_UPDATE: UInt32 = 2048
PHOTOACQ_IMPORT_VIDEO_AS_MULTIPLE_FILES: UInt32 = 4096
DSF_WPD_DEVICES: UInt32 = 1
DSF_WIA_CAMERAS: UInt32 = 2
DSF_WIA_SCANNERS: UInt32 = 4
DSF_STI_DEVICES: UInt32 = 8
DSF_TWAIN_DEVICES: UInt32 = 16
DSF_FS_DEVICES: UInt32 = 32
DSF_DV_DEVICES: UInt32 = 64
DSF_ALL_DEVICES: UInt32 = 65535
DSF_CPL_MODE: UInt32 = 65536
DSF_SHOW_OFFLINE: UInt32 = 131072
PAPS_PRESAVE: UInt32 = 0
PAPS_POSTSAVE: UInt32 = 1
PAPS_CLEANUP: UInt32 = 2
DEVICE_SELECTION_DEVICE_TYPE = Int32
DST_UNKNOWN_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 0
DST_WPD_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 1
DST_WIA_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 2
DST_STI_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 3
DSF_TWAIN_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 4
DST_FS_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 5
DST_DV_DEVICE: DEVICE_SELECTION_DEVICE_TYPE = 6
ERROR_ADVISE_MESSAGE_TYPE = Int32
PHOTOACQUIRE_ERROR_SKIPRETRYCANCEL: ERROR_ADVISE_MESSAGE_TYPE = 0
PHOTOACQUIRE_ERROR_RETRYCANCEL: ERROR_ADVISE_MESSAGE_TYPE = 1
PHOTOACQUIRE_ERROR_YESNO: ERROR_ADVISE_MESSAGE_TYPE = 2
PHOTOACQUIRE_ERROR_OK: ERROR_ADVISE_MESSAGE_TYPE = 3
ERROR_ADVISE_RESULT = Int32
PHOTOACQUIRE_RESULT_YES: ERROR_ADVISE_RESULT = 0
PHOTOACQUIRE_RESULT_NO: ERROR_ADVISE_RESULT = 1
PHOTOACQUIRE_RESULT_OK: ERROR_ADVISE_RESULT = 2
PHOTOACQUIRE_RESULT_SKIP: ERROR_ADVISE_RESULT = 3
PHOTOACQUIRE_RESULT_SKIP_ALL: ERROR_ADVISE_RESULT = 4
PHOTOACQUIRE_RESULT_RETRY: ERROR_ADVISE_RESULT = 5
PHOTOACQUIRE_RESULT_ABORT: ERROR_ADVISE_RESULT = 6
class IPhotoAcquire(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f23353-e31b-4955-a8ad-ca5ebf31e2ce}')
    @commethod(3)
    def CreatePhotoSource(self, pszDevice: win32more.Windows.Win32.Foundation.PWSTR, ppPhotoAcquireSource: POINTER(win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireSource_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Acquire(self, pPhotoAcquireSource: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireSource_head, fShowProgress: win32more.Windows.Win32.Foundation.BOOL, hWndParent: win32more.Windows.Win32.Foundation.HWND, pszApplicationName: win32more.Windows.Win32.Foundation.PWSTR, pPhotoAcquireProgressCB: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireProgressCB_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumResults(self, ppEnumFilePaths: POINTER(win32more.Windows.Win32.System.Com.IEnumString_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoAcquireDeviceSelectionDialog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f28837-55dd-4f37-aaf5-6855a9640467}')
    @commethod(3)
    def SetTitle(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSubmitButtonText(self, pszSubmitButtonText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoModal(self, hWndParent: win32more.Windows.Win32.Foundation.HWND, dwDeviceFlags: UInt32, pbstrDeviceId: POINTER(win32more.Windows.Win32.Foundation.BSTR), pnDeviceType: POINTER(win32more.Windows.Win32.Media.PictureAcquisition.DEVICE_SELECTION_DEVICE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoAcquireItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f21c97-28bf-4c02-b842-5e4e90139a30}')
    @commethod(3)
    def GetItemName(self, pbstrItemName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetThumbnail(self, sizeThumbnail: win32more.Windows.Win32.Foundation.SIZE, phbmpThumbnail: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProperty(self, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProperty(self, key: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStream(self, ppStream: POINTER(win32more.Windows.Win32.System.Com.IStream_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CanDelete(self, pfCanDelete: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSubItemCount(self, pnCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSubItemAt(self, nItemIndex: UInt32, ppPhotoAcquireItem: POINTER(win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoAcquireOptionsDialog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f2b3ee-bf64-47ee-89f4-4dedd79643f2}')
    @commethod(3)
    def Initialize(self, pszRegistryRoot: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Create(self, hWndParent: win32more.Windows.Win32.Foundation.HWND, phWndDialog: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Destroy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DoModal(self, hWndParent: win32more.Windows.Win32.Foundation.HWND, ppnReturnCode: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SaveData(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoAcquirePlugin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f2dceb-ecb8-4f77-8e47-e7a987c83dd0}')
    @commethod(3)
    def Initialize(self, pPhotoAcquireSource: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireSource_head, pPhotoAcquireProgressCB: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireProgressCB_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessItem(self, dwAcquireStage: UInt32, pPhotoAcquireItem: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head, pOriginalItemStream: win32more.Windows.Win32.System.Com.IStream_head, pszFinalFilename: win32more.Windows.Win32.Foundation.PWSTR, pPropertyStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransferComplete(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisplayConfigureDialog(self, hWndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoAcquireProgressCB(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f2ce1e-935e-4248-892c-130f32c45cb4}')
    @commethod(3)
    def Cancelled(self, pfCancelled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartEnumeration(self, pPhotoAcquireSource: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireSource_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FoundItem(self, pPhotoAcquireItem: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndEnumeration(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def StartTransfer(self, pPhotoAcquireSource: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireSource_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StartItemTransfer(self, nItemIndex: UInt32, pPhotoAcquireItem: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DirectoryCreated(self, pszDirectory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UpdateTransferPercent(self, fOverall: win32more.Windows.Win32.Foundation.BOOL, nPercent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EndItemTransfer(self, nItemIndex: UInt32, pPhotoAcquireItem: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EndTransfer(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StartDelete(self, pPhotoAcquireSource: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireSource_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def StartItemDelete(self, nItemIndex: UInt32, pPhotoAcquireItem: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UpdateDeletePercent(self, nPercent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EndItemDelete(self, nItemIndex: UInt32, pPhotoAcquireItem: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EndDelete(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EndSession(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDeleteAfterAcquire(self, pfDeleteAfterAcquire: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ErrorAdvise(self, hr: win32more.Windows.Win32.Foundation.HRESULT, pszErrorMessage: win32more.Windows.Win32.Foundation.PWSTR, nMessageType: win32more.Windows.Win32.Media.PictureAcquisition.ERROR_ADVISE_MESSAGE_TYPE, pnErrorAdviseResult: POINTER(win32more.Windows.Win32.Media.PictureAcquisition.ERROR_ADVISE_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetUserInput(self, riidType: POINTER(Guid), pUnknown: win32more.Windows.Win32.System.Com.IUnknown_head, pPropVarResult: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pPropVarDefault: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoAcquireSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f2b868-dd67-487c-9553-049240767e91}')
    @commethod(3)
    def InitializeFromRegistry(self, pszRegistryKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFlags(self, dwPhotoAcquireFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOutputFilenameTemplate(self, pszTemplate: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSequencePaddingWidth(self, dwWidth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSequenceZeroPadding(self, fZeroPad: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetGroupTag(self, pszGroupTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetAcquisitionTime(self, pftAcquisitionTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFlags(self, pdwPhotoAcquireFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputFilenameTemplate(self, pbstrTemplate: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSequencePaddingWidth(self, pdwWidth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSequenceZeroPadding(self, pfZeroPad: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetGroupTag(self, pbstrGroupTag: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetAcquisitionTime(self, pftAcquisitionTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoAcquireSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f2c703-8613-4282-a53b-6ec59c5883ac}')
    @commethod(3)
    def GetFriendlyName(self, pbstrFriendlyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceIcons(self, nSize: UInt32, phLargeIcon: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), phSmallIcon: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitializeItemList(self, fForceEnumeration: win32more.Windows.Win32.Foundation.BOOL, pPhotoAcquireProgressCB: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireProgressCB_head, pnItemCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemCount(self, pnItemCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetItemAt(self, nIndex: UInt32, ppPhotoAcquireItem: POINTER(win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireItem_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPhotoAcquireSettings(self, ppPhotoAcquireSettings: POINTER(win32more.Windows.Win32.Media.PictureAcquisition.IPhotoAcquireSettings_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDeviceId(self, pbstrDeviceId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BindToObject(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoProgressActionCB(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f242d0-b206-4e7d-b4c1-4755bcbb9c9f}')
    @commethod(3)
    def DoAction(self, hWndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPhotoProgressDialog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f246f9-0750-4f08-9381-2cd8e906a4ae}')
    @commethod(3)
    def Create(self, hwndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWindow(self, phwndProgressDialog: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Destroy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTitle(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowCheckbox(self, nCheckboxId: win32more.Windows.Win32.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetCheckboxText(self, nCheckboxId: win32more.Windows.Win32.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, pszCheckboxText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetCheckboxCheck(self, nCheckboxId: win32more.Windows.Win32.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, fChecked: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCheckboxTooltip(self, nCheckboxId: win32more.Windows.Win32.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, pszCheckboxTooltipText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsCheckboxChecked(self, nCheckboxId: win32more.Windows.Win32.Media.PictureAcquisition.PROGRESS_DIALOG_CHECKBOX_ID, pfChecked: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCaption(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetImage(self, nImageType: win32more.Windows.Win32.Media.PictureAcquisition.PROGRESS_DIALOG_IMAGE_TYPE, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, hBitmap: win32more.Windows.Win32.Graphics.Gdi.HBITMAP) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetPercentComplete(self, nPercent: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetProgressText(self, pszProgressText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetActionLinkCallback(self, pPhotoProgressActionCB: win32more.Windows.Win32.Media.PictureAcquisition.IPhotoProgressActionCB_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetActionLinkText(self, pszCaption: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ShowActionLink(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def IsCancelled(self, pfCancelled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetUserInput(self, riidType: POINTER(Guid), pUnknown: win32more.Windows.Win32.System.Com.IUnknown_head, pPropVarResult: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pPropVarDefault: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserInputString(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00f243a1-205b-45ba-ae26-abbc53aa7a6f}')
    @commethod(3)
    def GetSubmitButtonText(self, pbstrSubmitButtonText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPrompt(self, pbstrPromptTitle: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringId(self, pbstrStringId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringType(self, pnStringType: POINTER(win32more.Windows.Win32.Media.PictureAcquisition.USER_INPUT_STRING_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTooltipText(self, pbstrTooltipText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMaxLength(self, pcchMaxLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDefault(self, pbstrDefault: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMruCount(self, pnMruCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMruEntryAt(self, nIndex: UInt32, pbstrMruEntry: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetImage(self, nSize: UInt32, phBitmap: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP), phIcon: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PROGRESS_DIALOG_CHECKBOX_ID = Int32
PROGRESS_DIALOG_CHECKBOX_ID_DEFAULT: PROGRESS_DIALOG_CHECKBOX_ID = 0
PROGRESS_DIALOG_IMAGE_TYPE = Int32
PROGRESS_DIALOG_ICON_SMALL: PROGRESS_DIALOG_IMAGE_TYPE = 0
PROGRESS_DIALOG_ICON_LARGE: PROGRESS_DIALOG_IMAGE_TYPE = 1
PROGRESS_DIALOG_ICON_THUMBNAIL: PROGRESS_DIALOG_IMAGE_TYPE = 2
PROGRESS_DIALOG_BITMAP_THUMBNAIL: PROGRESS_DIALOG_IMAGE_TYPE = 3
PhotoAcquire = Guid('{00f26e02-e9f2-4a9f-9fdd-5a962fb26a98}')
PhotoAcquireAutoPlayDropTarget = Guid('{00f20eb5-8fd6-4d9d-b75e-36801766c8f1}')
PhotoAcquireAutoPlayHWEventHandler = Guid('{00f2b433-44e4-4d88-b2b0-2698a0a91dba}')
PhotoAcquireDeviceSelectionDialog = Guid('{00f29a34-b8a1-482c-bcf8-3ac7b0fe8f62}')
PhotoAcquireOptionsDialog = Guid('{00f210a1-62f0-438b-9f7e-9618d72a1831}')
PhotoProgressDialog = Guid('{00f24ca0-748f-4e8a-894f-0e0357c6799f}')
USER_INPUT_STRING_TYPE = Int32
USER_INPUT_DEFAULT: USER_INPUT_STRING_TYPE = 0
USER_INPUT_PATH_ELEMENT: USER_INPUT_STRING_TYPE = 1
make_head(_module, 'PKEY_PhotoAcquire_RelativePathname')
make_head(_module, 'PKEY_PhotoAcquire_FinalFilename')
make_head(_module, 'PKEY_PhotoAcquire_GroupTag')
make_head(_module, 'PKEY_PhotoAcquire_TransferResult')
make_head(_module, 'PKEY_PhotoAcquire_OriginalFilename')
make_head(_module, 'PKEY_PhotoAcquire_CameraSequenceNumber')
make_head(_module, 'PKEY_PhotoAcquire_IntermediateFile')
make_head(_module, 'PKEY_PhotoAcquire_SkipImport')
make_head(_module, 'PKEY_PhotoAcquire_DuplicateDetectionID')
make_head(_module, 'IPhotoAcquire')
make_head(_module, 'IPhotoAcquireDeviceSelectionDialog')
make_head(_module, 'IPhotoAcquireItem')
make_head(_module, 'IPhotoAcquireOptionsDialog')
make_head(_module, 'IPhotoAcquirePlugin')
make_head(_module, 'IPhotoAcquireProgressCB')
make_head(_module, 'IPhotoAcquireSettings')
make_head(_module, 'IPhotoAcquireSource')
make_head(_module, 'IPhotoProgressActionCB')
make_head(_module, 'IPhotoProgressDialog')
make_head(_module, 'IUserInputString')