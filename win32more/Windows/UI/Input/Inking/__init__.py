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
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Inking
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
HandwritingLineHeight = Int32
HandwritingLineHeight_Small: HandwritingLineHeight = 0
HandwritingLineHeight_Medium: HandwritingLineHeight = 1
HandwritingLineHeight_Large: HandwritingLineHeight = 2
class IInkDrawingAttributes(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes'
    _iid_ = Guid('{97a2176c-6774-48ad-84f0-48f5a9be74f9}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_PenTip(self) -> win32more.Windows.UI.Input.Inking.PenTipShape: ...
    @winrt_commethod(9)
    def put_PenTip(self, value: win32more.Windows.UI.Input.Inking.PenTipShape) -> Void: ...
    @winrt_commethod(10)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def put_Size(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(12)
    def get_IgnorePressure(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IgnorePressure(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_FitToCurve(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_FitToCurve(self, value: Boolean) -> Void: ...
    Color = property(get_Color, put_Color)
    PenTip = property(get_PenTip, put_PenTip)
    Size = property(get_Size, put_Size)
    IgnorePressure = property(get_IgnorePressure, put_IgnorePressure)
    FitToCurve = property(get_FitToCurve, put_FitToCurve)
class IInkDrawingAttributes2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes2'
    _iid_ = Guid('{7cab6508-8ec4-42fd-a5a5-e4b7d1d5316d}')
    @winrt_commethod(6)
    def get_PenTipTransform(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(7)
    def put_PenTipTransform(self, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(8)
    def get_DrawAsHighlighter(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_DrawAsHighlighter(self, value: Boolean) -> Void: ...
    PenTipTransform = property(get_PenTipTransform, put_PenTipTransform)
    DrawAsHighlighter = property(get_DrawAsHighlighter, put_DrawAsHighlighter)
class IInkDrawingAttributes3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes3'
    _iid_ = Guid('{72020002-7d5b-4690-8af4-e664cbe2b74f}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributesKind: ...
    @winrt_commethod(7)
    def get_PencilProperties(self) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributesPencilProperties: ...
    Kind = property(get_Kind, None)
    PencilProperties = property(get_PencilProperties, None)
class IInkDrawingAttributes4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes4'
    _iid_ = Guid('{ef65dc25-9f19-456d-91a3-bc3a3d91c5fb}')
    @winrt_commethod(6)
    def get_IgnoreTilt(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IgnoreTilt(self, value: Boolean) -> Void: ...
    IgnoreTilt = property(get_IgnoreTilt, put_IgnoreTilt)
class IInkDrawingAttributes5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes5'
    _iid_ = Guid('{d11aa0bb-0775-4852-ae64-41143a7ae6c9}')
    @winrt_commethod(6)
    def get_ModelerAttributes(self) -> win32more.Windows.UI.Input.Inking.InkModelerAttributes: ...
    ModelerAttributes = property(get_ModelerAttributes, None)
class IInkDrawingAttributesPencilProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties'
    _iid_ = Guid('{4f2534cb-2d86-41bb-b0e8-e4c2a0253c52}')
    @winrt_commethod(6)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(7)
    def put_Opacity(self, value: Double) -> Void: ...
    Opacity = property(get_Opacity, put_Opacity)
class IInkDrawingAttributesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributesStatics'
    _iid_ = Guid('{f731e03f-1a65-4862-96cb-6e1665e17f6d}')
    @winrt_commethod(6)
    def CreateForPencil(self) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
class IInkInputConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkInputConfiguration'
    _iid_ = Guid('{93a68dc4-0b7b-49d7-b34f-9901e524dcf2}')
    @winrt_commethod(6)
    def get_IsPrimaryBarrelButtonInputEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPrimaryBarrelButtonInputEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsEraserInputEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsEraserInputEnabled(self, value: Boolean) -> Void: ...
    IsPrimaryBarrelButtonInputEnabled = property(get_IsPrimaryBarrelButtonInputEnabled, put_IsPrimaryBarrelButtonInputEnabled)
    IsEraserInputEnabled = property(get_IsEraserInputEnabled, put_IsEraserInputEnabled)
class IInkInputConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkInputConfiguration2'
    _iid_ = Guid('{6ac2272e-81b4-5cc4-a36d-d057c387dfda}')
    @winrt_commethod(6)
    def get_IsPenHapticFeedbackEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPenHapticFeedbackEnabled(self, value: Boolean) -> Void: ...
    IsPenHapticFeedbackEnabled = property(get_IsPenHapticFeedbackEnabled, put_IsPenHapticFeedbackEnabled)
class IInkInputProcessingConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkInputProcessingConfiguration'
    _iid_ = Guid('{2778d85e-33ca-4b06-a6d3-ac3945116d37}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Input.Inking.InkInputProcessingMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.UI.Input.Inking.InkInputProcessingMode) -> Void: ...
    @winrt_commethod(8)
    def get_RightDragAction(self) -> win32more.Windows.UI.Input.Inking.InkInputRightDragAction: ...
    @winrt_commethod(9)
    def put_RightDragAction(self, value: win32more.Windows.UI.Input.Inking.InkInputRightDragAction) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    RightDragAction = property(get_RightDragAction, put_RightDragAction)
class IInkManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkManager'
    _iid_ = Guid('{4744737d-671b-4163-9c95-4e8d7a035fe1}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Input.Inking.InkManipulationMode: ...
    @winrt_commethod(7)
    def put_Mode(self, value: win32more.Windows.UI.Input.Inking.InkManipulationMode) -> Void: ...
    @winrt_commethod(8)
    def ProcessPointerDown(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(9)
    def ProcessPointerUpdate(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def ProcessPointerUp(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def SetDefaultDrawingAttributes(self, drawingAttributes: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_commethod(12)
    def RecognizeAsync2(self, recognitionTarget: win32more.Windows.UI.Input.Inking.InkRecognitionTarget) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    Mode = property(get_Mode, put_Mode)
class IInkModelerAttributes(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkModelerAttributes'
    _iid_ = Guid('{bad31f27-0cd9-4bfd-b6f3-9e03ba8d7454}')
    @winrt_commethod(6)
    def get_PredictionTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_PredictionTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ScalingFactor(self) -> Single: ...
    @winrt_commethod(9)
    def put_ScalingFactor(self, value: Single) -> Void: ...
    PredictionTime = property(get_PredictionTime, put_PredictionTime)
    ScalingFactor = property(get_ScalingFactor, put_ScalingFactor)
class IInkModelerAttributes2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkModelerAttributes2'
    _iid_ = Guid('{86d1d09a-4ef8-5e25-b7bc-b65424f16bb3}')
    @winrt_commethod(6)
    def get_UseVelocityBasedPressure(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_UseVelocityBasedPressure(self, value: Boolean) -> Void: ...
    UseVelocityBasedPressure = property(get_UseVelocityBasedPressure, put_UseVelocityBasedPressure)
class IInkPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPoint'
    _iid_ = Guid('{9f87272b-858c-46a5-9b41-d195970459fd}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Pressure(self) -> Single: ...
    Position = property(get_Position, None)
    Pressure = property(get_Pressure, None)
class IInkPoint2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPoint2'
    _iid_ = Guid('{fba9c3f7-ae56-4d5c-bd2f-0ac45f5e4af9}')
    @winrt_commethod(6)
    def get_TiltX(self) -> Single: ...
    @winrt_commethod(7)
    def get_TiltY(self) -> Single: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> UInt64: ...
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Timestamp = property(get_Timestamp, None)
class IInkPointFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPointFactory'
    _iid_ = Guid('{29e5d51c-c98f-405d-9f3b-e53e31068d4d}')
    @winrt_commethod(6)
    def CreateInkPoint(self, position: win32more.Windows.Foundation.Point, pressure: Single) -> win32more.Windows.UI.Input.Inking.InkPoint: ...
class IInkPointFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPointFactory2'
    _iid_ = Guid('{e0145e85-daff-45f2-ad69-050d8256a209}')
    @winrt_commethod(6)
    def CreateInkPointWithTiltAndTimestamp(self, position: win32more.Windows.Foundation.Point, pressure: Single, tiltX: Single, tiltY: Single, timestamp: UInt64) -> win32more.Windows.UI.Input.Inking.InkPoint: ...
class IInkPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenter'
    _iid_ = Guid('{a69b70e2-887b-458f-b173-4fe4438930a3}')
    @winrt_commethod(6)
    def get_IsInputEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsInputEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_InputDeviceTypes(self) -> win32more.Windows.UI.Core.CoreInputDeviceTypes: ...
    @winrt_commethod(9)
    def put_InputDeviceTypes(self, value: win32more.Windows.UI.Core.CoreInputDeviceTypes) -> Void: ...
    @winrt_commethod(10)
    def get_UnprocessedInput(self) -> win32more.Windows.UI.Input.Inking.InkUnprocessedInput: ...
    @winrt_commethod(11)
    def get_StrokeInput(self) -> win32more.Windows.UI.Input.Inking.InkStrokeInput: ...
    @winrt_commethod(12)
    def get_InputProcessingConfiguration(self) -> win32more.Windows.UI.Input.Inking.InkInputProcessingConfiguration: ...
    @winrt_commethod(13)
    def get_StrokeContainer(self) -> win32more.Windows.UI.Input.Inking.InkStrokeContainer: ...
    @winrt_commethod(14)
    def put_StrokeContainer(self, value: win32more.Windows.UI.Input.Inking.InkStrokeContainer) -> Void: ...
    @winrt_commethod(15)
    def CopyDefaultDrawingAttributes(self) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_commethod(16)
    def UpdateDefaultDrawingAttributes(self, value: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_commethod(17)
    def ActivateCustomDrying(self) -> win32more.Windows.UI.Input.Inking.InkSynchronizer: ...
    @winrt_commethod(18)
    def SetPredefinedConfiguration(self, value: win32more.Windows.UI.Input.Inking.InkPresenterPredefinedConfiguration) -> Void: ...
    @winrt_commethod(19)
    def add_StrokesCollected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkPresenter, win32more.Windows.UI.Input.Inking.InkStrokesCollectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_StrokesCollected(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_StrokesErased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkPresenter, win32more.Windows.UI.Input.Inking.InkStrokesErasedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_StrokesErased(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    InputDeviceTypes = property(get_InputDeviceTypes, put_InputDeviceTypes)
    UnprocessedInput = property(get_UnprocessedInput, None)
    StrokeInput = property(get_StrokeInput, None)
    InputProcessingConfiguration = property(get_InputProcessingConfiguration, None)
    StrokeContainer = property(get_StrokeContainer, put_StrokeContainer)
class IInkPresenter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenter2'
    _iid_ = Guid('{cf53e612-9a34-11e6-9f33-a24fc0d9649c}')
    @winrt_commethod(6)
    def get_HighContrastAdjustment(self) -> win32more.Windows.UI.Input.Inking.InkHighContrastAdjustment: ...
    @winrt_commethod(7)
    def put_HighContrastAdjustment(self, value: win32more.Windows.UI.Input.Inking.InkHighContrastAdjustment) -> Void: ...
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
class IInkPresenter3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenter3'
    _iid_ = Guid('{51e1ce89-d37d-4a90-83fc-7f5e9dfbf217}')
    @winrt_commethod(6)
    def get_InputConfiguration(self) -> win32more.Windows.UI.Input.Inking.InkInputConfiguration: ...
    InputConfiguration = property(get_InputConfiguration, None)
class IInkPresenterProtractor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterProtractor'
    _iid_ = Guid('{7de3f2aa-ef6c-4e91-a73b-5b70d56fbd17}')
    @winrt_commethod(6)
    def get_AreTickMarksVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreTickMarksVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AreRaysVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AreRaysVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsCenterMarkerVisible(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsCenterMarkerVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsAngleReadoutVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsAngleReadoutVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_IsResizable(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsResizable(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Radius(self) -> Double: ...
    @winrt_commethod(17)
    def put_Radius(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_AccentColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(19)
    def put_AccentColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    AreRaysVisible = property(get_AreRaysVisible, put_AreRaysVisible)
    IsCenterMarkerVisible = property(get_IsCenterMarkerVisible, put_IsCenterMarkerVisible)
    IsAngleReadoutVisible = property(get_IsAngleReadoutVisible, put_IsAngleReadoutVisible)
    IsResizable = property(get_IsResizable, put_IsResizable)
    Radius = property(get_Radius, put_Radius)
    AccentColor = property(get_AccentColor, put_AccentColor)
class IInkPresenterProtractorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterProtractorFactory'
    _iid_ = Guid('{320103c9-68fa-47e9-8127-8370711fc46c}')
    @winrt_commethod(6)
    def Create(self, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.InkPresenterProtractor: ...
class IInkPresenterRuler(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterRuler'
    _iid_ = Guid('{6cda7d5a-dec7-4dd7-877a-2133f183d48a}')
    @winrt_commethod(6)
    def get_Length(self) -> Double: ...
    @winrt_commethod(7)
    def put_Length(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Width(self) -> Double: ...
    @winrt_commethod(9)
    def put_Width(self, value: Double) -> Void: ...
    Length = property(get_Length, put_Length)
    Width = property(get_Width, put_Width)
class IInkPresenterRuler2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterRuler2'
    _iid_ = Guid('{45130dc1-bc61-44d4-a423-54712ae671c4}')
    @winrt_commethod(6)
    def get_AreTickMarksVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreTickMarksVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsCompassVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsCompassVisible(self, value: Boolean) -> Void: ...
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    IsCompassVisible = property(get_IsCompassVisible, put_IsCompassVisible)
class IInkPresenterRulerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterRulerFactory'
    _iid_ = Guid('{34361beb-9001-4a4b-a690-69dbaf63e501}')
    @winrt_commethod(6)
    def Create(self, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.InkPresenterRuler: ...
class IInkPresenterStencil(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterStencil'
    _iid_ = Guid('{30d12d6d-3e06-4d02-b116-277fb5d8addc}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.UI.Input.Inking.InkPresenterStencilKind: ...
    @winrt_commethod(7)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(10)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(11)
    def get_ForegroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(12)
    def put_ForegroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(13)
    def get_Transform(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(14)
    def put_Transform(self, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    Kind = property(get_Kind, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    Transform = property(get_Transform, put_Transform)
class IInkRecognitionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkRecognitionResult'
    _iid_ = Guid('{36461a94-5068-40ef-8a05-2c2fb60908a2}')
    @winrt_commethod(6)
    def get_BoundingRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def GetTextCandidates(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def GetStrokes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    BoundingRect = property(get_BoundingRect, None)
class IInkRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkRecognizer'
    _iid_ = Guid('{077ccea3-904d-442a-b151-aaca3631c43b}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class IInkRecognizerContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkRecognizerContainer'
    _iid_ = Guid('{a74d9a31-8047-4698-a912-f82a5085012f}')
    @winrt_commethod(6)
    def SetDefaultRecognizer(self, recognizer: win32more.Windows.UI.Input.Inking.InkRecognizer) -> Void: ...
    @winrt_commethod(7)
    def RecognizeAsync(self, strokeCollection: win32more.Windows.UI.Input.Inking.InkStrokeContainer, recognitionTarget: win32more.Windows.UI.Input.Inking.InkRecognitionTarget) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_commethod(8)
    def GetRecognizers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognizer]: ...
class IInkStroke(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke'
    _iid_ = Guid('{15144d60-cce3-4fcf-9d52-11518ab6afd4}')
    @winrt_commethod(6)
    def get_DrawingAttributes(self) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_commethod(7)
    def put_DrawingAttributes(self, value: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_commethod(8)
    def get_BoundingRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def get_Selected(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Selected(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_Recognized(self) -> Boolean: ...
    @winrt_commethod(12)
    def GetRenderingSegments(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStrokeRenderingSegment]: ...
    @winrt_commethod(13)
    def Clone(self) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    DrawingAttributes = property(get_DrawingAttributes, put_DrawingAttributes)
    BoundingRect = property(get_BoundingRect, None)
    Selected = property(get_Selected, put_Selected)
    Recognized = property(get_Recognized, None)
class IInkStroke2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke2'
    _iid_ = Guid('{5db9e4f4-bafa-4de1-89d3-201b1ed7d89b}')
    @winrt_commethod(6)
    def get_PointTransform(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(7)
    def put_PointTransform(self, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(8)
    def GetInkPoints(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkPoint]: ...
    PointTransform = property(get_PointTransform, put_PointTransform)
class IInkStroke3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke3'
    _iid_ = Guid('{4a807374-9499-411d-a1c4-68855d03d65f}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_StrokeStartedTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(8)
    def put_StrokeStartedTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(9)
    def get_StrokeDuration(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(10)
    def put_StrokeDuration(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    Id = property(get_Id, None)
    StrokeStartedTime = property(get_StrokeStartedTime, put_StrokeStartedTime)
    StrokeDuration = property(get_StrokeDuration, put_StrokeDuration)
class IInkStroke4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke4'
    _iid_ = Guid('{cd5b62e5-b6e9-5b91-a577-1921d2348690}')
    @winrt_commethod(6)
    def get_PointerId(self) -> UInt32: ...
    PointerId = property(get_PointerId, None)
class IInkStrokeBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeBuilder'
    _iid_ = Guid('{82bbd1dc-1c63-41dc-9e07-4b4a70ced801}')
    @winrt_commethod(6)
    def BeginStroke(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(7)
    def AppendToStroke(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(8)
    def EndStroke(self, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_commethod(9)
    def CreateStroke(self, points: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_commethod(10)
    def SetDefaultDrawingAttributes(self, drawingAttributes: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
class IInkStrokeBuilder2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeBuilder2'
    _iid_ = Guid('{bd82bc27-731f-4cbc-bbbf-6d468044f1e5}')
    @winrt_commethod(6)
    def CreateStrokeFromInkPoints(self, inkPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkPoint], transform: win32more.Windows.Foundation.Numerics.Matrix3x2) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
class IInkStrokeBuilder3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeBuilder3'
    _iid_ = Guid('{b2c71fcd-5472-46b1-a81d-c37a3d169441}')
    @winrt_commethod(6)
    def CreateStrokeFromInkPoints(self, inkPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkPoint], transform: win32more.Windows.Foundation.Numerics.Matrix3x2, strokeStartedTime: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime], strokeDuration: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
class IInkStrokeContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeContainer'
    _iid_ = Guid('{22accbc6-faa9-4f14-b68c-f6cee670ae16}')
    @winrt_commethod(6)
    def get_BoundingRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def AddStroke(self, stroke: win32more.Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_commethod(8)
    def DeleteSelected(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def MoveSelected(self, translation: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def SelectWithPolyLine(self, polyline: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def SelectWithLine(self, from_: win32more.Windows.Foundation.Point, to: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(12)
    def CopySelectedToClipboard(self) -> Void: ...
    @winrt_commethod(13)
    def PasteFromClipboard(self, position: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(14)
    def CanPasteFromClipboard(self) -> Boolean: ...
    @winrt_commethod(15)
    def LoadAsync(self, inputStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncActionWithProgress[UInt64]: ...
    @winrt_commethod(16)
    def SaveAsync(self, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_commethod(17)
    def UpdateRecognitionResults(self, recognitionResults: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]) -> Void: ...
    @winrt_commethod(18)
    def GetStrokes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_commethod(19)
    def GetRecognitionResults(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]: ...
    BoundingRect = property(get_BoundingRect, None)
class IInkStrokeContainer2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeContainer2'
    _iid_ = Guid('{8901d364-da36-4bcf-9e5c-d195825995b4}')
    @winrt_commethod(6)
    def AddStrokes(self, strokes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_commethod(7)
    def Clear(self) -> Void: ...
class IInkStrokeContainer3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeContainer3'
    _iid_ = Guid('{3d07bea5-baea-4c82-a719-7b83da1067d2}')
    @winrt_commethod(6)
    def SaveWithFormatAsync(self, outputStream: win32more.Windows.Storage.Streams.IOutputStream, inkPersistenceFormat: win32more.Windows.UI.Input.Inking.InkPersistenceFormat) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_commethod(7)
    def GetStrokeById(self, id: UInt32) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
class IInkStrokeInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeInput'
    _iid_ = Guid('{cf2ffe7b-5e10-43c6-a080-88f26e1dc67d}')
    @winrt_commethod(6)
    def add_StrokeStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_StrokeStarted(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_StrokeContinued(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StrokeContinued(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_StrokeEnded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StrokeEnded(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_StrokeCanceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StrokeCanceled(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_InkPresenter(self) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class IInkStrokeRenderingSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeRenderingSegment'
    _iid_ = Guid('{68510f1f-88e3-477a-a2fa-569f5f1f9bd5}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_BezierControlPoint1(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_BezierControlPoint2(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_Pressure(self) -> Single: ...
    @winrt_commethod(10)
    def get_TiltX(self) -> Single: ...
    @winrt_commethod(11)
    def get_TiltY(self) -> Single: ...
    @winrt_commethod(12)
    def get_Twist(self) -> Single: ...
    Position = property(get_Position, None)
    BezierControlPoint1 = property(get_BezierControlPoint1, None)
    BezierControlPoint2 = property(get_BezierControlPoint2, None)
    Pressure = property(get_Pressure, None)
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Twist = property(get_Twist, None)
class IInkStrokesCollectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokesCollectedEventArgs'
    _iid_ = Guid('{c4f3f229-1938-495c-b4d9-6de4b08d4811}')
    @winrt_commethod(6)
    def get_Strokes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class IInkStrokesErasedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokesErasedEventArgs'
    _iid_ = Guid('{a4216a22-1503-4ebf-8ff5-2de84584a8aa}')
    @winrt_commethod(6)
    def get_Strokes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class IInkSynchronizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkSynchronizer'
    _iid_ = Guid('{9b9ea160-ae9b-45f9-8407-4b493b163661}')
    @winrt_commethod(6)
    def BeginDry(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_commethod(7)
    def EndDry(self) -> Void: ...
class IInkUnprocessedInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkUnprocessedInput'
    _iid_ = Guid('{db4445e0-8398-4921-ac3b-ab978c5ba256}')
    @winrt_commethod(6)
    def add_PointerEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PointerEntered(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PointerHovered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PointerHovered(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PointerExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PointerExited(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PointerPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PointerPressed(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PointerMoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PointerMoved(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_PointerReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_PointerReleased(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_PointerLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_PointerLost(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def get_InkPresenter(self) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class IPenAndInkSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IPenAndInkSettings'
    _iid_ = Guid('{bc2ceb8f-0066-44a8-bb7a-b839b3deb8f5}')
    @winrt_commethod(6)
    def get_IsHandwritingDirectlyIntoTextFieldEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_PenHandedness(self) -> win32more.Windows.UI.Input.Inking.PenHandedness: ...
    @winrt_commethod(8)
    def get_HandwritingLineHeight(self) -> win32more.Windows.UI.Input.Inking.HandwritingLineHeight: ...
    @winrt_commethod(9)
    def get_FontFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_UserConsentsToHandwritingTelemetryCollection(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsTouchHandwritingEnabled(self) -> Boolean: ...
    IsHandwritingDirectlyIntoTextFieldEnabled = property(get_IsHandwritingDirectlyIntoTextFieldEnabled, None)
    PenHandedness = property(get_PenHandedness, None)
    HandwritingLineHeight = property(get_HandwritingLineHeight, None)
    FontFamilyName = property(get_FontFamilyName, None)
    UserConsentsToHandwritingTelemetryCollection = property(get_UserConsentsToHandwritingTelemetryCollection, None)
    IsTouchHandwritingEnabled = property(get_IsTouchHandwritingEnabled, None)
class IPenAndInkSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IPenAndInkSettings2'
    _iid_ = Guid('{3262da53-1f44-55e2-9929-ebf77e5481b8}')
    @winrt_commethod(6)
    def SetPenHandedness(self, value: win32more.Windows.UI.Input.Inking.PenHandedness) -> Void: ...
class IPenAndInkSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IPenAndInkSettingsStatics'
    _iid_ = Guid('{ed6dd036-5708-5c3c-96db-f2f552eab641}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.UI.Input.Inking.PenAndInkSettings: ...
class InkDrawingAttributes(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes
    _classid_ = 'Windows.UI.Input.Inking.InkDrawingAttributes'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_PenTip(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes) -> win32more.Windows.UI.Input.Inking.PenTipShape: ...
    @winrt_mixinmethod
    def put_PenTip(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes, value: win32more.Windows.UI.Input.Inking.PenTipShape) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_IgnorePressure(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnorePressure(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FitToCurve(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_FitToCurve(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PenTipTransform(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes2) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_PenTipTransform(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes2, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_DrawAsHighlighter(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes2) -> Boolean: ...
    @winrt_mixinmethod
    def put_DrawAsHighlighter(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes3) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributesKind: ...
    @winrt_mixinmethod
    def get_PencilProperties(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes3) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributesPencilProperties: ...
    @winrt_mixinmethod
    def get_IgnoreTilt(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreTilt(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ModelerAttributes(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributes5) -> win32more.Windows.UI.Input.Inking.InkModelerAttributes: ...
    @winrt_classmethod
    def CreateForPencil(cls: Windows.UI.Input.Inking.IInkDrawingAttributesStatics) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
    Color = property(get_Color, put_Color)
    PenTip = property(get_PenTip, put_PenTip)
    Size = property(get_Size, put_Size)
    IgnorePressure = property(get_IgnorePressure, put_IgnorePressure)
    FitToCurve = property(get_FitToCurve, put_FitToCurve)
    PenTipTransform = property(get_PenTipTransform, put_PenTipTransform)
    DrawAsHighlighter = property(get_DrawAsHighlighter, put_DrawAsHighlighter)
    Kind = property(get_Kind, None)
    PencilProperties = property(get_PencilProperties, None)
    IgnoreTilt = property(get_IgnoreTilt, put_IgnoreTilt)
    ModelerAttributes = property(get_ModelerAttributes, None)
InkDrawingAttributesKind = Int32
InkDrawingAttributesKind_Default: InkDrawingAttributesKind = 0
InkDrawingAttributesKind_Pencil: InkDrawingAttributesKind = 1
class InkDrawingAttributesPencilProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties
    _classid_ = 'Windows.UI.Input.Inking.InkDrawingAttributesPencilProperties'
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties, value: Double) -> Void: ...
    Opacity = property(get_Opacity, put_Opacity)
InkHighContrastAdjustment = Int32
InkHighContrastAdjustment_UseSystemColorsWhenNecessary: InkHighContrastAdjustment = 0
InkHighContrastAdjustment_UseSystemColors: InkHighContrastAdjustment = 1
InkHighContrastAdjustment_UseOriginalColors: InkHighContrastAdjustment = 2
class InkInputConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkInputConfiguration
    _classid_ = 'Windows.UI.Input.Inking.InkInputConfiguration'
    @winrt_mixinmethod
    def get_IsPrimaryBarrelButtonInputEnabled(self: win32more.Windows.UI.Input.Inking.IInkInputConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPrimaryBarrelButtonInputEnabled(self: win32more.Windows.UI.Input.Inking.IInkInputConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsEraserInputEnabled(self: win32more.Windows.UI.Input.Inking.IInkInputConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEraserInputEnabled(self: win32more.Windows.UI.Input.Inking.IInkInputConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPenHapticFeedbackEnabled(self: win32more.Windows.UI.Input.Inking.IInkInputConfiguration2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPenHapticFeedbackEnabled(self: win32more.Windows.UI.Input.Inking.IInkInputConfiguration2, value: Boolean) -> Void: ...
    IsPrimaryBarrelButtonInputEnabled = property(get_IsPrimaryBarrelButtonInputEnabled, put_IsPrimaryBarrelButtonInputEnabled)
    IsEraserInputEnabled = property(get_IsEraserInputEnabled, put_IsEraserInputEnabled)
    IsPenHapticFeedbackEnabled = property(get_IsPenHapticFeedbackEnabled, put_IsPenHapticFeedbackEnabled)
class InkInputProcessingConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkInputProcessingConfiguration
    _classid_ = 'Windows.UI.Input.Inking.InkInputProcessingConfiguration'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Input.Inking.IInkInputProcessingConfiguration) -> win32more.Windows.UI.Input.Inking.InkInputProcessingMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.UI.Input.Inking.IInkInputProcessingConfiguration, value: win32more.Windows.UI.Input.Inking.InkInputProcessingMode) -> Void: ...
    @winrt_mixinmethod
    def get_RightDragAction(self: win32more.Windows.UI.Input.Inking.IInkInputProcessingConfiguration) -> win32more.Windows.UI.Input.Inking.InkInputRightDragAction: ...
    @winrt_mixinmethod
    def put_RightDragAction(self: win32more.Windows.UI.Input.Inking.IInkInputProcessingConfiguration, value: win32more.Windows.UI.Input.Inking.InkInputRightDragAction) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    RightDragAction = property(get_RightDragAction, put_RightDragAction)
InkInputProcessingMode = Int32
InkInputProcessingMode_None: InkInputProcessingMode = 0
InkInputProcessingMode_Inking: InkInputProcessingMode = 1
InkInputProcessingMode_Erasing: InkInputProcessingMode = 2
InkInputRightDragAction = Int32
InkInputRightDragAction_LeaveUnprocessed: InkInputRightDragAction = 0
InkInputRightDragAction_AllowProcessing: InkInputRightDragAction = 1
class InkManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkManager
    _classid_ = 'Windows.UI.Input.Inking.InkManager'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkManager: ...
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Input.Inking.IInkManager) -> win32more.Windows.UI.Input.Inking.InkManipulationMode: ...
    @winrt_mixinmethod
    def put_Mode(self: win32more.Windows.UI.Input.Inking.IInkManager, value: win32more.Windows.UI.Input.Inking.InkManipulationMode) -> Void: ...
    @winrt_mixinmethod
    def ProcessPointerDown(self: win32more.Windows.UI.Input.Inking.IInkManager, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessPointerUpdate(self: win32more.Windows.UI.Input.Inking.IInkManager, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def ProcessPointerUp(self: win32more.Windows.UI.Input.Inking.IInkManager, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SetDefaultDrawingAttributes(self: win32more.Windows.UI.Input.Inking.IInkManager, drawingAttributes: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def RecognizeAsync2(self: win32more.Windows.UI.Input.Inking.IInkManager, recognitionTarget: win32more.Windows.UI.Input.Inking.InkRecognitionTarget) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def AddStroke(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, stroke: win32more.Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def DeleteSelected(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def MoveSelected(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, translation: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithPolyLine(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, polyline: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithLine(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, from_: win32more.Windows.Foundation.Point, to: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CopySelectedToClipboard(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> Void: ...
    @winrt_mixinmethod
    def PasteFromClipboard(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, position: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CanPasteFromClipboard(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> Boolean: ...
    @winrt_mixinmethod
    def LoadAsync(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, inputStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncActionWithProgress[UInt64]: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def UpdateRecognitionResults(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, recognitionResults: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]) -> Void: ...
    @winrt_mixinmethod
    def GetStrokes(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_mixinmethod
    def GetRecognitionResults(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]: ...
    @winrt_mixinmethod
    def SetDefaultRecognizer(self: win32more.Windows.UI.Input.Inking.IInkRecognizerContainer, recognizer: win32more.Windows.UI.Input.Inking.InkRecognizer) -> Void: ...
    @winrt_mixinmethod
    def RecognizeAsync(self: win32more.Windows.UI.Input.Inking.IInkRecognizerContainer, strokeCollection: win32more.Windows.UI.Input.Inking.InkStrokeContainer, recognitionTarget: win32more.Windows.UI.Input.Inking.InkRecognitionTarget) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_mixinmethod
    def GetRecognizers(self: win32more.Windows.UI.Input.Inking.IInkRecognizerContainer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognizer]: ...
    Mode = property(get_Mode, put_Mode)
    BoundingRect = property(get_BoundingRect, None)
InkManipulationMode = Int32
InkManipulationMode_Inking: InkManipulationMode = 0
InkManipulationMode_Erasing: InkManipulationMode = 1
InkManipulationMode_Selecting: InkManipulationMode = 2
class InkModelerAttributes(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkModelerAttributes
    _classid_ = 'Windows.UI.Input.Inking.InkModelerAttributes'
    @winrt_mixinmethod
    def get_PredictionTime(self: win32more.Windows.UI.Input.Inking.IInkModelerAttributes) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_PredictionTime(self: win32more.Windows.UI.Input.Inking.IInkModelerAttributes, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ScalingFactor(self: win32more.Windows.UI.Input.Inking.IInkModelerAttributes) -> Single: ...
    @winrt_mixinmethod
    def put_ScalingFactor(self: win32more.Windows.UI.Input.Inking.IInkModelerAttributes, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_UseVelocityBasedPressure(self: win32more.Windows.UI.Input.Inking.IInkModelerAttributes2) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseVelocityBasedPressure(self: win32more.Windows.UI.Input.Inking.IInkModelerAttributes2, value: Boolean) -> Void: ...
    PredictionTime = property(get_PredictionTime, put_PredictionTime)
    ScalingFactor = property(get_ScalingFactor, put_ScalingFactor)
    UseVelocityBasedPressure = property(get_UseVelocityBasedPressure, put_UseVelocityBasedPressure)
InkPersistenceFormat = Int32
InkPersistenceFormat_GifWithEmbeddedIsf: InkPersistenceFormat = 0
InkPersistenceFormat_Isf: InkPersistenceFormat = 1
class InkPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkPoint
    _classid_ = 'Windows.UI.Input.Inking.InkPoint'
    @winrt_factorymethod
    def CreateInkPoint(cls: Windows.UI.Input.Inking.IInkPointFactory, position: win32more.Windows.Foundation.Point, pressure: Single) -> win32more.Windows.UI.Input.Inking.InkPoint: ...
    @winrt_factorymethod
    def CreateInkPointWithTiltAndTimestamp(cls: Windows.UI.Input.Inking.IInkPointFactory2, position: win32more.Windows.Foundation.Point, pressure: Single, tiltX: Single, tiltY: Single, timestamp: UInt64) -> win32more.Windows.UI.Input.Inking.InkPoint: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.Inking.IInkPoint) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Windows.UI.Input.Inking.IInkPoint) -> Single: ...
    @winrt_mixinmethod
    def get_TiltX(self: win32more.Windows.UI.Input.Inking.IInkPoint2) -> Single: ...
    @winrt_mixinmethod
    def get_TiltY(self: win32more.Windows.UI.Input.Inking.IInkPoint2) -> Single: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.UI.Input.Inking.IInkPoint2) -> UInt64: ...
    Position = property(get_Position, None)
    Pressure = property(get_Pressure, None)
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Timestamp = property(get_Timestamp, None)
class InkPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkPresenter
    _classid_ = 'Windows.UI.Input.Inking.InkPresenter'
    @winrt_mixinmethod
    def get_IsInputEnabled(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInputEnabled(self: win32more.Windows.UI.Input.Inking.IInkPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDeviceTypes(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> win32more.Windows.UI.Core.CoreInputDeviceTypes: ...
    @winrt_mixinmethod
    def put_InputDeviceTypes(self: win32more.Windows.UI.Input.Inking.IInkPresenter, value: win32more.Windows.UI.Core.CoreInputDeviceTypes) -> Void: ...
    @winrt_mixinmethod
    def get_UnprocessedInput(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> win32more.Windows.UI.Input.Inking.InkUnprocessedInput: ...
    @winrt_mixinmethod
    def get_StrokeInput(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> win32more.Windows.UI.Input.Inking.InkStrokeInput: ...
    @winrt_mixinmethod
    def get_InputProcessingConfiguration(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> win32more.Windows.UI.Input.Inking.InkInputProcessingConfiguration: ...
    @winrt_mixinmethod
    def get_StrokeContainer(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> win32more.Windows.UI.Input.Inking.InkStrokeContainer: ...
    @winrt_mixinmethod
    def put_StrokeContainer(self: win32more.Windows.UI.Input.Inking.IInkPresenter, value: win32more.Windows.UI.Input.Inking.InkStrokeContainer) -> Void: ...
    @winrt_mixinmethod
    def CopyDefaultDrawingAttributes(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def UpdateDefaultDrawingAttributes(self: win32more.Windows.UI.Input.Inking.IInkPresenter, value: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def ActivateCustomDrying(self: win32more.Windows.UI.Input.Inking.IInkPresenter) -> win32more.Windows.UI.Input.Inking.InkSynchronizer: ...
    @winrt_mixinmethod
    def SetPredefinedConfiguration(self: win32more.Windows.UI.Input.Inking.IInkPresenter, value: win32more.Windows.UI.Input.Inking.InkPresenterPredefinedConfiguration) -> Void: ...
    @winrt_mixinmethod
    def add_StrokesCollected(self: win32more.Windows.UI.Input.Inking.IInkPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkPresenter, win32more.Windows.UI.Input.Inking.InkStrokesCollectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokesCollected(self: win32more.Windows.UI.Input.Inking.IInkPresenter, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokesErased(self: win32more.Windows.UI.Input.Inking.IInkPresenter, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkPresenter, win32more.Windows.UI.Input.Inking.InkStrokesErasedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokesErased(self: win32more.Windows.UI.Input.Inking.IInkPresenter, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HighContrastAdjustment(self: win32more.Windows.UI.Input.Inking.IInkPresenter2) -> win32more.Windows.UI.Input.Inking.InkHighContrastAdjustment: ...
    @winrt_mixinmethod
    def put_HighContrastAdjustment(self: win32more.Windows.UI.Input.Inking.IInkPresenter2, value: win32more.Windows.UI.Input.Inking.InkHighContrastAdjustment) -> Void: ...
    @winrt_mixinmethod
    def get_InputConfiguration(self: win32more.Windows.UI.Input.Inking.IInkPresenter3) -> win32more.Windows.UI.Input.Inking.InkInputConfiguration: ...
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    InputDeviceTypes = property(get_InputDeviceTypes, put_InputDeviceTypes)
    UnprocessedInput = property(get_UnprocessedInput, None)
    StrokeInput = property(get_StrokeInput, None)
    InputProcessingConfiguration = property(get_InputProcessingConfiguration, None)
    StrokeContainer = property(get_StrokeContainer, put_StrokeContainer)
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    InputConfiguration = property(get_InputConfiguration, None)
InkPresenterPredefinedConfiguration = Int32
InkPresenterPredefinedConfiguration_SimpleSinglePointer: InkPresenterPredefinedConfiguration = 0
InkPresenterPredefinedConfiguration_SimpleMultiplePointer: InkPresenterPredefinedConfiguration = 1
class InkPresenterProtractor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor
    _classid_ = 'Windows.UI.Input.Inking.InkPresenterProtractor'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Input.Inking.IInkPresenterProtractorFactory, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.InkPresenterProtractor: ...
    @winrt_mixinmethod
    def get_AreTickMarksVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreTickMarksVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AreRaysVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreRaysVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCenterMarkerVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCenterMarkerVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAngleReadoutVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAngleReadoutVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsResizable(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsResizable(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Radius(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor) -> Double: ...
    @winrt_mixinmethod
    def put_Radius(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AccentColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_AccentColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterProtractor, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.UI.Input.Inking.InkPresenterStencilKind: ...
    @winrt_mixinmethod
    def get_IsVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Transform(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_Transform(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    AreRaysVisible = property(get_AreRaysVisible, put_AreRaysVisible)
    IsCenterMarkerVisible = property(get_IsCenterMarkerVisible, put_IsCenterMarkerVisible)
    IsAngleReadoutVisible = property(get_IsAngleReadoutVisible, put_IsAngleReadoutVisible)
    IsResizable = property(get_IsResizable, put_IsResizable)
    Radius = property(get_Radius, put_Radius)
    AccentColor = property(get_AccentColor, put_AccentColor)
    Kind = property(get_Kind, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    Transform = property(get_Transform, put_Transform)
class InkPresenterRuler(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkPresenterRuler
    _classid_ = 'Windows.UI.Input.Inking.InkPresenterRuler'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Input.Inking.IInkPresenterRulerFactory, inkPresenter: win32more.Windows.UI.Input.Inking.InkPresenter) -> win32more.Windows.UI.Input.Inking.InkPresenterRuler: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler) -> Double: ...
    @winrt_mixinmethod
    def put_Length(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler) -> Double: ...
    @winrt_mixinmethod
    def put_Width(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.UI.Input.Inking.InkPresenterStencilKind: ...
    @winrt_mixinmethod
    def get_IsVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Transform(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_Transform(self: win32more.Windows.UI.Input.Inking.IInkPresenterStencil, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_AreTickMarksVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreTickMarksVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCompassVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCompassVisible(self: win32more.Windows.UI.Input.Inking.IInkPresenterRuler2, value: Boolean) -> Void: ...
    Length = property(get_Length, put_Length)
    Width = property(get_Width, put_Width)
    Kind = property(get_Kind, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    Transform = property(get_Transform, put_Transform)
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    IsCompassVisible = property(get_IsCompassVisible, put_IsCompassVisible)
InkPresenterStencilKind = Int32
InkPresenterStencilKind_Other: InkPresenterStencilKind = 0
InkPresenterStencilKind_Ruler: InkPresenterStencilKind = 1
InkPresenterStencilKind_Protractor: InkPresenterStencilKind = 2
class InkRecognitionResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkRecognitionResult
    _classid_ = 'Windows.UI.Input.Inking.InkRecognitionResult'
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.IInkRecognitionResult) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetTextCandidates(self: win32more.Windows.UI.Input.Inking.IInkRecognitionResult) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def GetStrokes(self: win32more.Windows.UI.Input.Inking.IInkRecognitionResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    BoundingRect = property(get_BoundingRect, None)
InkRecognitionTarget = Int32
InkRecognitionTarget_All: InkRecognitionTarget = 0
InkRecognitionTarget_Selected: InkRecognitionTarget = 1
InkRecognitionTarget_Recent: InkRecognitionTarget = 2
class InkRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkRecognizer
    _classid_ = 'Windows.UI.Input.Inking.InkRecognizer'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.UI.Input.Inking.IInkRecognizer) -> WinRT_String: ...
    Name = property(get_Name, None)
class InkRecognizerContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkRecognizerContainer
    _classid_ = 'Windows.UI.Input.Inking.InkRecognizerContainer'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkRecognizerContainer: ...
    @winrt_mixinmethod
    def SetDefaultRecognizer(self: win32more.Windows.UI.Input.Inking.IInkRecognizerContainer, recognizer: win32more.Windows.UI.Input.Inking.InkRecognizer) -> Void: ...
    @winrt_mixinmethod
    def RecognizeAsync(self: win32more.Windows.UI.Input.Inking.IInkRecognizerContainer, strokeCollection: win32more.Windows.UI.Input.Inking.InkStrokeContainer, recognitionTarget: win32more.Windows.UI.Input.Inking.InkRecognitionTarget) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_mixinmethod
    def GetRecognizers(self: win32more.Windows.UI.Input.Inking.IInkRecognizerContainer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognizer]: ...
class InkStroke(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkStroke
    _classid_ = 'Windows.UI.Input.Inking.InkStroke'
    @winrt_mixinmethod
    def get_DrawingAttributes(self: win32more.Windows.UI.Input.Inking.IInkStroke) -> win32more.Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def put_DrawingAttributes(self: win32more.Windows.UI.Input.Inking.IInkStroke, value: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.IInkStroke) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Selected(self: win32more.Windows.UI.Input.Inking.IInkStroke) -> Boolean: ...
    @winrt_mixinmethod
    def put_Selected(self: win32more.Windows.UI.Input.Inking.IInkStroke, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Recognized(self: win32more.Windows.UI.Input.Inking.IInkStroke) -> Boolean: ...
    @winrt_mixinmethod
    def GetRenderingSegments(self: win32more.Windows.UI.Input.Inking.IInkStroke) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStrokeRenderingSegment]: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.UI.Input.Inking.IInkStroke) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def get_PointTransform(self: win32more.Windows.UI.Input.Inking.IInkStroke2) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_PointTransform(self: win32more.Windows.UI.Input.Inking.IInkStroke2, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def GetInkPoints(self: win32more.Windows.UI.Input.Inking.IInkStroke2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkPoint]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Inking.IInkStroke3) -> UInt32: ...
    @winrt_mixinmethod
    def get_StrokeStartedTime(self: win32more.Windows.UI.Input.Inking.IInkStroke3) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_StrokeStartedTime(self: win32more.Windows.UI.Input.Inking.IInkStroke3, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDuration(self: win32more.Windows.UI.Input.Inking.IInkStroke3) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_StrokeDuration(self: win32more.Windows.UI.Input.Inking.IInkStroke3, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_PointerId(self: win32more.Windows.UI.Input.Inking.IInkStroke4) -> UInt32: ...
    DrawingAttributes = property(get_DrawingAttributes, put_DrawingAttributes)
    BoundingRect = property(get_BoundingRect, None)
    Selected = property(get_Selected, put_Selected)
    Recognized = property(get_Recognized, None)
    PointTransform = property(get_PointTransform, put_PointTransform)
    Id = property(get_Id, None)
    StrokeStartedTime = property(get_StrokeStartedTime, put_StrokeStartedTime)
    StrokeDuration = property(get_StrokeDuration, put_StrokeDuration)
    PointerId = property(get_PointerId, None)
class InkStrokeBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeBuilder'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkStrokeBuilder: ...
    @winrt_mixinmethod
    def BeginStroke(self: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def AppendToStroke(self: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.UI.Input.PointerPoint: ...
    @winrt_mixinmethod
    def EndStroke(self: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: win32more.Windows.UI.Input.PointerPoint) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def CreateStroke(self: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder, points: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def SetDefaultDrawingAttributes(self: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder, drawingAttributes: win32more.Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def CreateStrokeFromInkPoints(self: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder2, inkPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkPoint], transform: win32more.Windows.Foundation.Numerics.Matrix3x2) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def CreateStrokeFromInkPoints_2(self: win32more.Windows.UI.Input.Inking.IInkStrokeBuilder3, inkPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkPoint], transform: win32more.Windows.Foundation.Numerics.Matrix3x2, strokeStartedTime: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime], strokeDuration: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
class InkStrokeContainer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkStrokeContainer
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeContainer'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkStrokeContainer: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def AddStroke(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, stroke: win32more.Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def DeleteSelected(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def MoveSelected(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, translation: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithPolyLine(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, polyline: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithLine(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, from_: win32more.Windows.Foundation.Point, to: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CopySelectedToClipboard(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> Void: ...
    @winrt_mixinmethod
    def PasteFromClipboard(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, position: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CanPasteFromClipboard(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> Boolean: ...
    @winrt_mixinmethod
    def LoadAsync(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, inputStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncActionWithProgress[UInt64]: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def UpdateRecognitionResults(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer, recognitionResults: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]) -> Void: ...
    @winrt_mixinmethod
    def GetStrokes(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_mixinmethod
    def GetRecognitionResults(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkRecognitionResult]: ...
    @winrt_mixinmethod
    def AddStrokes(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer2, strokes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer2) -> Void: ...
    @winrt_mixinmethod
    def SaveWithFormatAsync(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer3, outputStream: win32more.Windows.Storage.Streams.IOutputStream, inkPersistenceFormat: win32more.Windows.UI.Input.Inking.InkPersistenceFormat) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def GetStrokeById(self: win32more.Windows.UI.Input.Inking.IInkStrokeContainer3, id: UInt32) -> win32more.Windows.UI.Input.Inking.InkStroke: ...
    BoundingRect = property(get_BoundingRect, None)
class InkStrokeInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkStrokeInput
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeInput'
    @winrt_mixinmethod
    def add_StrokeStarted(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeStarted(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokeContinued(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeContinued(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokeEnded(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeEnded(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokeCanceled(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkStrokeInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeCanceled(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: win32more.Windows.UI.Input.Inking.IInkStrokeInput) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class InkStrokeRenderingSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeRenderingSegment'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BezierControlPoint1(self: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BezierControlPoint2(self: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_mixinmethod
    def get_TiltX(self: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_mixinmethod
    def get_TiltY(self: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_mixinmethod
    def get_Twist(self: win32more.Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    Position = property(get_Position, None)
    BezierControlPoint1 = property(get_BezierControlPoint1, None)
    BezierControlPoint2 = property(get_BezierControlPoint2, None)
    Pressure = property(get_Pressure, None)
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Twist = property(get_Twist, None)
class InkStrokesCollectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkStrokesCollectedEventArgs
    _classid_ = 'Windows.UI.Input.Inking.InkStrokesCollectedEventArgs'
    @winrt_mixinmethod
    def get_Strokes(self: win32more.Windows.UI.Input.Inking.IInkStrokesCollectedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class InkStrokesErasedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkStrokesErasedEventArgs
    _classid_ = 'Windows.UI.Input.Inking.InkStrokesErasedEventArgs'
    @winrt_mixinmethod
    def get_Strokes(self: win32more.Windows.UI.Input.Inking.IInkStrokesErasedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class InkSynchronizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkSynchronizer
    _classid_ = 'Windows.UI.Input.Inking.InkSynchronizer'
    @winrt_mixinmethod
    def BeginDry(self: win32more.Windows.UI.Input.Inking.IInkSynchronizer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_mixinmethod
    def EndDry(self: win32more.Windows.UI.Input.Inking.IInkSynchronizer) -> Void: ...
class InkUnprocessedInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput
    _classid_ = 'Windows.UI.Input.Inking.InkUnprocessedInput'
    @winrt_mixinmethod
    def add_PointerEntered(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerHovered(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerHovered(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerLost(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Inking.InkUnprocessedInput, win32more.Windows.UI.Core.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerLost(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: win32more.Windows.UI.Input.Inking.IInkUnprocessedInput) -> win32more.Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class PenAndInkSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.IPenAndInkSettings
    _classid_ = 'Windows.UI.Input.Inking.PenAndInkSettings'
    @winrt_mixinmethod
    def get_IsHandwritingDirectlyIntoTextFieldEnabled(self: win32more.Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_PenHandedness(self: win32more.Windows.UI.Input.Inking.IPenAndInkSettings) -> win32more.Windows.UI.Input.Inking.PenHandedness: ...
    @winrt_mixinmethod
    def get_HandwritingLineHeight(self: win32more.Windows.UI.Input.Inking.IPenAndInkSettings) -> win32more.Windows.UI.Input.Inking.HandwritingLineHeight: ...
    @winrt_mixinmethod
    def get_FontFamilyName(self: win32more.Windows.UI.Input.Inking.IPenAndInkSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserConsentsToHandwritingTelemetryCollection(self: win32more.Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTouchHandwritingEnabled(self: win32more.Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_mixinmethod
    def SetPenHandedness(self: win32more.Windows.UI.Input.Inking.IPenAndInkSettings2, value: win32more.Windows.UI.Input.Inking.PenHandedness) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.UI.Input.Inking.IPenAndInkSettingsStatics) -> win32more.Windows.UI.Input.Inking.PenAndInkSettings: ...
    IsHandwritingDirectlyIntoTextFieldEnabled = property(get_IsHandwritingDirectlyIntoTextFieldEnabled, None)
    PenHandedness = property(get_PenHandedness, None)
    HandwritingLineHeight = property(get_HandwritingLineHeight, None)
    FontFamilyName = property(get_FontFamilyName, None)
    UserConsentsToHandwritingTelemetryCollection = property(get_UserConsentsToHandwritingTelemetryCollection, None)
    IsTouchHandwritingEnabled = property(get_IsTouchHandwritingEnabled, None)
PenHandedness = Int32
PenHandedness_Right: PenHandedness = 0
PenHandedness_Left: PenHandedness = 1
PenTipShape = Int32
PenTipShape_Circle: PenTipShape = 0
PenTipShape_Rectangle: PenTipShape = 1
make_head(_module, 'IInkDrawingAttributes')
make_head(_module, 'IInkDrawingAttributes2')
make_head(_module, 'IInkDrawingAttributes3')
make_head(_module, 'IInkDrawingAttributes4')
make_head(_module, 'IInkDrawingAttributes5')
make_head(_module, 'IInkDrawingAttributesPencilProperties')
make_head(_module, 'IInkDrawingAttributesStatics')
make_head(_module, 'IInkInputConfiguration')
make_head(_module, 'IInkInputConfiguration2')
make_head(_module, 'IInkInputProcessingConfiguration')
make_head(_module, 'IInkManager')
make_head(_module, 'IInkModelerAttributes')
make_head(_module, 'IInkModelerAttributes2')
make_head(_module, 'IInkPoint')
make_head(_module, 'IInkPoint2')
make_head(_module, 'IInkPointFactory')
make_head(_module, 'IInkPointFactory2')
make_head(_module, 'IInkPresenter')
make_head(_module, 'IInkPresenter2')
make_head(_module, 'IInkPresenter3')
make_head(_module, 'IInkPresenterProtractor')
make_head(_module, 'IInkPresenterProtractorFactory')
make_head(_module, 'IInkPresenterRuler')
make_head(_module, 'IInkPresenterRuler2')
make_head(_module, 'IInkPresenterRulerFactory')
make_head(_module, 'IInkPresenterStencil')
make_head(_module, 'IInkRecognitionResult')
make_head(_module, 'IInkRecognizer')
make_head(_module, 'IInkRecognizerContainer')
make_head(_module, 'IInkStroke')
make_head(_module, 'IInkStroke2')
make_head(_module, 'IInkStroke3')
make_head(_module, 'IInkStroke4')
make_head(_module, 'IInkStrokeBuilder')
make_head(_module, 'IInkStrokeBuilder2')
make_head(_module, 'IInkStrokeBuilder3')
make_head(_module, 'IInkStrokeContainer')
make_head(_module, 'IInkStrokeContainer2')
make_head(_module, 'IInkStrokeContainer3')
make_head(_module, 'IInkStrokeInput')
make_head(_module, 'IInkStrokeRenderingSegment')
make_head(_module, 'IInkStrokesCollectedEventArgs')
make_head(_module, 'IInkStrokesErasedEventArgs')
make_head(_module, 'IInkSynchronizer')
make_head(_module, 'IInkUnprocessedInput')
make_head(_module, 'IPenAndInkSettings')
make_head(_module, 'IPenAndInkSettings2')
make_head(_module, 'IPenAndInkSettingsStatics')
make_head(_module, 'InkDrawingAttributes')
make_head(_module, 'InkDrawingAttributesPencilProperties')
make_head(_module, 'InkInputConfiguration')
make_head(_module, 'InkInputProcessingConfiguration')
make_head(_module, 'InkManager')
make_head(_module, 'InkModelerAttributes')
make_head(_module, 'InkPoint')
make_head(_module, 'InkPresenter')
make_head(_module, 'InkPresenterProtractor')
make_head(_module, 'InkPresenterRuler')
make_head(_module, 'InkRecognitionResult')
make_head(_module, 'InkRecognizer')
make_head(_module, 'InkRecognizerContainer')
make_head(_module, 'InkStroke')
make_head(_module, 'InkStrokeBuilder')
make_head(_module, 'InkStrokeContainer')
make_head(_module, 'InkStrokeInput')
make_head(_module, 'InkStrokeRenderingSegment')
make_head(_module, 'InkStrokesCollectedEventArgs')
make_head(_module, 'InkStrokesErasedEventArgs')
make_head(_module, 'InkSynchronizer')
make_head(_module, 'InkUnprocessedInput')
make_head(_module, 'PenAndInkSettings')
