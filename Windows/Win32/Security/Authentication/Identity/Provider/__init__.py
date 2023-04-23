from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Security.Authentication.Identity.Provider
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ACCOUNT_STATE = Int32
NOT_CONNECTED: ACCOUNT_STATE = 0
CONNECTING: ACCOUNT_STATE = 1
CONNECT_COMPLETED: ACCOUNT_STATE = 2
IDENTITY_KEYWORD_ASSOCIATED: String = 'associated'
IDENTITY_KEYWORD_LOCAL: String = 'local'
IDENTITY_KEYWORD_HOMEGROUP: String = 'homegroup'
IDENTITY_KEYWORD_CONNECTED: String = 'connected'
OID_OAssociatedIdentityProviderObject: Guid = Guid('98c5a3dd-db68-4f1a-8d-2b-90-79-cd-fe-af-61')
STR_OUT_OF_BOX_EXPERIENCE: String = 'OutOfBoxExperience'
STR_MODERN_SETTINGS_ADD_USER: String = 'ModernSettingsAddUser'
STR_OUT_OF_BOX_UPGRADE_EXPERIENCE: String = 'OutOfBoxUpgradeExperience'
STR_COMPLETE_ACCOUNT: String = 'CompleteAccount'
STR_NTH_USER_FIRST_AUTH: String = 'NthUserFirstAuth'
STR_USER_NAME: String = 'Username'
STR_PROPERTY_STORE: String = 'PropertyStore'
class AsyncIAssociatedIdentityProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2834d6ed-297e-4e72-8a-51-96-1e-86-f0-51-52')
    @commethod(3)
    def Begin_AssociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_AssociateIdentity(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DisassociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DisassociateIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_ChangeCredential(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_ChangeCredential(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIConnectedIdentityProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9ce55141-bce9-4e15-82-4d-43-d7-9f-51-2f-93')
    @commethod(3)
    def Begin_ConnectIdentity(self, AuthBuffer: POINTER(Byte), AuthBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_ConnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DisconnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DisconnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_IsConnected(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_IsConnected(self, Connected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_GetUrl(self, Identifier: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_URL, Context: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_GetUrl(self, PostData: POINTER(Windows.Win32.System.Com.VARIANT_head), Url: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_GetAccountState(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_GetAccountState(self, pState: POINTER(Windows.Win32.Security.Authentication.Identity.Provider.ACCOUNT_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityAdvise(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3ab4c8da-d038-4830-8d-d9-32-53-c5-5a-12-7f')
    @commethod(3)
    def Begin_IdentityUpdated(self, dwIdentityUpdateEvents: UInt32, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_IdentityUpdated(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityAuthentication(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f9a2f918-feca-4e9c-96-33-61-cb-f1-3e-d3-4d')
    @commethod(3)
    def Begin_SetIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_SetIdentityCredential(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_ValidateIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32, ppIdentityProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_ValidateIdentityCredential(self, ppIdentityProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c6fc9901-c433-4646-8f-48-4e-46-87-aa-e2-a0')
    @commethod(3)
    def Begin_GetIdentityEnum(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_GetIdentityEnum(self, ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Create(self, lpszUserName: Windows.Win32.Foundation.PWSTR, pKeywordsToAdd: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Create(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_Import(self, pPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_Import(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_Delete(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, pKeywordsToDelete: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_FindByUniqueID(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_FindByUniqueID(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Begin_GetProviderPropertyStore(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Finish_GetProviderPropertyStore(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Begin_Advise(self, pIdentityAdvise: Windows.Win32.Security.Authentication.Identity.Provider.IIdentityAdvise_head, dwIdentityUpdateEvents: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Finish_Advise(self, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Begin_UnAdvise(self, dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Finish_UnAdvise(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eefa1616-48de-4872-aa-64-6e-62-06-53-5a-51')
    @commethod(3)
    def Begin_GetCount(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_GetCount(self, pdwProviders: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_GetAt(self, dwProvider: UInt32, pProvGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_GetAt(self, pProvGuid: POINTER(Guid), ppIdentityProvider: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Begin_AddToCache(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_AddToCache(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Begin_ConvertToSid(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid), cbSid: UInt16, pSid: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Finish_ConvertToSid(self, pSid: POINTER(Byte), pcbRequiredSid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Begin_EnumerateIdentities(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Finish_EnumerateIdentities(self, ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Begin_Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Finish_Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class AsyncIIdentityStoreEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fca3af9a-8a07-4eae-86-32-ec-3d-e6-58-a3-6a')
    @commethod(3)
    def Begin_CreateConnectedIdentity(self, LocalName: Windows.Win32.Foundation.PWSTR, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_CreateConnectedIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_DeleteConnectedIdentity(self, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_DeleteConnectedIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
CIdentityProfileHandler = Guid('ecf5bf46-e3b6-449a-b5-6b-43-f5-8f-86-78-14')
CoClassIdentityStore = Guid('30d49246-d217-465f-b0-0b-ac-9d-dd-65-2e-b7')
class IAssociatedIdentityProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2af066b3-4cbb-4cba-a7-98-20-4b-6a-f6-8c-c0')
    @commethod(3)
    def AssociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisassociateIdentity(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChangeCredential(self, hwndParent: Windows.Win32.Foundation.HWND, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IConnectedIdentityProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b7417b54-e08c-429b-96-c8-67-8d-13-69-ec-b1')
    @commethod(3)
    def ConnectIdentity(self, AuthBuffer: POINTER(Byte), AuthBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisconnectIdentity(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsConnected(self, Connected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUrl(self, Identifier: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_URL, Context: Windows.Win32.System.Com.IBindCtx_head, PostData: POINTER(Windows.Win32.System.Com.VARIANT_head), Url: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAccountState(self, pState: POINTER(Windows.Win32.Security.Authentication.Identity.Provider.ACCOUNT_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
IDENTITY_TYPE = Int32
IDENTITIES_ALL: IDENTITY_TYPE = 0
IDENTITIES_ME_ONLY: IDENTITY_TYPE = 1
IDENTITY_URL = Int32
IDENTITY_URL_CREATE_ACCOUNT_WIZARD: IDENTITY_URL = 0
IDENTITY_URL_SIGN_IN_WIZARD: IDENTITY_URL = 1
IDENTITY_URL_CHANGE_PASSWORD_WIZARD: IDENTITY_URL = 2
IDENTITY_URL_IFEXISTS_WIZARD: IDENTITY_URL = 3
IDENTITY_URL_ACCOUNT_SETTINGS: IDENTITY_URL = 4
IDENTITY_URL_RESTORE_WIZARD: IDENTITY_URL = 5
IDENTITY_URL_CONNECT_WIZARD: IDENTITY_URL = 6
class IIdentityAdvise(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4e982fed-d14b-440c-b8-d6-bb-38-64-53-d3-86')
    @commethod(3)
    def IdentityUpdated(self, dwIdentityUpdateEvents: Windows.Win32.Security.Authentication.Identity.Provider.IdentityUpdateEvent, lpszUniqueID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityAuthentication(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5e7ef254-979f-43b5-b7-4e-06-e4-eb-7d-f0-f9')
    @commethod(3)
    def SetIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ValidateIdentityCredential(self, CredBuffer: POINTER(Byte), CredBufferLength: UInt32, ppIdentityProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0d1b9e0c-e8ba-4f55-a8-1b-bc-e9-34-b9-48-f5')
    @commethod(3)
    def GetIdentityEnum(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Create(self, lpszUserName: Windows.Win32.Foundation.PWSTR, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head), pKeywordsToAdd: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Import(self, pPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, pKeywordsToDelete: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindByUniqueID(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProviderPropertyStore(self, ppPropertyStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(self, pIdentityAdvise: Windows.Win32.Security.Authentication.Identity.Provider.IIdentityAdvise_head, dwIdentityUpdateEvents: Windows.Win32.Security.Authentication.Identity.Provider.IdentityUpdateEvent, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UnAdvise(self, dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('df586fa5-6f35-44f1-b2-09-b3-8e-16-97-72-eb')
    @commethod(3)
    def GetCount(self, pdwProviders: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, dwProvider: UInt32, pProvGuid: POINTER(Guid), ppIdentityProvider: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddToCache(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertToSid(self, lpszUniqueID: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid), cbSid: UInt16, pSid: POINTER(Byte), pcbRequiredSid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumerateIdentities(self, eIdentityType: Windows.Win32.Security.Authentication.Identity.Provider.IDENTITY_TYPE, pFilterkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pFilterPropVarValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppIdentityEnum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityStoreEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f9f9eb98-8f7f-4e38-95-77-69-80-11-4c-e3-2b')
    @commethod(3)
    def CreateConnectedIdentity(self, LocalName: Windows.Win32.Foundation.PWSTR, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteConnectedIdentity(self, ConnectedName: Windows.Win32.Foundation.PWSTR, ProviderGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
IdentityUpdateEvent = Int32
IDENTITY_ASSOCIATED: IdentityUpdateEvent = 1
IDENTITY_DISASSOCIATED: IdentityUpdateEvent = 2
IDENTITY_CREATED: IdentityUpdateEvent = 4
IDENTITY_IMPORTED: IdentityUpdateEvent = 8
IDENTITY_DELETED: IdentityUpdateEvent = 16
IDENTITY_PROPCHANGED: IdentityUpdateEvent = 32
IDENTITY_CONNECTED: IdentityUpdateEvent = 64
IDENTITY_DISCONNECTED: IdentityUpdateEvent = 128
make_head(_module, 'AsyncIAssociatedIdentityProvider')
make_head(_module, 'AsyncIConnectedIdentityProvider')
make_head(_module, 'AsyncIIdentityAdvise')
make_head(_module, 'AsyncIIdentityAuthentication')
make_head(_module, 'AsyncIIdentityProvider')
make_head(_module, 'AsyncIIdentityStore')
make_head(_module, 'AsyncIIdentityStoreEx')
make_head(_module, 'IAssociatedIdentityProvider')
make_head(_module, 'IConnectedIdentityProvider')
make_head(_module, 'IIdentityAdvise')
make_head(_module, 'IIdentityAuthentication')
make_head(_module, 'IIdentityProvider')
make_head(_module, 'IIdentityStore')
make_head(_module, 'IIdentityStoreEx')