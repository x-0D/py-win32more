from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Media.Audio
import Windows.Win32.Media.DeviceManager
import Windows.Win32.Media.MediaFoundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Ole
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
IOCTL_MTP_CUSTOM_COMMAND: UInt32 = 827348045
MTP_NEXTPHASE_READ_DATA: UInt32 = 1
MTP_NEXTPHASE_WRITE_DATA: UInt32 = 2
MTP_NEXTPHASE_NO_DATA: UInt32 = 3
RSA_KEY_LEN: UInt32 = 64
SAC_SESSION_KEYLEN: UInt32 = 8
SAC_PROTOCOL_WMDM: UInt32 = 1
SAC_PROTOCOL_V1: UInt32 = 2
SAC_CERT_X509: UInt32 = 1
SAC_CERT_V1: UInt32 = 2
WMDM_DEVICE_PROTOCOL_MTP: Guid = Guid('979e54e5-0afc-4604-8d-93-dc-79-8a-4b-cf-45')
WMDM_DEVICE_PROTOCOL_RAPI: Guid = Guid('2a11ed91-8c8f-41e4-82-d1-83-86-e0-03-56-1c')
WMDM_DEVICE_PROTOCOL_MSC: Guid = Guid('a4d2c26c-a881-44bb-bd-5d-1f-70-3c-71-f7-a9')
WMDM_SERVICE_PROVIDER_VENDOR_MICROSOFT: Guid = Guid('7de8686d-78ee-43ea-a4-96-c6-25-ac-91-cc-5d')
WMDMID_LENGTH: UInt32 = 128
WMDM_MAC_LENGTH: UInt32 = 8
WMDM_S_NOT_ALL_PROPERTIES_APPLIED: Int32 = 282625
WMDM_S_NOT_ALL_PROPERTIES_RETRIEVED: Int32 = 282626
WMDM_E_BUSY: Int32 = -2147201024
WMDM_E_INTERFACEDEAD: Int32 = -2147201023
WMDM_E_INVALIDTYPE: Int32 = -2147201022
WMDM_E_PROCESSFAILED: Int32 = -2147201021
WMDM_E_NOTSUPPORTED: Int32 = -2147201020
WMDM_E_NOTCERTIFIED: Int32 = -2147201019
WMDM_E_NORIGHTS: Int32 = -2147201018
WMDM_E_CALL_OUT_OF_SEQUENCE: Int32 = -2147201017
WMDM_E_BUFFERTOOSMALL: Int32 = -2147201016
WMDM_E_MOREDATA: Int32 = -2147201015
WMDM_E_MAC_CHECK_FAILED: Int32 = -2147201014
WMDM_E_USER_CANCELLED: Int32 = -2147201013
WMDM_E_SDMI_TRIGGER: Int32 = -2147201012
WMDM_E_SDMI_NOMORECOPIES: Int32 = -2147201011
WMDM_E_REVOKED: Int32 = -2147201010
WMDM_E_LICENSE_NOTEXIST: Int32 = -2147201009
WMDM_E_INCORRECT_APPSEC: Int32 = -2147201008
WMDM_E_INCORRECT_RIGHTS: Int32 = -2147201007
WMDM_E_LICENSE_EXPIRED: Int32 = -2147201006
WMDM_E_CANTOPEN_PMSN_SERVICE_PIPE: Int32 = -2147201005
WMDM_E_TOO_MANY_SESSIONS: Int32 = -2147201005
WMDM_WMDM_REVOKED: UInt32 = 1
WMDM_APP_REVOKED: UInt32 = 2
WMDM_SP_REVOKED: UInt32 = 4
WMDM_SCP_REVOKED: UInt32 = 8
WMDM_GET_FORMAT_SUPPORT_AUDIO: UInt32 = 1
WMDM_GET_FORMAT_SUPPORT_VIDEO: UInt32 = 2
WMDM_GET_FORMAT_SUPPORT_FILE: UInt32 = 4
WMDM_RIGHTS_PLAYBACKCOUNT: UInt32 = 1
WMDM_RIGHTS_EXPIRATIONDATE: UInt32 = 2
WMDM_RIGHTS_GROUPID: UInt32 = 4
WMDM_RIGHTS_FREESERIALIDS: UInt32 = 8
WMDM_RIGHTS_NAMEDSERIALIDS: UInt32 = 16
WMDM_DEVICE_TYPE_PLAYBACK: UInt32 = 1
WMDM_DEVICE_TYPE_RECORD: UInt32 = 2
WMDM_DEVICE_TYPE_DECODE: UInt32 = 4
WMDM_DEVICE_TYPE_ENCODE: UInt32 = 8
WMDM_DEVICE_TYPE_STORAGE: UInt32 = 16
WMDM_DEVICE_TYPE_VIRTUAL: UInt32 = 32
WMDM_DEVICE_TYPE_SDMI: UInt32 = 64
WMDM_DEVICE_TYPE_NONSDMI: UInt32 = 128
WMDM_DEVICE_TYPE_NONREENTRANT: UInt32 = 256
WMDM_DEVICE_TYPE_FILELISTRESYNC: UInt32 = 512
WMDM_DEVICE_TYPE_VIEW_PREF_METADATAVIEW: UInt32 = 1024
WMDM_POWER_CAP_BATTERY: UInt32 = 1
WMDM_POWER_CAP_EXTERNAL: UInt32 = 2
WMDM_POWER_IS_BATTERY: UInt32 = 4
WMDM_POWER_IS_EXTERNAL: UInt32 = 8
WMDM_POWER_PERCENT_AVAILABLE: UInt32 = 16
WMDM_STATUS_READY: UInt32 = 1
WMDM_STATUS_BUSY: UInt32 = 2
WMDM_STATUS_DEVICE_NOTPRESENT: UInt32 = 4
WMDM_STATUS_DEVICECONTROL_PLAYING: UInt32 = 8
WMDM_STATUS_DEVICECONTROL_RECORDING: UInt32 = 16
WMDM_STATUS_DEVICECONTROL_PAUSED: UInt32 = 32
WMDM_STATUS_DEVICECONTROL_REMOTE: UInt32 = 64
WMDM_STATUS_DEVICECONTROL_STREAM: UInt32 = 128
WMDM_STATUS_STORAGE_NOTPRESENT: UInt32 = 256
WMDM_STATUS_STORAGE_INITIALIZING: UInt32 = 512
WMDM_STATUS_STORAGE_BROKEN: UInt32 = 1024
WMDM_STATUS_STORAGE_NOTSUPPORTED: UInt32 = 2048
WMDM_STATUS_STORAGE_UNFORMATTED: UInt32 = 4096
WMDM_STATUS_STORAGECONTROL_INSERTING: UInt32 = 8192
WMDM_STATUS_STORAGECONTROL_DELETING: UInt32 = 16384
WMDM_STATUS_STORAGECONTROL_APPENDING: UInt32 = 32768
WMDM_STATUS_STORAGECONTROL_MOVING: UInt32 = 65536
WMDM_STATUS_STORAGECONTROL_READING: UInt32 = 131072
WMDM_DEVICECAP_CANPLAY: UInt32 = 1
WMDM_DEVICECAP_CANSTREAMPLAY: UInt32 = 2
WMDM_DEVICECAP_CANRECORD: UInt32 = 4
WMDM_DEVICECAP_CANSTREAMRECORD: UInt32 = 8
WMDM_DEVICECAP_CANPAUSE: UInt32 = 16
WMDM_DEVICECAP_CANRESUME: UInt32 = 32
WMDM_DEVICECAP_CANSTOP: UInt32 = 64
WMDM_DEVICECAP_CANSEEK: UInt32 = 128
WMDM_DEVICECAP_HASSECURECLOCK: UInt32 = 256
WMDM_SEEK_REMOTECONTROL: UInt32 = 1
WMDM_SEEK_STREAMINGAUDIO: UInt32 = 2
WMDM_STORAGE_ATTR_FILESYSTEM: UInt32 = 1
WMDM_STORAGE_ATTR_REMOVABLE: UInt32 = 2
WMDM_STORAGE_ATTR_NONREMOVABLE: UInt32 = 4
WMDM_FILE_ATTR_FOLDER: UInt32 = 8
WMDM_FILE_ATTR_LINK: UInt32 = 16
WMDM_FILE_ATTR_FILE: UInt32 = 32
WMDM_FILE_ATTR_VIDEO: UInt32 = 64
WMDM_STORAGE_ATTR_CANEDITMETADATA: UInt32 = 128
WMDM_STORAGE_ATTR_FOLDERS: UInt32 = 256
WMDM_FILE_ATTR_AUDIO: UInt32 = 4096
WMDM_FILE_ATTR_DATA: UInt32 = 8192
WMDM_FILE_ATTR_CANPLAY: UInt32 = 16384
WMDM_FILE_ATTR_CANDELETE: UInt32 = 32768
WMDM_FILE_ATTR_CANMOVE: UInt32 = 65536
WMDM_FILE_ATTR_CANRENAME: UInt32 = 131072
WMDM_FILE_ATTR_CANREAD: UInt32 = 262144
WMDM_FILE_ATTR_MUSIC: UInt32 = 524288
WMDM_FILE_CREATE_OVERWRITE: UInt32 = 1048576
WMDM_FILE_ATTR_AUDIOBOOK: UInt32 = 2097152
WMDM_FILE_ATTR_HIDDEN: UInt32 = 4194304
WMDM_FILE_ATTR_SYSTEM: UInt32 = 8388608
WMDM_FILE_ATTR_READONLY: UInt32 = 16777216
WMDM_STORAGE_ATTR_HAS_FOLDERS: UInt32 = 33554432
WMDM_STORAGE_ATTR_HAS_FILES: UInt32 = 67108864
WMDM_STORAGE_IS_DEFAULT: UInt32 = 134217728
WMDM_STORAGE_CONTAINS_DEFAULT: UInt32 = 268435456
WMDM_STORAGE_ATTR_VIRTUAL: UInt32 = 536870912
WMDM_STORAGECAP_FOLDERSINROOT: UInt32 = 1
WMDM_STORAGECAP_FILESINROOT: UInt32 = 2
WMDM_STORAGECAP_FOLDERSINFOLDERS: UInt32 = 4
WMDM_STORAGECAP_FILESINFOLDERS: UInt32 = 8
WMDM_STORAGECAP_FOLDERLIMITEXISTS: UInt32 = 16
WMDM_STORAGECAP_FILELIMITEXISTS: UInt32 = 32
WMDM_STORAGECAP_NOT_INITIALIZABLE: UInt32 = 64
WMDM_MODE_BLOCK: UInt32 = 1
WMDM_MODE_THREAD: UInt32 = 2
WMDM_CONTENT_FILE: UInt32 = 4
WMDM_CONTENT_FOLDER: UInt32 = 8
WMDM_CONTENT_OPERATIONINTERFACE: UInt32 = 16
WMDM_MODE_QUERY: UInt32 = 32
WMDM_MODE_PROGRESS: UInt32 = 64
WMDM_MODE_TRANSFER_PROTECTED: UInt32 = 128
WMDM_MODE_TRANSFER_UNPROTECTED: UInt32 = 256
WMDM_STORAGECONTROL_INSERTBEFORE: UInt32 = 512
WMDM_STORAGECONTROL_INSERTAFTER: UInt32 = 1024
WMDM_STORAGECONTROL_INSERTINTO: UInt32 = 2048
WMDM_MODE_RECURSIVE: UInt32 = 4096
WMDM_RIGHTS_PLAY_ON_PC: UInt32 = 1
WMDM_RIGHTS_COPY_TO_NON_SDMI_DEVICE: UInt32 = 2
WMDM_RIGHTS_COPY_TO_CD: UInt32 = 8
WMDM_RIGHTS_COPY_TO_SDMI_DEVICE: UInt32 = 16
WMDM_SEEK_BEGIN: UInt32 = 1
WMDM_SEEK_CURRENT: UInt32 = 2
WMDM_SEEK_END: UInt32 = 8
DO_NOT_VIRTUALIZE_STORAGES_AS_DEVICES: UInt32 = 1
ALLOW_OUTOFBAND_NOTIFICATION: UInt32 = 2
MDSP_READ: UInt32 = 1
MDSP_WRITE: UInt32 = 2
MDSP_SEEK_BOF: UInt32 = 1
MDSP_SEEK_CUR: UInt32 = 2
MDSP_SEEK_EOF: UInt32 = 4
WMDM_SCP_EXAMINE_EXTENSION: Int32 = 1
WMDM_SCP_EXAMINE_DATA: Int32 = 2
WMDM_SCP_DECIDE_DATA: Int32 = 8
WMDM_SCP_PROTECTED_OUTPUT: Int32 = 16
WMDM_SCP_UNPROTECTED_OUTPUT: Int32 = 32
WMDM_SCP_RIGHTS_DATA: Int32 = 64
WMDM_SCP_TRANSFER_OBJECTDATA: Int32 = 32
WMDM_SCP_NO_MORE_CHANGES: Int32 = 64
WMDM_SCP_DRMINFO_NOT_DRMPROTECTED: Int32 = 0
WMDM_SCP_DRMINFO_V1HEADER: Int32 = 1
WMDM_SCP_DRMINFO_V2HEADER: Int32 = 2
SCP_EVENTID_ACQSECURECLOCK: Guid = Guid('86248cc9-4a59-43e2-91-46-48-a7-f3-f4-14-0c')
SCP_EVENTID_NEEDTOINDIV: Guid = Guid('87a507c7-b469-4386-b9-76-d5-d1-ce-53-8a-6f')
SCP_EVENTID_DRMINFO: Guid = Guid('213dd287-41d2-432b-9e-3f-3b-4f-7b-35-81-dd')
SCP_PARAMID_DRMVERSION: Guid = Guid('41d0155d-7cc7-4217-ad-a9-00-50-74-62-4d-a4')
SAC_MAC_LEN: UInt32 = 8
WMDM_LOG_SEV_INFO: UInt32 = 1
WMDM_LOG_SEV_WARN: UInt32 = 2
WMDM_LOG_SEV_ERROR: UInt32 = 4
WMDM_LOG_NOTIMESTAMP: UInt32 = 16
g_wszWMDMFileName: String = 'WMDM/FileName'
g_wszWMDMFormatCode: String = 'WMDM/FormatCode'
g_wszWMDMLastModifiedDate: String = 'WMDM/LastModifiedDate'
g_wszWMDMFileCreationDate: String = 'WMDM/FileCreationDate'
g_wszWMDMFileSize: String = 'WMDM/FileSize'
g_wszWMDMFileAttributes: String = 'WMDM/FileAttributes'
g_wszAudioWAVECodec: String = 'WMDM/AudioWAVECodec'
g_wszVideoFourCCCodec: String = 'WMDM/VideoFourCCCodec'
g_wszWMDMTitle: String = 'WMDM/Title'
g_wszWMDMAuthor: String = 'WMDM/Author'
g_wszWMDMDescription: String = 'WMDM/Description'
g_wszWMDMIsProtected: String = 'WMDM/IsProtected'
g_wszWMDMAlbumTitle: String = 'WMDM/AlbumTitle'
g_wszWMDMAlbumArtist: String = 'WMDM/AlbumArtist'
g_wszWMDMTrack: String = 'WMDM/Track'
g_wszWMDMGenre: String = 'WMDM/Genre'
g_wszWMDMTrackMood: String = 'WMDM/TrackMood'
g_wszWMDMAlbumCoverFormat: String = 'WMDM/AlbumCoverFormat'
g_wszWMDMAlbumCoverSize: String = 'WMDM/AlbumCoverSize'
g_wszWMDMAlbumCoverHeight: String = 'WMDM/AlbumCoverHeight'
g_wszWMDMAlbumCoverWidth: String = 'WMDM/AlbumCoverWidth'
g_wszWMDMAlbumCoverDuration: String = 'WMDM/AlbumCoverDuration'
g_wszWMDMAlbumCoverData: String = 'WMDM/AlbumCoverData'
g_wszWMDMYear: String = 'WMDM/Year'
g_wszWMDMComposer: String = 'WMDM/Composer'
g_wszWMDMCodec: String = 'WMDM/Codec'
g_wszWMDMDRMId: String = 'WMDM/DRMId'
g_wszWMDMBitrate: String = 'WMDM/Bitrate'
g_wszWMDMBitRateType: String = 'WMDM/BitRateType'
g_wszWMDMSampleRate: String = 'WMDM/SampleRate'
g_wszWMDMNumChannels: String = 'WMDM/NumChannels'
g_wszWMDMBlockAlignment: String = 'WMDM/BlockAlignment'
g_wszWMDMAudioBitDepth: String = 'WMDM/AudioBitDepth'
g_wszWMDMTotalBitrate: String = 'WMDM/TotalBitrate'
g_wszWMDMVideoBitrate: String = 'WMDM/VideoBitrate'
g_wszWMDMFrameRate: String = 'WMDM/FrameRate'
g_wszWMDMScanType: String = 'WMDM/ScanType'
g_wszWMDMKeyFrameDistance: String = 'WMDM/KeyFrameDistance'
g_wszWMDMBufferSize: String = 'WMDM/BufferSize'
g_wszWMDMQualitySetting: String = 'WMDM/QualitySetting'
g_wszWMDMEncodingProfile: String = 'WMDM/EncodingProfile'
g_wszWMDMDuration: String = 'WMDM/Duration'
g_wszWMDMAlbumArt: String = 'WMDM/AlbumArt'
g_wszWMDMBuyNow: String = 'WMDM/BuyNow'
g_wszWMDMNonConsumable: String = 'WMDM/NonConsumable'
g_wszWMDMediaClassPrimaryID: String = 'WMDM/MediaClassPrimaryID'
g_wszWMDMMediaClassSecondaryID: String = 'WMDM/MediaClassSecondaryID'
g_wszWMDMUserEffectiveRating: String = 'WMDM/UserEffectiveRating'
g_wszWMDMUserRating: String = 'WMDM/UserRating'
g_wszWMDMUserRatingOnDevice: String = 'WMDM/UserRatingOnDevice'
g_wszWMDMPlayCount: String = 'WMDM/PlayCount'
g_wszWMDMDevicePlayCount: String = 'WMDM/DevicePlayCount'
g_wszWMDMAuthorDate: String = 'WMDM/AuthorDate'
g_wszWMDMUserLastPlayTime: String = 'WMDM/UserLastPlayTime'
g_wszWMDMSubTitle: String = 'WMDM/SubTitle'
g_wszWMDMSubTitleDescription: String = 'WMDM/SubTitleDescription'
g_wszWMDMMediaCredits: String = 'WMDM/MediaCredits'
g_wszWMDMMediaStationName: String = 'WMDM/MediaStationName'
g_wszWMDMMediaOriginalChannel: String = 'WMDM/MediaOriginalChannel'
g_wszWMDMMediaOriginalBroadcastDateTime: String = 'WMDM/MediaOriginalBroadcastDateTime'
g_wszWMDMProviderCopyright: String = 'WMDM/ProviderCopyright'
g_wszWMDMSyncID: String = 'WMDM/SyncID'
g_wszWMDMPersistentUniqueID: String = 'WMDM/PersistentUniqueID'
g_wszWMDMWidth: String = 'WMDM/Width'
g_wszWMDMHeight: String = 'WMDM/Height'
g_wszWMDMSyncTime: String = 'WMDM/SyncTime'
g_wszWMDMParentalRating: String = 'WMDM/ParentalRating'
g_wszWMDMMetaGenre: String = 'WMDM/MetaGenre'
g_wszWMDMIsRepeat: String = 'WMDM/IsRepeat'
g_wszWMDMSupportedDeviceProperties: String = 'WMDM/SupportedDeviceProperties'
g_wszWMDMDeviceFriendlyName: String = 'WMDM/DeviceFriendlyName'
g_wszWMDMFormatsSupported: String = 'WMDM/FormatsSupported'
g_wszWMDMFormatsSupportedAreOrdered: String = 'WMDM/FormatsSupportedAreOrdered'
g_wszWMDMSyncRelationshipID: String = 'WMDM/SyncRelationshipID'
g_wszWMDMDeviceModelName: String = 'WMDM/DeviceModelName'
g_wszWMDMDeviceFirmwareVersion: String = 'WMDM/DeviceFirmwareVersion'
g_wszWMDMDeviceVendorExtension: String = 'WMDM/DeviceVendorExtension'
g_wszWMDMDeviceProtocol: String = 'WMDM/DeviceProtocol'
g_wszWMDMDeviceServiceProviderVendor: String = 'WMDM/DeviceServiceProviderVendor'
g_wszWMDMDeviceRevocationInfo: String = 'WMDM/DeviceRevocationInfo'
g_wszWMDMCollectionID: String = 'WMDM/CollectionID'
g_wszWMDMOwner: String = 'WMDM/Owner'
g_wszWMDMEditor: String = 'WMDM/Editor'
g_wszWMDMWebmaster: String = 'WMDM/Webmaster'
g_wszWMDMSourceURL: String = 'WMDM/SourceURL'
g_wszWMDMDestinationURL: String = 'WMDM/DestinationURL'
g_wszWMDMCategory: String = 'WMDM/Category'
g_wszWMDMTimeBookmark: String = 'WMDM/TimeBookmark'
g_wszWMDMObjectBookmark: String = 'WMDM/ObjectBookmark'
g_wszWMDMByteBookmark: String = 'WMDM/ByteBookmark'
g_wszWMDMDataOffset: String = 'WMDM/DataOffset'
g_wszWMDMDataLength: String = 'WMDM/DataLength'
g_wszWMDMDataUnits: String = 'WMDM/DataUnits'
g_wszWMDMTimeToLive: String = 'WMDM/TimeToLive'
g_wszWMDMMediaGuid: String = 'WMDM/MediaGuid'
g_wszWPDPassthroughPropertyValues: String = 'WPD/PassthroughPropertyValues'
EVENT_WMDM_CONTENT_TRANSFER: Guid = Guid('339c9bf4-bcfe-4ed8-94-df-ea-f8-c2-6a-b6-1b')
MTP_COMMAND_MAX_PARAMS: UInt32 = 5
MTP_RESPONSE_MAX_PARAMS: UInt32 = 5
MTP_RESPONSE_OK: UInt16 = 8193
class IComponentAuthenticate(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a9889c00-6d2b-11d3-84-96-00-c0-4f-79-db-c0')
    @commethod(3)
    def SACAuth(self, dwProtocolID: UInt32, dwPass: UInt32, pbDataIn: POINTER(Byte), dwDataInLen: UInt32, ppbDataOut: POINTER(POINTER(Byte)), pdwDataOutLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SACGetProtocols(self, ppdwProtocols: POINTER(POINTER(UInt32)), pdwProtocolCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPDevice(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a12-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetName(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetManufacturer(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersion(self, pdwVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pdwType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSerialNumber(self, pSerialNumber: POINTER(Windows.Win32.Media.DeviceManager.WMDMID_head), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPowerSource(self, pdwPowerSource: POINTER(UInt32), pdwPercentRemaining: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDeviceIcon(self, hIcon: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumStorage(self, ppEnumStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPEnumStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormatSupport(self, pFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)), pnFormatCount: POINTER(UInt32), pppwszMimeType: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pnMimeTypeCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SendOpaqueCommand(self, pCommand: POINTER(Windows.Win32.Media.DeviceManager.OPAQUECOMMAND_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPDevice2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDSPDevice
    Guid = Guid('420d16ad-c97d-4e00-82-aa-00-e9-f4-33-5d-dd')
    @commethod(14)
    def GetStorage(self, pszStorageName: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFormatSupport2(self, dwFlags: UInt32, ppAudioFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)), pnAudioFormatCount: POINTER(UInt32), ppVideoFormatEx: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)), pnVideoFormatCount: POINTER(UInt32), ppFileType: POINTER(POINTER(Windows.Win32.Media.DeviceManager.WMFILECAPABILITIES_head)), pnFileTypeCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSpecifyPropertyPages(self, ppSpecifyPropPages: POINTER(Windows.Win32.System.Ole.ISpecifyPropertyPages_head), pppUnknowns: POINTER(POINTER(Windows.Win32.System.Com.IUnknown_head)), pcUnks: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCanonicalName(self, pwszPnPName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPDevice3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDSPDevice2
    Guid = Guid('1a839845-fc55-487c-97-6f-ee-38-ac-0e-8c-4e')
    @commethod(18)
    def GetProperty(self, pwszPropName: Windows.Win32.Foundation.PWSTR, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetProperty(self, pwszPropName: Windows.Win32.Foundation.PWSTR, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFormatCapability(self, format: Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE, pFormatSupport: POINTER(Windows.Win32.Media.DeviceManager.WMDM_FORMAT_CAPABILITY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeviceIoControl(self, dwIoControlCode: UInt32, lpInBuffer: POINTER(Byte), nInBufferSize: UInt32, lpOutBuffer: POINTER(Byte), pnOutBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FindStorage(self, findScope: Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPDeviceControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a14-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetDCStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pdwCapabilitiesMask: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Play(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Record(self, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(self, fuMode: UInt32, nOffset: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPDirectTransfer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c2fe57a8-9304-478c-9e-e4-47-e3-97-b9-12-d7')
    @commethod(3)
    def TransferToDevice(self, pwszSourceFilePath: Windows.Win32.Foundation.PWSTR, pSourceOperation: Windows.Win32.Media.DeviceManager.IWMDMOperation_head, fuFlags: UInt32, pwszDestinationName: Windows.Win32.Foundation.PWSTR, pSourceMetaData: Windows.Win32.Media.DeviceManager.IWMDMMetaData_head, pTransferProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head, ppNewObject: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPEnumDevice(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a11-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def Next(self, celt: UInt32, ppDevice: POINTER(Windows.Win32.Media.DeviceManager.IMDSPDevice_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumDevice: POINTER(Windows.Win32.Media.DeviceManager.IMDSPEnumDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPEnumStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a15-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def Next(self, celt: UInt32, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPEnumStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a18-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def Open(self, fuMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Read(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Write(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self, fuMode: UInt32, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Seek(self, fuFlags: UInt32, dwOffset: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Rename(self, pwszNewName: Windows.Win32.Foundation.PWSTR, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Move(self, fuMode: UInt32, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head, pTarget: Windows.Win32.Media.DeviceManager.IMDSPStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPObject2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDSPObject
    Guid = Guid('3f34cd3e-5907-4341-9a-f9-97-f4-18-7c-3a-a5')
    @commethod(11)
    def ReadOnClearChannel(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def WriteOnClearChannel(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPObjectInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a19-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetPlayLength(self, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPlayLength(self, dwLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPlayOffset(self, pdwOffset: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPlayOffset(self, dwOffset: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalLength(self, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLastPlayPosition(self, pdwLastPos: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLongestPlayPosition(self, pdwLongestPos: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPRevoked(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a4e8f2d4-3f31-464d-b5-3d-4f-c3-35-99-81-84')
    @commethod(3)
    def GetRevocationURL(self, ppwszRevocationURL: POINTER(Windows.Win32.Foundation.PWSTR), pdwBufferLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a16-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def SetAttributes(self, dwAttributes: UInt32, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStorageGlobals(self, ppStorageGlobals: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributes(self, pdwAttributes: POINTER(UInt32), pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetName(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDate(self, pDateTimeUTC: POINTER(Windows.Win32.Media.DeviceManager.WMDMDATETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(self, pdwSizeLow: POINTER(UInt32), pdwSizeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRights(self, ppRights: POINTER(POINTER(Windows.Win32.Media.DeviceManager.WMDMRIGHTS_head)), pnRightsCount: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateStorage(self, dwAttributes: UInt32, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pwszName: Windows.Win32.Foundation.PWSTR, ppNewStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumStorage(self, ppEnumStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPEnumStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SendOpaqueCommand(self, pCommand: POINTER(Windows.Win32.Media.DeviceManager.OPAQUECOMMAND_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDSPStorage
    Guid = Guid('0a5e07a5-6454-4451-9c-36-1c-6a-e7-e2-b1-d6')
    @commethod(13)
    def GetStorage(self, pszStorageName: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateStorage2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pAudioFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head), pwszName: Windows.Win32.Foundation.PWSTR, qwFileSize: UInt64, ppNewStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetAttributes2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pAudioFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAttributes2(self, pdwAttributes: POINTER(UInt32), pdwAttributesEx: POINTER(UInt32), pAudioFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDSPStorage2
    Guid = Guid('6c669867-97ed-4a67-97-06-1c-55-29-d2-a4-14')
    @commethod(17)
    def GetMetadata(self, pMetadata: Windows.Win32.Media.DeviceManager.IWMDMMetaData_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetMetadata(self, pMetadata: Windows.Win32.Media.DeviceManager.IWMDMMetaData_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorage4(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDSPStorage3
    Guid = Guid('3133b2c4-515c-481b-b1-ce-39-32-7e-cb-4f-74')
    @commethod(19)
    def SetReferences(self, dwRefs: UInt32, ppISPStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetReferences(self, pdwRefs: POINTER(UInt32), pppISPStorage: POINTER(POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateStorageWithMetadata(self, dwAttributes: UInt32, pwszName: Windows.Win32.Foundation.PWSTR, pMetadata: Windows.Win32.Media.DeviceManager.IWMDMMetaData_head, qwFileSize: UInt64, ppNewStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetSpecifiedMetadata(self, cProperties: UInt32, ppwszPropNames: POINTER(Windows.Win32.Foundation.PWSTR), pMetadata: Windows.Win32.Media.DeviceManager.IWMDMMetaData_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def FindStorage(self, findScope: Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetParent(self, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDSPStorageGlobals(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a17-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetCapabilities(self, pdwCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSerialNumber(self, pSerialNum: POINTER(Windows.Win32.Media.DeviceManager.WMDMID_head), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalSize(self, pdwTotalSizeLow: POINTER(UInt32), pdwTotalSizeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTotalFree(self, pdwFreeLow: POINTER(UInt32), pdwFreeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalBad(self, pdwBadLow: POINTER(UInt32), pdwBadHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Initialize(self, fuMode: UInt32, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDevice(self, ppDevice: POINTER(Windows.Win32.Media.DeviceManager.IMDSPDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetRootStorage(self, ppRoot: POINTER(Windows.Win32.Media.DeviceManager.IMDSPStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDServiceProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a10-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetDeviceCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumDevices(self, ppEnumDevice: POINTER(Windows.Win32.Media.DeviceManager.IMDSPEnumDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMDServiceProvider2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDServiceProvider
    Guid = Guid('b2fa24b7-cda3-4694-98-62-41-3a-e1-a3-48-19')
    @commethod(5)
    def CreateDevice(self, pwszDevicePath: Windows.Win32.Foundation.PWSTR, pdwCount: POINTER(UInt32), pppDeviceArray: POINTER(POINTER(Windows.Win32.Media.DeviceManager.IMDSPDevice_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IMDServiceProvider3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IMDServiceProvider2
    Guid = Guid('4ed13ef3-a971-4d19-9f-51-0e-18-26-b2-da-57')
    @commethod(6)
    def SetDeviceEnumPreference(self, dwEnumPref: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureAuthenticate(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a0f-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetSecureQuery(self, ppSecureQuery: POINTER(Windows.Win32.Media.DeviceManager.ISCPSecureQuery_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureAuthenticate2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.ISCPSecureAuthenticate
    Guid = Guid('b580cfae-1672-47e2-ac-aa-44-bb-ec-bc-ae-5b')
    @commethod(4)
    def GetSCPSession(self, ppSCPSession: POINTER(Windows.Win32.Media.DeviceManager.ISCPSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureExchange(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a0e-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def TransferContainerData(self, pData: POINTER(Byte), dwSize: UInt32, pfuReadyFlags: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ObjectData(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransferComplete(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureExchange2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.ISCPSecureExchange
    Guid = Guid('6c62fc7b-2690-483f-9d-44-0a-20-cb-35-57-7c')
    @commethod(6)
    def TransferContainerData2(self, pData: POINTER(Byte), dwSize: UInt32, pProgressCallback: Windows.Win32.Media.DeviceManager.IWMDMProgress3_head, pfuReadyFlags: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureExchange3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.ISCPSecureExchange2
    Guid = Guid('ab4e77e4-8908-4b17-bd-2a-b1-db-e6-dd-69-e1')
    @commethod(7)
    def TransferContainerDataOnClearChannel(self, pDevice: Windows.Win32.Media.DeviceManager.IMDSPDevice_head, pData: POINTER(Byte), dwSize: UInt32, pProgressCallback: Windows.Win32.Media.DeviceManager.IWMDMProgress3_head, pfuReadyFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetObjectDataOnClearChannel(self, pDevice: Windows.Win32.Media.DeviceManager.IMDSPDevice_head, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def TransferCompleteForDevice(self, pDevice: Windows.Win32.Media.DeviceManager.IMDSPDevice_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureQuery(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a0d-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetDataDemands(self, pfuFlags: POINTER(UInt32), pdwMinRightsData: POINTER(UInt32), pdwMinExamineData: POINTER(UInt32), pdwMinDecideData: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ExamineData(self, fuFlags: UInt32, pwszExtension: Windows.Win32.Foundation.PWSTR, pData: POINTER(Byte), dwSize: UInt32, abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MakeDecision(self, fuFlags: UInt32, pData: POINTER(Byte), dwSize: UInt32, dwAppSec: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStorageGlobals: Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals_head, ppExchange: POINTER(Windows.Win32.Media.DeviceManager.ISCPSecureExchange_head), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRights(self, pData: POINTER(Byte), dwSize: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStgGlobals: Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals_head, ppRights: POINTER(POINTER(Windows.Win32.Media.DeviceManager.WMDMRIGHTS_head)), pnRightsCount: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureQuery2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.ISCPSecureQuery
    Guid = Guid('ebe17e25-4fd7-4632-af-46-6d-93-d4-fc-c7-2e')
    @commethod(7)
    def MakeDecision2(self, fuFlags: UInt32, pData: POINTER(Byte), dwSize: UInt32, dwAppSec: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStorageGlobals: Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals_head, pAppCertApp: POINTER(Byte), dwAppCertAppLen: UInt32, pAppCertSP: POINTER(Byte), dwAppCertSPLen: UInt32, pszRevocationURL: POINTER(Windows.Win32.Foundation.PWSTR), pdwRevocationURLLen: POINTER(UInt32), pdwRevocationBitFlag: POINTER(UInt32), pqwFileSize: POINTER(UInt64), pUnknown: Windows.Win32.System.Com.IUnknown_head, ppExchange: POINTER(Windows.Win32.Media.DeviceManager.ISCPSecureExchange_head), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSecureQuery3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.ISCPSecureQuery2
    Guid = Guid('b7edd1a2-4dab-484b-b3-c5-ad-39-b8-b4-c0-b1')
    @commethod(8)
    def GetRightsOnClearChannel(self, pData: POINTER(Byte), dwSize: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStgGlobals: Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals_head, pProgressCallback: Windows.Win32.Media.DeviceManager.IWMDMProgress3_head, ppRights: POINTER(POINTER(Windows.Win32.Media.DeviceManager.WMDMRIGHTS_head)), pnRightsCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MakeDecisionOnClearChannel(self, fuFlags: UInt32, pData: POINTER(Byte), dwSize: UInt32, dwAppSec: UInt32, pbSPSessionKey: POINTER(Byte), dwSessionKeyLen: UInt32, pStorageGlobals: Windows.Win32.Media.DeviceManager.IMDSPStorageGlobals_head, pProgressCallback: Windows.Win32.Media.DeviceManager.IWMDMProgress3_head, pAppCertApp: POINTER(Byte), dwAppCertAppLen: UInt32, pAppCertSP: POINTER(Byte), dwAppCertSPLen: UInt32, pszRevocationURL: POINTER(Windows.Win32.Foundation.PWSTR), pdwRevocationURLLen: POINTER(UInt32), pdwRevocationBitFlag: POINTER(UInt32), pqwFileSize: POINTER(UInt64), pUnknown: Windows.Win32.System.Com.IUnknown_head, ppExchange: POINTER(Windows.Win32.Media.DeviceManager.ISCPSecureExchange_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISCPSession(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('88a3e6ed-eee4-4619-bb-b3-fd-4f-b6-27-15-d1')
    @commethod(3)
    def BeginSession(self, pIDevice: Windows.Win32.Media.DeviceManager.IMDSPDevice_head, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndSession(self, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSecureQuery(self, ppSecureQuery: POINTER(Windows.Win32.Media.DeviceManager.ISCPSecureQuery_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMDevice(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a02-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetName(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetManufacturer(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetVersion(self, pdwVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetType(self, pdwType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSerialNumber(self, pSerialNumber: POINTER(Windows.Win32.Media.DeviceManager.WMDMID_head), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPowerSource(self, pdwPowerSource: POINTER(UInt32), pdwPercentRemaining: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDeviceIcon(self, hIcon: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumStorage(self, ppEnumStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMEnumStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormatSupport(self, ppFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)), pnFormatCount: POINTER(UInt32), pppwszMimeType: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pnMimeTypeCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SendOpaqueCommand(self, pCommand: POINTER(Windows.Win32.Media.DeviceManager.OPAQUECOMMAND_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMDevice2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMDevice
    Guid = Guid('e34f3d37-9d67-4fc1-92-52-62-d2-8b-2f-8b-55')
    @commethod(14)
    def GetStorage(self, pszStorageName: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFormatSupport2(self, dwFlags: UInt32, ppAudioFormatEx: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)), pnAudioFormatCount: POINTER(UInt32), ppVideoFormatEx: POINTER(POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)), pnVideoFormatCount: POINTER(UInt32), ppFileType: POINTER(POINTER(Windows.Win32.Media.DeviceManager.WMFILECAPABILITIES_head)), pnFileTypeCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSpecifyPropertyPages(self, ppSpecifyPropPages: POINTER(Windows.Win32.System.Ole.ISpecifyPropertyPages_head), pppUnknowns: POINTER(POINTER(Windows.Win32.System.Com.IUnknown_head)), pcUnks: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCanonicalName(self, pwszPnPName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMDevice3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMDevice2
    Guid = Guid('6c03e4fe-05db-4dda-9e-3c-06-23-3a-6d-5d-65')
    @commethod(18)
    def GetProperty(self, pwszPropName: Windows.Win32.Foundation.PWSTR, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetProperty(self, pwszPropName: Windows.Win32.Foundation.PWSTR, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFormatCapability(self, format: Windows.Win32.Media.DeviceManager.WMDM_FORMATCODE, pFormatSupport: POINTER(Windows.Win32.Media.DeviceManager.WMDM_FORMAT_CAPABILITY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeviceIoControl(self, dwIoControlCode: UInt32, lpInBuffer: POINTER(Byte), nInBufferSize: UInt32, lpOutBuffer: POINTER(Byte), pnOutBufferSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def FindStorage(self, findScope: Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMDeviceControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a04-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCapabilities(self, pdwCapabilitiesMask: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Play(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Record(self, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(self, fuMode: UInt32, nOffset: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMDeviceSession(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('82af0a65-9d96-412c-83-e5-3c-43-e4-b0-6c-c7')
    @commethod(3)
    def BeginSession(self, type: Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndSession(self, type: Windows.Win32.Media.DeviceManager.WMDM_SESSION_TYPE, pCtx: POINTER(Byte), dwSizeCtx: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMEnumDevice(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a01-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def Next(self, celt: UInt32, ppDevice: POINTER(Windows.Win32.Media.DeviceManager.IWMDMDevice_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumDevice: POINTER(Windows.Win32.Media.DeviceManager.IWMDMEnumDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMEnumStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a05-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def Next(self, celt: UInt32, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32, pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnumStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMEnumStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMLogger(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('110a3200-5a79-11d3-8d-78-44-45-53-54-00-00')
    @commethod(3)
    def IsEnabled(self, pfEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Enable(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLogFileName(self, pszFilename: Windows.Win32.Foundation.PSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLogFileName(self, pszFilename: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LogString(self, dwFlags: UInt32, pszSrcName: Windows.Win32.Foundation.PSTR, pszLog: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def LogDword(self, dwFlags: UInt32, pszSrcName: Windows.Win32.Foundation.PSTR, pszLogFormat: Windows.Win32.Foundation.PSTR, dwLog: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSizeParams(self, pdwMaxSize: POINTER(UInt32), pdwShrinkToSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSizeParams(self, dwMaxSize: UInt32, dwShrinkToSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMMetaData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ec3b0663-0951-460a-9a-80-0d-ce-ed-3c-04-3c')
    @commethod(3)
    def AddItem(self, Type: Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE, pwszTagName: Windows.Win32.Foundation.PWSTR, pValue: POINTER(Byte), iLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryByName(self, pwszTagName: Windows.Win32.Foundation.PWSTR, pType: POINTER(Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE), pValue: POINTER(POINTER(Byte)), pcbLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryByIndex(self, iIndex: UInt32, ppwszName: POINTER(POINTER(UInt16)), pType: POINTER(Windows.Win32.Media.DeviceManager.WMDM_TAG_DATATYPE), ppValue: POINTER(POINTER(Byte)), pcbLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemCount(self, iCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMNotification(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3f5e95c0-0f43-4ed4-93-d2-c8-9a-45-d5-9b-81')
    @commethod(3)
    def WMDMMessage(self, dwMessageType: UInt32, pwszCanonicalName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMObjectInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a09-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetPlayLength(self, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPlayLength(self, dwLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPlayOffset(self, pdwOffset: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPlayOffset(self, dwOffset: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalLength(self, pdwLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLastPlayPosition(self, pdwLastPos: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLongestPlayPosition(self, pdwLongestPos: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMOperation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a0b-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def BeginRead(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginWrite(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObjectName(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetObjectName(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectAttributes(self, pdwAttributes: POINTER(UInt32), pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetObjectAttributes(self, dwAttributes: UInt32, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetObjectTotalSize(self, pdwSize: POINTER(UInt32), pdwSizeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetObjectTotalSize(self, dwSize: UInt32, dwSizeHigh: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def TransferObjectData(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def End(self, phCompletionCode: POINTER(Windows.Win32.Foundation.HRESULT), pNewObject: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMOperation2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMOperation
    Guid = Guid('33445b48-7df7-425c-ad-8f-0f-c6-d8-2f-9f-75')
    @commethod(13)
    def SetObjectAttributes2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetObjectAttributes2(self, pdwAttributes: POINTER(UInt32), pdwAttributesEx: POINTER(UInt32), pAudioFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMOperation3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMOperation
    Guid = Guid('d1f9b46a-9ca8-46d8-9d-0f-1e-c9-ba-e5-49-19')
    @commethod(13)
    def TransferObjectDataOnClearChannel(self, pData: POINTER(Byte), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMProgress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a0c-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def Begin(self, dwEstimatedTicks: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Progress(self, dwTranspiredTicks: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def End(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMProgress2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMProgress
    Guid = Guid('3a43f550-b383-4e92-b0-4a-e6-bb-c6-60-fe-fc')
    @commethod(6)
    def End2(self, hrCompletionCode: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMProgress3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMProgress2
    Guid = Guid('21de01cb-3bb4-4929-b2-1a-17-af-3f-80-f6-58')
    @commethod(7)
    def Begin3(self, EventId: Guid, dwEstimatedTicks: UInt32, pContext: POINTER(Windows.Win32.Media.DeviceManager.OPAQUECOMMAND_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Progress3(self, EventId: Guid, dwTranspiredTicks: UInt32, pContext: POINTER(Windows.Win32.Media.DeviceManager.OPAQUECOMMAND_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def End3(self, EventId: Guid, hrCompletionCode: Windows.Win32.Foundation.HRESULT, pContext: POINTER(Windows.Win32.Media.DeviceManager.OPAQUECOMMAND_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMRevoked(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ebeccedb-88ee-4e55-b6-a4-8d-9f-07-d6-96-aa')
    @commethod(3)
    def GetRevocationURL(self, ppwszRevocationURL: POINTER(Windows.Win32.Foundation.PWSTR), pdwBufferLen: POINTER(UInt32), pdwRevokedBitFlag: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a06-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def SetAttributes(self, dwAttributes: UInt32, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStorageGlobals(self, ppStorageGlobals: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorageGlobals_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributes(self, pdwAttributes: POINTER(UInt32), pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetName(self, pwszName: Windows.Win32.Foundation.PWSTR, nMaxChars: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDate(self, pDateTimeUTC: POINTER(Windows.Win32.Media.DeviceManager.WMDMDATETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(self, pdwSizeLow: POINTER(UInt32), pdwSizeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRights(self, ppRights: POINTER(POINTER(Windows.Win32.Media.DeviceManager.WMDMRIGHTS_head)), pnRightsCount: POINTER(UInt32), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumStorage(self, pEnumStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMEnumStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SendOpaqueCommand(self, pCommand: POINTER(Windows.Win32.Media.DeviceManager.OPAQUECOMMAND_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMStorage
    Guid = Guid('1ed5a144-5cd5-4683-9e-ff-72-cb-db-2d-95-33')
    @commethod(12)
    def GetStorage(self, pszStorageName: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetAttributes2(self, dwAttributes: UInt32, dwAttributesEx: UInt32, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetAttributes2(self, pdwAttributes: POINTER(UInt32), pdwAttributesEx: POINTER(UInt32), pAudioFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pVideoFormat: POINTER(Windows.Win32.Media.MediaFoundation.VIDEOINFOHEADER_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMStorage2
    Guid = Guid('97717eea-926a-464e-96-a4-24-7b-02-16-02-6e')
    @commethod(15)
    def GetMetadata(self, ppMetadata: POINTER(Windows.Win32.Media.DeviceManager.IWMDMMetaData_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetMetadata(self, pMetadata: Windows.Win32.Media.DeviceManager.IWMDMMetaData_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateEmptyMetadataObject(self, ppMetadata: POINTER(Windows.Win32.Media.DeviceManager.IWMDMMetaData_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetEnumPreference(self, pMode: POINTER(Windows.Win32.Media.DeviceManager.WMDM_STORAGE_ENUM_MODE), nViews: UInt32, pViews: POINTER(Windows.Win32.Media.DeviceManager.WMDMMetadataView_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorage4(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMStorage3
    Guid = Guid('c225bac5-a03a-40b8-9a-23-91-cf-47-8c-64-a6')
    @commethod(19)
    def SetReferences(self, dwRefs: UInt32, ppIWMDMStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetReferences(self, pdwRefs: POINTER(UInt32), pppIWMDMStorage: POINTER(POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRightsWithProgress(self, pIProgressCallback: Windows.Win32.Media.DeviceManager.IWMDMProgress3_head, ppRights: POINTER(POINTER(Windows.Win32.Media.DeviceManager.WMDMRIGHTS_head)), pnRightsCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetSpecifiedMetadata(self, cProperties: UInt32, ppwszPropNames: POINTER(Windows.Win32.Foundation.PWSTR), ppMetadata: POINTER(Windows.Win32.Media.DeviceManager.IWMDMMetaData_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def FindStorage(self, findScope: Windows.Win32.Media.DeviceManager.WMDM_FIND_SCOPE, pwszUniqueID: Windows.Win32.Foundation.PWSTR, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetParent(self, ppStorage: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a08-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def Insert(self, fuMode: UInt32, pwszFile: Windows.Win32.Foundation.PWSTR, pOperation: Windows.Win32.Media.DeviceManager.IWMDMOperation_head, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head, ppNewObject: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Delete(self, fuMode: UInt32, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Rename(self, fuMode: UInt32, pwszNewName: Windows.Win32.Foundation.PWSTR, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Read(self, fuMode: UInt32, pwszFile: Windows.Win32.Foundation.PWSTR, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head, pOperation: Windows.Win32.Media.DeviceManager.IWMDMOperation_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Move(self, fuMode: UInt32, pTargetObject: Windows.Win32.Media.DeviceManager.IWMDMStorage_head, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageControl2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMStorageControl
    Guid = Guid('972c2e88-bd6c-4125-8e-09-84-f8-37-e6-37-b6')
    @commethod(8)
    def Insert2(self, fuMode: UInt32, pwszFileSource: Windows.Win32.Foundation.PWSTR, pwszFileDest: Windows.Win32.Foundation.PWSTR, pOperation: Windows.Win32.Media.DeviceManager.IWMDMOperation_head, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head, pUnknown: Windows.Win32.System.Com.IUnknown_head, ppNewObject: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageControl3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDMStorageControl2
    Guid = Guid('b3266365-d4f3-4696-8d-53-bd-27-ec-60-99-3a')
    @commethod(9)
    def Insert3(self, fuMode: UInt32, fuType: UInt32, pwszFileSource: Windows.Win32.Foundation.PWSTR, pwszFileDest: Windows.Win32.Foundation.PWSTR, pOperation: Windows.Win32.Media.DeviceManager.IWMDMOperation_head, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head, pMetaData: Windows.Win32.Media.DeviceManager.IWMDMMetaData_head, pUnknown: Windows.Win32.System.Com.IUnknown_head, ppNewObject: POINTER(Windows.Win32.Media.DeviceManager.IWMDMStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDMStorageGlobals(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a07-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetCapabilities(self, pdwCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSerialNumber(self, pSerialNum: POINTER(Windows.Win32.Media.DeviceManager.WMDMID_head), abMac: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTotalSize(self, pdwTotalSizeLow: POINTER(UInt32), pdwTotalSizeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTotalFree(self, pdwFreeLow: POINTER(UInt32), pdwFreeHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTotalBad(self, pdwBadLow: POINTER(UInt32), pdwBadHigh: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Initialize(self, fuMode: UInt32, pProgress: Windows.Win32.Media.DeviceManager.IWMDMProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dcb3a00-33ed-11d3-84-70-00-c0-4f-79-db-c0')
    @commethod(3)
    def GetRevision(self, pdwRevision: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumDevices(self, ppEnumDevice: POINTER(Windows.Win32.Media.DeviceManager.IWMDMEnumDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceManager2(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDeviceManager
    Guid = Guid('923e5249-8731-4c5b-9b-1c-b8-b6-0b-6e-46-af')
    @commethod(6)
    def GetDeviceFromCanonicalName(self, pwszCanonicalName: Windows.Win32.Foundation.PWSTR, ppDevice: POINTER(Windows.Win32.Media.DeviceManager.IWMDMDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumDevices2(self, ppEnumDevice: POINTER(Windows.Win32.Media.DeviceManager.IWMDMEnumDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reinitialize(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWMDeviceManager3(c_void_p):
    extends: Windows.Win32.Media.DeviceManager.IWMDeviceManager2
    Guid = Guid('af185c41-100d-46ed-be-2e-9c-e8-c4-45-94-ef')
    @commethod(9)
    def SetDeviceEnumPreference(self, dwEnumPref: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class MACINFO(EasyCastStructure):
    fUsed: Windows.Win32.Foundation.BOOL
    abMacState: Byte * 36
class MTP_COMMAND_DATA_IN(EasyCastStructure):
    OpCode: UInt16
    NumParams: UInt32
    Params: UInt32 * 5
    NextPhase: UInt32
    CommandWriteDataSize: UInt32
    CommandWriteData: Byte * 1
    _pack_ = 1
class MTP_COMMAND_DATA_OUT(EasyCastStructure):
    ResponseCode: UInt16
    NumParams: UInt32
    Params: UInt32 * 5
    CommandReadDataSize: UInt32
    CommandReadData: Byte * 1
    _pack_ = 1
MediaDevMgr = Guid('25baad81-3560-11d3-84-71-00-c0-4f-79-db-c0')
MediaDevMgrClassFactory = Guid('50040c1d-bdbf-4924-b8-73-f1-4d-6c-5b-fd-66')
class OPAQUECOMMAND(EasyCastStructure):
    guidCommand: Guid
    dwDataLen: UInt32
    pData: POINTER(Byte)
    abMAC: Byte * 20
class WMDMDATETIME(EasyCastStructure):
    wYear: UInt16
    wMonth: UInt16
    wDay: UInt16
    wHour: UInt16
    wMinute: UInt16
    wSecond: UInt16
class WMDMDetermineMaxPropStringLen(EasyCastUnion):
    sz001: Char * 27
    sz002: Char * 31
    sz003: Char * 14
    sz004: Char * 16
    sz005: Char * 22
    sz006: Char * 14
    sz007: Char * 20
    sz008: Char * 20
    sz009: Char * 22
    sz010: Char * 11
    sz011: Char * 12
    sz012: Char * 17
    sz013: Char * 17
    sz014: Char * 16
    sz015: Char * 17
    sz016: Char * 11
    sz017: Char * 11
    sz018: Char * 15
    sz019: Char * 22
    sz020: Char * 20
    sz021: Char * 22
    sz022: Char * 21
    sz023: Char * 24
    sz024: Char * 20
    sz025: Char * 10
    sz026: Char * 14
    sz027: Char * 11
    sz028: Char * 11
    sz029: Char * 13
    sz030: Char * 17
    sz031: Char * 16
    sz032: Char * 17
    sz033: Char * 20
    sz034: Char * 19
    sz035: Char * 18
    sz036: Char * 18
    sz037: Char * 15
    sz041: Char * 14
    sz043: Char * 22
    sz044: Char * 16
    sz045: Char * 20
    sz046: Char * 14
    sz047: Char * 14
    sz048: Char * 12
    sz049: Char * 25
    sz050: Char * 26
    sz051: Char * 25
    sz052: Char * 16
    sz053: Char * 24
    sz054: Char * 15
    sz055: Char * 21
    sz056: Char * 16
    sz057: Char * 22
    sz058: Char * 14
    sz059: Char * 25
    sz060: Char * 18
    sz061: Char * 22
    sz062: Char * 26
    sz063: Char * 36
    sz064: Char * 23
    sz065: Char * 12
    sz066: Char * 24
    sz067: Char * 11
    sz068: Char * 12
    sz069: Char * 14
    sz070: Char * 20
    sz071: Char * 15
    sz072: Char * 14
    sz073: Char * 31
    sz074: Char * 24
    sz075: Char * 22
    sz076: Char * 24
    sz077: Char * 21
    sz078: Char * 27
    sz079: Char * 27
    sz080: Char * 20
    sz081: Char * 33
    sz082: Char * 21
    sz083: Char * 32
    sz084: Char * 26
    sz085: Char * 18
    sz086: Char * 30
WMDMDevice = Guid('807b3cdf-357a-11d3-84-71-00-c0-4f-79-db-c0')
WMDMDeviceEnum = Guid('430e35af-3971-11d3-84-74-00-c0-4f-79-db-c0')
class WMDMID(EasyCastStructure):
    cbSize: UInt32
    dwVendorID: UInt32
    pID: Byte * 128
    SerialNumberLength: UInt32
WMDMLogger = Guid('110a3202-5a79-11d3-8d-78-44-45-53-54-00-00')
WMDMMessage = Int32
WMDM_MSG_DEVICE_ARRIVAL: WMDMMessage = 0
WMDM_MSG_DEVICE_REMOVAL: WMDMMessage = 1
WMDM_MSG_MEDIA_ARRIVAL: WMDMMessage = 2
WMDM_MSG_MEDIA_REMOVAL: WMDMMessage = 3
class WMDMMetadataView(EasyCastStructure):
    pwszViewName: Windows.Win32.Foundation.PWSTR
    nDepth: UInt32
    ppwszTags: POINTER(POINTER(UInt16))
class WMDMRIGHTS(EasyCastStructure):
    cbSize: UInt32
    dwContentType: UInt32
    fuFlags: UInt32
    fuRights: UInt32
    dwAppSec: UInt32
    dwPlaybackCount: UInt32
    ExpirationDate: Windows.Win32.Media.DeviceManager.WMDMDATETIME
WMDMStorage = Guid('807b3ce0-357a-11d3-84-71-00-c0-4f-79-db-c0')
WMDMStorageEnum = Guid('eb401a3b-3af7-11d3-84-74-00-c0-4f-79-db-c0')
WMDMStorageGlobal = Guid('807b3ce1-357a-11d3-84-71-00-c0-4f-79-db-c0')
WMDM_ENUM_PROP_VALID_VALUES_FORM = Int32
WMDM_ENUM_PROP_VALID_VALUES_ANY: WMDM_ENUM_PROP_VALID_VALUES_FORM = 0
WMDM_ENUM_PROP_VALID_VALUES_RANGE: WMDM_ENUM_PROP_VALID_VALUES_FORM = 1
WMDM_ENUM_PROP_VALID_VALUES_ENUM: WMDM_ENUM_PROP_VALID_VALUES_FORM = 2
WMDM_FIND_SCOPE = Int32
WMDM_FIND_SCOPE_GLOBAL: WMDM_FIND_SCOPE = 0
WMDM_FIND_SCOPE_IMMEDIATE_CHILDREN: WMDM_FIND_SCOPE = 1
WMDM_FORMATCODE = Int32
WMDM_FORMATCODE_NOTUSED: WMDM_FORMATCODE = 0
WMDM_FORMATCODE_ALLIMAGES: WMDM_FORMATCODE = -1
WMDM_FORMATCODE_UNDEFINED: WMDM_FORMATCODE = 12288
WMDM_FORMATCODE_ASSOCIATION: WMDM_FORMATCODE = 12289
WMDM_FORMATCODE_SCRIPT: WMDM_FORMATCODE = 12290
WMDM_FORMATCODE_EXECUTABLE: WMDM_FORMATCODE = 12291
WMDM_FORMATCODE_TEXT: WMDM_FORMATCODE = 12292
WMDM_FORMATCODE_HTML: WMDM_FORMATCODE = 12293
WMDM_FORMATCODE_DPOF: WMDM_FORMATCODE = 12294
WMDM_FORMATCODE_AIFF: WMDM_FORMATCODE = 12295
WMDM_FORMATCODE_WAVE: WMDM_FORMATCODE = 12296
WMDM_FORMATCODE_MP3: WMDM_FORMATCODE = 12297
WMDM_FORMATCODE_AVI: WMDM_FORMATCODE = 12298
WMDM_FORMATCODE_MPEG: WMDM_FORMATCODE = 12299
WMDM_FORMATCODE_ASF: WMDM_FORMATCODE = 12300
WMDM_FORMATCODE_RESERVED_FIRST: WMDM_FORMATCODE = 12301
WMDM_FORMATCODE_RESERVED_LAST: WMDM_FORMATCODE = 14335
WMDM_FORMATCODE_IMAGE_UNDEFINED: WMDM_FORMATCODE = 14336
WMDM_FORMATCODE_IMAGE_EXIF: WMDM_FORMATCODE = 14337
WMDM_FORMATCODE_IMAGE_TIFFEP: WMDM_FORMATCODE = 14338
WMDM_FORMATCODE_IMAGE_FLASHPIX: WMDM_FORMATCODE = 14339
WMDM_FORMATCODE_IMAGE_BMP: WMDM_FORMATCODE = 14340
WMDM_FORMATCODE_IMAGE_CIFF: WMDM_FORMATCODE = 14341
WMDM_FORMATCODE_IMAGE_GIF: WMDM_FORMATCODE = 14343
WMDM_FORMATCODE_IMAGE_JFIF: WMDM_FORMATCODE = 14344
WMDM_FORMATCODE_IMAGE_PCD: WMDM_FORMATCODE = 14345
WMDM_FORMATCODE_IMAGE_PICT: WMDM_FORMATCODE = 14346
WMDM_FORMATCODE_IMAGE_PNG: WMDM_FORMATCODE = 14347
WMDM_FORMATCODE_IMAGE_TIFF: WMDM_FORMATCODE = 14349
WMDM_FORMATCODE_IMAGE_TIFFIT: WMDM_FORMATCODE = 14350
WMDM_FORMATCODE_IMAGE_JP2: WMDM_FORMATCODE = 14351
WMDM_FORMATCODE_IMAGE_JPX: WMDM_FORMATCODE = 14352
WMDM_FORMATCODE_IMAGE_RESERVED_FIRST: WMDM_FORMATCODE = 14353
WMDM_FORMATCODE_IMAGE_RESERVED_LAST: WMDM_FORMATCODE = 16383
WMDM_FORMATCODE_UNDEFINEDFIRMWARE: WMDM_FORMATCODE = 47106
WMDM_FORMATCODE_WBMP: WMDM_FORMATCODE = 47107
WMDM_FORMATCODE_JPEGXR: WMDM_FORMATCODE = 47108
WMDM_FORMATCODE_WINDOWSIMAGEFORMAT: WMDM_FORMATCODE = 47233
WMDM_FORMATCODE_UNDEFINEDAUDIO: WMDM_FORMATCODE = 47360
WMDM_FORMATCODE_WMA: WMDM_FORMATCODE = 47361
WMDM_FORMATCODE_OGG: WMDM_FORMATCODE = 47362
WMDM_FORMATCODE_AAC: WMDM_FORMATCODE = 47363
WMDM_FORMATCODE_AUDIBLE: WMDM_FORMATCODE = 47364
WMDM_FORMATCODE_FLAC: WMDM_FORMATCODE = 47366
WMDM_FORMATCODE_QCELP: WMDM_FORMATCODE = 47367
WMDM_FORMATCODE_AMR: WMDM_FORMATCODE = 47368
WMDM_FORMATCODE_UNDEFINEDVIDEO: WMDM_FORMATCODE = 47488
WMDM_FORMATCODE_WMV: WMDM_FORMATCODE = 47489
WMDM_FORMATCODE_MP4: WMDM_FORMATCODE = 47490
WMDM_FORMATCODE_MP2: WMDM_FORMATCODE = 47491
WMDM_FORMATCODE_3GP: WMDM_FORMATCODE = 47492
WMDM_FORMATCODE_3G2: WMDM_FORMATCODE = 47493
WMDM_FORMATCODE_AVCHD: WMDM_FORMATCODE = 47494
WMDM_FORMATCODE_ATSCTS: WMDM_FORMATCODE = 47495
WMDM_FORMATCODE_DVBTS: WMDM_FORMATCODE = 47496
WMDM_FORMATCODE_MKV: WMDM_FORMATCODE = 47497
WMDM_FORMATCODE_MKA: WMDM_FORMATCODE = 47498
WMDM_FORMATCODE_MK3D: WMDM_FORMATCODE = 47499
WMDM_FORMATCODE_UNDEFINEDCOLLECTION: WMDM_FORMATCODE = 47616
WMDM_FORMATCODE_ABSTRACTMULTIMEDIAALBUM: WMDM_FORMATCODE = 47617
WMDM_FORMATCODE_ABSTRACTIMAGEALBUM: WMDM_FORMATCODE = 47618
WMDM_FORMATCODE_ABSTRACTAUDIOALBUM: WMDM_FORMATCODE = 47619
WMDM_FORMATCODE_ABSTRACTVIDEOALBUM: WMDM_FORMATCODE = 47620
WMDM_FORMATCODE_ABSTRACTAUDIOVIDEOPLAYLIST: WMDM_FORMATCODE = 47621
WMDM_FORMATCODE_ABSTRACTCONTACTGROUP: WMDM_FORMATCODE = 47622
WMDM_FORMATCODE_ABSTRACTMESSAGEFOLDER: WMDM_FORMATCODE = 47623
WMDM_FORMATCODE_ABSTRACTCHAPTEREDPRODUCTION: WMDM_FORMATCODE = 47624
WMDM_FORMATCODE_MEDIA_CAST: WMDM_FORMATCODE = 47627
WMDM_FORMATCODE_WPLPLAYLIST: WMDM_FORMATCODE = 47632
WMDM_FORMATCODE_M3UPLAYLIST: WMDM_FORMATCODE = 47633
WMDM_FORMATCODE_MPLPLAYLIST: WMDM_FORMATCODE = 47634
WMDM_FORMATCODE_ASXPLAYLIST: WMDM_FORMATCODE = 47635
WMDM_FORMATCODE_PLSPLAYLIST: WMDM_FORMATCODE = 47636
WMDM_FORMATCODE_UNDEFINEDDOCUMENT: WMDM_FORMATCODE = 47744
WMDM_FORMATCODE_ABSTRACTDOCUMENT: WMDM_FORMATCODE = 47745
WMDM_FORMATCODE_XMLDOCUMENT: WMDM_FORMATCODE = 47746
WMDM_FORMATCODE_MICROSOFTWORDDOCUMENT: WMDM_FORMATCODE = 47747
WMDM_FORMATCODE_MHTCOMPILEDHTMLDOCUMENT: WMDM_FORMATCODE = 47748
WMDM_FORMATCODE_MICROSOFTEXCELSPREADSHEET: WMDM_FORMATCODE = 47749
WMDM_FORMATCODE_MICROSOFTPOWERPOINTDOCUMENT: WMDM_FORMATCODE = 47750
WMDM_FORMATCODE_UNDEFINEDMESSAGE: WMDM_FORMATCODE = 47872
WMDM_FORMATCODE_ABSTRACTMESSAGE: WMDM_FORMATCODE = 47873
WMDM_FORMATCODE_UNDEFINEDCONTACT: WMDM_FORMATCODE = 48000
WMDM_FORMATCODE_ABSTRACTCONTACT: WMDM_FORMATCODE = 48001
WMDM_FORMATCODE_VCARD2: WMDM_FORMATCODE = 48002
WMDM_FORMATCODE_VCARD3: WMDM_FORMATCODE = 48003
WMDM_FORMATCODE_UNDEFINEDCALENDARITEM: WMDM_FORMATCODE = 48640
WMDM_FORMATCODE_ABSTRACTCALENDARITEM: WMDM_FORMATCODE = 48641
WMDM_FORMATCODE_VCALENDAR1: WMDM_FORMATCODE = 48642
WMDM_FORMATCODE_VCALENDAR2: WMDM_FORMATCODE = 48643
WMDM_FORMATCODE_UNDEFINEDWINDOWSEXECUTABLE: WMDM_FORMATCODE = 48768
WMDM_FORMATCODE_M4A: WMDM_FORMATCODE = 1297101889
WMDM_FORMATCODE_3GPA: WMDM_FORMATCODE = 860311617
WMDM_FORMATCODE_3G2A: WMDM_FORMATCODE = 860303937
WMDM_FORMATCODE_SECTION: WMDM_FORMATCODE = 48770
class WMDM_FORMAT_CAPABILITY(EasyCastStructure):
    nPropConfig: UInt32
    pConfigs: POINTER(Windows.Win32.Media.DeviceManager.WMDM_PROP_CONFIG_head)
class WMDM_PROP_CONFIG(EasyCastStructure):
    nPreference: UInt32
    nPropDesc: UInt32
    pPropDesc: POINTER(Windows.Win32.Media.DeviceManager.WMDM_PROP_DESC_head)
class WMDM_PROP_DESC(EasyCastStructure):
    pwszPropName: Windows.Win32.Foundation.PWSTR
    ValidValuesForm: Windows.Win32.Media.DeviceManager.WMDM_ENUM_PROP_VALID_VALUES_FORM
    ValidValues: _ValidValues_e__Union
    class _ValidValues_e__Union(EasyCastUnion):
        ValidValuesRange: Windows.Win32.Media.DeviceManager.WMDM_PROP_VALUES_RANGE
        EnumeratedValidValues: Windows.Win32.Media.DeviceManager.WMDM_PROP_VALUES_ENUM
class WMDM_PROP_VALUES_ENUM(EasyCastStructure):
    cEnumValues: UInt32
    pValues: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
class WMDM_PROP_VALUES_RANGE(EasyCastStructure):
    rangeMin: Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
    rangeMax: Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
    rangeStep: Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
WMDM_SESSION_TYPE = Int32
WMDM_SESSION_NONE: WMDM_SESSION_TYPE = 0
WMDM_SESSION_TRANSFER_TO_DEVICE: WMDM_SESSION_TYPE = 1
WMDM_SESSION_TRANSFER_FROM_DEVICE: WMDM_SESSION_TYPE = 16
WMDM_SESSION_DELETE: WMDM_SESSION_TYPE = 256
WMDM_SESSION_CUSTOM: WMDM_SESSION_TYPE = 4096
WMDM_STORAGE_ENUM_MODE = Int32
ENUM_MODE_RAW: WMDM_STORAGE_ENUM_MODE = 0
ENUM_MODE_USE_DEVICE_PREF: WMDM_STORAGE_ENUM_MODE = 1
ENUM_MODE_METADATA_VIEWS: WMDM_STORAGE_ENUM_MODE = 2
WMDM_TAG_DATATYPE = Int32
WMDM_TYPE_DWORD: WMDM_TAG_DATATYPE = 0
WMDM_TYPE_STRING: WMDM_TAG_DATATYPE = 1
WMDM_TYPE_BINARY: WMDM_TAG_DATATYPE = 2
WMDM_TYPE_BOOL: WMDM_TAG_DATATYPE = 3
WMDM_TYPE_QWORD: WMDM_TAG_DATATYPE = 4
WMDM_TYPE_WORD: WMDM_TAG_DATATYPE = 5
WMDM_TYPE_GUID: WMDM_TAG_DATATYPE = 6
WMDM_TYPE_DATE: WMDM_TAG_DATATYPE = 7
class WMFILECAPABILITIES(EasyCastStructure):
    pwszMimeType: Windows.Win32.Foundation.PWSTR
    dwReserved: UInt32
make_head(_module, 'IComponentAuthenticate')
make_head(_module, 'IMDSPDevice')
make_head(_module, 'IMDSPDevice2')
make_head(_module, 'IMDSPDevice3')
make_head(_module, 'IMDSPDeviceControl')
make_head(_module, 'IMDSPDirectTransfer')
make_head(_module, 'IMDSPEnumDevice')
make_head(_module, 'IMDSPEnumStorage')
make_head(_module, 'IMDSPObject')
make_head(_module, 'IMDSPObject2')
make_head(_module, 'IMDSPObjectInfo')
make_head(_module, 'IMDSPRevoked')
make_head(_module, 'IMDSPStorage')
make_head(_module, 'IMDSPStorage2')
make_head(_module, 'IMDSPStorage3')
make_head(_module, 'IMDSPStorage4')
make_head(_module, 'IMDSPStorageGlobals')
make_head(_module, 'IMDServiceProvider')
make_head(_module, 'IMDServiceProvider2')
make_head(_module, 'IMDServiceProvider3')
make_head(_module, 'ISCPSecureAuthenticate')
make_head(_module, 'ISCPSecureAuthenticate2')
make_head(_module, 'ISCPSecureExchange')
make_head(_module, 'ISCPSecureExchange2')
make_head(_module, 'ISCPSecureExchange3')
make_head(_module, 'ISCPSecureQuery')
make_head(_module, 'ISCPSecureQuery2')
make_head(_module, 'ISCPSecureQuery3')
make_head(_module, 'ISCPSession')
make_head(_module, 'IWMDMDevice')
make_head(_module, 'IWMDMDevice2')
make_head(_module, 'IWMDMDevice3')
make_head(_module, 'IWMDMDeviceControl')
make_head(_module, 'IWMDMDeviceSession')
make_head(_module, 'IWMDMEnumDevice')
make_head(_module, 'IWMDMEnumStorage')
make_head(_module, 'IWMDMLogger')
make_head(_module, 'IWMDMMetaData')
make_head(_module, 'IWMDMNotification')
make_head(_module, 'IWMDMObjectInfo')
make_head(_module, 'IWMDMOperation')
make_head(_module, 'IWMDMOperation2')
make_head(_module, 'IWMDMOperation3')
make_head(_module, 'IWMDMProgress')
make_head(_module, 'IWMDMProgress2')
make_head(_module, 'IWMDMProgress3')
make_head(_module, 'IWMDMRevoked')
make_head(_module, 'IWMDMStorage')
make_head(_module, 'IWMDMStorage2')
make_head(_module, 'IWMDMStorage3')
make_head(_module, 'IWMDMStorage4')
make_head(_module, 'IWMDMStorageControl')
make_head(_module, 'IWMDMStorageControl2')
make_head(_module, 'IWMDMStorageControl3')
make_head(_module, 'IWMDMStorageGlobals')
make_head(_module, 'IWMDeviceManager')
make_head(_module, 'IWMDeviceManager2')
make_head(_module, 'IWMDeviceManager3')
make_head(_module, 'MACINFO')
make_head(_module, 'MTP_COMMAND_DATA_IN')
make_head(_module, 'MTP_COMMAND_DATA_OUT')
make_head(_module, 'OPAQUECOMMAND')
make_head(_module, 'WMDMDATETIME')
make_head(_module, 'WMDMDetermineMaxPropStringLen')
make_head(_module, 'WMDMID')
make_head(_module, 'WMDMMetadataView')
make_head(_module, 'WMDMRIGHTS')
make_head(_module, 'WMDM_FORMAT_CAPABILITY')
make_head(_module, 'WMDM_PROP_CONFIG')
make_head(_module, 'WMDM_PROP_DESC')
make_head(_module, 'WMDM_PROP_VALUES_ENUM')
make_head(_module, 'WMDM_PROP_VALUES_RANGE')
make_head(_module, 'WMFILECAPABILITIES')