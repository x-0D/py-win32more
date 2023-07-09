from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.SystemServices
import win32more.Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ADVANCED_FEATURE_FLAGS = UInt16
FADF_AUTO: ADVANCED_FEATURE_FLAGS = 1
FADF_STATIC: ADVANCED_FEATURE_FLAGS = 2
FADF_EMBEDDED: ADVANCED_FEATURE_FLAGS = 4
FADF_FIXEDSIZE: ADVANCED_FEATURE_FLAGS = 16
FADF_RECORD: ADVANCED_FEATURE_FLAGS = 32
FADF_HAVEIID: ADVANCED_FEATURE_FLAGS = 64
FADF_HAVEVARTYPE: ADVANCED_FEATURE_FLAGS = 128
FADF_BSTR: ADVANCED_FEATURE_FLAGS = 256
FADF_UNKNOWN: ADVANCED_FEATURE_FLAGS = 512
FADF_DISPATCH: ADVANCED_FEATURE_FLAGS = 1024
FADF_VARIANT: ADVANCED_FEATURE_FLAGS = 2048
FADF_RESERVED: ADVANCED_FEATURE_FLAGS = 61448
ADVF = Int32
ADVF_NODATA: ADVF = 1
ADVF_PRIMEFIRST: ADVF = 2
ADVF_ONLYONCE: ADVF = 4
ADVF_DATAONSTOP: ADVF = 64
ADVFCACHE_NOHANDLER: ADVF = 8
ADVFCACHE_FORCEBUILTIN: ADVF = 16
ADVFCACHE_ONSAVE: ADVF = 32
APTTYPE = Int32
APTTYPE_CURRENT: APTTYPE = -1
APTTYPE_STA: APTTYPE = 0
APTTYPE_MTA: APTTYPE = 1
APTTYPE_NA: APTTYPE = 2
APTTYPE_MAINSTA: APTTYPE = 3
APTTYPEQUALIFIER = Int32
APTTYPEQUALIFIER_NONE: APTTYPEQUALIFIER = 0
APTTYPEQUALIFIER_IMPLICIT_MTA: APTTYPEQUALIFIER = 1
APTTYPEQUALIFIER_NA_ON_MTA: APTTYPEQUALIFIER = 2
APTTYPEQUALIFIER_NA_ON_STA: APTTYPEQUALIFIER = 3
APTTYPEQUALIFIER_NA_ON_IMPLICIT_MTA: APTTYPEQUALIFIER = 4
APTTYPEQUALIFIER_NA_ON_MAINSTA: APTTYPEQUALIFIER = 5
APTTYPEQUALIFIER_APPLICATION_STA: APTTYPEQUALIFIER = 6
APTTYPEQUALIFIER_RESERVED_1: APTTYPEQUALIFIER = 7
class AUTHENTICATEINFO(EasyCastStructure):
    dwFlags: UInt32
    dwReserved: UInt32
