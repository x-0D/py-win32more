from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices
BUS1394_VIRTUAL_DEVICE_LIST_KEY: String = 'Virtual Device List'
BUS1394_LOCAL_HOST_INSTANCE_KEY: String = 'LOCAL HOST EUI64'
IOCTL_IEEE1394_API_REQUEST: UInt32 = 2229248
IEEE1394_API_ADD_VIRTUAL_DEVICE: UInt32 = 1
IEEE1394_API_REMOVE_VIRTUAL_DEVICE: UInt32 = 2
IEEE1394_API_DEVICE_ACCESS_TRANSFER: UInt32 = 3
IEEE1394_API_SET_LOCAL_NODE_PROPERTIES: UInt32 = 4
IEEE1394_REQUEST_FLAG_UNICODE: UInt32 = 1
IEEE1394_REQUEST_FLAG_PERSISTENT: UInt32 = 2
IEEE1394_REQUEST_FLAG_USE_LOCAL_HOST_EUI: UInt32 = 4
IEEE1394API_NOTIFICATION_DEVICE_ACCESS: UInt32 = 1
IEEE1394API_NOTIFICATION_BUS_RESET: UInt32 = 2
IEEE1394API_DEVICE_OWNERSHIP_LOCAL_NODE: UInt32 = 1
IEEE1394API_RESOURCE_OWNERSHIP_LOCAL_NODE: UInt32 = 2
IEEE1394API_DEVICE_OWNERSHIP_REMOTE_NODE: UInt32 = 4
IEEE1394API_RESOURCE_OWNERSHIP_REMOTE_NODE: UInt32 = 8
IEEE1394API_ACCESS_SHARED_READ: UInt32 = 16
IEEE1394API_ACCESS_SHARED_WRITE: UInt32 = 32
IEEE1394API_ACCESS_EXCLUSIVE: UInt32 = 64
IEEE1394API_REMOTE_ACCESS_TRANSFER_REQUEST: UInt32 = 1
IEEE1394API_BUS_RESET_LOCAL_NODE_IS_ROOT: UInt32 = 1
IEEE1394API_BUS_RESET_LOCAL_NODE_IS_IRM: UInt32 = 2
IEEE1394API_BUS_RESET_LOCAL_NODE_INITIATED: UInt32 = 4
class IEEE1394_API_REQUEST(Structure):
    RequestNumber: UInt32
    Flags: UInt32
    u: _u_e__Union
    class _u_e__Union(Union):
        AddVirtualDevice: win32more.Windows.Win32.Devices.IEEE1394_VDEV_PNP_REQUEST
        RemoveVirtualDevice: win32more.Windows.Win32.Devices.IEEE1394_VDEV_PNP_REQUEST
class IEEE1394_VDEV_PNP_REQUEST(Structure):
    fulFlags: UInt32
    Reserved: UInt32
    InstanceId: UInt64
    DeviceId: Byte


make_ready(__name__)