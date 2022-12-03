from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Devices.Properties
import win32more.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_DEVPKEY_DeviceInterface_Autoplay_Silent():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('434dd28f-9e75-450a-9a-b9-ff-61-e6-18-ba-d0'), pid=2)
def _define_DEVPKEY_NAME():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac'), pid=10)
def _define_DEVPKEY_Device_DeviceDesc():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=2)
def _define_DEVPKEY_Device_HardwareIds():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=3)
def _define_DEVPKEY_Device_CompatibleIds():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=4)
def _define_DEVPKEY_Device_Service():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=6)
def _define_DEVPKEY_Device_Class():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=9)
def _define_DEVPKEY_Device_ClassGuid():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=10)
def _define_DEVPKEY_Device_Driver():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=11)
def _define_DEVPKEY_Device_ConfigFlags():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=12)
def _define_DEVPKEY_Device_Manufacturer():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=13)
def _define_DEVPKEY_Device_FriendlyName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=14)
def _define_DEVPKEY_Device_LocationInfo():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=15)
def _define_DEVPKEY_Device_PDOName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=16)
def _define_DEVPKEY_Device_Capabilities():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=17)
def _define_DEVPKEY_Device_UINumber():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=18)
def _define_DEVPKEY_Device_UpperFilters():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=19)
def _define_DEVPKEY_Device_LowerFilters():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=20)
def _define_DEVPKEY_Device_BusTypeGuid():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=21)
def _define_DEVPKEY_Device_LegacyBusType():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=22)
def _define_DEVPKEY_Device_BusNumber():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=23)
def _define_DEVPKEY_Device_EnumeratorName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=24)
def _define_DEVPKEY_Device_Security():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=25)
def _define_DEVPKEY_Device_SecuritySDS():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=26)
def _define_DEVPKEY_Device_DevType():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=27)
def _define_DEVPKEY_Device_Exclusive():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=28)
def _define_DEVPKEY_Device_Characteristics():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=29)
def _define_DEVPKEY_Device_Address():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=30)
def _define_DEVPKEY_Device_UINumberDescFormat():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=31)
def _define_DEVPKEY_Device_PowerData():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=32)
def _define_DEVPKEY_Device_RemovalPolicy():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=33)
def _define_DEVPKEY_Device_RemovalPolicyDefault():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=34)
def _define_DEVPKEY_Device_RemovalPolicyOverride():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=35)
def _define_DEVPKEY_Device_InstallState():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=36)
def _define_DEVPKEY_Device_LocationPaths():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=37)
def _define_DEVPKEY_Device_BaseContainerId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a45c254e-df1c-4efd-80-20-67-d1-46-a8-50-e0'), pid=38)
def _define_DEVPKEY_Device_InstanceId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=256)
def _define_DEVPKEY_Device_DevNodeStatus():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=2)
def _define_DEVPKEY_Device_ProblemCode():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=3)
def _define_DEVPKEY_Device_EjectionRelations():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=4)
def _define_DEVPKEY_Device_RemovalRelations():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=5)
def _define_DEVPKEY_Device_PowerRelations():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=6)
def _define_DEVPKEY_Device_BusRelations():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=7)
def _define_DEVPKEY_Device_Parent():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=8)
def _define_DEVPKEY_Device_Children():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=9)
def _define_DEVPKEY_Device_Siblings():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=10)
def _define_DEVPKEY_Device_TransportRelations():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=11)
def _define_DEVPKEY_Device_ProblemStatus():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4340a6c5-93fa-4706-97-2c-7b-64-80-08-a5-a7'), pid=12)
def _define_DEVPKEY_Device_Reported():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=2)
def _define_DEVPKEY_Device_Legacy():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80497100-8c73-48b9-aa-d9-ce-38-7e-19-c5-6e'), pid=3)
def _define_DEVPKEY_Device_ContainerId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=2)
def _define_DEVPKEY_Device_InLocalMachineContainer():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('8c7ed206-3f8a-4827-b3-ab-ae-9e-1f-ae-fc-6c'), pid=4)
def _define_DEVPKEY_Device_Model():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=39)
def _define_DEVPKEY_Device_ModelId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=2)
def _define_DEVPKEY_Device_FriendlyNameAttributes():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=3)
def _define_DEVPKEY_Device_ManufacturerAttributes():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=4)
def _define_DEVPKEY_Device_PresenceNotForDevice():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=5)
def _define_DEVPKEY_Device_SignalStrength():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=6)
def _define_DEVPKEY_Device_IsAssociateableByUserAction():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=7)
def _define_DEVPKEY_Device_ShowInUninstallUI():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('80d81ea6-7473-4b0c-82-16-ef-c1-1a-2c-4c-8b'), pid=8)
def _define_DEVPKEY_Device_Numa_Proximity_Domain():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=1)
def _define_DEVPKEY_Device_DHP_Rebalance_Policy():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=2)
def _define_DEVPKEY_Device_Numa_Node():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=3)
def _define_DEVPKEY_Device_BusReportedDeviceDesc():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=4)
def _define_DEVPKEY_Device_IsPresent():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=5)
def _define_DEVPKEY_Device_HasProblem():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=6)
def _define_DEVPKEY_Device_ConfigurationId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=7)
def _define_DEVPKEY_Device_ReportedDeviceIdsHash():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=8)
def _define_DEVPKEY_Device_PhysicalDeviceLocation():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=9)
def _define_DEVPKEY_Device_BiosDeviceName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=10)
def _define_DEVPKEY_Device_DriverProblemDesc():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=11)
def _define_DEVPKEY_Device_DebuggerSafe():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=12)
def _define_DEVPKEY_Device_PostInstallInProgress():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=13)
def _define_DEVPKEY_Device_Stack():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=14)
def _define_DEVPKEY_Device_ExtendedConfigurationIds():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=15)
def _define_DEVPKEY_Device_IsRebootRequired():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=16)
def _define_DEVPKEY_Device_FirmwareDate():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=17)
def _define_DEVPKEY_Device_FirmwareVersion():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=18)
def _define_DEVPKEY_Device_FirmwareRevision():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=19)
def _define_DEVPKEY_Device_DependencyProviders():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=20)
def _define_DEVPKEY_Device_DependencyDependents():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=21)
def _define_DEVPKEY_Device_SoftRestartSupported():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=22)
def _define_DEVPKEY_Device_ExtendedAddress():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=23)
def _define_DEVPKEY_Device_AssignedToGuest():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=24)
def _define_DEVPKEY_Device_CreatorProcessId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('540b947e-8b40-45bc-a8-a2-6a-0b-89-4c-bd-a2'), pid=25)
def _define_DEVPKEY_Device_SessionId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=6)
def _define_DEVPKEY_Device_InstallDate():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=100)
def _define_DEVPKEY_Device_FirstInstallDate():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=101)
def _define_DEVPKEY_Device_LastArrivalDate():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=102)
def _define_DEVPKEY_Device_LastRemovalDate():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=103)
def _define_DEVPKEY_Device_DriverDate():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=2)
def _define_DEVPKEY_Device_DriverVersion():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=3)
def _define_DEVPKEY_Device_DriverDesc():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=4)
def _define_DEVPKEY_Device_DriverInfPath():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=5)
def _define_DEVPKEY_Device_DriverInfSection():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=6)
def _define_DEVPKEY_Device_DriverInfSectionExt():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=7)
def _define_DEVPKEY_Device_MatchingDeviceId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=8)
def _define_DEVPKEY_Device_DriverProvider():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=9)
def _define_DEVPKEY_Device_DriverPropPageProvider():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=10)
def _define_DEVPKEY_Device_DriverCoInstallers():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=11)
def _define_DEVPKEY_Device_ResourcePickerTags():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=12)
def _define_DEVPKEY_Device_ResourcePickerExceptions():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=13)
def _define_DEVPKEY_Device_DriverRank():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=14)
def _define_DEVPKEY_Device_DriverLogoLevel():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=15)
def _define_DEVPKEY_Device_NoConnectSound():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=17)
def _define_DEVPKEY_Device_GenericDriverInstalled():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=18)
def _define_DEVPKEY_Device_AdditionalSoftwareRequested():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('a8b865dd-2e3d-4094-ad-97-e5-93-a7-0c-75-d6'), pid=19)
def _define_DEVPKEY_Device_SafeRemovalRequired():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=2)
def _define_DEVPKEY_Device_SafeRemovalRequiredOverride():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('afd97640-86a3-4210-b6-7c-28-9c-41-aa-be-55'), pid=3)
def _define_DEVPKEY_DrvPkg_Model():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=2)
def _define_DEVPKEY_DrvPkg_VendorWebSite():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=3)
def _define_DEVPKEY_DrvPkg_DetailedDescription():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=4)
def _define_DEVPKEY_DrvPkg_DocumentationLink():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=5)
def _define_DEVPKEY_DrvPkg_Icon():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=6)
def _define_DEVPKEY_DrvPkg_BrandingIcon():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('cf73bb51-3abf-44a2-85-e0-9a-3d-c7-a1-21-32'), pid=7)
def _define_DEVPKEY_DeviceClass_UpperFilters():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=19)
def _define_DEVPKEY_DeviceClass_LowerFilters():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=20)
def _define_DEVPKEY_DeviceClass_Security():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=25)
def _define_DEVPKEY_DeviceClass_SecuritySDS():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=26)
def _define_DEVPKEY_DeviceClass_DevType():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=27)
def _define_DEVPKEY_DeviceClass_Exclusive():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=28)
def _define_DEVPKEY_DeviceClass_Characteristics():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('4321918b-f69e-470d-a5-de-4d-88-c7-5a-d2-4b'), pid=29)
def _define_DEVPKEY_DeviceClass_Name():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=2)
def _define_DEVPKEY_DeviceClass_ClassName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=3)
def _define_DEVPKEY_DeviceClass_Icon():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=4)
def _define_DEVPKEY_DeviceClass_ClassInstaller():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=5)
def _define_DEVPKEY_DeviceClass_PropPageProvider():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=6)
def _define_DEVPKEY_DeviceClass_NoInstallClass():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=7)
def _define_DEVPKEY_DeviceClass_NoDisplayClass():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=8)
def _define_DEVPKEY_DeviceClass_SilentInstall():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=9)
def _define_DEVPKEY_DeviceClass_NoUseClass():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=10)
def _define_DEVPKEY_DeviceClass_DefaultService():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=11)
def _define_DEVPKEY_DeviceClass_IconPath():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('259abffc-50a7-47ce-af-08-68-c9-a7-d7-33-66'), pid=12)
def _define_DEVPKEY_DeviceClass_DHPRebalanceOptOut():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('d14d3ef3-66cf-4ba2-9d-38-0d-db-37-ab-47-01'), pid=2)
def _define_DEVPKEY_DeviceClass_ClassCoInstallers():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('713d1703-a2e2-49f5-92-14-56-47-2e-f3-da-5c'), pid=2)
def _define_DEVPKEY_DeviceInterface_FriendlyName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=2)
def _define_DEVPKEY_DeviceInterface_Enabled():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=3)
def _define_DEVPKEY_DeviceInterface_ClassGuid():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=4)
def _define_DEVPKEY_DeviceInterface_ReferenceString():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=5)
def _define_DEVPKEY_DeviceInterface_Restricted():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=6)
def _define_DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=8)
def _define_DEVPKEY_DeviceInterface_SchematicName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('026e516e-b814-414b-83-cd-85-6d-6f-ef-48-22'), pid=9)
def _define_DEVPKEY_DeviceInterfaceClass_DefaultInterface():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('14c83a99-0b3f-44b7-be-4c-a1-78-d3-99-05-64'), pid=2)
def _define_DEVPKEY_DeviceInterfaceClass_Name():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('14c83a99-0b3f-44b7-be-4c-a1-78-d3-99-05-64'), pid=3)
def _define_DEVPKEY_DeviceContainer_Address():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=51)
def _define_DEVPKEY_DeviceContainer_DiscoveryMethod():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=52)
def _define_DEVPKEY_DeviceContainer_IsEncrypted():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=53)
def _define_DEVPKEY_DeviceContainer_IsAuthenticated():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=54)
def _define_DEVPKEY_DeviceContainer_IsConnected():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=55)
def _define_DEVPKEY_DeviceContainer_IsPaired():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=56)
def _define_DEVPKEY_DeviceContainer_Icon():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=57)
def _define_DEVPKEY_DeviceContainer_Version():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=65)
def _define_DEVPKEY_DeviceContainer_Last_Seen():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=66)
def _define_DEVPKEY_DeviceContainer_Last_Connected():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=67)
def _define_DEVPKEY_DeviceContainer_IsShowInDisconnectedState():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=68)
def _define_DEVPKEY_DeviceContainer_IsLocalMachine():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=70)
def _define_DEVPKEY_DeviceContainer_MetadataPath():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=71)
def _define_DEVPKEY_DeviceContainer_IsMetadataSearchInProgress():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=72)
def _define_DEVPKEY_DeviceContainer_MetadataChecksum():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=73)
def _define_DEVPKEY_DeviceContainer_IsNotInterestingForDisplay():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=74)
def _define_DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=76)
def _define_DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=77)
def _define_DEVPKEY_DeviceContainer_BaselineExperienceId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=78)
def _define_DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=79)
def _define_DEVPKEY_DeviceContainer_AssociationArray():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=80)
def _define_DEVPKEY_DeviceContainer_DeviceDescription1():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=81)
def _define_DEVPKEY_DeviceContainer_DeviceDescription2():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=82)
def _define_DEVPKEY_DeviceContainer_HasProblem():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=83)
def _define_DEVPKEY_DeviceContainer_IsSharedDevice():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=84)
def _define_DEVPKEY_DeviceContainer_IsNetworkDevice():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=85)
def _define_DEVPKEY_DeviceContainer_IsDefaultDevice():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=86)
def _define_DEVPKEY_DeviceContainer_MetadataCabinet():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=87)
def _define_DEVPKEY_DeviceContainer_RequiresPairingElevation():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=88)
def _define_DEVPKEY_DeviceContainer_ExperienceId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=89)
def _define_DEVPKEY_DeviceContainer_Category():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=90)
def _define_DEVPKEY_DeviceContainer_Category_Desc_Singular():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=91)
def _define_DEVPKEY_DeviceContainer_Category_Desc_Plural():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=92)
def _define_DEVPKEY_DeviceContainer_Category_Icon():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=93)
def _define_DEVPKEY_DeviceContainer_CategoryGroup_Desc():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=94)
def _define_DEVPKEY_DeviceContainer_CategoryGroup_Icon():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=95)
def _define_DEVPKEY_DeviceContainer_PrimaryCategory():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=97)
def _define_DEVPKEY_DeviceContainer_UnpairUninstall():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=98)
def _define_DEVPKEY_DeviceContainer_RequiresUninstallElevation():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=99)
def _define_DEVPKEY_DeviceContainer_DeviceFunctionSubRank():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=100)
def _define_DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=101)
def _define_DEVPKEY_DeviceContainer_ConfigFlags():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=105)
def _define_DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=106)
def _define_DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=107)
def _define_DEVPKEY_DeviceContainer_IsRebootRequired():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('78c34fc8-104a-4aca-9e-a4-52-4d-52-99-6e-57'), pid=108)
def _define_DEVPKEY_DeviceContainer_FriendlyName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=12288)
def _define_DEVPKEY_DeviceContainer_Manufacturer():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8192)
def _define_DEVPKEY_DeviceContainer_ModelName():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8194)
def _define_DEVPKEY_DeviceContainer_ModelNumber():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('656a3bb3-ecc0-43fd-84-77-4a-e0-40-4a-96-cd'), pid=8195)
def _define_DEVPKEY_DeviceContainer_InstallInProgress():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('83da6326-97a6-4088-94-53-a1-92-3f-57-3b-29'), pid=9)
def _define_DEVPKEY_DevQuery_ObjectType():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('13673f42-a3d6-49f6-b4-da-ae-46-e0-c5-23-7c'), pid=2)
DEVPROP_TYPEMOD_ARRAY = 4096
DEVPROP_TYPEMOD_LIST = 8192
DEVPROP_TYPE_EMPTY = 0
DEVPROP_TYPE_NULL = 1
DEVPROP_TYPE_SBYTE = 2
DEVPROP_TYPE_BYTE = 3
DEVPROP_TYPE_INT16 = 4
DEVPROP_TYPE_UINT16 = 5
DEVPROP_TYPE_INT32 = 6
DEVPROP_TYPE_UINT32 = 7
DEVPROP_TYPE_INT64 = 8
DEVPROP_TYPE_UINT64 = 9
DEVPROP_TYPE_FLOAT = 10
DEVPROP_TYPE_DOUBLE = 11
DEVPROP_TYPE_DECIMAL = 12
DEVPROP_TYPE_GUID = 13
DEVPROP_TYPE_CURRENCY = 14
DEVPROP_TYPE_DATE = 15
DEVPROP_TYPE_FILETIME = 16
DEVPROP_TYPE_BOOLEAN = 17
DEVPROP_TYPE_STRING = 18
DEVPROP_TYPE_SECURITY_DESCRIPTOR = 19
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING = 20
DEVPROP_TYPE_DEVPROPKEY = 21
DEVPROP_TYPE_DEVPROPTYPE = 22
DEVPROP_TYPE_ERROR = 23
DEVPROP_TYPE_NTSTATUS = 24
DEVPROP_TYPE_STRING_INDIRECT = 25
MAX_DEVPROP_TYPE = 25
MAX_DEVPROP_TYPEMOD = 8192
DEVPROP_MASK_TYPE = 4095
DEVPROP_MASK_TYPEMOD = 61440
DEVPROPID_FIRST_USABLE = 2
def _define_DEVPROPCOMPKEY_head():
    class DEVPROPCOMPKEY(Structure):
        pass
    return DEVPROPCOMPKEY
