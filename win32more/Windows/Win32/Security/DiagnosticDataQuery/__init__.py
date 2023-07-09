from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.DiagnosticDataQuery
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('DiagnosticDataQuery.dll')
def DdqCreateSession(accessLevel: win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel, hSession: POINTER(win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqCloseSession(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetSessionAccessLevel(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, accessLevel: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticDataAccessLevelAllowed(accessLevel: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DdqAccessLevel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordStats(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, searchCriteria: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA_head), recordCount: POINTER(UInt32), minRowId: POINTER(Int64), maxRowId: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordPayload(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, rowId: Int64, payload: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTags(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, locale: win32more.Windows.Win32.Foundation.PWSTR, hTagDescription: POINTER(win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordLocaleTags(hTagDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTagAtIndex(hTagDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION, index: UInt32, tagDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordLocaleTagCount(hTagDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_TAG_DESCRIPTION, tagDescriptionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducers(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, hProducerDescription: POINTER(win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordProducers(hProducerDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerAtIndex(hProducerDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION, index: UInt32, producerDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerCount(hProducerDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_PRODUCER_DESCRIPTION, producerDescriptionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordProducerCategories(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerName: win32more.Windows.Win32.Foundation.PWSTR, hCategoryDescription: POINTER(win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordProducerCategories(hCategoryDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCategoryAtIndex(hCategoryDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION, index: UInt32, categoryDescription: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCategoryCount(hCategoryDescription: win32more.Windows.Win32.Security.HDIAGNOSTIC_EVENT_CATEGORY_DESCRIPTION, categoryDescriptionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqIsDiagnosticRecordSampledIn(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, providerGroup: POINTER(Guid), providerId: POINTER(Guid), providerName: win32more.Windows.Win32.Foundation.PWSTR, eventId: POINTER(UInt32), eventName: win32more.Windows.Win32.Foundation.PWSTR, eventVersion: POINTER(UInt32), eventKeywords: POINTER(UInt64), isSampledIn: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordPage(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, searchCriteria: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_SEARCH_CRITERIA_head), offset: UInt32, pageRecordCount: UInt32, baseRowId: Int64, hRecord: POINTER(win32more.Windows.Win32.Security.HDIAGNOSTIC_RECORD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticRecordPage(hRecord: win32more.Windows.Win32.Security.HDIAGNOSTIC_RECORD) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordAtIndex(hRecord: win32more.Windows.Win32.Security.HDIAGNOSTIC_RECORD, index: UInt32, record: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_RECORD_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordCount(hRecord: win32more.Windows.Win32.Security.HDIAGNOSTIC_RECORD, recordCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportStoreReportCount(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, reportCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqCancelDiagnosticRecordOperation(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReport(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, hReport: POINTER(win32more.Windows.Win32.Security.HDIAGNOSTIC_REPORT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqFreeDiagnosticReport(hReport: win32more.Windows.Win32.Security.HDIAGNOSTIC_REPORT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportAtIndex(hReport: win32more.Windows.Win32.Security.HDIAGNOSTIC_REPORT, index: UInt32, report: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_DATA_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticReportCount(hReport: win32more.Windows.Win32.Security.HDIAGNOSTIC_REPORT, reportCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqExtractDiagnosticReport(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, reportStoreType: UInt32, reportKey: win32more.Windows.Win32.Foundation.PWSTR, destinationPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordTagDistribution(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, tagStats: POINTER(POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TAG_STATS_head)), statCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordBinaryDistribution(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, topNBinaries: UInt32, binaryStats: POINTER(POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_BINARY_STATS_head)), statCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetDiagnosticRecordSummary(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), producerNameCount: UInt32, generalStats: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_GENERAL_STATS_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqSetTranscriptConfiguration(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, desiredConfig: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DiagnosticDataQuery.dll')
def DdqGetTranscriptConfiguration(hSession: win32more.Windows.Win32.Security.HDIAGNOSTIC_DATA_QUERY_SESSION, currentConfig: POINTER(win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DIAGNOSTIC_DATA_EVENT_BINARY_STATS(EasyCastStructure):
    moduleName: win32more.Windows.Win32.Foundation.PWSTR
    friendlyModuleName: win32more.Windows.Win32.Foundation.PWSTR
    eventCount: UInt32
    uploadSizeBytes: UInt64
class DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION(EasyCastStructure):
    id: Int32
    name: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION(EasyCastStructure):
    name: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION(EasyCastStructure):
    privacyTag: Int32
    name: win32more.Windows.Win32.Foundation.PWSTR
    description: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_EVENT_TAG_STATS(EasyCastStructure):
    privacyTag: Int32
    eventCount: UInt32
class DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION(EasyCastStructure):
    hoursOfHistoryToKeep: UInt32
    maxStoreMegabytes: UInt32
    requestedMaxStoreMegabytes: UInt32
class DIAGNOSTIC_DATA_GENERAL_STATS(EasyCastStructure):
    optInLevel: UInt32
    transcriptSizeBytes: UInt64
    oldestEventTimestamp: UInt64
    totalEventCountLast24Hours: UInt32
    averageDailyEvents: Single
class DIAGNOSTIC_DATA_RECORD(EasyCastStructure):
    rowId: Int64
    timestamp: UInt64
    eventKeywords: UInt64
    fullEventName: win32more.Windows.Win32.Foundation.PWSTR
    providerGroupGuid: win32more.Windows.Win32.Foundation.PWSTR
    producerName: win32more.Windows.Win32.Foundation.PWSTR
    privacyTags: POINTER(Int32)
    privacyTagCount: UInt32
    categoryIds: POINTER(Int32)
    categoryIdCount: UInt32
    isCoreData: win32more.Windows.Win32.Foundation.BOOL
    extra1: win32more.Windows.Win32.Foundation.PWSTR
    extra2: win32more.Windows.Win32.Foundation.PWSTR
    extra3: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_DATA_SEARCH_CRITERIA(EasyCastStructure):
    producerNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    producerNameCount: UInt32
    textToMatch: win32more.Windows.Win32.Foundation.PWSTR
    categoryIds: POINTER(Int32)
    categoryIdCount: UInt32
    privacyTags: POINTER(Int32)
    privacyTagCount: UInt32
    coreDataOnly: win32more.Windows.Win32.Foundation.BOOL
class DIAGNOSTIC_REPORT_DATA(EasyCastStructure):
    signature: win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_SIGNATURE
    bucketId: Guid
    reportId: Guid
    creationTime: win32more.Windows.Win32.Foundation.FILETIME
    sizeInBytes: UInt64
    cabId: win32more.Windows.Win32.Foundation.PWSTR
    reportStatus: UInt32
    reportIntegratorId: Guid
    fileNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    fileCount: UInt32
    friendlyEventName: win32more.Windows.Win32.Foundation.PWSTR
    applicationName: win32more.Windows.Win32.Foundation.PWSTR
    applicationPath: win32more.Windows.Win32.Foundation.PWSTR
    description: win32more.Windows.Win32.Foundation.PWSTR
    bucketIdString: win32more.Windows.Win32.Foundation.PWSTR
    legacyBucketId: UInt64
    reportKey: win32more.Windows.Win32.Foundation.PWSTR
class DIAGNOSTIC_REPORT_PARAMETER(EasyCastStructure):
    name: Char * 129
    value: Char * 260
class DIAGNOSTIC_REPORT_SIGNATURE(EasyCastStructure):
    eventName: Char * 65
    parameters: win32more.Windows.Win32.Security.DiagnosticDataQuery.DIAGNOSTIC_REPORT_PARAMETER * 10
DdqAccessLevel = Int32
DdqAccessLevel_NoData: DdqAccessLevel = 0
DdqAccessLevel_CurrentUserData: DdqAccessLevel = 1
DdqAccessLevel_AllUserData: DdqAccessLevel = 2
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_BINARY_STATS')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_CATEGORY_DESCRIPTION')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_PRODUCER_DESCRIPTION')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_TAG_DESCRIPTION')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_TAG_STATS')
make_head(_module, 'DIAGNOSTIC_DATA_EVENT_TRANSCRIPT_CONFIGURATION')
make_head(_module, 'DIAGNOSTIC_DATA_GENERAL_STATS')
make_head(_module, 'DIAGNOSTIC_DATA_RECORD')
make_head(_module, 'DIAGNOSTIC_DATA_SEARCH_CRITERIA')
make_head(_module, 'DIAGNOSTIC_REPORT_DATA')
make_head(_module, 'DIAGNOSTIC_REPORT_PARAMETER')
make_head(_module, 'DIAGNOSTIC_REPORT_SIGNATURE')