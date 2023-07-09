from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.ApplicationVerifier
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AVRF_BACKTRACE_INFORMATION(EasyCastStructure):
    Depth: UInt32
    Index: UInt32
    ReturnAddresses: UInt64 * 32
@winfunctype_pointer
def AVRF_HANDLEOPERATION_ENUMERATE_CALLBACK(HandleOperation: POINTER(win32more.Windows.Win32.System.ApplicationVerifier.AVRF_HANDLE_OPERATION_head), EnumerationContext: VoidPtr, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
class AVRF_HANDLE_OPERATION(EasyCastStructure):
    Handle: UInt64
    ProcessId: UInt32
    ThreadId: UInt32
    OperationType: UInt32
    Spare0: UInt32
    BackTraceInformation: win32more.Windows.Win32.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION
@winfunctype_pointer
def AVRF_HEAPALLOCATION_ENUMERATE_CALLBACK(HeapAllocation: POINTER(win32more.Windows.Win32.System.ApplicationVerifier.AVRF_HEAP_ALLOCATION_head), EnumerationContext: VoidPtr, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
class AVRF_HEAP_ALLOCATION(EasyCastStructure):
    HeapHandle: UInt64
    UserAllocation: UInt64
    UserAllocationSize: UInt64
    Allocation: UInt64
    AllocationSize: UInt64
    UserAllocationState: UInt32
    HeapState: UInt32
    HeapContext: UInt64
    BackTraceInformation: POINTER(win32more.Windows.Win32.System.ApplicationVerifier.AVRF_BACKTRACE_INFORMATION_head)
@winfunctype_pointer
def AVRF_RESOURCE_ENUMERATE_CALLBACK(ResourceDescription: VoidPtr, EnumerationContext: VoidPtr, EnumerationLevel: POINTER(UInt32)) -> UInt32: ...
AVRF_MAX_TRACES: UInt32 = 32
@winfunctype('verifier.dll')
def VerifierEnumerateResource(Process: win32more.Windows.Win32.Foundation.HANDLE, Flags: win32more.Windows.Win32.System.ApplicationVerifier.VERIFIER_ENUM_RESOURCE_FLAGS, ResourceType: UInt32, ResourceCallback: win32more.Windows.Win32.System.ApplicationVerifier.AVRF_RESOURCE_ENUMERATE_CALLBACK, EnumerationContext: VoidPtr) -> UInt32: ...
VERIFIER_ENUM_RESOURCE_FLAGS = UInt32
AVRF_ENUM_RESOURCES_FLAGS_DONT_RESOLVE_TRACES: VERIFIER_ENUM_RESOURCE_FLAGS = 2
AVRF_ENUM_RESOURCES_FLAGS_SUSPEND: VERIFIER_ENUM_RESOURCE_FLAGS = 1
eAvrfResourceTypes = Int32
eAvrfResourceTypes_AvrfResourceHeapAllocation: eAvrfResourceTypes = 0
eAvrfResourceTypes_AvrfResourceHandleTrace: eAvrfResourceTypes = 1
eAvrfResourceTypes_AvrfResourceMax: eAvrfResourceTypes = 2
eHANDLE_TRACE_OPERATIONS = Int32
eHANDLE_TRACE_OPERATIONS_OperationDbUnused: eHANDLE_TRACE_OPERATIONS = 0
eHANDLE_TRACE_OPERATIONS_OperationDbOPEN: eHANDLE_TRACE_OPERATIONS = 1
eHANDLE_TRACE_OPERATIONS_OperationDbCLOSE: eHANDLE_TRACE_OPERATIONS = 2
eHANDLE_TRACE_OPERATIONS_OperationDbBADREF: eHANDLE_TRACE_OPERATIONS = 3
eHeapAllocationState = Int32
eHeapAllocationState_HeapFullPageHeap: eHeapAllocationState = 1073741824
eHeapAllocationState_HeapMetadata: eHeapAllocationState = -2147483648
eHeapAllocationState_HeapStateMask: eHeapAllocationState = -65536
eHeapEnumerationLevel = Int32
eHeapEnumerationLevel_HeapEnumerationEverything: eHeapEnumerationLevel = 0
eHeapEnumerationLevel_HeapEnumerationStop: eHeapEnumerationLevel = -1
eUserAllocationState = Int32
eUserAllocationState_AllocationStateUnknown: eUserAllocationState = 0
eUserAllocationState_AllocationStateBusy: eUserAllocationState = 1
eUserAllocationState_AllocationStateFree: eUserAllocationState = 2
make_head(_module, 'AVRF_BACKTRACE_INFORMATION')
make_head(_module, 'AVRF_HANDLEOPERATION_ENUMERATE_CALLBACK')
make_head(_module, 'AVRF_HANDLE_OPERATION')
make_head(_module, 'AVRF_HEAPALLOCATION_ENUMERATE_CALLBACK')
make_head(_module, 'AVRF_HEAP_ALLOCATION')
make_head(_module, 'AVRF_RESOURCE_ENUMERATE_CALLBACK')