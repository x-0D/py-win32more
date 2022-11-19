from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Graphics.Hlsl

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
D3DCOMPILER_DLL = 'd3dcompiler_47.dll'
D3DCOMPILE_OPTIMIZATION_LEVEL2 = 49152
D3D_COMPILE_STANDARD_FILE_INCLUDE = 1
__all__ = [
    "D3DCOMPILER_DLL",
    "D3DCOMPILE_OPTIMIZATION_LEVEL2",
    "D3D_COMPILE_STANDARD_FILE_INCLUDE",
]