def _define_DEVPROPCOMPKEY():
    DEVPROPCOMPKEY = win32more.Devices.Properties.DEVPROPCOMPKEY_head
    DEVPROPCOMPKEY._fields_ = [
        ('Key', win32more.Devices.Properties.DEVPROPKEY),
        ('Store', win32more.Devices.Properties.DEVPROPSTORE),
        ('LocaleName', win32more.Foundation.PWSTR),
    ]
    return DEVPROPCOMPKEY
def _define_DEVPROPERTY_head():
    class DEVPROPERTY(Structure):
        pass
    return DEVPROPERTY
def _define_DEVPROPERTY():
    DEVPROPERTY = win32more.Devices.Properties.DEVPROPERTY_head
    DEVPROPERTY._fields_ = [
        ('CompKey', win32more.Devices.Properties.DEVPROPCOMPKEY),
        ('Type', UInt32),
        ('BufferSize', UInt32),
        ('Buffer', c_void_p),
    ]
    return DEVPROPERTY
def _define_DEVPROPKEY_head():
    class DEVPROPKEY(Structure):
        pass
    return DEVPROPKEY
def _define_DEVPROPKEY():
    DEVPROPKEY = win32more.Devices.Properties.DEVPROPKEY_head
    DEVPROPKEY._fields_ = [
        ('fmtid', Guid),
        ('pid', UInt32),
    ]
    return DEVPROPKEY
