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
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Gaming.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _GameBar_Meta_(ComPtr.__class__):
    pass
class GameBar(ComPtr, metaclass=_GameBar_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.UI.GameBar'
    @winrt_classmethod
    def add_VisibilityChanged(cls: win32more.Windows.Gaming.UI.IGameBarStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_VisibilityChanged(cls: win32more.Windows.Gaming.UI.IGameBarStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_IsInputRedirectedChanged(cls: win32more.Windows.Gaming.UI.IGameBarStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_IsInputRedirectedChanged(cls: win32more.Windows.Gaming.UI.IGameBarStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Visible(cls: win32more.Windows.Gaming.UI.IGameBarStatics) -> Boolean: ...
    @winrt_classmethod
    def get_IsInputRedirected(cls: win32more.Windows.Gaming.UI.IGameBarStatics) -> Boolean: ...
    _GameBar_Meta_.Visible = property(get_Visible.__wrapped__, None)
    _GameBar_Meta_.IsInputRedirected = property(get_IsInputRedirected.__wrapped__, None)
GameChatMessageOrigin = Int32
GameChatMessageOrigin_Voice: GameChatMessageOrigin = 0
GameChatMessageOrigin_Text: GameChatMessageOrigin = 1
class GameChatMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.UI.IGameChatMessageReceivedEventArgs
    _classid_ = 'Windows.Gaming.UI.GameChatMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Gaming.UI.IGameChatMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppDisplayName(self: win32more.Windows.Gaming.UI.IGameChatMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SenderName(self: win32more.Windows.Gaming.UI.IGameChatMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Windows.Gaming.UI.IGameChatMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Origin(self: win32more.Windows.Gaming.UI.IGameChatMessageReceivedEventArgs) -> win32more.Windows.Gaming.UI.GameChatMessageOrigin: ...
    AppId = property(get_AppId, None)
    AppDisplayName = property(get_AppDisplayName, None)
    SenderName = property(get_SenderName, None)
    Message = property(get_Message, None)
    Origin = property(get_Origin, None)
class GameChatOverlay(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.UI.IGameChatOverlay
    _classid_ = 'Windows.Gaming.UI.GameChatOverlay'
    @winrt_mixinmethod
    def get_DesiredPosition(self: win32more.Windows.Gaming.UI.IGameChatOverlay) -> win32more.Windows.Gaming.UI.GameChatOverlayPosition: ...
    @winrt_mixinmethod
    def put_DesiredPosition(self: win32more.Windows.Gaming.UI.IGameChatOverlay, value: win32more.Windows.Gaming.UI.GameChatOverlayPosition) -> Void: ...
    @winrt_mixinmethod
    def AddMessage(self: win32more.Windows.Gaming.UI.IGameChatOverlay, sender: WinRT_String, message: WinRT_String, origin: win32more.Windows.Gaming.UI.GameChatMessageOrigin) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Gaming.UI.IGameChatOverlayStatics) -> win32more.Windows.Gaming.UI.GameChatOverlay: ...
    DesiredPosition = property(get_DesiredPosition, put_DesiredPosition)
GameChatOverlayContract: UInt32 = 65536
class GameChatOverlayMessageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.UI.IGameChatOverlayMessageSource
    _classid_ = 'Windows.Gaming.UI.GameChatOverlayMessageSource'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Gaming.UI.GameChatOverlayMessageSource: ...
    @winrt_mixinmethod
    def add_MessageReceived(self: win32more.Windows.Gaming.UI.IGameChatOverlayMessageSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.UI.GameChatOverlayMessageSource, win32more.Windows.Gaming.UI.GameChatMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MessageReceived(self: win32more.Windows.Gaming.UI.IGameChatOverlayMessageSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetDelayBeforeClosingAfterMessageReceived(self: win32more.Windows.Gaming.UI.IGameChatOverlayMessageSource, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
GameChatOverlayPosition = Int32
GameChatOverlayPosition_BottomCenter: GameChatOverlayPosition = 0
GameChatOverlayPosition_BottomLeft: GameChatOverlayPosition = 1
GameChatOverlayPosition_BottomRight: GameChatOverlayPosition = 2
GameChatOverlayPosition_MiddleRight: GameChatOverlayPosition = 3
GameChatOverlayPosition_MiddleLeft: GameChatOverlayPosition = 4
GameChatOverlayPosition_TopCenter: GameChatOverlayPosition = 5
GameChatOverlayPosition_TopLeft: GameChatOverlayPosition = 6
GameChatOverlayPosition_TopRight: GameChatOverlayPosition = 7
class GameUIProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.UI.IGameUIProviderActivatedEventArgs
    _classid_ = 'Windows.Gaming.UI.GameUIProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_GameUIArgs(self: win32more.Windows.Gaming.UI.IGameUIProviderActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.Gaming.UI.IGameUIProviderActivatedEventArgs, results: win32more.Windows.Foundation.Collections.ValueSet) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    GameUIArgs = property(get_GameUIArgs, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
GamingUIProviderContract: UInt32 = 65536
class IGameBarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.UI.IGameBarStatics'
    _iid_ = Guid('{1db9a292-cc78-4173-be45-b61e67283ea7}')
    @winrt_commethod(6)
    def add_VisibilityChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_VisibilityChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_IsInputRedirectedChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IsInputRedirectedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsInputRedirected(self) -> Boolean: ...
    Visible = property(get_Visible, None)
    IsInputRedirected = property(get_IsInputRedirected, None)
class IGameChatMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.UI.IGameChatMessageReceivedEventArgs'
    _iid_ = Guid('{a28201f1-3fb9-4e42-a403-7afce2023b1e}')
    @winrt_commethod(6)
    def get_AppId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SenderName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Origin(self) -> win32more.Windows.Gaming.UI.GameChatMessageOrigin: ...
    AppId = property(get_AppId, None)
    AppDisplayName = property(get_AppDisplayName, None)
    SenderName = property(get_SenderName, None)
    Message = property(get_Message, None)
    Origin = property(get_Origin, None)
class IGameChatOverlay(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.UI.IGameChatOverlay'
    _iid_ = Guid('{fbc64865-f6fc-4a48-ae07-03ac6ed43704}')
    @winrt_commethod(6)
    def get_DesiredPosition(self) -> win32more.Windows.Gaming.UI.GameChatOverlayPosition: ...
    @winrt_commethod(7)
    def put_DesiredPosition(self, value: win32more.Windows.Gaming.UI.GameChatOverlayPosition) -> Void: ...
    @winrt_commethod(8)
    def AddMessage(self, sender: WinRT_String, message: WinRT_String, origin: win32more.Windows.Gaming.UI.GameChatMessageOrigin) -> Void: ...
    DesiredPosition = property(get_DesiredPosition, put_DesiredPosition)
class IGameChatOverlayMessageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.UI.IGameChatOverlayMessageSource'
    _iid_ = Guid('{1e177397-59fb-4f4f-8e9a-80acf817743c}')
    @winrt_commethod(6)
    def add_MessageReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Gaming.UI.GameChatOverlayMessageSource, win32more.Windows.Gaming.UI.GameChatMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MessageReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def SetDelayBeforeClosingAfterMessageReceived(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
class IGameChatOverlayStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.UI.IGameChatOverlayStatics'
    _iid_ = Guid('{89acf614-7867-49f7-9687-25d9dbf444d1}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Gaming.UI.GameChatOverlay: ...
class IGameUIProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.UI.IGameUIProviderActivatedEventArgs'
    _iid_ = Guid('{a7b3203e-caf7-4ded-bbd2-47de43bb6dd5}')
    @winrt_commethod(6)
    def get_GameUIArgs(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(7)
    def ReportCompleted(self, results: win32more.Windows.Foundation.Collections.ValueSet) -> Void: ...
    GameUIArgs = property(get_GameUIArgs, None)
make_head(_module, 'GameBar')
make_head(_module, 'GameChatMessageReceivedEventArgs')
make_head(_module, 'GameChatOverlay')
make_head(_module, 'GameChatOverlayMessageSource')
make_head(_module, 'GameUIProviderActivatedEventArgs')
make_head(_module, 'IGameBarStatics')
make_head(_module, 'IGameChatMessageReceivedEventArgs')
make_head(_module, 'IGameChatOverlay')
make_head(_module, 'IGameChatOverlayMessageSource')
make_head(_module, 'IGameChatOverlayStatics')
make_head(_module, 'IGameUIProviderActivatedEventArgs')