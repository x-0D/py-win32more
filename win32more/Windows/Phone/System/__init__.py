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
import win32more.Windows.Phone.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISystemProtectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.ISystemProtectionStatics'
    _iid_ = Guid('{49c36560-97e1-4d99-8bfb-befeaa6ace6d}')
    @winrt_commethod(6)
    def get_ScreenLocked(self) -> Boolean: ...
    ScreenLocked = property(get_ScreenLocked, None)
class ISystemProtectionUnlockStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.ISystemProtectionUnlockStatics'
    _iid_ = Guid('{0692fa3f-8f11-4c4b-aa0d-87d7af7b1779}')
    @winrt_commethod(6)
    def RequestScreenUnlock(self) -> Void: ...
class _SystemProtection_Meta_(ComPtr.__class__):
    pass
class SystemProtection(ComPtr, metaclass=_SystemProtection_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.SystemProtection'
    @winrt_classmethod
    def RequestScreenUnlock(cls: win32more.Windows.Phone.System.ISystemProtectionUnlockStatics) -> Void: ...
    @winrt_classmethod
    def get_ScreenLocked(cls: win32more.Windows.Phone.System.ISystemProtectionStatics) -> Boolean: ...
    _SystemProtection_Meta_.ScreenLocked = property(get_ScreenLocked.__wrapped__, None)
make_head(_module, 'ISystemProtectionStatics')
make_head(_module, 'ISystemProtectionUnlockStatics')
make_head(_module, 'SystemProtection')