DEVPROPSTORE = Int32
DEVPROP_STORE_SYSTEM = 0
DEVPROP_STORE_USER = 1
__all__ = [
    "DEVPKEY_DevQuery_ObjectType",
    "DEVPKEY_DeviceClass_Characteristics",
    "DEVPKEY_DeviceClass_ClassCoInstallers",
    "DEVPKEY_DeviceClass_ClassInstaller",
    "DEVPKEY_DeviceClass_ClassName",
    "DEVPKEY_DeviceClass_DHPRebalanceOptOut",
    "DEVPKEY_DeviceClass_DefaultService",
    "DEVPKEY_DeviceClass_DevType",
    "DEVPKEY_DeviceClass_Exclusive",
    "DEVPKEY_DeviceClass_Icon",
    "DEVPKEY_DeviceClass_IconPath",
    "DEVPKEY_DeviceClass_LowerFilters",
    "DEVPKEY_DeviceClass_Name",
    "DEVPKEY_DeviceClass_NoDisplayClass",
    "DEVPKEY_DeviceClass_NoInstallClass",
    "DEVPKEY_DeviceClass_NoUseClass",
    "DEVPKEY_DeviceClass_PropPageProvider",
    "DEVPKEY_DeviceClass_Security",
    "DEVPKEY_DeviceClass_SecuritySDS",
    "DEVPKEY_DeviceClass_SilentInstall",
    "DEVPKEY_DeviceClass_UpperFilters",
    "DEVPKEY_DeviceContainer_Address",
    "DEVPKEY_DeviceContainer_AlwaysShowDeviceAsConnected",
    "DEVPKEY_DeviceContainer_AssociationArray",
    "DEVPKEY_DeviceContainer_BaselineExperienceId",
    "DEVPKEY_DeviceContainer_Category",
    "DEVPKEY_DeviceContainer_CategoryGroup_Desc",
    "DEVPKEY_DeviceContainer_CategoryGroup_Icon",
    "DEVPKEY_DeviceContainer_Category_Desc_Plural",
    "DEVPKEY_DeviceContainer_Category_Desc_Singular",
    "DEVPKEY_DeviceContainer_Category_Icon",
    "DEVPKEY_DeviceContainer_ConfigFlags",
    "DEVPKEY_DeviceContainer_CustomPrivilegedPackageFamilyNames",
    "DEVPKEY_DeviceContainer_DeviceDescription1",
    "DEVPKEY_DeviceContainer_DeviceDescription2",
    "DEVPKEY_DeviceContainer_DeviceFunctionSubRank",
    "DEVPKEY_DeviceContainer_DiscoveryMethod",
    "DEVPKEY_DeviceContainer_ExperienceId",
    "DEVPKEY_DeviceContainer_FriendlyName",
    "DEVPKEY_DeviceContainer_HasProblem",
    "DEVPKEY_DeviceContainer_Icon",
    "DEVPKEY_DeviceContainer_InstallInProgress",
    "DEVPKEY_DeviceContainer_IsAuthenticated",
    "DEVPKEY_DeviceContainer_IsConnected",
    "DEVPKEY_DeviceContainer_IsDefaultDevice",
    "DEVPKEY_DeviceContainer_IsDeviceUniquelyIdentifiable",
    "DEVPKEY_DeviceContainer_IsEncrypted",
    "DEVPKEY_DeviceContainer_IsLocalMachine",
    "DEVPKEY_DeviceContainer_IsMetadataSearchInProgress",
    "DEVPKEY_DeviceContainer_IsNetworkDevice",
    "DEVPKEY_DeviceContainer_IsNotInterestingForDisplay",
    "DEVPKEY_DeviceContainer_IsPaired",
    "DEVPKEY_DeviceContainer_IsRebootRequired",
    "DEVPKEY_DeviceContainer_IsSharedDevice",
    "DEVPKEY_DeviceContainer_IsShowInDisconnectedState",
    "DEVPKEY_DeviceContainer_Last_Connected",
    "DEVPKEY_DeviceContainer_Last_Seen",
    "DEVPKEY_DeviceContainer_LaunchDeviceStageFromExplorer",
    "DEVPKEY_DeviceContainer_LaunchDeviceStageOnDeviceConnect",
    "DEVPKEY_DeviceContainer_Manufacturer",
    "DEVPKEY_DeviceContainer_MetadataCabinet",
    "DEVPKEY_DeviceContainer_MetadataChecksum",
    "DEVPKEY_DeviceContainer_MetadataPath",
    "DEVPKEY_DeviceContainer_ModelName",
    "DEVPKEY_DeviceContainer_ModelNumber",
    "DEVPKEY_DeviceContainer_PrimaryCategory",
    "DEVPKEY_DeviceContainer_PrivilegedPackageFamilyNames",
    "DEVPKEY_DeviceContainer_RequiresPairingElevation",
    "DEVPKEY_DeviceContainer_RequiresUninstallElevation",
    "DEVPKEY_DeviceContainer_UnpairUninstall",
    "DEVPKEY_DeviceContainer_Version",
    "DEVPKEY_DeviceInterfaceClass_DefaultInterface",
    "DEVPKEY_DeviceInterfaceClass_Name",
    "DEVPKEY_DeviceInterface_Autoplay_Silent",
    "DEVPKEY_DeviceInterface_ClassGuid",
    "DEVPKEY_DeviceInterface_Enabled",
    "DEVPKEY_DeviceInterface_FriendlyName",
    "DEVPKEY_DeviceInterface_ReferenceString",
    "DEVPKEY_DeviceInterface_Restricted",
    "DEVPKEY_DeviceInterface_SchematicName",
    "DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities",
    "DEVPKEY_Device_AdditionalSoftwareRequested",
    "DEVPKEY_Device_Address",
    "DEVPKEY_Device_AssignedToGuest",
    "DEVPKEY_Device_BaseContainerId",
    "DEVPKEY_Device_BiosDeviceName",
    "DEVPKEY_Device_BusNumber",
    "DEVPKEY_Device_BusRelations",
    "DEVPKEY_Device_BusReportedDeviceDesc",
    "DEVPKEY_Device_BusTypeGuid",
    "DEVPKEY_Device_Capabilities",
    "DEVPKEY_Device_Characteristics",
    "DEVPKEY_Device_Children",
    "DEVPKEY_Device_Class",
    "DEVPKEY_Device_ClassGuid",
    "DEVPKEY_Device_CompatibleIds",
    "DEVPKEY_Device_ConfigFlags",
    "DEVPKEY_Device_ConfigurationId",
    "DEVPKEY_Device_ContainerId",
    "DEVPKEY_Device_CreatorProcessId",
    "DEVPKEY_Device_DHP_Rebalance_Policy",
    "DEVPKEY_Device_DebuggerSafe",
    "DEVPKEY_Device_DependencyDependents",
    "DEVPKEY_Device_DependencyProviders",
    "DEVPKEY_Device_DevNodeStatus",
    "DEVPKEY_Device_DevType",
    "DEVPKEY_Device_DeviceDesc",
    "DEVPKEY_Device_Driver",
    "DEVPKEY_Device_DriverCoInstallers",
    "DEVPKEY_Device_DriverDate",
    "DEVPKEY_Device_DriverDesc",
    "DEVPKEY_Device_DriverInfPath",
    "DEVPKEY_Device_DriverInfSection",
    "DEVPKEY_Device_DriverInfSectionExt",
    "DEVPKEY_Device_DriverLogoLevel",
    "DEVPKEY_Device_DriverProblemDesc",
    "DEVPKEY_Device_DriverPropPageProvider",
    "DEVPKEY_Device_DriverProvider",
    "DEVPKEY_Device_DriverRank",
    "DEVPKEY_Device_DriverVersion",
    "DEVPKEY_Device_EjectionRelations",
    "DEVPKEY_Device_EnumeratorName",
    "DEVPKEY_Device_Exclusive",
    "DEVPKEY_Device_ExtendedAddress",
    "DEVPKEY_Device_ExtendedConfigurationIds",
    "DEVPKEY_Device_FirmwareDate",
    "DEVPKEY_Device_FirmwareRevision",
    "DEVPKEY_Device_FirmwareVersion",
    "DEVPKEY_Device_FirstInstallDate",
    "DEVPKEY_Device_FriendlyName",
    "DEVPKEY_Device_FriendlyNameAttributes",
    "DEVPKEY_Device_GenericDriverInstalled",
    "DEVPKEY_Device_HardwareIds",
    "DEVPKEY_Device_HasProblem",
    "DEVPKEY_Device_InLocalMachineContainer",
    "DEVPKEY_Device_InstallDate",
    "DEVPKEY_Device_InstallState",
    "DEVPKEY_Device_InstanceId",
    "DEVPKEY_Device_IsAssociateableByUserAction",
    "DEVPKEY_Device_IsPresent",
    "DEVPKEY_Device_IsRebootRequired",
    "DEVPKEY_Device_LastArrivalDate",
    "DEVPKEY_Device_LastRemovalDate",
    "DEVPKEY_Device_Legacy",
    "DEVPKEY_Device_LegacyBusType",
    "DEVPKEY_Device_LocationInfo",
    "DEVPKEY_Device_LocationPaths",
    "DEVPKEY_Device_LowerFilters",
    "DEVPKEY_Device_Manufacturer",
    "DEVPKEY_Device_ManufacturerAttributes",
    "DEVPKEY_Device_MatchingDeviceId",
    "DEVPKEY_Device_Model",
    "DEVPKEY_Device_ModelId",
    "DEVPKEY_Device_NoConnectSound",
    "DEVPKEY_Device_Numa_Node",
    "DEVPKEY_Device_Numa_Proximity_Domain",
    "DEVPKEY_Device_PDOName",
    "DEVPKEY_Device_Parent",
    "DEVPKEY_Device_PhysicalDeviceLocation",
    "DEVPKEY_Device_PostInstallInProgress",
    "DEVPKEY_Device_PowerData",
    "DEVPKEY_Device_PowerRelations",
    "DEVPKEY_Device_PresenceNotForDevice",
    "DEVPKEY_Device_ProblemCode",
    "DEVPKEY_Device_ProblemStatus",
    "DEVPKEY_Device_RemovalPolicy",
    "DEVPKEY_Device_RemovalPolicyDefault",
    "DEVPKEY_Device_RemovalPolicyOverride",
    "DEVPKEY_Device_RemovalRelations",
    "DEVPKEY_Device_Reported",
    "DEVPKEY_Device_ReportedDeviceIdsHash",
    "DEVPKEY_Device_ResourcePickerExceptions",
    "DEVPKEY_Device_ResourcePickerTags",
    "DEVPKEY_Device_SafeRemovalRequired",
    "DEVPKEY_Device_SafeRemovalRequiredOverride",
    "DEVPKEY_Device_Security",
    "DEVPKEY_Device_SecuritySDS",
    "DEVPKEY_Device_Service",
    "DEVPKEY_Device_SessionId",
    "DEVPKEY_Device_ShowInUninstallUI",
    "DEVPKEY_Device_Siblings",
    "DEVPKEY_Device_SignalStrength",
    "DEVPKEY_Device_SoftRestartSupported",
    "DEVPKEY_Device_Stack",
    "DEVPKEY_Device_TransportRelations",
    "DEVPKEY_Device_UINumber",
    "DEVPKEY_Device_UINumberDescFormat",
    "DEVPKEY_Device_UpperFilters",
    "DEVPKEY_DrvPkg_BrandingIcon",
    "DEVPKEY_DrvPkg_DetailedDescription",
    "DEVPKEY_DrvPkg_DocumentationLink",
    "DEVPKEY_DrvPkg_Icon",
    "DEVPKEY_DrvPkg_Model",
    "DEVPKEY_DrvPkg_VendorWebSite",
    "DEVPKEY_NAME",
    "DEVPROPCOMPKEY",
    "DEVPROPERTY",
    "DEVPROPID_FIRST_USABLE",
    "DEVPROPKEY",
    "DEVPROPSTORE",
    "DEVPROP_MASK_TYPE",
    "DEVPROP_MASK_TYPEMOD",
    "DEVPROP_STORE_SYSTEM",
    "DEVPROP_STORE_USER",
    "DEVPROP_TYPEMOD_ARRAY",
    "DEVPROP_TYPEMOD_LIST",
    "DEVPROP_TYPE_BOOLEAN",
    "DEVPROP_TYPE_BYTE",
    "DEVPROP_TYPE_CURRENCY",
    "DEVPROP_TYPE_DATE",
    "DEVPROP_TYPE_DECIMAL",
    "DEVPROP_TYPE_DEVPROPKEY",
    "DEVPROP_TYPE_DEVPROPTYPE",
    "DEVPROP_TYPE_DOUBLE",
    "DEVPROP_TYPE_EMPTY",
    "DEVPROP_TYPE_ERROR",
    "DEVPROP_TYPE_FILETIME",
    "DEVPROP_TYPE_FLOAT",
    "DEVPROP_TYPE_GUID",
    "DEVPROP_TYPE_INT16",
    "DEVPROP_TYPE_INT32",
    "DEVPROP_TYPE_INT64",
    "DEVPROP_TYPE_NTSTATUS",
    "DEVPROP_TYPE_NULL",
    "DEVPROP_TYPE_SBYTE",
    "DEVPROP_TYPE_SECURITY_DESCRIPTOR",
    "DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING",
    "DEVPROP_TYPE_STRING",
    "DEVPROP_TYPE_STRING_INDIRECT",
    "DEVPROP_TYPE_UINT16",
    "DEVPROP_TYPE_UINT32",
    "DEVPROP_TYPE_UINT64",
    "MAX_DEVPROP_TYPE",
    "MAX_DEVPROP_TYPEMOD",
]