COLE_DEFAULT_PRINCIPAL: win32more.Windows.Win32.Foundation.PWSTR = -1
COLE_DEFAULT_AUTHINFO: Int32 = -1
MARSHALINTERFACE_MIN: UInt32 = 500
ASYNC_MODE_COMPATIBILITY: Int32 = 1
ASYNC_MODE_DEFAULT: Int32 = 0
STGTY_REPEAT: Int32 = 256
STG_TOEND: Int32 = -1
STG_LAYOUT_SEQUENTIAL: Int32 = 0
STG_LAYOUT_INTERLEAVED: Int32 = 1
COM_RIGHTS_EXECUTE: UInt32 = 1
COM_RIGHTS_EXECUTE_LOCAL: UInt32 = 2
COM_RIGHTS_EXECUTE_REMOTE: UInt32 = 4
COM_RIGHTS_ACTIVATE_LOCAL: UInt32 = 8
COM_RIGHTS_ACTIVATE_REMOTE: UInt32 = 16
COM_RIGHTS_RESERVED1: UInt32 = 32
COM_RIGHTS_RESERVED2: UInt32 = 64
CWMO_MAX_HANDLES: UInt32 = 56
ROTREGFLAGS_ALLOWANYCLIENT: UInt32 = 1
APPIDREGFLAGS_ACTIVATE_IUSERVER_INDESKTOP: UInt32 = 1
APPIDREGFLAGS_SECURE_SERVER_PROCESS_SD_AND_BIND: UInt32 = 2
APPIDREGFLAGS_ISSUE_ACTIVATION_RPC_AT_IDENTIFY: UInt32 = 4
APPIDREGFLAGS_IUSERVER_UNMODIFIED_LOGON_TOKEN: UInt32 = 8
APPIDREGFLAGS_IUSERVER_SELF_SID_IN_LAUNCH_PERMISSION: UInt32 = 16
APPIDREGFLAGS_IUSERVER_ACTIVATE_IN_CLIENT_SESSION_ONLY: UInt32 = 32
APPIDREGFLAGS_RESERVED1: UInt32 = 64
APPIDREGFLAGS_RESERVED2: UInt32 = 128
APPIDREGFLAGS_RESERVED3: UInt32 = 256
APPIDREGFLAGS_RESERVED4: UInt32 = 512
APPIDREGFLAGS_RESERVED5: UInt32 = 1024
APPIDREGFLAGS_AAA_NO_IMPLICIT_ACTIVATE_AS_IU: UInt32 = 2048
APPIDREGFLAGS_RESERVED7: UInt32 = 4096
APPIDREGFLAGS_RESERVED8: UInt32 = 8192
APPIDREGFLAGS_RESERVED9: UInt32 = 16384
DCOMSCM_ACTIVATION_USE_ALL_AUTHNSERVICES: UInt32 = 1
DCOMSCM_ACTIVATION_DISALLOW_UNSECURE_CALL: UInt32 = 2
DCOMSCM_RESOLVE_USE_ALL_AUTHNSERVICES: UInt32 = 4
DCOMSCM_RESOLVE_DISALLOW_UNSECURE_CALL: UInt32 = 8
DCOMSCM_PING_USE_MID_AUTHNSERVICE: UInt32 = 16
DCOMSCM_PING_DISALLOW_UNSECURE_CALL: UInt32 = 32
MAXLSN: UInt64 = 9223372036854775807
DMUS_ERRBASE: UInt32 = 4096
@winfunctype('ole32.dll')
def CoBuildVersion() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoInitialize(pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterMallocSpy(pMallocSpy: win32more.Windows.Win32.System.Com.IMallocSpy_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeMallocSpy() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterInitializeSpy(pSpy: win32more.Windows.Win32.System.Com.IInitializeSpy_head, puliCookie: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeInitializeSpy(uliCookie: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetSystemSecurityPermissions(comSDType: win32more.Windows.Win32.System.Com.COMSD, ppSD: POINTER(win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoLoadLibrary(lpszLibName: win32more.Windows.Win32.Foundation.PWSTR, bAutoFree: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('OLE32.dll')
def CoFreeLibrary(hInst: win32more.Windows.Win32.Foundation.HINSTANCE) -> Void: ...
@winfunctype('OLE32.dll')
def CoFreeAllLibraries() -> Void: ...
@winfunctype('OLE32.dll')
def CoAllowSetForegroundWindow(pUnk: win32more.Windows.Win32.System.Com.IUnknown_head, lpvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def DcomChannelSetHResult(pvReserved: VoidPtr, pulReserved: POINTER(UInt32), appsHR: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoIsOle1Class(rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CLSIDFromProgIDEx(lpszProgID: win32more.Windows.Win32.Foundation.PWSTR, lpclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoFileTimeToDosDateTime(lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head), lpDosDate: POINTER(UInt16), lpDosTime: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CoDosDateTimeToFileTime(nDosDate: UInt16, nDosTime: UInt16, lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CoFileTimeNow(lpFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoRegisterChannelHook(ExtensionUuid: POINTER(Guid), pChannelHook: win32more.Windows.Win32.System.Com.IChannelHook_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoTreatAsClass(clsidOld: POINTER(Guid), clsidNew: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateDataAdviseHolder(ppDAHolder: POINTER(win32more.Windows.Win32.System.Com.IDataAdviseHolder_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateDataCache(pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, rclsid: POINTER(Guid), iid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoInstall(pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, dwFlags: UInt32, pClassSpec: POINTER(win32more.Windows.Win32.System.Com.uCLSSPEC_head), pQuery: POINTER(win32more.Windows.Win32.System.Com.QUERYCONTEXT_head), pszCodeBase: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def BindMoniker(pmk: win32more.Windows.Win32.System.Com.IMoniker_head, grfOpt: UInt32, iidResult: POINTER(Guid), ppvResult: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetObject(pszName: win32more.Windows.Win32.Foundation.PWSTR, pBindOptions: POINTER(win32more.Windows.Win32.System.Com.BIND_OPTS_head), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def MkParseDisplayName(pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, szUserName: win32more.Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def MonikerRelativePathTo(pmkSrc: win32more.Windows.Win32.System.Com.IMoniker_head, pmkDest: win32more.Windows.Win32.System.Com.IMoniker_head, ppmkRelPath: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head), dwReserved: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def MonikerCommonPrefixWith(pmkThis: win32more.Windows.Win32.System.Com.IMoniker_head, pmkOther: win32more.Windows.Win32.System.Com.IMoniker_head, ppmkCommon: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateBindCtx(reserved: UInt32, ppbc: POINTER(win32more.Windows.Win32.System.Com.IBindCtx_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateGenericComposite(pmkFirst: win32more.Windows.Win32.System.Com.IMoniker_head, pmkRest: win32more.Windows.Win32.System.Com.IMoniker_head, ppmkComposite: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetClassFile(szFilename: win32more.Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateClassMoniker(rclsid: POINTER(Guid), ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateFileMoniker(lpszPathName: win32more.Windows.Win32.Foundation.PWSTR, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateItemMoniker(lpszDelim: win32more.Windows.Win32.Foundation.PWSTR, lpszItem: win32more.Windows.Win32.Foundation.PWSTR, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateAntiMoniker(ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreatePointerMoniker(punk: win32more.Windows.Win32.System.Com.IUnknown_head, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateObjrefMoniker(punk: win32more.Windows.Win32.System.Com.IUnknown_head, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetRunningObjectTable(reserved: UInt32, pprot: POINTER(win32more.Windows.Win32.System.Com.IRunningObjectTable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CreateStdProgressIndicator(hwndParent: win32more.Windows.Win32.Foundation.HWND, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pIbscCaller: win32more.Windows.Win32.System.Com.IBindStatusCallback_head, ppIbsc: POINTER(win32more.Windows.Win32.System.Com.IBindStatusCallback_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetMalloc(dwMemContext: UInt32, ppMalloc: POINTER(win32more.Windows.Win32.System.Com.IMalloc_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoUninitialize() -> Void: ...
@winfunctype('OLE32.dll')
def CoGetCurrentProcess() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoInitializeEx(pvReserved: VoidPtr, dwCoInit: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCallerTID(lpdwTID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCurrentLogicalThreadId(pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetContextToken(pToken: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetApartmentType(pAptType: POINTER(win32more.Windows.Win32.System.Com.APTTYPE), pAptQualifier: POINTER(win32more.Windows.Win32.System.Com.APTTYPEQUALIFIER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoIncrementMTAUsage(pCookie: POINTER(win32more.Windows.Win32.System.Com.CO_MTA_USAGE_COOKIE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoDecrementMTAUsage(Cookie: win32more.Windows.Win32.System.Com.CO_MTA_USAGE_COOKIE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoAllowUnmarshalerCLSID(clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetObjectContext(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetClassObject(rclsid: POINTER(Guid), dwClsContext: UInt32, pvReserved: VoidPtr, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterClassObject(rclsid: POINTER(Guid), pUnk: win32more.Windows.Win32.System.Com.IUnknown_head, dwClsContext: win32more.Windows.Win32.System.Com.CLSCTX, flags: UInt32, lpdwRegister: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeClassObject(dwRegister: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoResumeClassObjects() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSuspendClassObjects() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoAddRefServerProcess() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoReleaseServerProcess() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoGetPSClsid(riid: POINTER(Guid), pClsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterPSClsid(riid: POINTER(Guid), rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterSurrogate(pSurrogate: win32more.Windows.Win32.System.Com.ISurrogate_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoDisconnectObject(pUnk: win32more.Windows.Win32.System.Com.IUnknown_head, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoLockObjectExternal(pUnk: win32more.Windows.Win32.System.Com.IUnknown_head, fLock: win32more.Windows.Win32.Foundation.BOOL, fLastUnlockReleases: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoIsHandlerConnected(pUnk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CoCreateFreeThreadedMarshaler(punkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, ppunkMarshal: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoFreeUnusedLibraries() -> Void: ...
@winfunctype('OLE32.dll')
def CoFreeUnusedLibrariesEx(dwUnloadDelay: UInt32, dwReserved: UInt32) -> Void: ...
@winfunctype('OLE32.dll')
def CoDisconnectContext(dwTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoInitializeSecurity(pSecDesc: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, cAuthSvc: Int32, asAuthSvc: POINTER(win32more.Windows.Win32.System.Com.SOLE_AUTHENTICATION_SERVICE_head), pReserved1: VoidPtr, dwAuthnLevel: win32more.Windows.Win32.System.Com.RPC_C_AUTHN_LEVEL, dwImpLevel: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL, pAuthList: VoidPtr, dwCapabilities: UInt32, pReserved3: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCallContext(riid: POINTER(Guid), ppInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoQueryProxyBlanket(pProxy: win32more.Windows.Win32.System.Com.IUnknown_head, pwAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pAuthnLevel: POINTER(UInt32), pImpLevel: POINTER(UInt32), pAuthInfo: POINTER(VoidPtr), pCapabilites: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSetProxyBlanket(pProxy: win32more.Windows.Win32.System.Com.IUnknown_head, dwAuthnSvc: UInt32, dwAuthzSvc: UInt32, pServerPrincName: win32more.Windows.Win32.Foundation.PWSTR, dwAuthnLevel: win32more.Windows.Win32.System.Com.RPC_C_AUTHN_LEVEL, dwImpLevel: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL, pAuthInfo: VoidPtr, dwCapabilities: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCopyProxy(pProxy: win32more.Windows.Win32.System.Com.IUnknown_head, ppCopy: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoQueryClientBlanket(pAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pAuthnLevel: POINTER(UInt32), pImpLevel: POINTER(UInt32), pPrivs: POINTER(VoidPtr), pCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoImpersonateClient() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevertToSelf() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoQueryAuthenticationServices(pcAuthSvc: POINTER(UInt32), asAuthSvc: POINTER(POINTER(win32more.Windows.Win32.System.Com.SOLE_AUTHENTICATION_SERVICE_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSwitchCallContext(pNewObject: win32more.Windows.Win32.System.Com.IUnknown_head, ppOldObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCreateInstance(rclsid: POINTER(Guid), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, dwClsContext: win32more.Windows.Win32.System.Com.CLSCTX, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCreateInstanceEx(Clsid: POINTER(Guid), punkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, dwClsCtx: win32more.Windows.Win32.System.Com.CLSCTX, pServerInfo: POINTER(win32more.Windows.Win32.System.Com.COSERVERINFO_head), dwCount: UInt32, pResults: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCreateInstanceFromApp(Clsid: POINTER(Guid), punkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, dwClsCtx: win32more.Windows.Win32.System.Com.CLSCTX, reserved: VoidPtr, dwCount: UInt32, pResults: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterActivationFilter(pActivationFilter: win32more.Windows.Win32.System.Com.IActivationFilter_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCancelObject(dwThreadId: UInt32, iid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSetCancelObject(pUnk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCancelCall(dwThreadId: UInt32, ulTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoTestCancel() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoEnableCallCancellation(pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoDisableCallCancellation(pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StringFromCLSID(rclsid: POINTER(Guid), lplpsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CLSIDFromString(lpsz: win32more.Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StringFromIID(rclsid: POINTER(Guid), lplpsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def IIDFromString(lpsz: win32more.Windows.Win32.Foundation.PWSTR, lpiid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ProgIDFromCLSID(clsid: POINTER(Guid), lplpszProgID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CLSIDFromProgID(lpszProgID: win32more.Windows.Win32.Foundation.PWSTR, lpclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StringFromGUID2(rguid: POINTER(Guid), lpsz: win32more.Windows.Win32.Foundation.PWSTR, cchMax: Int32) -> Int32: ...
@winfunctype('OLE32.dll')
def CoCreateGuid(pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoWaitForMultipleHandles(dwFlags: UInt32, dwTimeout: UInt32, cHandles: UInt32, pHandles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), lpdwindex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoWaitForMultipleObjects(dwFlags: UInt32, dwTimeout: UInt32, cHandles: UInt32, pHandles: POINTER(win32more.Windows.Win32.Foundation.HANDLE), lpdwindex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetTreatAsClass(clsidOld: POINTER(Guid), pClsidNew: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoInvalidateRemoteMachineBindings(pszMachineName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoTaskMemAlloc(cb: UIntPtr) -> VoidPtr: ...
@winfunctype('OLE32.dll')
def CoTaskMemRealloc(pv: VoidPtr, cb: UIntPtr) -> VoidPtr: ...
@winfunctype('OLE32.dll')
def CoTaskMemFree(pv: VoidPtr) -> Void: ...
@winfunctype('OLE32.dll')
def CoRegisterDeviceCatalog(deviceInstanceId: win32more.Windows.Win32.Foundation.PWSTR, cookie: POINTER(win32more.Windows.Win32.System.Com.CO_DEVICE_CATALOG_COOKIE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeDeviceCatalog(cookie: win32more.Windows.Win32.System.Com.CO_DEVICE_CATALOG_COOKIE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('URLMON.dll')
def CreateUri(pwzURI: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.System.Com.URI_CREATE_FLAGS, dwReserved: UIntPtr, ppURI: POINTER(win32more.Windows.Win32.System.Com.IUri_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('URLMON.dll')
def CreateUriWithFragment(pwzURI: win32more.Windows.Win32.Foundation.PWSTR, pwzFragment: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UIntPtr, ppURI: POINTER(win32more.Windows.Win32.System.Com.IUri_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateUriFromMultiByteString(pszANSIInputUri: win32more.Windows.Win32.Foundation.PSTR, dwEncodingFlags: UInt32, dwCodePage: UInt32, dwCreateFlags: UInt32, dwReserved: UIntPtr, ppUri: POINTER(win32more.Windows.Win32.System.Com.IUri_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('URLMON.dll')
def CreateIUriBuilder(pIUri: win32more.Windows.Win32.System.Com.IUri_head, dwFlags: UInt32, dwReserved: UIntPtr, ppIUriBuilder: POINTER(win32more.Windows.Win32.System.Com.IUriBuilder_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SetErrorInfo(dwReserved: UInt32, perrinfo: win32more.Windows.Win32.System.Com.IErrorInfo_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetErrorInfo(dwReserved: UInt32, pperrinfo: POINTER(win32more.Windows.Win32.System.Com.IErrorInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ApplicationType = Int32
ApplicationType_ServerApplication: ApplicationType = 0
ApplicationType_LibraryApplication: ApplicationType = 1
class AsyncIAdviseSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000150-0000-0000-c000-000000000046}')
    @commethod(3)
    def Begin_OnDataChange(self, pFormatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pStgmed: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head)) -> Void: ...
    @commethod(4)
    def Finish_OnDataChange(self) -> Void: ...
    @commethod(5)
    def Begin_OnViewChange(self, dwAspect: UInt32, lindex: Int32) -> Void: ...
    @commethod(6)
    def Finish_OnViewChange(self) -> Void: ...
    @commethod(7)
    def Begin_OnRename(self, pmk: win32more.Windows.Win32.System.Com.IMoniker_head) -> Void: ...
    @commethod(8)
    def Finish_OnRename(self) -> Void: ...
    @commethod(9)
    def Begin_OnSave(self) -> Void: ...
    @commethod(10)
    def Finish_OnSave(self) -> Void: ...
    @commethod(11)
    def Begin_OnClose(self) -> Void: ...
    @commethod(12)
    def Finish_OnClose(self) -> Void: ...
class AsyncIAdviseSink2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.AsyncIAdviseSink
    _iid_ = Guid('{00000151-0000-0000-c000-000000000046}')
    @commethod(13)
    def Begin_OnLinkSrcChange(self, pmk: win32more.Windows.Win32.System.Com.IMoniker_head) -> Void: ...
    @commethod(14)
    def Finish_OnLinkSrcChange(self) -> Void: ...
class AsyncIMultiQI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000e0020-0000-0000-c000-000000000046}')
    @commethod(3)
    def Begin_QueryMultipleInterfaces(self, cMQIs: UInt32, pMQIs: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_QueryMultipleInterfaces(self, pMQIs: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class AsyncIPipeByte(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db2f3acb-2f86-11d1-8e04-00c04fb9989a}')
    @commethod(3)
    def Begin_Pull(self, cRequest: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_Pull(self, buf: POINTER(Byte), pcReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Push(self, buf: POINTER(Byte), cSent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Push(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class AsyncIPipeDouble(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db2f3acf-2f86-11d1-8e04-00c04fb9989a}')
    @commethod(3)
    def Begin_Pull(self, cRequest: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_Pull(self, buf: POINTER(Double), pcReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Push(self, buf: POINTER(Double), cSent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Push(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class AsyncIPipeLong(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db2f3acd-2f86-11d1-8e04-00c04fb9989a}')
    @commethod(3)
    def Begin_Pull(self, cRequest: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_Pull(self, buf: POINTER(Int32), pcReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Push(self, buf: POINTER(Int32), cSent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Push(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class AsyncIUnknown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000e0000-0000-0000-c000-000000000046}')
    @commethod(3)
    def Begin_QueryInterface(self, riid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_QueryInterface(self, ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_AddRef(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_AddRef(self) -> UInt32: ...
    @commethod(7)
    def Begin_Release(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_Release(self) -> UInt32: ...
class BINDINFO(EasyCastStructure):
    cbSize: UInt32
    szExtraInfo: win32more.Windows.Win32.Foundation.PWSTR
    stgmedData: win32more.Windows.Win32.System.Com.STGMEDIUM
    grfBindInfoF: UInt32
    dwBindVerb: UInt32
    szCustomVerb: win32more.Windows.Win32.Foundation.PWSTR
    cbstgmedData: UInt32
    dwOptions: UInt32
    dwOptionsFlags: UInt32
    dwCodePage: UInt32
    securityAttributes: win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES
    iid: Guid
    pUnk: win32more.Windows.Win32.System.Com.IUnknown_head
    dwReserved: UInt32
BINDINFOF = Int32
BINDINFOF_URLENCODESTGMEDDATA: BINDINFOF = 1
BINDINFOF_URLENCODEDEXTRAINFO: BINDINFOF = 2
class BINDPTR(EasyCastUnion):
    lpfuncdesc: POINTER(win32more.Windows.Win32.System.Com.FUNCDESC_head)
    lpvardesc: POINTER(win32more.Windows.Win32.System.Com.VARDESC_head)
    lptcomp: win32more.Windows.Win32.System.Com.ITypeComp_head
BIND_FLAGS = Int32
BIND_MAYBOTHERUSER: BIND_FLAGS = 1
BIND_JUSTTESTEXISTENCE: BIND_FLAGS = 2
class BIND_OPTS(EasyCastStructure):
    cbStruct: UInt32
    grfFlags: UInt32
    grfMode: UInt32
    dwTickCountDeadline: UInt32
class BIND_OPTS2(EasyCastStructure):
    Base: win32more.Windows.Win32.System.Com.BIND_OPTS
    dwTrackFlags: UInt32
    dwClassContext: UInt32
    locale: UInt32
    pServerInfo: POINTER(win32more.Windows.Win32.System.Com.COSERVERINFO_head)
class BIND_OPTS3(EasyCastStructure):
    Base: win32more.Windows.Win32.System.Com.BIND_OPTS2
    hwnd: win32more.Windows.Win32.Foundation.HWND
class BLOB(EasyCastStructure):
    cbSize: UInt32
    pBlobData: POINTER(Byte)
class BYTE_BLOB(EasyCastStructure):
    clSize: UInt32
    abData: Byte * 1
class BYTE_SIZEDARR(EasyCastStructure):
    clSize: UInt32
    pData: POINTER(Byte)
CALLCONV = Int32
CC_FASTCALL: CALLCONV = 0
CC_CDECL: CALLCONV = 1
CC_MSCPASCAL: CALLCONV = 2
CC_PASCAL: CALLCONV = 2
CC_MACPASCAL: CALLCONV = 3
CC_STDCALL: CALLCONV = 4
CC_FPFASTCALL: CALLCONV = 5
CC_SYSCALL: CALLCONV = 6
CC_MPWCDECL: CALLCONV = 7
CC_MPWPASCAL: CALLCONV = 8
CC_MAX: CALLCONV = 9
CALLTYPE = Int32
CALLTYPE_TOPLEVEL: CALLTYPE = 1
CALLTYPE_NESTED: CALLTYPE = 2
CALLTYPE_ASYNC: CALLTYPE = 3
CALLTYPE_TOPLEVEL_CALLPENDING: CALLTYPE = 4
CALLTYPE_ASYNC_CALLPENDING: CALLTYPE = 5
class CATEGORYINFO(EasyCastStructure):
    catid: Guid
    lcid: UInt32
    szDescription: Char * 128
CLSCTX = UInt32
CLSCTX_INPROC_SERVER: CLSCTX = 1
CLSCTX_INPROC_HANDLER: CLSCTX = 2
CLSCTX_LOCAL_SERVER: CLSCTX = 4
CLSCTX_INPROC_SERVER16: CLSCTX = 8
CLSCTX_REMOTE_SERVER: CLSCTX = 16
CLSCTX_INPROC_HANDLER16: CLSCTX = 32
CLSCTX_RESERVED1: CLSCTX = 64
CLSCTX_RESERVED2: CLSCTX = 128
CLSCTX_RESERVED3: CLSCTX = 256
CLSCTX_RESERVED4: CLSCTX = 512
CLSCTX_NO_CODE_DOWNLOAD: CLSCTX = 1024
CLSCTX_RESERVED5: CLSCTX = 2048
CLSCTX_NO_CUSTOM_MARSHAL: CLSCTX = 4096
CLSCTX_ENABLE_CODE_DOWNLOAD: CLSCTX = 8192
CLSCTX_NO_FAILURE_LOG: CLSCTX = 16384
CLSCTX_DISABLE_AAA: CLSCTX = 32768
CLSCTX_ENABLE_AAA: CLSCTX = 65536
CLSCTX_FROM_DEFAULT_CONTEXT: CLSCTX = 131072
CLSCTX_ACTIVATE_X86_SERVER: CLSCTX = 262144
CLSCTX_ACTIVATE_32_BIT_SERVER: CLSCTX = 262144
CLSCTX_ACTIVATE_64_BIT_SERVER: CLSCTX = 524288
CLSCTX_ENABLE_CLOAKING: CLSCTX = 1048576
CLSCTX_APPCONTAINER: CLSCTX = 4194304
CLSCTX_ACTIVATE_AAA_AS_IU: CLSCTX = 8388608
CLSCTX_RESERVED6: CLSCTX = 16777216
CLSCTX_ACTIVATE_ARM32_SERVER: CLSCTX = 33554432
CLSCTX_ALLOW_LOWER_TRUST_REGISTRATION: CLSCTX = 67108864
CLSCTX_PS_DLL: CLSCTX = 2147483648
CLSCTX_ALL: CLSCTX = 23
CLSCTX_SERVER: CLSCTX = 21
class COAUTHIDENTITY(EasyCastStructure):
    User: POINTER(UInt16)
    UserLength: UInt32
    Domain: POINTER(UInt16)
    DomainLength: UInt32
    Password: POINTER(UInt16)
    PasswordLength: UInt32
    Flags: UInt32
class COAUTHINFO(EasyCastStructure):
    dwAuthnSvc: UInt32
    dwAuthzSvc: UInt32
    pwszServerPrincName: win32more.Windows.Win32.Foundation.PWSTR
    dwAuthnLevel: UInt32
    dwImpersonationLevel: UInt32
    pAuthIdentityData: POINTER(win32more.Windows.Win32.System.Com.COAUTHIDENTITY_head)
    dwCapabilities: UInt32
COINIT = Int32
COINIT_APARTMENTTHREADED: COINIT = 2
COINIT_MULTITHREADED: COINIT = 0
COINIT_DISABLE_OLE1DDE: COINIT = 4
COINIT_SPEED_OVER_MEMORY: COINIT = 8
COINITBASE = Int32
COINITBASE_MULTITHREADED: COINITBASE = 0
COMSD = Int32
SD_LAUNCHPERMISSIONS: COMSD = 0
SD_ACCESSPERMISSIONS: COMSD = 1
SD_LAUNCHRESTRICTIONS: COMSD = 2
SD_ACCESSRESTRICTIONS: COMSD = 3
class CONNECTDATA(EasyCastStructure):
    pUnk: win32more.Windows.Win32.System.Com.IUnknown_head
    dwCookie: UInt32
class COSERVERINFO(EasyCastStructure):
    dwReserved1: UInt32
    pwszName: win32more.Windows.Win32.Foundation.PWSTR
    pAuthInfo: POINTER(win32more.Windows.Win32.System.Com.COAUTHINFO_head)
    dwReserved2: UInt32
COWAIT_FLAGS = Int32
COWAIT_DEFAULT: COWAIT_FLAGS = 0
COWAIT_WAITALL: COWAIT_FLAGS = 1
COWAIT_ALERTABLE: COWAIT_FLAGS = 2
COWAIT_INPUTAVAILABLE: COWAIT_FLAGS = 4
COWAIT_DISPATCH_CALLS: COWAIT_FLAGS = 8
COWAIT_DISPATCH_WINDOW_MESSAGES: COWAIT_FLAGS = 16
CO_DEVICE_CATALOG_COOKIE = IntPtr
CO_MARSHALING_CONTEXT_ATTRIBUTES = Int32
CO_MARSHALING_SOURCE_IS_APP_CONTAINER: CO_MARSHALING_CONTEXT_ATTRIBUTES = 0
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_1: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483648
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_2: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483647
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_3: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483646
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_4: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483645
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_5: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483644
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_6: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483643
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_7: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483642
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_8: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483641
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_9: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483640
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_10: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483639
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_11: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483638
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_12: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483637
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_13: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483636
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_14: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483635
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_15: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483634
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_16: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483633
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_17: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483632
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_18: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483631
CO_MTA_USAGE_COOKIE = IntPtr
class CSPLATFORM(EasyCastStructure):
    dwPlatformId: UInt32
    dwVersionHi: UInt32
    dwVersionLo: UInt32
    dwProcessorArch: UInt32
class CUSTDATA(EasyCastStructure):
    cCustData: UInt32
    prgCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATAITEM_head)
class CUSTDATAITEM(EasyCastStructure):
    guid: Guid
    varValue: win32more.Windows.Win32.System.Variant.VARIANT
CWMO_FLAGS = Int32
CWMO_DEFAULT: CWMO_FLAGS = 0
CWMO_DISPATCH_CALLS: CWMO_FLAGS = 1
CWMO_DISPATCH_WINDOW_MESSAGES: CWMO_FLAGS = 2
class CY(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    int64: Int64
    class _Anonymous_e__Struct(EasyCastStructure):
        Lo: UInt32
        Hi: Int32
class ComCallData(EasyCastStructure):
    dwDispid: UInt32
    dwReserved: UInt32
    pUserDefined: VoidPtr
class ContextProperty(EasyCastStructure):
    policyId: Guid
    flags: UInt32
    pUnk: win32more.Windows.Win32.System.Com.IUnknown_head
DATADIR = Int32
DATADIR_GET: DATADIR = 1
DATADIR_SET: DATADIR = 2
DCOM_CALL_STATE = Int32
DCOM_NONE: DCOM_CALL_STATE = 0
DCOM_CALL_COMPLETE: DCOM_CALL_STATE = 1
DCOM_CALL_CANCELED: DCOM_CALL_STATE = 2
DESCKIND = Int32
DESCKIND_NONE: DESCKIND = 0
DESCKIND_FUNCDESC: DESCKIND = 1
DESCKIND_VARDESC: DESCKIND = 2
DESCKIND_TYPECOMP: DESCKIND = 3
DESCKIND_IMPLICITAPPOBJ: DESCKIND = 4
DESCKIND_MAX: DESCKIND = 5
DISPATCH_FLAGS = UInt16
DISPATCH_METHOD: DISPATCH_FLAGS = 1
DISPATCH_PROPERTYGET: DISPATCH_FLAGS = 2
DISPATCH_PROPERTYPUT: DISPATCH_FLAGS = 4
DISPATCH_PROPERTYPUTREF: DISPATCH_FLAGS = 8
class DISPPARAMS(EasyCastStructure):
    rgvarg: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)
    rgdispidNamedArgs: POINTER(Int32)
    cArgs: UInt32
    cNamedArgs: UInt32
DVASPECT = UInt32
DVASPECT_CONTENT: DVASPECT = 1
DVASPECT_THUMBNAIL: DVASPECT = 2
DVASPECT_ICON: DVASPECT = 4
DVASPECT_DOCPRINT: DVASPECT = 8
DVASPECT_OPAQUE: DVASPECT = 16
DVASPECT_TRANSPARENT: DVASPECT = 32
class DVTARGETDEVICE(EasyCastStructure):
    tdSize: UInt32
    tdDriverNameOffset: UInt16
    tdDeviceNameOffset: UInt16
    tdPortNameOffset: UInt16
    tdExtDevmodeOffset: UInt16
    tdData: Byte * 1
class DWORD_BLOB(EasyCastStructure):
    clSize: UInt32
    alData: UInt32 * 1
class DWORD_SIZEDARR(EasyCastStructure):
    clSize: UInt32
    pData: POINTER(UInt32)
class ELEMDESC(EasyCastStructure):
    tdesc: win32more.Windows.Win32.System.Com.TYPEDESC
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        idldesc: win32more.Windows.Win32.System.Com.IDLDESC
        paramdesc: win32more.Windows.Win32.System.Ole.PARAMDESC
EOLE_AUTHENTICATION_CAPABILITIES = Int32
EOAC_NONE: EOLE_AUTHENTICATION_CAPABILITIES = 0
EOAC_MUTUAL_AUTH: EOLE_AUTHENTICATION_CAPABILITIES = 1
EOAC_STATIC_CLOAKING: EOLE_AUTHENTICATION_CAPABILITIES = 32
EOAC_DYNAMIC_CLOAKING: EOLE_AUTHENTICATION_CAPABILITIES = 64
EOAC_ANY_AUTHORITY: EOLE_AUTHENTICATION_CAPABILITIES = 128
EOAC_MAKE_FULLSIC: EOLE_AUTHENTICATION_CAPABILITIES = 256
EOAC_DEFAULT: EOLE_AUTHENTICATION_CAPABILITIES = 2048
EOAC_SECURE_REFS: EOLE_AUTHENTICATION_CAPABILITIES = 2
EOAC_ACCESS_CONTROL: EOLE_AUTHENTICATION_CAPABILITIES = 4
EOAC_APPID: EOLE_AUTHENTICATION_CAPABILITIES = 8
EOAC_DYNAMIC: EOLE_AUTHENTICATION_CAPABILITIES = 16
EOAC_REQUIRE_FULLSIC: EOLE_AUTHENTICATION_CAPABILITIES = 512
EOAC_AUTO_IMPERSONATE: EOLE_AUTHENTICATION_CAPABILITIES = 1024
EOAC_DISABLE_AAA: EOLE_AUTHENTICATION_CAPABILITIES = 4096
EOAC_NO_CUSTOM_MARSHAL: EOLE_AUTHENTICATION_CAPABILITIES = 8192
EOAC_RESERVED1: EOLE_AUTHENTICATION_CAPABILITIES = 16384
class EXCEPINFO(EasyCastStructure):
    wCode: UInt16
    wReserved: UInt16
    bstrSource: win32more.Windows.Win32.Foundation.BSTR
    bstrDescription: win32more.Windows.Win32.Foundation.BSTR
    bstrHelpFile: win32more.Windows.Win32.Foundation.BSTR
    dwHelpContext: UInt32
    pvReserved: VoidPtr
    pfnDeferredFillIn: win32more.Windows.Win32.System.Com.LPEXCEPFINO_DEFERRED_FILLIN
    scode: Int32
EXTCONN = Int32
EXTCONN_STRONG: EXTCONN = 1
EXTCONN_WEAK: EXTCONN = 2
EXTCONN_CALLABLE: EXTCONN = 4
class FLAGGED_BYTE_BLOB(EasyCastStructure):
    fFlags: UInt32
    clSize: UInt32
    abData: Byte * 1
class FLAGGED_WORD_BLOB(EasyCastStructure):
    fFlags: UInt32
    clSize: UInt32
    asData: UInt16 * 1
class FLAG_STGMEDIUM(EasyCastStructure):
    ContextFlags: Int32
    fPassOwnership: Int32
    Stgmed: win32more.Windows.Win32.System.Com.STGMEDIUM
class FORMATETC(EasyCastStructure):
    cfFormat: UInt16
    ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE_head)
    dwAspect: UInt32
    lindex: Int32
    tymed: UInt32
class FUNCDESC(EasyCastStructure):
    memid: Int32
    lprgscode: POINTER(Int32)
    lprgelemdescParam: POINTER(win32more.Windows.Win32.System.Com.ELEMDESC_head)
    funckind: win32more.Windows.Win32.System.Com.FUNCKIND
    invkind: win32more.Windows.Win32.System.Com.INVOKEKIND
    callconv: win32more.Windows.Win32.System.Com.CALLCONV
    cParams: Int16
    cParamsOpt: Int16
    oVft: Int16
    cScodes: Int16
    elemdescFunc: win32more.Windows.Win32.System.Com.ELEMDESC
    wFuncFlags: win32more.Windows.Win32.System.Com.FUNCFLAGS
FUNCFLAGS = UInt16
FUNCFLAG_FRESTRICTED: FUNCFLAGS = 1
FUNCFLAG_FSOURCE: FUNCFLAGS = 2
FUNCFLAG_FBINDABLE: FUNCFLAGS = 4
FUNCFLAG_FREQUESTEDIT: FUNCFLAGS = 8
FUNCFLAG_FDISPLAYBIND: FUNCFLAGS = 16
FUNCFLAG_FDEFAULTBIND: FUNCFLAGS = 32
FUNCFLAG_FHIDDEN: FUNCFLAGS = 64
FUNCFLAG_FUSESGETLASTERROR: FUNCFLAGS = 128
FUNCFLAG_FDEFAULTCOLLELEM: FUNCFLAGS = 256
FUNCFLAG_FUIDEFAULT: FUNCFLAGS = 512
FUNCFLAG_FNONBROWSABLE: FUNCFLAGS = 1024
FUNCFLAG_FREPLACEABLE: FUNCFLAGS = 2048
FUNCFLAG_FIMMEDIATEBIND: FUNCFLAGS = 4096
FUNCKIND = Int32
FUNC_VIRTUAL: FUNCKIND = 0
FUNC_PUREVIRTUAL: FUNCKIND = 1
FUNC_NONVIRTUAL: FUNCKIND = 2
FUNC_STATIC: FUNCKIND = 3
FUNC_DISPATCH: FUNCKIND = 4
class GDI_OBJECT(EasyCastStructure):
    ObjectType: UInt32
    u: _u_e__Struct
    class _u_e__Struct(EasyCastUnion):
        hBitmap: POINTER(win32more.Windows.Win32.System.SystemServices.userHBITMAP_head)
        hPalette: POINTER(win32more.Windows.Win32.System.SystemServices.userHPALETTE_head)
        hGeneric: POINTER(win32more.Windows.Win32.System.SystemServices.userHGLOBAL_head)
GLOBALOPT_EH_VALUES = Int32
COMGLB_EXCEPTION_HANDLE: GLOBALOPT_EH_VALUES = 0
COMGLB_EXCEPTION_DONOT_HANDLE_FATAL: GLOBALOPT_EH_VALUES = 1
COMGLB_EXCEPTION_DONOT_HANDLE: GLOBALOPT_EH_VALUES = 1
COMGLB_EXCEPTION_DONOT_HANDLE_ANY: GLOBALOPT_EH_VALUES = 2
GLOBALOPT_PROPERTIES = Int32
COMGLB_EXCEPTION_HANDLING: GLOBALOPT_PROPERTIES = 1
COMGLB_APPID: GLOBALOPT_PROPERTIES = 2
COMGLB_RPC_THREADPOOL_SETTING: GLOBALOPT_PROPERTIES = 3
COMGLB_RO_SETTINGS: GLOBALOPT_PROPERTIES = 4
COMGLB_UNMARSHALING_POLICY: GLOBALOPT_PROPERTIES = 5
COMGLB_PROPERTIES_RESERVED1: GLOBALOPT_PROPERTIES = 6
COMGLB_PROPERTIES_RESERVED2: GLOBALOPT_PROPERTIES = 7
COMGLB_PROPERTIES_RESERVED3: GLOBALOPT_PROPERTIES = 8
GLOBALOPT_RO_FLAGS = Int32
COMGLB_STA_MODALLOOP_REMOVE_TOUCH_MESSAGES: GLOBALOPT_RO_FLAGS = 1
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REMOVE_INPUT_MESSAGES: GLOBALOPT_RO_FLAGS = 2
COMGLB_STA_MODALLOOP_SHARED_QUEUE_DONOT_REMOVE_INPUT_MESSAGES: GLOBALOPT_RO_FLAGS = 4
COMGLB_FAST_RUNDOWN: GLOBALOPT_RO_FLAGS = 8
COMGLB_RESERVED1: GLOBALOPT_RO_FLAGS = 16
COMGLB_RESERVED2: GLOBALOPT_RO_FLAGS = 32
COMGLB_RESERVED3: GLOBALOPT_RO_FLAGS = 64
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REORDER_POINTER_MESSAGES: GLOBALOPT_RO_FLAGS = 128
COMGLB_RESERVED4: GLOBALOPT_RO_FLAGS = 256
COMGLB_RESERVED5: GLOBALOPT_RO_FLAGS = 512
COMGLB_RESERVED6: GLOBALOPT_RO_FLAGS = 1024
GLOBALOPT_RPCTP_VALUES = Int32
COMGLB_RPC_THREADPOOL_SETTING_DEFAULT_POOL: GLOBALOPT_RPCTP_VALUES = 0
COMGLB_RPC_THREADPOOL_SETTING_PRIVATE_POOL: GLOBALOPT_RPCTP_VALUES = 1
GLOBALOPT_UNMARSHALING_POLICY_VALUES = Int32
COMGLB_UNMARSHALING_POLICY_NORMAL: GLOBALOPT_UNMARSHALING_POLICY_VALUES = 0
COMGLB_UNMARSHALING_POLICY_STRONG: GLOBALOPT_UNMARSHALING_POLICY_VALUES = 1
COMGLB_UNMARSHALING_POLICY_HYBRID: GLOBALOPT_UNMARSHALING_POLICY_VALUES = 2
class HYPER_SIZEDARR(EasyCastStructure):
    clSize: UInt32
    pData: POINTER(Int64)
class IActivationFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000017-0000-0000-c000-000000000046}')
    @commethod(3)
    def HandleActivation(self, dwActivationType: UInt32, rclsid: POINTER(Guid), pReplacementClsId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAddrExclusionControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000148-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetCurrentAddrExclusionList(self, riid: POINTER(Guid), ppEnumerator: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAddrExclusionList(self, pEnumerator: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAddrTrackingControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000147-0000-0000-c000-000000000046}')
    @commethod(3)
    def EnableCOMDynamicAddrTracking(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisableCOMDynamicAddrTracking(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAdviseSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000010f-0000-0000-c000-000000000046}')
    @commethod(3)
    def OnDataChange(self, pFormatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pStgmed: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head)) -> Void: ...
    @commethod(4)
    def OnViewChange(self, dwAspect: UInt32, lindex: Int32) -> Void: ...
    @commethod(5)
    def OnRename(self, pmk: win32more.Windows.Win32.System.Com.IMoniker_head) -> Void: ...
    @commethod(6)
    def OnSave(self) -> Void: ...
    @commethod(7)
    def OnClose(self) -> Void: ...
class IAdviseSink2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IAdviseSink
    _iid_ = Guid('{00000125-0000-0000-c000-000000000046}')
    @commethod(8)
    def OnLinkSrcChange(self, pmk: win32more.Windows.Win32.System.Com.IMoniker_head) -> Void: ...
class IAgileObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{94ea2b94-e9cc-49e0-c0ff-ee64ca8f5b90}')
class IAsyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002a-0000-0000-c000-000000000046}')
    @commethod(3)
    def CompleteCall(self, Result: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCallContext(self, riid: POINTER(Guid), pInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetState(self, pulStateFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAsyncRpcChannelBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IRpcChannelBuffer2
    _iid_ = Guid('{a5029fb6-3c34-11d1-9c99-00c04fb998aa}')
    @commethod(9)
    def Send(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pSync: win32more.Windows.Win32.System.Com.ISynchronize_head, pulStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Receive(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pulStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDestCtxEx(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pdwDestContext: POINTER(UInt32), ppvDestContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAuthenticate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9d0-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def Authenticate(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND), pszUsername: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pszPassword: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAuthenticateEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IAuthenticate
    _iid_ = Guid('{2ad1edaf-d83d-48b5-9adf-03dbe19f53bd}')
    @commethod(4)
    def AuthenticateEx(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND), pszUsername: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pszPassword: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pauthinfo: POINTER(win32more.Windows.Win32.System.Com.AUTHENTICATEINFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBindCtx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000e-0000-0000-c000-000000000046}')
    @commethod(3)
    def RegisterObjectBound(self, punk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeObjectBound(self, punk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReleaseBoundObjects(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetBindOptions(self, pbindopts: POINTER(win32more.Windows.Win32.System.Com.BIND_OPTS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBindOptions(self, pbindopts: POINTER(win32more.Windows.Win32.System.Com.BIND_OPTS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRunningObjectTable(self, pprot: POINTER(win32more.Windows.Win32.System.Com.IRunningObjectTable_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterObjectParam(self, pszKey: win32more.Windows.Win32.Foundation.PWSTR, punk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetObjectParam(self, pszKey: win32more.Windows.Win32.Foundation.PWSTR, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumObjectParam(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumString_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RevokeObjectParam(self, pszKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBindHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc4801a1-2ba9-11cf-a229-00aa003d7352}')
    @commethod(3)
    def CreateMoniker(self, szName: win32more.Windows.Win32.Foundation.PWSTR, pBC: win32more.Windows.Win32.System.Com.IBindCtx_head, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MonikerBindToStorage(self, pMk: win32more.Windows.Win32.System.Com.IMoniker_head, pBC: win32more.Windows.Win32.System.Com.IBindCtx_head, pBSC: win32more.Windows.Win32.System.Com.IBindStatusCallback_head, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MonikerBindToObject(self, pMk: win32more.Windows.Win32.System.Com.IMoniker_head, pBC: win32more.Windows.Win32.System.Com.IBindCtx_head, pBSC: win32more.Windows.Win32.System.Com.IBindStatusCallback_head, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBindStatusCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c1-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def OnStartBinding(self, dwReserved: UInt32, pib: win32more.Windows.Win32.System.Com.IBinding_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPriority(self, pnPriority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnLowResource(self, reserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnProgress(self, ulProgress: UInt32, ulProgressMax: UInt32, ulStatusCode: UInt32, szStatusText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnStopBinding(self, hresult: win32more.Windows.Win32.Foundation.HRESULT, szError: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBindInfo(self, grfBINDF: POINTER(UInt32), pbindinfo: POINTER(win32more.Windows.Win32.System.Com.BINDINFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnDataAvailable(self, grfBSCF: UInt32, dwSize: UInt32, pformatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pstgmed: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnObjectAvailable(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBindStatusCallbackEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IBindStatusCallback
    _iid_ = Guid('{aaa74ef9-8ee7-4659-88d9-f8c504da73cc}')
    @commethod(11)
    def GetBindInfoEx(self, grfBINDF: POINTER(UInt32), pbindinfo: POINTER(win32more.Windows.Win32.System.Com.BINDINFO_head), grfBINDF2: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBinding(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c0-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Suspend(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPriority(self, nPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPriority(self, pnPriority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBindResult(self, pclsidProtocol: POINTER(Guid), pdwResult: POINTER(UInt32), pszResult: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBlockingLock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30f3d47a-6447-11d1-8e3c-00c04fb9386d}')
    @commethod(3)
    def Lock(self, dwTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unlock(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICallFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1c733a30-2a1c-11ce-ade5-00aa0044773d}')
    @commethod(3)
    def CreateCall(self, riid: POINTER(Guid), pCtrlUnk: win32more.Windows.Win32.System.Com.IUnknown_head, riid2: POINTER(Guid), ppv: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICancelMethodCalls(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000029-0000-0000-c000-000000000046}')
    @commethod(3)
    def Cancel(self, ulSeconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TestCancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICatInformation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0002e013-0000-0000-c000-000000000046}')
    @commethod(3)
    def EnumCategories(self, lcid: UInt32, ppenumCategoryInfo: POINTER(win32more.Windows.Win32.System.Com.IEnumCATEGORYINFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategoryDesc(self, rcatid: POINTER(Guid), lcid: UInt32, pszDesc: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumClassesOfCategories(self, cImplemented: UInt32, rgcatidImpl: POINTER(Guid), cRequired: UInt32, rgcatidReq: POINTER(Guid), ppenumClsid: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsClassOfCategories(self, rclsid: POINTER(Guid), cImplemented: UInt32, rgcatidImpl: POINTER(Guid), cRequired: UInt32, rgcatidReq: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumImplCategoriesOfClass(self, rclsid: POINTER(Guid), ppenumCatid: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumReqCategoriesOfClass(self, rclsid: POINTER(Guid), ppenumCatid: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICatRegister(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0002e012-0000-0000-c000-000000000046}')
    @commethod(3)
    def RegisterCategories(self, cCategories: UInt32, rgCategoryInfo: POINTER(win32more.Windows.Win32.System.Com.CATEGORYINFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnRegisterCategories(self, cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterClassImplCategories(self, rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnRegisterClassImplCategories(self, rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterClassReqCategories(self, rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnRegisterClassReqCategories(self, rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IChannelHook(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1008c4a0-7613-11cf-9af1-0020af6e72f4}')
    @commethod(3)
    def ClientGetSize(self, uExtent: POINTER(Guid), riid: POINTER(Guid), pDataSize: POINTER(UInt32)) -> Void: ...
    @commethod(4)
    def ClientFillBuffer(self, uExtent: POINTER(Guid), riid: POINTER(Guid), pDataSize: POINTER(UInt32), pDataBuffer: VoidPtr) -> Void: ...
    @commethod(5)
    def ClientNotify(self, uExtent: POINTER(Guid), riid: POINTER(Guid), cbDataSize: UInt32, pDataBuffer: VoidPtr, lDataRep: UInt32, hrFault: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
    @commethod(6)
    def ServerNotify(self, uExtent: POINTER(Guid), riid: POINTER(Guid), cbDataSize: UInt32, pDataBuffer: VoidPtr, lDataRep: UInt32) -> Void: ...
    @commethod(7)
    def ServerGetSize(self, uExtent: POINTER(Guid), riid: POINTER(Guid), hrFault: win32more.Windows.Win32.Foundation.HRESULT, pDataSize: POINTER(UInt32)) -> Void: ...
    @commethod(8)
    def ServerFillBuffer(self, uExtent: POINTER(Guid), riid: POINTER(Guid), pDataSize: POINTER(UInt32), pDataBuffer: VoidPtr, hrFault: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
class IClassActivator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000140-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetClassObject(self, rclsid: POINTER(Guid), dwClassContext: UInt32, locale: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IClassFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000001-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateInstance(self, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockServer(self, fLock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IClientSecurity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013d-0000-0000-c000-000000000046}')
    @commethod(3)
    def QueryBlanket(self, pProxy: win32more.Windows.Win32.System.Com.IUnknown_head, pAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(POINTER(UInt16)), pAuthnLevel: POINTER(win32more.Windows.Win32.System.Com.RPC_C_AUTHN_LEVEL), pImpLevel: POINTER(win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL), pAuthInfo: POINTER(VoidPtr), pCapabilites: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBlanket(self, pProxy: win32more.Windows.Win32.System.Com.IUnknown_head, dwAuthnSvc: UInt32, dwAuthzSvc: UInt32, pServerPrincName: win32more.Windows.Win32.Foundation.PWSTR, dwAuthnLevel: win32more.Windows.Win32.System.Com.RPC_C_AUTHN_LEVEL, dwImpLevel: win32more.Windows.Win32.System.Com.RPC_C_IMP_LEVEL, pAuthInfo: VoidPtr, dwCapabilities: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CopyProxy(self, pProxy: win32more.Windows.Win32.System.Com.IUnknown_head, ppCopy: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComThreadingInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000001ce-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetCurrentApartmentType(self, pAptType: POINTER(win32more.Windows.Win32.System.Com.APTTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentThreadType(self, pThreadType: POINTER(win32more.Windows.Win32.System.Com.THDTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentLogicalThreadId(self, pguidLogicalThreadId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetCurrentLogicalThreadId(self, rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConnectionPoint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b286-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def GetConnectionInterface(self, pIID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnectionPointContainer(self, ppCPC: POINTER(win32more.Windows.Win32.System.Com.IConnectionPointContainer_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Advise(self, pUnkSink: win32more.Windows.Win32.System.Com.IUnknown_head, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumConnections(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumConnections_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConnectionPointContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b284-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def EnumConnectionPoints(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumConnectionPoints_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindConnectionPoint(self, riid: POINTER(Guid), ppCP: POINTER(win32more.Windows.Win32.System.Com.IConnectionPoint_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000001c0-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetProperty(self, rpolicyId: POINTER(Guid), flags: UInt32, pUnk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveProperty(self, rPolicyId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProperty(self, rGuid: POINTER(Guid), pFlags: POINTER(UInt32), ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumContextProps(self, ppEnumContextProps: POINTER(win32more.Windows.Win32.System.Com.IEnumContextProps_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000001da-0000-0000-c000-000000000046}')
    @commethod(3)
    def ContextCallback(self, pfnCallback: win32more.Windows.Win32.System.Com.PFNCONTEXTCALL, pParam: POINTER(win32more.Windows.Win32.System.Com.ComCallData_head), riid: POINTER(Guid), iMethod: Int32, pUnk: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDLDESC(EasyCastStructure):
    dwReserved: UIntPtr
    wIDLFlags: win32more.Windows.Win32.System.Com.IDLFLAGS
IDLFLAGS = UInt16
IDLFLAG_NONE: IDLFLAGS = 0
IDLFLAG_FIN: IDLFLAGS = 1
IDLFLAG_FOUT: IDLFLAGS = 2
IDLFLAG_FLCID: IDLFLAGS = 4
IDLFLAG_FRETVAL: IDLFLAGS = 8
class IDataAdviseHolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000110-0000-0000-c000-000000000046}')
    @commethod(3)
    def Advise(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject_head, pFetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), advf: UInt32, pAdvise: win32more.Windows.Win32.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumAdvise(self, ppenumAdvise: POINTER(win32more.Windows.Win32.System.Com.IEnumSTATDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendOnDataChange(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject_head, dwReserved: UInt32, advf: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000010e-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetData(self, pformatetcIn: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataHere(self, pformatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryGetData(self, pformatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCanonicalFormatEtc(self, pformatectIn: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pformatetcOut: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetData(self, pformatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM_head), fRelease: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumFormatEtc(self, dwDirection: UInt32, ppenumFormatEtc: POINTER(win32more.Windows.Win32.System.Com.IEnumFORMATETC_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DAdvise(self, pformatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), advf: UInt32, pAdvSink: win32more.Windows.Win32.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DUnadvise(self, dwConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumDAdvise(self, ppenumAdvise: POINTER(win32more.Windows.Win32.System.Com.IEnumSTATDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDispatch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020400-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetTypeInfoCount(self, pctinfo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypeInfo(self, iTInfo: UInt32, lcid: UInt32, ppTInfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIDsOfNames(self, riid: POINTER(Guid), rgszNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cNames: UInt32, lcid: UInt32, rgDispId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Invoke(self, dispIdMember: Int32, riid: POINTER(Guid), lcid: UInt32, wFlags: win32more.Windows.Win32.System.Com.DISPATCH_FLAGS, pDispParams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS_head), pVarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pExcepInfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumCATEGORYINFO(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0002e011-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.CATEGORYINFO_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumCATEGORYINFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumConnectionPoints(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b285-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def Next(self, cConnections: UInt32, ppCP: POINTER(win32more.Windows.Win32.System.Com.IConnectionPoint_head), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cConnections: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumConnectionPoints_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumConnections(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b287-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def Next(self, cConnections: UInt32, rgcd: POINTER(win32more.Windows.Win32.System.Com.CONNECTDATA_head), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cConnections: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumConnections_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumContextProps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000001c1-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, pContextProperties: POINTER(win32more.Windows.Win32.System.Com.ContextProperty_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumContextProps: POINTER(win32more.Windows.Win32.System.Com.IEnumContextProps_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Count(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumFORMATETC(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000103-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.FORMATETC_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumFORMATETC_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumGUID(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0002e000-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumMoniker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000102-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATDATA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000105-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.STATDATA_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumSTATDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumString(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000101-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumString_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumUnknown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000100-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cf2b120-547d-101b-8e65-08002b2bd119}')
    @commethod(3)
    def GetGUID(self, pGUID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSource(self, pBstrSource: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDescription(self, pBstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetHelpFile(self, pBstrHelpFile: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelpContext(self, pdwHelpContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IErrorLog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3127ca40-446e-11ce-8135-00aa004bb851}')
    @commethod(3)
    def AddError(self, pszPropName: win32more.Windows.Win32.Foundation.PWSTR, pExcepInfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExternalConnection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000019-0000-0000-c000-000000000046}')
    @commethod(3)
    def AddConnection(self, extconn: UInt32, reserved: UInt32) -> UInt32: ...
    @commethod(4)
    def ReleaseConnection(self, extconn: UInt32, reserved: UInt32, fLastReleaseCloses: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
class IFastRundown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000040-0000-0000-c000-000000000046}')
class IForegroundTransfer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000145-0000-0000-c000-000000000046}')
    @commethod(3)
    def AllowForegroundTransfer(self, lpvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGlobalInterfaceTable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000146-0000-0000-c000-000000000046}')
    @commethod(3)
    def RegisterInterfaceInGlobal(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeInterfaceFromGlobal(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInterfaceFromGlobal(self, dwCookie: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGlobalOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000015b-0000-0000-c000-000000000046}')
    @commethod(3)
    def Set(self, dwProperty: win32more.Windows.Win32.System.Com.GLOBALOPT_PROPERTIES, dwValue: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Query(self, dwProperty: win32more.Windows.Win32.System.Com.GLOBALOPT_PROPERTIES, pdwValue: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeSpy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000034-0000-0000-c000-000000000046}')
    @commethod(3)
    def PreInitialize(self, dwCoInit: UInt32, dwCurThreadAptRefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostInitialize(self, hrCoInit: win32more.Windows.Win32.Foundation.HRESULT, dwCoInit: UInt32, dwNewThreadAptRefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PreUninitialize(self, dwCurThreadAptRefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PostUninitialize(self, dwNewThreadAptRefs: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternalUnknown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000021-0000-0000-c000-000000000046}')
    @commethod(3)
    def QueryInternalInterface(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IMPLTYPEFLAGS = Int32
IMPLTYPEFLAG_FDEFAULT: IMPLTYPEFLAGS = 1
IMPLTYPEFLAG_FSOURCE: IMPLTYPEFLAGS = 2
IMPLTYPEFLAG_FRESTRICTED: IMPLTYPEFLAGS = 4
IMPLTYPEFLAG_FDEFAULTVTABLE: IMPLTYPEFLAGS = 8
class IMachineGlobalObjectTable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26d709ac-f70b-4421-a96f-d2878fafb00d}')
    @commethod(3)
    def RegisterObject(self, clsid: POINTER(Guid), identifier: win32more.Windows.Win32.Foundation.PWSTR, object: win32more.Windows.Win32.System.Com.IUnknown_head, token: POINTER(win32more.Windows.Win32.System.Com.MachineGlobalObjectTableRegistrationToken)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObject(self, clsid: POINTER(Guid), identifier: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeObject(self, token: win32more.Windows.Win32.System.Com.MachineGlobalObjectTableRegistrationToken) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMalloc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000002-0000-0000-c000-000000000046}')
    @commethod(3)
    def Alloc(self, cb: UIntPtr) -> VoidPtr: ...
    @commethod(4)
    def Realloc(self, pv: VoidPtr, cb: UIntPtr) -> VoidPtr: ...
    @commethod(5)
    def Free(self, pv: VoidPtr) -> Void: ...
    @commethod(6)
    def GetSize(self, pv: VoidPtr) -> UIntPtr: ...
    @commethod(7)
    def DidAlloc(self, pv: VoidPtr) -> Int32: ...
    @commethod(8)
    def HeapMinimize(self) -> Void: ...
class IMallocSpy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000001d-0000-0000-c000-000000000046}')
    @commethod(3)
    def PreAlloc(self, cbRequest: UIntPtr) -> UIntPtr: ...
    @commethod(4)
    def PostAlloc(self, pActual: VoidPtr) -> VoidPtr: ...
    @commethod(5)
    def PreFree(self, pRequest: VoidPtr, fSpyed: win32more.Windows.Win32.Foundation.BOOL) -> VoidPtr: ...
    @commethod(6)
    def PostFree(self, fSpyed: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(7)
    def PreRealloc(self, pRequest: VoidPtr, cbRequest: UIntPtr, ppNewRequest: POINTER(VoidPtr), fSpyed: win32more.Windows.Win32.Foundation.BOOL) -> UIntPtr: ...
    @commethod(8)
    def PostRealloc(self, pActual: VoidPtr, fSpyed: win32more.Windows.Win32.Foundation.BOOL) -> VoidPtr: ...
    @commethod(9)
    def PreGetSize(self, pRequest: VoidPtr, fSpyed: win32more.Windows.Win32.Foundation.BOOL) -> VoidPtr: ...
    @commethod(10)
    def PostGetSize(self, cbActual: UIntPtr, fSpyed: win32more.Windows.Win32.Foundation.BOOL) -> UIntPtr: ...
    @commethod(11)
    def PreDidAlloc(self, pRequest: VoidPtr, fSpyed: win32more.Windows.Win32.Foundation.BOOL) -> VoidPtr: ...
    @commethod(12)
    def PostDidAlloc(self, pRequest: VoidPtr, fSpyed: win32more.Windows.Win32.Foundation.BOOL, fActual: Int32) -> Int32: ...
    @commethod(13)
    def PreHeapMinimize(self) -> Void: ...
    @commethod(14)
    def PostHeapMinimize(self) -> Void: ...
class IMoniker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersistStream
    _iid_ = Guid('{0000000f-0000-0000-c000-000000000046}')
    @commethod(8)
    def BindToObject(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, pmkToLeft: win32more.Windows.Win32.System.Com.IMoniker_head, riidResult: POINTER(Guid), ppvResult: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BindToStorage(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, pmkToLeft: win32more.Windows.Win32.System.Com.IMoniker_head, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reduce(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, dwReduceHowFar: UInt32, ppmkToLeft: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head), ppmkReduced: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ComposeWith(self, pmkRight: win32more.Windows.Win32.System.Com.IMoniker_head, fOnlyIfNotGeneric: win32more.Windows.Win32.Foundation.BOOL, ppmkComposite: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Enum(self, fForward: win32more.Windows.Win32.Foundation.BOOL, ppenumMoniker: POINTER(win32more.Windows.Win32.System.Com.IEnumMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsEqual(self, pmkOtherMoniker: win32more.Windows.Win32.System.Com.IMoniker_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Hash(self, pdwHash: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsRunning(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, pmkToLeft: win32more.Windows.Win32.System.Com.IMoniker_head, pmkNewlyRunning: win32more.Windows.Win32.System.Com.IMoniker_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTimeOfLastChange(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, pmkToLeft: win32more.Windows.Win32.System.Com.IMoniker_head, pFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Inverse(self, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CommonPrefixWith(self, pmkOther: win32more.Windows.Win32.System.Com.IMoniker_head, ppmkPrefix: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RelativePathTo(self, pmkOther: win32more.Windows.Win32.System.Com.IMoniker_head, ppmkRelPath: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDisplayName(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, pmkToLeft: win32more.Windows.Win32.System.Com.IMoniker_head, ppszDisplayName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ParseDisplayName(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, pmkToLeft: win32more.Windows.Win32.System.Com.IMoniker_head, pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmkOut: POINTER(win32more.Windows.Win32.System.Com.IMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsSystemMoniker(self, pdwMksys: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultiQI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000020-0000-0000-c000-000000000046}')
    @commethod(3)
    def QueryMultipleInterfaces(self, cMQIs: UInt32, pMQIs: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INTERFACEINFO(EasyCastStructure):
    pUnk: win32more.Windows.Win32.System.Com.IUnknown_head
    iid: Guid
    wMethod: UInt16
INVOKEKIND = Int32
INVOKE_FUNC: INVOKEKIND = 1
INVOKE_PROPERTYGET: INVOKEKIND = 2
INVOKE_PROPERTYPUT: INVOKEKIND = 4
INVOKE_PROPERTYPUTREF: INVOKEKIND = 8
class INoMarshal(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ecc8691b-c1db-4dc0-855e-65f6c551af49}')
class IOplockStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d19c834-8879-11d1-83e9-00c04fc2c6d4}')
    @commethod(3)
    def CreateStorageEx(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32, stgfmt: UInt32, grfAttrs: UInt32, riid: POINTER(Guid), ppstgOpen: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenStorageEx(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32, stgfmt: UInt32, grfAttrs: UInt32, riid: POINTER(Guid), ppstgOpen: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPSFactoryBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5f569d0-593b-101a-b569-08002b2dbf7a}')
    @commethod(3)
    def CreateProxy(self, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppProxy: POINTER(win32more.Windows.Win32.System.Com.IRpcProxyBuffer_head), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateStub(self, riid: POINTER(Guid), pUnkServer: win32more.Windows.Win32.System.Com.IUnknown_head, ppStub: POINTER(win32more.Windows.Win32.System.Com.IRpcStubBuffer_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersist(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000010c-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetClassID(self, pClassID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistFile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{0000010b-0000-0000-c000-000000000046}')
    @commethod(4)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, dwMode: win32more.Windows.Win32.System.Com.STGM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR, fRemember: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SaveCompleted(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurFile(self, ppszFileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistMemory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{bd1ae5e0-a6ae-11ce-bd37-504200c10000}')
    @commethod(4)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pMem: VoidPtr, cbSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pMem: VoidPtr, fClearDirty: win32more.Windows.Win32.Foundation.BOOL, cbSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSizeMax(self, pCbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InitNew(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{00000109-0000-0000-c000-000000000046}')
    @commethod(4)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pStm: win32more.Windows.Win32.System.Com.IStream_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pStm: win32more.Windows.Win32.System.Com.IStream_head, fClearDirty: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSizeMax(self, pcbSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistStreamInit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{7fd52380-4e07-101b-ae2d-08002b2ec713}')
    @commethod(4)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pStm: win32more.Windows.Win32.System.Com.IStream_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pStm: win32more.Windows.Win32.System.Com.IStream_head, fClearDirty: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSizeMax(self, pCbSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InitNew(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPipeByte(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db2f3aca-2f86-11d1-8e04-00c04fb9989a}')
    @commethod(3)
    def Pull(self, buf: POINTER(Byte), cRequest: UInt32, pcReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Push(self, buf: POINTER(Byte), cSent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPipeDouble(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db2f3ace-2f86-11d1-8e04-00c04fb9989a}')
    @commethod(3)
    def Pull(self, buf: POINTER(Double), cRequest: UInt32, pcReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Push(self, buf: POINTER(Double), cSent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPipeLong(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db2f3acc-2f86-11d1-8e04-00c04fb9989a}')
    @commethod(3)
    def Pull(self, buf: POINTER(Int32), cRequest: UInt32, pcReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Push(self, buf: POINTER(Int32), cSent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProcessInitControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{72380d55-8d2b-43a3-8513-2b6ef31434e9}')
    @commethod(3)
    def ResetInitializerTimeout(self, dwSecondsRemaining: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProcessLock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000001d5-0000-0000-c000-000000000046}')
    @commethod(3)
    def AddRefOnProcess(self) -> UInt32: ...
    @commethod(4)
    def ReleaseRefOnProcess(self) -> UInt32: ...
class IProgressNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9d758a0-4617-11cf-95fc-00aa00680db4}')
    @commethod(3)
    def OnProgress(self, dwProgressCurrent: UInt32, dwProgressMaximum: UInt32, fAccurate: win32more.Windows.Win32.Foundation.BOOL, fOwner: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IROTData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f29f6bc0-5021-11ce-aa15-00006901293f}')
    @commethod(3)
    def GetComparisonData(self, pbData: POINTER(Byte), cbMax: UInt32, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IReleaseMarshalBuffers(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eb0cb9e8-7996-11d2-872e-0000f8080859}')
    @commethod(3)
    def ReleaseMarshalBuffer(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), dwFlags: UInt32, pChnl: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRpcChannelBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5f56b60-593b-101a-b569-08002b2dbf7a}')
    @commethod(3)
    def GetBuffer(self, pMessage: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), riid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendReceive(self, pMessage: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FreeBuffer(self, pMessage: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDestCtx(self, pdwDestContext: POINTER(UInt32), ppvDestContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsConnected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRpcChannelBuffer2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IRpcChannelBuffer
    _iid_ = Guid('{594f31d0-7f19-11d0-b194-00a0c90dc8bf}')
    @commethod(8)
    def GetProtocolVersion(self, pdwVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRpcChannelBuffer3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IRpcChannelBuffer2
    _iid_ = Guid('{25b15600-0115-11d0-bf0d-00aa00b8dfd2}')
    @commethod(9)
    def Send(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pulStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Receive(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), ulSize: UInt32, pulStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCallContext(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), riid: POINTER(Guid), pInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDestCtxEx(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pdwDestContext: POINTER(UInt32), ppvDestContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetState(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterAsync(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), pAsyncMgr: win32more.Windows.Win32.System.Com.IAsyncManager_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRpcHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000149-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetDCOMProtocolVersion(self, pComVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIIDFromOBJREF(self, pObjRef: VoidPtr, piid: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRpcOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000144-0000-0000-c000-000000000046}')
    @commethod(3)
    def Set(self, pPrx: win32more.Windows.Win32.System.Com.IUnknown_head, dwProperty: win32more.Windows.Win32.System.Com.RPCOPT_PROPERTIES, dwValue: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Query(self, pPrx: win32more.Windows.Win32.System.Com.IUnknown_head, dwProperty: win32more.Windows.Win32.System.Com.RPCOPT_PROPERTIES, pdwValue: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRpcProxyBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5f56a34-593b-101a-b569-08002b2dbf7a}')
    @commethod(3)
    def Connect(self, pRpcChannelBuffer: win32more.Windows.Win32.System.Com.IRpcChannelBuffer_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self) -> Void: ...
class IRpcStubBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5f56afc-593b-101a-b569-08002b2dbf7a}')
    @commethod(3)
    def Connect(self, pUnkServer: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self) -> Void: ...
    @commethod(5)
    def Invoke(self, _prpcmsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head), _pRpcChannelBuffer: win32more.Windows.Win32.System.Com.IRpcChannelBuffer_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsIIDSupported(self, riid: POINTER(Guid)) -> win32more.Windows.Win32.System.Com.IRpcStubBuffer_head: ...
    @commethod(7)
    def CountRefs(self) -> UInt32: ...
    @commethod(8)
    def DebugServerQueryInterface(self, ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DebugServerRelease(self, pv: VoidPtr) -> Void: ...
class IRpcSyntaxNegotiate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{58a08519-24c8-4935-b482-3fd823333a4f}')
    @commethod(3)
    def NegotiateSyntax(self, pMsg: POINTER(win32more.Windows.Win32.System.Com.RPCOLEMESSAGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRunnableObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000126-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetRunningClass(self, lpClsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Run(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsRunning(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(6)
    def LockRunning(self, fLock: win32more.Windows.Win32.Foundation.BOOL, fLastUnlockCloses: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetContainedObject(self, fContained: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRunningObjectTable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000010-0000-0000-c000-000000000046}')
    @commethod(3)
    def Register(self, grfFlags: win32more.Windows.Win32.System.Com.ROT_FLAGS, punkObject: win32more.Windows.Win32.System.Com.IUnknown_head, pmkObjectName: win32more.Windows.Win32.System.Com.IMoniker_head, pdwRegister: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Revoke(self, dwRegister: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsRunning(self, pmkObjectName: win32more.Windows.Win32.System.Com.IMoniker_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(self, pmkObjectName: win32more.Windows.Win32.System.Com.IMoniker_head, ppunkObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NoteChangeTime(self, dwRegister: UInt32, pfiletime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTimeOfLastChange(self, pmkObjectName: win32more.Windows.Win32.System.Com.IMoniker_head, pfiletime: POINTER(win32more.Windows.Win32.Foundation.FILETIME_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRunning(self, ppenumMoniker: POINTER(win32more.Windows.Win32.System.Com.IEnumMoniker_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISequentialStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c733a30-2a1c-11ce-ade5-00aa0044773d}')
    @commethod(3)
    def Read(self, pv: VoidPtr, cb: UInt32, pcbRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IServerSecurity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013e-0000-0000-c000-000000000046}')
    @commethod(3)
    def QueryBlanket(self, pAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(POINTER(UInt16)), pAuthnLevel: POINTER(UInt32), pImpLevel: POINTER(UInt32), pPrivs: POINTER(VoidPtr), pCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ImpersonateClient(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RevertToSelf(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsImpersonating(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d5140c1-7436-11ce-8034-00aa006009fa}')
    @commethod(3)
    def QueryService(self, guidService: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStdMarshalInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000018-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetClassForHandler(self, dwDestContext: UInt32, pvDestContext: VoidPtr, pClsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.ISequentialStream
    _iid_ = Guid('{0000000c-0000-0000-c000-000000000046}')
    @commethod(5)
    def Seek(self, dlibMove: Int64, dwOrigin: win32more.Windows.Win32.System.Com.STREAM_SEEK, plibNewPosition: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(self, libNewSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyTo(self, pstm: win32more.Windows.Win32.System.Com.IStream_head, cb: UInt64, pcbRead: POINTER(UInt64), pcbWritten: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Commit(self, grfCommitFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Revert(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnlockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Stat(self, pstatstg: POINTER(win32more.Windows.Win32.System.Com.STATSTG_head), grfStatFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(self, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISupportAllowLowerTrustActivation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e9956ef2-3828-4b4b-8fa9-7db61dee4954}')
class ISupportErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df0b3d60-548f-101b-8e65-08002b2bd119}')
    @commethod(3)
    def InterfaceSupportsErrorInfo(self, riid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISurrogate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000022-0000-0000-c000-000000000046}')
    @commethod(3)
    def LoadDllServer(self, Clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FreeSurrogate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISurrogateService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000001d4-0000-0000-c000-000000000046}')
    @commethod(3)
    def Init(self, rguidProcessID: POINTER(Guid), pProcessLock: win32more.Windows.Win32.System.Com.IProcessLock_head, pfApplicationAware: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ApplicationLaunch(self, rguidApplID: POINTER(Guid), appType: win32more.Windows.Win32.System.Com.ApplicationType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ApplicationFree(self, rguidApplID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CatalogRefresh(self, ulReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessShutdown(self, shutdownType: win32more.Windows.Win32.System.Com.ShutdownType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISynchronize(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000030-0000-0000-c000-000000000046}')
    @commethod(3)
    def Wait(self, dwFlags: UInt32, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Signal(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISynchronizeContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000033-0000-0000-c000-000000000046}')
    @commethod(3)
    def AddSynchronize(self, pSync: win32more.Windows.Win32.System.Com.ISynchronize_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WaitMultiple(self, dwFlags: UInt32, dwTimeOut: UInt32, ppSync: POINTER(win32more.Windows.Win32.System.Com.ISynchronize_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISynchronizeEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.ISynchronizeHandle
    _iid_ = Guid('{00000032-0000-0000-c000-000000000046}')
    @commethod(4)
    def SetEventHandle(self, ph: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISynchronizeHandle(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000031-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetHandle(self, ph: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISynchronizeMutex(ComPtr):
    extends: win32more.Windows.Win32.System.Com.ISynchronize
    _iid_ = Guid('{00000025-0000-0000-c000-000000000046}')
    @commethod(6)
    def ReleaseMutex(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITimeAndNoticeControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc0bf6ae-8878-11d1-83e9-00c04fc2c6d4}')
    @commethod(3)
    def SuppressChanges(self, res1: UInt32, res2: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeComp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020403-0000-0000-c000-000000000046}')
    @commethod(3)
    def Bind(self, szName: win32more.Windows.Win32.Foundation.PWSTR, lHashVal: UInt32, wFlags: UInt16, ppTInfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo_head), pDescKind: POINTER(win32more.Windows.Win32.System.Com.DESCKIND), pBindPtr: POINTER(win32more.Windows.Win32.System.Com.BINDPTR_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BindType(self, szName: win32more.Windows.Win32.Foundation.PWSTR, lHashVal: UInt32, ppTInfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo_head), ppTComp: POINTER(win32more.Windows.Win32.System.Com.ITypeComp_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020401-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetTypeAttr(self, ppTypeAttr: POINTER(POINTER(win32more.Windows.Win32.System.Com.TYPEATTR_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypeComp(self, ppTComp: POINTER(win32more.Windows.Win32.System.Com.ITypeComp_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFuncDesc(self, index: UInt32, ppFuncDesc: POINTER(POINTER(win32more.Windows.Win32.System.Com.FUNCDESC_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVarDesc(self, index: UInt32, ppVarDesc: POINTER(POINTER(win32more.Windows.Win32.System.Com.VARDESC_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNames(self, memid: Int32, rgBstrNames: POINTER(win32more.Windows.Win32.Foundation.BSTR), cMaxNames: UInt32, pcNames: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetRefTypeOfImplType(self, index: UInt32, pRefType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetImplTypeFlags(self, index: UInt32, pImplTypeFlags: POINTER(win32more.Windows.Win32.System.Com.IMPLTYPEFLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetIDsOfNames(self, rgszNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cNames: UInt32, pMemId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Invoke(self, pvInstance: VoidPtr, memid: Int32, wFlags: win32more.Windows.Win32.System.Com.DISPATCH_FLAGS, pDispParams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS_head), pVarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head), pExcepInfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDocumentation(self, memid: Int32, pBstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pBstrDocString: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwHelpContext: POINTER(UInt32), pBstrHelpFile: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDllEntry(self, memid: Int32, invKind: win32more.Windows.Win32.System.Com.INVOKEKIND, pBstrDllName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pBstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pwOrdinal: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRefTypeInfo(self, hRefType: UInt32, ppTInfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AddressOfMember(self, memid: Int32, invKind: win32more.Windows.Win32.System.Com.INVOKEKIND, ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateInstance(self, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetMops(self, memid: Int32, pBstrMops: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetContainingTypeLib(self, ppTLib: POINTER(win32more.Windows.Win32.System.Com.ITypeLib_head), pIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ReleaseTypeAttr(self, pTypeAttr: POINTER(win32more.Windows.Win32.System.Com.TYPEATTR_head)) -> Void: ...
    @commethod(20)
    def ReleaseFuncDesc(self, pFuncDesc: POINTER(win32more.Windows.Win32.System.Com.FUNCDESC_head)) -> Void: ...
    @commethod(21)
    def ReleaseVarDesc(self, pVarDesc: POINTER(win32more.Windows.Win32.System.Com.VARDESC_head)) -> Void: ...
class ITypeInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.ITypeInfo
    _iid_ = Guid('{00020412-0000-0000-c000-000000000046}')
    @commethod(22)
    def GetTypeKind(self, pTypeKind: POINTER(win32more.Windows.Win32.System.Com.TYPEKIND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetTypeFlags(self, pTypeFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetFuncIndexOfMemId(self, memid: Int32, invKind: win32more.Windows.Win32.System.Com.INVOKEKIND, pFuncIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetVarIndexOfMemId(self, memid: Int32, pVarIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetCustData(self, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetFuncCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetParamCustData(self, indexFunc: UInt32, indexParam: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetVarCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetImplTypeCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetDocumentation2(self, memid: Int32, lcid: UInt32, pbstrHelpString: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwHelpStringContext: POINTER(UInt32), pbstrHelpStringDll: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetAllCustData(self, pCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetAllFuncCustData(self, index: UInt32, pCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetAllParamCustData(self, indexFunc: UInt32, indexParam: UInt32, pCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetAllVarCustData(self, index: UInt32, pCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetAllImplTypeCustData(self, index: UInt32, pCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeLib(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020402-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetTypeInfoCount(self) -> UInt32: ...
    @commethod(4)
    def GetTypeInfo(self, index: UInt32, ppTInfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTypeInfoType(self, index: UInt32, pTKind: POINTER(win32more.Windows.Win32.System.Com.TYPEKIND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTypeInfoOfGuid(self, guid: POINTER(Guid), ppTinfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLibAttr(self, ppTLibAttr: POINTER(POINTER(win32more.Windows.Win32.System.Com.TLIBATTR_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTypeComp(self, ppTComp: POINTER(win32more.Windows.Win32.System.Com.ITypeComp_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDocumentation(self, index: Int32, pBstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pBstrDocString: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwHelpContext: POINTER(UInt32), pBstrHelpFile: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsName(self, szNameBuf: win32more.Windows.Win32.Foundation.PWSTR, lHashVal: UInt32, pfName: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindName(self, szNameBuf: win32more.Windows.Win32.Foundation.PWSTR, lHashVal: UInt32, ppTInfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo_head), rgMemId: POINTER(Int32), pcFound: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ReleaseTLibAttr(self, pTLibAttr: POINTER(win32more.Windows.Win32.System.Com.TLIBATTR_head)) -> Void: ...
class ITypeLib2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.ITypeLib
    _iid_ = Guid('{00020411-0000-0000-c000-000000000046}')
    @commethod(13)
    def GetCustData(self, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetLibStatistics(self, pcUniqueNames: POINTER(UInt32), pcchUniqueNames: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDocumentation2(self, index: Int32, lcid: UInt32, pbstrHelpString: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwHelpStringContext: POINTER(UInt32), pbstrHelpStringDll: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAllCustData(self, pCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeLibRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{76a3e735-02df-4a12-98eb-043ad3600af3}')
    @commethod(3)
    def GetGuid(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersion(self, pVersion: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLcid(self, pLcid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetWin32Path(self, pWin32Path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetWin64Path(self, pWin64Path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayName(self, pDisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFlags(self, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetHelpDir(self, pHelpDir: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeLibRegistrationReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ed6a8a2a-b160-4e77-8f73-aa7435cd5c27}')
    @commethod(3)
    def EnumTypeLibRegistrations(self, ppEnumUnknown: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUnknown(ComPtr):
    extends: None
    _iid_ = Guid('{00000000-0000-0000-c000-000000000046}')
    @commethod(0)
    def QueryInterface(self, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(1)
    def AddRef(self) -> UInt32: ...
    @commethod(2)
    def Release(self) -> UInt32: ...
class IUri(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a39ee748-6a27-4817-a6f2-13914bef5890}')
    @commethod(3)
    def GetPropertyBSTR(self, uriProp: win32more.Windows.Win32.System.Com.Uri_PROPERTY, pbstrProperty: POINTER(win32more.Windows.Win32.Foundation.BSTR), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyLength(self, uriProp: win32more.Windows.Win32.System.Com.Uri_PROPERTY, pcchProperty: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyDWORD(self, uriProp: win32more.Windows.Win32.System.Com.Uri_PROPERTY, pdwProperty: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HasProperty(self, uriProp: win32more.Windows.Win32.System.Com.Uri_PROPERTY, pfHasProperty: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAbsoluteUri(self, pbstrAbsoluteUri: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAuthority(self, pbstrAuthority: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDisplayUri(self, pbstrDisplayString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDomain(self, pbstrDomain: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetExtension(self, pbstrExtension: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFragment(self, pbstrFragment: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHost(self, pbstrHost: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetPassword(self, pbstrPassword: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPath(self, pbstrPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetPathAndQuery(self, pbstrPathAndQuery: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetQuery(self, pbstrQuery: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetRawUri(self, pbstrRawUri: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetSchemeName(self, pbstrSchemeName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetUserInfo(self, pbstrUserInfo: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetUserName(self, pbstrUserName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetHostType(self, pdwHostType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetPort(self, pdwPort: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetScheme(self, pdwScheme: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetZone(self, pdwZone: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetProperties(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def IsEqual(self, pUri: win32more.Windows.Win32.System.Com.IUri_head, pfEqual: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUriBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4221b2e1-8955-46c0-bd5b-de9897565de7}')
    @commethod(3)
    def CreateUriSimple(self, dwAllowEncodingPropertyMask: UInt32, dwReserved: UIntPtr, ppIUri: POINTER(win32more.Windows.Win32.System.Com.IUri_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateUri(self, dwCreateFlags: UInt32, dwAllowEncodingPropertyMask: UInt32, dwReserved: UIntPtr, ppIUri: POINTER(win32more.Windows.Win32.System.Com.IUri_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateUriWithFlags(self, dwCreateFlags: UInt32, dwUriBuilderFlags: UInt32, dwAllowEncodingPropertyMask: UInt32, dwReserved: UIntPtr, ppIUri: POINTER(win32more.Windows.Win32.System.Com.IUri_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIUri(self, ppIUri: POINTER(win32more.Windows.Win32.System.Com.IUri_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetIUri(self, pIUri: win32more.Windows.Win32.System.Com.IUri_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFragment(self, pcchFragment: POINTER(UInt32), ppwzFragment: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetHost(self, pcchHost: POINTER(UInt32), ppwzHost: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPassword(self, pcchPassword: POINTER(UInt32), ppwzPassword: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPath(self, pcchPath: POINTER(UInt32), ppwzPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPort(self, pfHasPort: POINTER(win32more.Windows.Win32.Foundation.BOOL), pdwPort: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetQuery(self, pcchQuery: POINTER(UInt32), ppwzQuery: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSchemeName(self, pcchSchemeName: POINTER(UInt32), ppwzSchemeName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetUserName(self, pcchUserName: POINTER(UInt32), ppwzUserName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetFragment(self, pwzNewValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetHost(self, pwzNewValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetPassword(self, pwzNewValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetPath(self, pwzNewValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetPort(self, fHasPort: win32more.Windows.Win32.Foundation.BOOL, dwNewValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetQuery(self, pwzNewValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetSchemeName(self, pwzNewValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetUserName(self, pwzNewValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def RemoveProperties(self, dwPropertyMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def HasBeenModified(self, pfModified: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUrlMon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000026-0000-0000-c000-000000000046}')
    @commethod(3)
    def AsyncGetClassBits(self, rclsid: POINTER(Guid), pszTYPE: win32more.Windows.Win32.Foundation.PWSTR, pszExt: win32more.Windows.Win32.Foundation.PWSTR, dwFileVersionMS: UInt32, dwFileVersionLS: UInt32, pszCodeBase: win32more.Windows.Win32.Foundation.PWSTR, pbc: win32more.Windows.Win32.System.Com.IBindCtx_head, dwClassContext: UInt32, riid: POINTER(Guid), flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWaitMultiple(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002b-0000-0000-c000-000000000046}')
    @commethod(3)
    def WaitMultiple(self, timeout: UInt32, pSync: POINTER(win32more.Windows.Win32.System.Com.ISynchronize_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddSynchronize(self, pSync: win32more.Windows.Win32.System.Com.ISynchronize_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LOCKTYPE = Int32
LOCK_WRITE: LOCKTYPE = 1
LOCK_EXCLUSIVE: LOCKTYPE = 2
LOCK_ONLYONCE: LOCKTYPE = 4
@winfunctype_pointer
def LPEXCEPFINO_DEFERRED_FILLIN(pExcepInfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNCANUNLOADNOW() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNGETCLASSOBJECT(param0: POINTER(Guid), param1: POINTER(Guid), param2: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MEMCTX = Int32
MEMCTX_TASK: MEMCTX = 1
MEMCTX_SHARED: MEMCTX = 2
MEMCTX_MACSYSTEM: MEMCTX = 3
MEMCTX_UNKNOWN: MEMCTX = -1
MEMCTX_SAME: MEMCTX = -2
MKRREDUCE = Int32
MKRREDUCE_ONE: MKRREDUCE = 196608
MKRREDUCE_TOUSER: MKRREDUCE = 131072
MKRREDUCE_THROUGHUSER: MKRREDUCE = 65536
MKRREDUCE_ALL: MKRREDUCE = 0
MKSYS = Int32
MKSYS_NONE: MKSYS = 0
MKSYS_GENERICCOMPOSITE: MKSYS = 1
MKSYS_FILEMONIKER: MKSYS = 2
MKSYS_ANTIMONIKER: MKSYS = 3
MKSYS_ITEMMONIKER: MKSYS = 4
MKSYS_POINTERMONIKER: MKSYS = 5
MKSYS_CLASSMONIKER: MKSYS = 7
MKSYS_OBJREFMONIKER: MKSYS = 8
MKSYS_SESSIONMONIKER: MKSYS = 9
MKSYS_LUAMONIKER: MKSYS = 10
MSHCTX = Int32
MSHCTX_LOCAL: MSHCTX = 0
MSHCTX_NOSHAREDMEM: MSHCTX = 1
MSHCTX_DIFFERENTMACHINE: MSHCTX = 2
MSHCTX_INPROC: MSHCTX = 3
MSHCTX_CROSSCTX: MSHCTX = 4
MSHCTX_CONTAINER: MSHCTX = 5
MSHLFLAGS = Int32
MSHLFLAGS_NORMAL: MSHLFLAGS = 0
MSHLFLAGS_TABLESTRONG: MSHLFLAGS = 1
MSHLFLAGS_TABLEWEAK: MSHLFLAGS = 2
MSHLFLAGS_NOPING: MSHLFLAGS = 4
MSHLFLAGS_RESERVED1: MSHLFLAGS = 8
MSHLFLAGS_RESERVED2: MSHLFLAGS = 16
MSHLFLAGS_RESERVED3: MSHLFLAGS = 32
MSHLFLAGS_RESERVED4: MSHLFLAGS = 64
class MULTI_QI(EasyCastStructure):
    pIID: POINTER(Guid)
    pItf: win32more.Windows.Win32.System.Com.IUnknown_head
    hr: win32more.Windows.Win32.Foundation.HRESULT
MachineGlobalObjectTableRegistrationToken = IntPtr
PENDINGMSG = Int32
PENDINGMSG_CANCELCALL: PENDINGMSG = 0
PENDINGMSG_WAITNOPROCESS: PENDINGMSG = 1
PENDINGMSG_WAITDEFPROCESS: PENDINGMSG = 2
PENDINGTYPE = Int32
PENDINGTYPE_TOPLEVEL: PENDINGTYPE = 1
PENDINGTYPE_NESTED: PENDINGTYPE = 2
@winfunctype_pointer
def PFNCONTEXTCALL(pParam: POINTER(win32more.Windows.Win32.System.Com.ComCallData_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class QUERYCONTEXT(EasyCastStructure):
    dwContext: UInt32
    Platform: win32more.Windows.Win32.System.Com.CSPLATFORM
    Locale: UInt32
    dwVersionHi: UInt32
    dwVersionLo: UInt32
REGCLS = Int32
REGCLS_SINGLEUSE: REGCLS = 0
REGCLS_MULTIPLEUSE: REGCLS = 1
REGCLS_MULTI_SEPARATE: REGCLS = 2
REGCLS_SUSPENDED: REGCLS = 4
REGCLS_SURROGATE: REGCLS = 8
REGCLS_AGILE: REGCLS = 16
ROT_FLAGS = UInt32
ROTFLAGS_REGISTRATIONKEEPSALIVE: ROT_FLAGS = 1
ROTFLAGS_ALLOWANYCLIENT: ROT_FLAGS = 2
class RPCOLEMESSAGE(EasyCastStructure):
    reserved1: VoidPtr
    dataRepresentation: UInt32
    Buffer: VoidPtr
    cbBuffer: UInt32
    iMethod: UInt32
    reserved2: VoidPtr * 5
    rpcFlags: UInt32
RPCOPT_PROPERTIES = Int32
COMBND_RPCTIMEOUT: RPCOPT_PROPERTIES = 1
COMBND_SERVER_LOCALITY: RPCOPT_PROPERTIES = 2
COMBND_RESERVED1: RPCOPT_PROPERTIES = 4
COMBND_RESERVED2: RPCOPT_PROPERTIES = 5
COMBND_RESERVED3: RPCOPT_PROPERTIES = 8
COMBND_RESERVED4: RPCOPT_PROPERTIES = 16
RPCOPT_SERVER_LOCALITY_VALUES = Int32
SERVER_LOCALITY_PROCESS_LOCAL: RPCOPT_SERVER_LOCALITY_VALUES = 0
SERVER_LOCALITY_MACHINE_LOCAL: RPCOPT_SERVER_LOCALITY_VALUES = 1
SERVER_LOCALITY_REMOTE: RPCOPT_SERVER_LOCALITY_VALUES = 2
RPC_C_AUTHN_LEVEL = UInt32
RPC_C_AUTHN_LEVEL_DEFAULT: RPC_C_AUTHN_LEVEL = 0
RPC_C_AUTHN_LEVEL_NONE: RPC_C_AUTHN_LEVEL = 1
RPC_C_AUTHN_LEVEL_CONNECT: RPC_C_AUTHN_LEVEL = 2
RPC_C_AUTHN_LEVEL_CALL: RPC_C_AUTHN_LEVEL = 3
RPC_C_AUTHN_LEVEL_PKT: RPC_C_AUTHN_LEVEL = 4
RPC_C_AUTHN_LEVEL_PKT_INTEGRITY: RPC_C_AUTHN_LEVEL = 5
RPC_C_AUTHN_LEVEL_PKT_PRIVACY: RPC_C_AUTHN_LEVEL = 6
RPC_C_IMP_LEVEL = UInt32
RPC_C_IMP_LEVEL_DEFAULT: RPC_C_IMP_LEVEL = 0
RPC_C_IMP_LEVEL_ANONYMOUS: RPC_C_IMP_LEVEL = 1
RPC_C_IMP_LEVEL_IDENTIFY: RPC_C_IMP_LEVEL = 2
RPC_C_IMP_LEVEL_IMPERSONATE: RPC_C_IMP_LEVEL = 3
RPC_C_IMP_LEVEL_DELEGATE: RPC_C_IMP_LEVEL = 4
class RemSTGMEDIUM(EasyCastStructure):
    tymed: UInt32
    dwHandleType: UInt32
    pData: UInt32
    pUnkForRelease: UInt32
    cbData: UInt32
    data: Byte * 1
class SAFEARRAY(EasyCastStructure):
    cDims: UInt16
    fFeatures: win32more.Windows.Win32.System.Com.ADVANCED_FEATURE_FLAGS
    cbElements: UInt32
    cLocks: UInt32
    pvData: VoidPtr
    rgsabound: win32more.Windows.Win32.System.Com.SAFEARRAYBOUND * 1
class SAFEARRAYBOUND(EasyCastStructure):
    cElements: UInt32
    lLbound: Int32
class SChannelHookCallInfo(EasyCastStructure):
    iid: Guid
    cbSize: UInt32
    uCausality: Guid
    dwServerPid: UInt32
    iMethod: UInt32
    pObject: VoidPtr
SERVERCALL = Int32
SERVERCALL_ISHANDLED: SERVERCALL = 0
SERVERCALL_REJECTED: SERVERCALL = 1
SERVERCALL_RETRYLATER: SERVERCALL = 2
class SOLE_AUTHENTICATION_INFO(EasyCastStructure):
    dwAuthnSvc: UInt32
    dwAuthzSvc: UInt32
    pAuthInfo: VoidPtr
class SOLE_AUTHENTICATION_LIST(EasyCastStructure):
    cAuthInfo: UInt32
    aAuthInfo: POINTER(win32more.Windows.Win32.System.Com.SOLE_AUTHENTICATION_INFO_head)
class SOLE_AUTHENTICATION_SERVICE(EasyCastStructure):
    dwAuthnSvc: UInt32
    dwAuthzSvc: UInt32
    pPrincipalName: win32more.Windows.Win32.Foundation.PWSTR
    hr: win32more.Windows.Win32.Foundation.HRESULT
class STATDATA(EasyCastStructure):
    formatetc: win32more.Windows.Win32.System.Com.FORMATETC
    advf: UInt32
    pAdvSink: win32more.Windows.Win32.System.Com.IAdviseSink_head
    dwConnection: UInt32
STATFLAG = Int32
STATFLAG_DEFAULT: STATFLAG = 0
STATFLAG_NONAME: STATFLAG = 1
STATFLAG_NOOPEN: STATFLAG = 2
class STATSTG(EasyCastStructure):
    pwcsName: win32more.Windows.Win32.Foundation.PWSTR
    type: UInt32
    cbSize: UInt64
    mtime: win32more.Windows.Win32.Foundation.FILETIME
    ctime: win32more.Windows.Win32.Foundation.FILETIME
    atime: win32more.Windows.Win32.Foundation.FILETIME
    grfMode: win32more.Windows.Win32.System.Com.STGM
    grfLocksSupported: UInt32
    clsid: Guid
    grfStateBits: UInt32
    reserved: UInt32
STGC = Int32
STGC_DEFAULT: STGC = 0
STGC_OVERWRITE: STGC = 1
STGC_ONLYIFCURRENT: STGC = 2
STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE: STGC = 4
STGC_CONSOLIDATE: STGC = 8
STGM = UInt32
STGM_DIRECT: STGM = 0
STGM_TRANSACTED: STGM = 65536
STGM_SIMPLE: STGM = 134217728
STGM_READ: STGM = 0
STGM_WRITE: STGM = 1
STGM_READWRITE: STGM = 2
STGM_SHARE_DENY_NONE: STGM = 64
STGM_SHARE_DENY_READ: STGM = 48
STGM_SHARE_DENY_WRITE: STGM = 32
STGM_SHARE_EXCLUSIVE: STGM = 16
STGM_PRIORITY: STGM = 262144
STGM_DELETEONRELEASE: STGM = 67108864
STGM_NOSCRATCH: STGM = 1048576
STGM_CREATE: STGM = 4096
STGM_CONVERT: STGM = 131072
STGM_FAILIFTHERE: STGM = 0
STGM_NOSNAPSHOT: STGM = 2097152
STGM_DIRECT_SWMR: STGM = 4194304
class STGMEDIUM(EasyCastStructure):
    tymed: UInt32
    u: _u_e__Union
    pUnkForRelease: win32more.Windows.Win32.System.Com.IUnknown_head
    class _u_e__Union(EasyCastUnion):
        hBitmap: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
        hMetaFilePict: VoidPtr
        hEnhMetaFile: win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE
        hGlobal: win32more.Windows.Win32.Foundation.HGLOBAL
        lpszFileName: win32more.Windows.Win32.Foundation.PWSTR
        pstm: win32more.Windows.Win32.System.Com.IStream_head
        pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage_head
STGTY = Int32
STGTY_STORAGE: STGTY = 1
STGTY_STREAM: STGTY = 2
STGTY_LOCKBYTES: STGTY = 3
STGTY_PROPERTY: STGTY = 4
STREAM_SEEK = UInt32
STREAM_SEEK_SET: STREAM_SEEK = 0
STREAM_SEEK_CUR: STREAM_SEEK = 1
STREAM_SEEK_END: STREAM_SEEK = 2
SYSKIND = Int32
SYS_WIN16: SYSKIND = 0
SYS_WIN32: SYSKIND = 1
SYS_MAC: SYSKIND = 2
SYS_WIN64: SYSKIND = 3
ShutdownType = Int32
ShutdownType_IdleShutdown: ShutdownType = 0
ShutdownType_ForcedShutdown: ShutdownType = 1
class StorageLayout(EasyCastStructure):
    LayoutType: UInt32
    pwcsElementName: win32more.Windows.Win32.Foundation.PWSTR
    cOffset: Int64
    cBytes: Int64
THDTYPE = Int32
THDTYPE_BLOCKMESSAGES: THDTYPE = 0
THDTYPE_PROCESSMESSAGES: THDTYPE = 1
class TLIBATTR(EasyCastStructure):
    guid: Guid
    lcid: UInt32
    syskind: win32more.Windows.Win32.System.Com.SYSKIND
    wMajorVerNum: UInt16
    wMinorVerNum: UInt16
    wLibFlags: UInt16
TYMED = Int32
TYMED_HGLOBAL: TYMED = 1
TYMED_FILE: TYMED = 2
TYMED_ISTREAM: TYMED = 4
TYMED_ISTORAGE: TYMED = 8
TYMED_GDI: TYMED = 16
TYMED_MFPICT: TYMED = 32
TYMED_ENHMF: TYMED = 64
TYMED_NULL: TYMED = 0
class TYPEATTR(EasyCastStructure):
    guid: Guid
    lcid: UInt32
    dwReserved: UInt32
    memidConstructor: Int32
    memidDestructor: Int32
    lpstrSchema: win32more.Windows.Win32.Foundation.PWSTR
    cbSizeInstance: UInt32
    typekind: win32more.Windows.Win32.System.Com.TYPEKIND
    cFuncs: UInt16
    cVars: UInt16
    cImplTypes: UInt16
    cbSizeVft: UInt16
    cbAlignment: UInt16
    wTypeFlags: UInt16
    wMajorVerNum: UInt16
    wMinorVerNum: UInt16
    tdescAlias: win32more.Windows.Win32.System.Com.TYPEDESC
    idldescType: win32more.Windows.Win32.System.Com.IDLDESC
class TYPEDESC(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    vt: win32more.Windows.Win32.System.Variant.VARENUM
    class _Anonymous_e__Union(EasyCastUnion):
        lptdesc: POINTER(win32more.Windows.Win32.System.Com.TYPEDESC_head)
        lpadesc: POINTER(win32more.Windows.Win32.System.Ole.ARRAYDESC_head)
        hreftype: UInt32
TYPEKIND = Int32
TKIND_ENUM: TYPEKIND = 0
TKIND_RECORD: TYPEKIND = 1
TKIND_MODULE: TYPEKIND = 2
TKIND_INTERFACE: TYPEKIND = 3
TKIND_DISPATCH: TYPEKIND = 4
TKIND_COCLASS: TYPEKIND = 5
TKIND_ALIAS: TYPEKIND = 6
TKIND_UNION: TYPEKIND = 7
TKIND_MAX: TYPEKIND = 8
TYSPEC = Int32
TYSPEC_CLSID: TYSPEC = 0
TYSPEC_FILEEXT: TYSPEC = 1
TYSPEC_MIMETYPE: TYSPEC = 2
TYSPEC_FILENAME: TYSPEC = 3
TYSPEC_PROGID: TYSPEC = 4
TYSPEC_PACKAGENAME: TYSPEC = 5
TYSPEC_OBJECTID: TYSPEC = 6
URI_CREATE_FLAGS = UInt32
Uri_CREATE_ALLOW_RELATIVE: URI_CREATE_FLAGS = 1
Uri_CREATE_ALLOW_IMPLICIT_WILDCARD_SCHEME: URI_CREATE_FLAGS = 2
Uri_CREATE_ALLOW_IMPLICIT_FILE_SCHEME: URI_CREATE_FLAGS = 4
Uri_CREATE_NOFRAG: URI_CREATE_FLAGS = 8
Uri_CREATE_NO_CANONICALIZE: URI_CREATE_FLAGS = 16
Uri_CREATE_CANONICALIZE: URI_CREATE_FLAGS = 256
Uri_CREATE_FILE_USE_DOS_PATH: URI_CREATE_FLAGS = 32
Uri_CREATE_DECODE_EXTRA_INFO: URI_CREATE_FLAGS = 64
Uri_CREATE_NO_DECODE_EXTRA_INFO: URI_CREATE_FLAGS = 128
Uri_CREATE_CRACK_UNKNOWN_SCHEMES: URI_CREATE_FLAGS = 512
Uri_CREATE_NO_CRACK_UNKNOWN_SCHEMES: URI_CREATE_FLAGS = 1024
Uri_CREATE_PRE_PROCESS_HTML_URI: URI_CREATE_FLAGS = 2048
Uri_CREATE_NO_PRE_PROCESS_HTML_URI: URI_CREATE_FLAGS = 4096
Uri_CREATE_IE_SETTINGS: URI_CREATE_FLAGS = 8192
Uri_CREATE_NO_IE_SETTINGS: URI_CREATE_FLAGS = 16384
Uri_CREATE_NO_ENCODE_FORBIDDEN_CHARACTERS: URI_CREATE_FLAGS = 32768
Uri_CREATE_NORMALIZE_INTL_CHARACTERS: URI_CREATE_FLAGS = 65536
Uri_CREATE_CANONICALIZE_ABSOLUTE: URI_CREATE_FLAGS = 131072
Uri_PROPERTY = Int32
Uri_PROPERTY_ABSOLUTE_URI: Uri_PROPERTY = 0
Uri_PROPERTY_STRING_START: Uri_PROPERTY = 0
Uri_PROPERTY_AUTHORITY: Uri_PROPERTY = 1
Uri_PROPERTY_DISPLAY_URI: Uri_PROPERTY = 2
Uri_PROPERTY_DOMAIN: Uri_PROPERTY = 3
Uri_PROPERTY_EXTENSION: Uri_PROPERTY = 4
Uri_PROPERTY_FRAGMENT: Uri_PROPERTY = 5
Uri_PROPERTY_HOST: Uri_PROPERTY = 6
Uri_PROPERTY_PASSWORD: Uri_PROPERTY = 7
Uri_PROPERTY_PATH: Uri_PROPERTY = 8
Uri_PROPERTY_PATH_AND_QUERY: Uri_PROPERTY = 9
Uri_PROPERTY_QUERY: Uri_PROPERTY = 10
Uri_PROPERTY_RAW_URI: Uri_PROPERTY = 11
Uri_PROPERTY_SCHEME_NAME: Uri_PROPERTY = 12
Uri_PROPERTY_USER_INFO: Uri_PROPERTY = 13
Uri_PROPERTY_USER_NAME: Uri_PROPERTY = 14
Uri_PROPERTY_STRING_LAST: Uri_PROPERTY = 14
Uri_PROPERTY_HOST_TYPE: Uri_PROPERTY = 15
Uri_PROPERTY_DWORD_START: Uri_PROPERTY = 15
Uri_PROPERTY_PORT: Uri_PROPERTY = 16
Uri_PROPERTY_SCHEME: Uri_PROPERTY = 17
Uri_PROPERTY_ZONE: Uri_PROPERTY = 18
Uri_PROPERTY_DWORD_LAST: Uri_PROPERTY = 18
class VARDESC(EasyCastStructure):
    memid: Int32
    lpstrSchema: win32more.Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    elemdescVar: win32more.Windows.Win32.System.Com.ELEMDESC
    wVarFlags: win32more.Windows.Win32.System.Com.VARFLAGS
    varkind: win32more.Windows.Win32.System.Com.VARKIND
    class _Anonymous_e__Union(EasyCastUnion):
        oInst: UInt32
        lpvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT_head)
VARFLAGS = UInt16
VARFLAG_FREADONLY: VARFLAGS = 1
VARFLAG_FSOURCE: VARFLAGS = 2
VARFLAG_FBINDABLE: VARFLAGS = 4
VARFLAG_FREQUESTEDIT: VARFLAGS = 8
VARFLAG_FDISPLAYBIND: VARFLAGS = 16
VARFLAG_FDEFAULTBIND: VARFLAGS = 32
VARFLAG_FHIDDEN: VARFLAGS = 64
VARFLAG_FRESTRICTED: VARFLAGS = 128
VARFLAG_FDEFAULTCOLLELEM: VARFLAGS = 256
VARFLAG_FUIDEFAULT: VARFLAGS = 512
VARFLAG_FNONBROWSABLE: VARFLAGS = 1024
VARFLAG_FREPLACEABLE: VARFLAGS = 2048
VARFLAG_FIMMEDIATEBIND: VARFLAGS = 4096
VARKIND = Int32
VAR_PERINSTANCE: VARKIND = 0
VAR_STATIC: VARKIND = 1
VAR_CONST: VARKIND = 2
VAR_DISPATCH: VARKIND = 3
class WORD_BLOB(EasyCastStructure):
    clSize: UInt32
    asData: UInt16 * 1
class WORD_SIZEDARR(EasyCastStructure):
    clSize: UInt32
    pData: POINTER(UInt16)
class uCLSSPEC(EasyCastStructure):
    tyspec: UInt32
    tagged_union: _tagged_union_e__Struct
    class _tagged_union_e__Struct(EasyCastUnion):
        clsid: Guid
        pFileExt: win32more.Windows.Win32.Foundation.PWSTR
        pMimeType: win32more.Windows.Win32.Foundation.PWSTR
        pProgId: win32more.Windows.Win32.Foundation.PWSTR
        pFileName: win32more.Windows.Win32.Foundation.PWSTR
        ByName: _ByName_e__Struct
        ByObjectId: _ByObjectId_e__Struct
        class _ByName_e__Struct(EasyCastStructure):
            pPackageName: win32more.Windows.Win32.Foundation.PWSTR
            PolicyId: Guid
        class _ByObjectId_e__Struct(EasyCastStructure):
            ObjectId: Guid
            PolicyId: Guid
class userFLAG_STGMEDIUM(EasyCastStructure):
    ContextFlags: Int32
    fPassOwnership: Int32
    Stgmed: win32more.Windows.Win32.System.Com.userSTGMEDIUM
class userSTGMEDIUM(EasyCastStructure):
    u: _STGMEDIUM_UNION
    pUnkForRelease: win32more.Windows.Win32.System.Com.IUnknown_head
    class _STGMEDIUM_UNION(EasyCastStructure):
        tymed: UInt32
        u: _u_e__Struct
        class _u_e__Struct(EasyCastUnion):
            hMetaFilePict: POINTER(win32more.Windows.Win32.System.SystemServices.userHMETAFILEPICT_head)
            hHEnhMetaFile: POINTER(win32more.Windows.Win32.System.SystemServices.userHENHMETAFILE_head)
            hGdiHandle: POINTER(win32more.Windows.Win32.System.Com.GDI_OBJECT_head)
            hGlobal: POINTER(win32more.Windows.Win32.System.SystemServices.userHGLOBAL_head)
            lpszFileName: win32more.Windows.Win32.Foundation.PWSTR
            pstm: POINTER(win32more.Windows.Win32.System.Com.BYTE_BLOB_head)
            pstg: POINTER(win32more.Windows.Win32.System.Com.BYTE_BLOB_head)
make_head(_module, 'AUTHENTICATEINFO')
make_head(_module, 'AsyncIAdviseSink')
make_head(_module, 'AsyncIAdviseSink2')
make_head(_module, 'AsyncIMultiQI')
make_head(_module, 'AsyncIPipeByte')
make_head(_module, 'AsyncIPipeDouble')
make_head(_module, 'AsyncIPipeLong')
make_head(_module, 'AsyncIUnknown')
make_head(_module, 'BINDINFO')
make_head(_module, 'BINDPTR')
make_head(_module, 'BIND_OPTS')
make_head(_module, 'BIND_OPTS2')
make_head(_module, 'BIND_OPTS3')
make_head(_module, 'BLOB')
make_head(_module, 'BYTE_BLOB')
make_head(_module, 'BYTE_SIZEDARR')
make_head(_module, 'CATEGORYINFO')
make_head(_module, 'COAUTHIDENTITY')
make_head(_module, 'COAUTHINFO')
make_head(_module, 'CONNECTDATA')
make_head(_module, 'COSERVERINFO')
make_head(_module, 'CSPLATFORM')
make_head(_module, 'CUSTDATA')
make_head(_module, 'CUSTDATAITEM')
make_head(_module, 'CY')
make_head(_module, 'ComCallData')
make_head(_module, 'ContextProperty')
make_head(_module, 'DISPPARAMS')
make_head(_module, 'DVTARGETDEVICE')
make_head(_module, 'DWORD_BLOB')
make_head(_module, 'DWORD_SIZEDARR')
make_head(_module, 'ELEMDESC')
make_head(_module, 'EXCEPINFO')
make_head(_module, 'FLAGGED_BYTE_BLOB')
make_head(_module, 'FLAGGED_WORD_BLOB')
make_head(_module, 'FLAG_STGMEDIUM')
make_head(_module, 'FORMATETC')
make_head(_module, 'FUNCDESC')
make_head(_module, 'GDI_OBJECT')
make_head(_module, 'HYPER_SIZEDARR')
make_head(_module, 'IActivationFilter')
make_head(_module, 'IAddrExclusionControl')
make_head(_module, 'IAddrTrackingControl')
make_head(_module, 'IAdviseSink')
make_head(_module, 'IAdviseSink2')
make_head(_module, 'IAgileObject')
make_head(_module, 'IAsyncManager')
make_head(_module, 'IAsyncRpcChannelBuffer')
make_head(_module, 'IAuthenticate')
make_head(_module, 'IAuthenticateEx')
make_head(_module, 'IBindCtx')
make_head(_module, 'IBindHost')
make_head(_module, 'IBindStatusCallback')
make_head(_module, 'IBindStatusCallbackEx')
make_head(_module, 'IBinding')
make_head(_module, 'IBlockingLock')
make_head(_module, 'ICallFactory')
make_head(_module, 'ICancelMethodCalls')
make_head(_module, 'ICatInformation')
make_head(_module, 'ICatRegister')
make_head(_module, 'IChannelHook')
make_head(_module, 'IClassActivator')
make_head(_module, 'IClassFactory')
make_head(_module, 'IClientSecurity')
make_head(_module, 'IComThreadingInfo')
make_head(_module, 'IConnectionPoint')
make_head(_module, 'IConnectionPointContainer')
make_head(_module, 'IContext')
make_head(_module, 'IContextCallback')
make_head(_module, 'IDLDESC')
make_head(_module, 'IDataAdviseHolder')
make_head(_module, 'IDataObject')
make_head(_module, 'IDispatch')
make_head(_module, 'IEnumCATEGORYINFO')
make_head(_module, 'IEnumConnectionPoints')
make_head(_module, 'IEnumConnections')
make_head(_module, 'IEnumContextProps')
make_head(_module, 'IEnumFORMATETC')
make_head(_module, 'IEnumGUID')
make_head(_module, 'IEnumMoniker')
make_head(_module, 'IEnumSTATDATA')
make_head(_module, 'IEnumString')
make_head(_module, 'IEnumUnknown')
make_head(_module, 'IErrorInfo')
make_head(_module, 'IErrorLog')
make_head(_module, 'IExternalConnection')
make_head(_module, 'IFastRundown')
make_head(_module, 'IForegroundTransfer')
make_head(_module, 'IGlobalInterfaceTable')
make_head(_module, 'IGlobalOptions')
make_head(_module, 'IInitializeSpy')
make_head(_module, 'IInternalUnknown')
make_head(_module, 'IMachineGlobalObjectTable')
make_head(_module, 'IMalloc')
make_head(_module, 'IMallocSpy')
make_head(_module, 'IMoniker')
make_head(_module, 'IMultiQI')
make_head(_module, 'INTERFACEINFO')
make_head(_module, 'INoMarshal')
make_head(_module, 'IOplockStorage')
make_head(_module, 'IPSFactoryBuffer')
make_head(_module, 'IPersist')
make_head(_module, 'IPersistFile')
make_head(_module, 'IPersistMemory')
make_head(_module, 'IPersistStream')
make_head(_module, 'IPersistStreamInit')
make_head(_module, 'IPipeByte')
make_head(_module, 'IPipeDouble')
make_head(_module, 'IPipeLong')
make_head(_module, 'IProcessInitControl')
make_head(_module, 'IProcessLock')
make_head(_module, 'IProgressNotify')
make_head(_module, 'IROTData')
make_head(_module, 'IReleaseMarshalBuffers')
make_head(_module, 'IRpcChannelBuffer')
make_head(_module, 'IRpcChannelBuffer2')
make_head(_module, 'IRpcChannelBuffer3')
make_head(_module, 'IRpcHelper')
make_head(_module, 'IRpcOptions')
make_head(_module, 'IRpcProxyBuffer')
make_head(_module, 'IRpcStubBuffer')
make_head(_module, 'IRpcSyntaxNegotiate')
make_head(_module, 'IRunnableObject')
make_head(_module, 'IRunningObjectTable')
make_head(_module, 'ISequentialStream')
make_head(_module, 'IServerSecurity')
make_head(_module, 'IServiceProvider')
make_head(_module, 'IStdMarshalInfo')
make_head(_module, 'IStream')
make_head(_module, 'ISupportAllowLowerTrustActivation')
make_head(_module, 'ISupportErrorInfo')
make_head(_module, 'ISurrogate')
make_head(_module, 'ISurrogateService')
make_head(_module, 'ISynchronize')
make_head(_module, 'ISynchronizeContainer')
make_head(_module, 'ISynchronizeEvent')
make_head(_module, 'ISynchronizeHandle')
make_head(_module, 'ISynchronizeMutex')
make_head(_module, 'ITimeAndNoticeControl')
make_head(_module, 'ITypeComp')
make_head(_module, 'ITypeInfo')
make_head(_module, 'ITypeInfo2')
make_head(_module, 'ITypeLib')
make_head(_module, 'ITypeLib2')
make_head(_module, 'ITypeLibRegistration')
make_head(_module, 'ITypeLibRegistrationReader')
make_head(_module, 'IUnknown')
make_head(_module, 'IUri')
make_head(_module, 'IUriBuilder')
make_head(_module, 'IUrlMon')
make_head(_module, 'IWaitMultiple')
make_head(_module, 'LPEXCEPFINO_DEFERRED_FILLIN')
make_head(_module, 'LPFNCANUNLOADNOW')
make_head(_module, 'LPFNGETCLASSOBJECT')
make_head(_module, 'MULTI_QI')
make_head(_module, 'PFNCONTEXTCALL')
make_head(_module, 'QUERYCONTEXT')
make_head(_module, 'RPCOLEMESSAGE')
make_head(_module, 'RemSTGMEDIUM')
make_head(_module, 'SAFEARRAY')
make_head(_module, 'SAFEARRAYBOUND')
make_head(_module, 'SChannelHookCallInfo')
make_head(_module, 'SOLE_AUTHENTICATION_INFO')
make_head(_module, 'SOLE_AUTHENTICATION_LIST')
make_head(_module, 'SOLE_AUTHENTICATION_SERVICE')
make_head(_module, 'STATDATA')
make_head(_module, 'STATSTG')
make_head(_module, 'STGMEDIUM')
make_head(_module, 'StorageLayout')
make_head(_module, 'TLIBATTR')
make_head(_module, 'TYPEATTR')
make_head(_module, 'TYPEDESC')
make_head(_module, 'VARDESC')
make_head(_module, 'WORD_BLOB')
make_head(_module, 'WORD_SIZEDARR')
make_head(_module, 'uCLSSPEC')
make_head(_module, 'userFLAG_STGMEDIUM')
make_head(_module, 'userSTGMEDIUM')