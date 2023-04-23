from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.Performance.HardwareCounterProfiling
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('KERNEL32.dll')
def EnableThreadProfiling(ThreadHandle: Windows.Win32.Foundation.HANDLE, Flags: UInt32, HardwareCounters: UInt64, PerformanceDataHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DisableThreadProfiling(PerformanceDataHandle: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def QueryThreadProfiling(ThreadHandle: Windows.Win32.Foundation.HANDLE, Enabled: POINTER(Windows.Win32.Foundation.BOOLEAN)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ReadThreadProfilingData(PerformanceDataHandle: Windows.Win32.Foundation.HANDLE, Flags: UInt32, PerformanceData: POINTER(Windows.Win32.System.Performance.HardwareCounterProfiling.PERFORMANCE_DATA_head)) -> UInt32: ...
class HARDWARE_COUNTER_DATA(EasyCastStructure):
    Type: Windows.Win32.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_TYPE
    Reserved: UInt32
    Value: UInt64
HARDWARE_COUNTER_TYPE = Int32
HARDWARE_COUNTER_TYPE_PMCCounter: HARDWARE_COUNTER_TYPE = 0
HARDWARE_COUNTER_TYPE_MaxHardwareCounterType: HARDWARE_COUNTER_TYPE = 1
class PERFORMANCE_DATA(EasyCastStructure):
    Size: UInt16
    Version: Byte
    HwCountersCount: Byte
    ContextSwitchCount: UInt32
    WaitReasonBitMap: UInt64
    CycleTime: UInt64
    RetryCount: UInt32
    Reserved: UInt32
    HwCounters: Windows.Win32.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_DATA * 16
make_head(_module, 'HARDWARE_COUNTER_DATA')
make_head(_module, 'PERFORMANCE_DATA')