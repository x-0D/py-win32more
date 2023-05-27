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
import win32more.Windows.Graphics
import win32more.Windows.Graphics.DirectX
import win32more.Windows.Graphics.Effects
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AmbientLight(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionLight
    default_interface: win32more.Windows.UI.Composition.IAmbientLight
    _classid_ = 'Windows.UI.Composition.AmbientLight'
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Composition.IAmbientLight) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Composition.IAmbientLight, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Intensity(self: win32more.Windows.UI.Composition.IAmbientLight2) -> Single: ...
    @winrt_mixinmethod
    def put_Intensity(self: win32more.Windows.UI.Composition.IAmbientLight2, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    Intensity = property(get_Intensity, put_Intensity)
class _AnimationController_Meta_(ComPtr.__class__):
    pass
class AnimationController(ComPtr, metaclass=_AnimationController_Meta_):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.IAnimationController
    _classid_ = 'Windows.UI.Composition.AnimationController'
    @winrt_mixinmethod
    def get_PlaybackRate(self: win32more.Windows.UI.Composition.IAnimationController) -> Single: ...
    @winrt_mixinmethod
    def put_PlaybackRate(self: win32more.Windows.UI.Composition.IAnimationController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.UI.Composition.IAnimationController) -> Single: ...
    @winrt_mixinmethod
    def put_Progress(self: win32more.Windows.UI.Composition.IAnimationController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ProgressBehavior(self: win32more.Windows.UI.Composition.IAnimationController) -> win32more.Windows.UI.Composition.AnimationControllerProgressBehavior: ...
    @winrt_mixinmethod
    def put_ProgressBehavior(self: win32more.Windows.UI.Composition.IAnimationController, value: win32more.Windows.UI.Composition.AnimationControllerProgressBehavior) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Windows.UI.Composition.IAnimationController) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Windows.UI.Composition.IAnimationController) -> Void: ...
    @winrt_classmethod
    def get_MaxPlaybackRate(cls: Windows.UI.Composition.IAnimationControllerStatics) -> Single: ...
    @winrt_classmethod
    def get_MinPlaybackRate(cls: Windows.UI.Composition.IAnimationControllerStatics) -> Single: ...
    PlaybackRate = property(get_PlaybackRate, put_PlaybackRate)
    Progress = property(get_Progress, put_Progress)
    ProgressBehavior = property(get_ProgressBehavior, put_ProgressBehavior)
    _AnimationController_Meta_.MaxPlaybackRate = property(get_MaxPlaybackRate.__wrapped__, None)
    _AnimationController_Meta_.MinPlaybackRate = property(get_MinPlaybackRate.__wrapped__, None)
AnimationControllerProgressBehavior = Int32
AnimationControllerProgressBehavior_Default: AnimationControllerProgressBehavior = 0
AnimationControllerProgressBehavior_IncludesDelayTime: AnimationControllerProgressBehavior = 1
AnimationDelayBehavior = Int32
AnimationDelayBehavior_SetInitialValueAfterDelay: AnimationDelayBehavior = 0
AnimationDelayBehavior_SetInitialValueBeforeDelay: AnimationDelayBehavior = 1
AnimationDirection = Int32
AnimationDirection_Normal: AnimationDirection = 0
AnimationDirection_Reverse: AnimationDirection = 1
AnimationDirection_Alternate: AnimationDirection = 2
AnimationDirection_AlternateReverse: AnimationDirection = 3
AnimationIterationBehavior = Int32
AnimationIterationBehavior_Count: AnimationIterationBehavior = 0
AnimationIterationBehavior_Forever: AnimationIterationBehavior = 1
AnimationPropertyAccessMode = Int32
AnimationPropertyAccessMode_None: AnimationPropertyAccessMode = 0
AnimationPropertyAccessMode_ReadOnly: AnimationPropertyAccessMode = 1
AnimationPropertyAccessMode_WriteOnly: AnimationPropertyAccessMode = 2
AnimationPropertyAccessMode_ReadWrite: AnimationPropertyAccessMode = 3
class AnimationPropertyInfo(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.IAnimationPropertyInfo
    _classid_ = 'Windows.UI.Composition.AnimationPropertyInfo'
    @winrt_mixinmethod
    def get_AccessMode(self: win32more.Windows.UI.Composition.IAnimationPropertyInfo) -> win32more.Windows.UI.Composition.AnimationPropertyAccessMode: ...
    @winrt_mixinmethod
    def put_AccessMode(self: win32more.Windows.UI.Composition.IAnimationPropertyInfo, value: win32more.Windows.UI.Composition.AnimationPropertyAccessMode) -> Void: ...
    @winrt_mixinmethod
    def GetResolvedCompositionObject(self: win32more.Windows.UI.Composition.IAnimationPropertyInfo2) -> win32more.Windows.UI.Composition.CompositionObject: ...
    @winrt_mixinmethod
    def GetResolvedCompositionObjectProperty(self: win32more.Windows.UI.Composition.IAnimationPropertyInfo2) -> WinRT_String: ...
    AccessMode = property(get_AccessMode, put_AccessMode)
AnimationStopBehavior = Int32
AnimationStopBehavior_LeaveCurrentValue: AnimationStopBehavior = 0
AnimationStopBehavior_SetToInitialValue: AnimationStopBehavior = 1
AnimationStopBehavior_SetToFinalValue: AnimationStopBehavior = 2
class BackEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.IBackEasingFunction
    _classid_ = 'Windows.UI.Composition.BackEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Composition.IBackEasingFunction) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Amplitude(self: win32more.Windows.UI.Composition.IBackEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Amplitude = property(get_Amplitude, None)
class BooleanKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IBooleanKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.BooleanKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IBooleanKeyFrameAnimation, normalizedProgressKey: Single, value: Boolean) -> Void: ...
class BounceEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.IBounceEasingFunction
    _classid_ = 'Windows.UI.Composition.BounceEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Composition.IBounceEasingFunction) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Bounces(self: win32more.Windows.UI.Composition.IBounceEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def get_Bounciness(self: win32more.Windows.UI.Composition.IBounceEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Bounces = property(get_Bounces, None)
    Bounciness = property(get_Bounciness, None)
class BounceScalarNaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.ScalarNaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.IBounceScalarNaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.BounceScalarNaturalMotionAnimation'
    @winrt_mixinmethod
    def get_Acceleration(self: win32more.Windows.UI.Composition.IBounceScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Acceleration(self: win32more.Windows.UI.Composition.IBounceScalarNaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Restitution(self: win32more.Windows.UI.Composition.IBounceScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Restitution(self: win32more.Windows.UI.Composition.IBounceScalarNaturalMotionAnimation, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class BounceVector2NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.Vector2NaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.IBounceVector2NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.BounceVector2NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_Acceleration(self: win32more.Windows.UI.Composition.IBounceVector2NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Acceleration(self: win32more.Windows.UI.Composition.IBounceVector2NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Restitution(self: win32more.Windows.UI.Composition.IBounceVector2NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Restitution(self: win32more.Windows.UI.Composition.IBounceVector2NaturalMotionAnimation, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class BounceVector3NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.Vector3NaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.IBounceVector3NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.BounceVector3NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_Acceleration(self: win32more.Windows.UI.Composition.IBounceVector3NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Acceleration(self: win32more.Windows.UI.Composition.IBounceVector3NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Restitution(self: win32more.Windows.UI.Composition.IBounceVector3NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_Restitution(self: win32more.Windows.UI.Composition.IBounceVector3NaturalMotionAnimation, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class CircleEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.ICircleEasingFunction
    _classid_ = 'Windows.UI.Composition.CircleEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Composition.ICircleEasingFunction) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class ColorKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IColorKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.ColorKeyFrameAnimation'
    @winrt_mixinmethod
    def get_InterpolationColorSpace(self: win32more.Windows.UI.Composition.IColorKeyFrameAnimation) -> win32more.Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_mixinmethod
    def put_InterpolationColorSpace(self: win32more.Windows.UI.Composition.IColorKeyFrameAnimation, value: win32more.Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IColorKeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IColorKeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.UI.Color, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    InterpolationColorSpace = property(get_InterpolationColorSpace, put_InterpolationColorSpace)
class CompositionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionAnimation
    _classid_ = 'Windows.UI.Composition.CompositionAnimation'
    @winrt_mixinmethod
    def ClearAllParameters(self: win32more.Windows.UI.Composition.ICompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def ClearParameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetColorParameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetMatrix3x2Parameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def SetMatrix4x4Parameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def SetQuaternionParameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def SetReferenceParameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, compositionObject: win32more.Windows.UI.Composition.CompositionObject) -> Void: ...
    @winrt_mixinmethod
    def SetScalarParameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: Single) -> Void: ...
    @winrt_mixinmethod
    def SetVector2Parameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def SetVector3Parameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def SetVector4Parameter(self: win32more.Windows.UI.Composition.ICompositionAnimation, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def SetBooleanParameter(self: win32more.Windows.UI.Composition.ICompositionAnimation2, key: WinRT_String, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Target(self: win32more.Windows.UI.Composition.ICompositionAnimation2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Target(self: win32more.Windows.UI.Composition.ICompositionAnimation2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValueExpressions(self: win32more.Windows.UI.Composition.ICompositionAnimation3) -> win32more.Windows.UI.Composition.InitialValueExpressionCollection: ...
    @winrt_mixinmethod
    def SetExpressionReferenceParameter(self: win32more.Windows.UI.Composition.ICompositionAnimation4, parameterName: WinRT_String, source: win32more.Windows.UI.Composition.IAnimationObject) -> Void: ...
    Target = property(get_Target, put_Target)
    InitialValueExpressions = property(get_InitialValueExpressions, None)
class CompositionAnimationGroup(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionAnimationGroup
    _classid_ = 'Windows.UI.Composition.CompositionAnimationGroup'
    @winrt_mixinmethod
    def get_Count(self: win32more.Windows.UI.Composition.ICompositionAnimationGroup) -> Int32: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.UI.Composition.ICompositionAnimationGroup, value: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Composition.ICompositionAnimationGroup, value: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: win32more.Windows.UI.Composition.ICompositionAnimationGroup) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.CompositionAnimation]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.CompositionAnimation]: ...
    Count = property(get_Count, None)
class CompositionBackdropBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionBackdropBrush
    _classid_ = 'Windows.UI.Composition.CompositionBackdropBrush'
CompositionBackfaceVisibility = Int32
CompositionBackfaceVisibility_Inherit: CompositionBackfaceVisibility = 0
CompositionBackfaceVisibility_Visible: CompositionBackfaceVisibility = 1
CompositionBackfaceVisibility_Hidden: CompositionBackfaceVisibility = 2
class CompositionBatchCompletedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionBatchCompletedEventArgs
    _classid_ = 'Windows.UI.Composition.CompositionBatchCompletedEventArgs'
CompositionBatchTypes = UInt32
CompositionBatchTypes_None: CompositionBatchTypes = 0
CompositionBatchTypes_Animation: CompositionBatchTypes = 1
CompositionBatchTypes_Effect: CompositionBatchTypes = 2
CompositionBatchTypes_InfiniteAnimation: CompositionBatchTypes = 4
CompositionBatchTypes_AllAnimations: CompositionBatchTypes = 5
CompositionBitmapInterpolationMode = Int32
CompositionBitmapInterpolationMode_NearestNeighbor: CompositionBitmapInterpolationMode = 0
CompositionBitmapInterpolationMode_Linear: CompositionBitmapInterpolationMode = 1
CompositionBitmapInterpolationMode_MagLinearMinLinearMipLinear: CompositionBitmapInterpolationMode = 2
CompositionBitmapInterpolationMode_MagLinearMinLinearMipNearest: CompositionBitmapInterpolationMode = 3
CompositionBitmapInterpolationMode_MagLinearMinNearestMipLinear: CompositionBitmapInterpolationMode = 4
CompositionBitmapInterpolationMode_MagLinearMinNearestMipNearest: CompositionBitmapInterpolationMode = 5
CompositionBitmapInterpolationMode_MagNearestMinLinearMipLinear: CompositionBitmapInterpolationMode = 6
CompositionBitmapInterpolationMode_MagNearestMinLinearMipNearest: CompositionBitmapInterpolationMode = 7
CompositionBitmapInterpolationMode_MagNearestMinNearestMipLinear: CompositionBitmapInterpolationMode = 8
CompositionBitmapInterpolationMode_MagNearestMinNearestMipNearest: CompositionBitmapInterpolationMode = 9
CompositionBorderMode = Int32
CompositionBorderMode_Inherit: CompositionBorderMode = 0
CompositionBorderMode_Soft: CompositionBorderMode = 1
CompositionBorderMode_Hard: CompositionBorderMode = 2
class CompositionBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionBrush
    _classid_ = 'Windows.UI.Composition.CompositionBrush'
class CompositionCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.ICompositionCapabilities
    _classid_ = 'Windows.UI.Composition.CompositionCapabilities'
    @winrt_mixinmethod
    def AreEffectsSupported(self: win32more.Windows.UI.Composition.ICompositionCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def AreEffectsFast(self: win32more.Windows.UI.Composition.ICompositionCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.UI.Composition.ICompositionCapabilities, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Composition.CompositionCapabilities, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.UI.Composition.ICompositionCapabilities, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Composition.ICompositionCapabilitiesStatics) -> win32more.Windows.UI.Composition.CompositionCapabilities: ...
class CompositionClip(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionClip
    _classid_ = 'Windows.UI.Composition.CompositionClip'
    @winrt_mixinmethod
    def get_AnchorPoint(self: win32more.Windows.UI.Composition.ICompositionClip2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: win32more.Windows.UI.Composition.ICompositionClip2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionClip2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionClip2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionClip2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionClip2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionClip2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionClip2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionClip2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionClip2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.ICompositionClip2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Composition.ICompositionClip2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionClip2) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionClip2, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class CompositionColorBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionColorBrush
    _classid_ = 'Windows.UI.Composition.CompositionColorBrush'
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Composition.ICompositionColorBrush) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Composition.ICompositionColorBrush, value: win32more.Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class CompositionColorGradientStop(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionColorGradientStop
    _classid_ = 'Windows.UI.Composition.CompositionColorGradientStop'
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Composition.ICompositionColorGradientStop) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Composition.ICompositionColorGradientStop, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionColorGradientStop) -> Single: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionColorGradientStop, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
class CompositionColorGradientStopCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.ICompositionColorGradientStopCollection
    _classid_ = 'Windows.UI.Composition.CompositionColorGradientStopCollection'
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.CompositionColorGradientStop]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.CompositionColorGradientStop]: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], index: UInt32) -> win32more.Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Composition.CompositionColorGradientStop]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], value: win32more.Windows.UI.Composition.CompositionColorGradientStop, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], index: UInt32, value: win32more.Windows.UI.Composition.CompositionColorGradientStop) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], index: UInt32, value: win32more.Windows.UI.Composition.CompositionColorGradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], value: win32more.Windows.UI.Composition.CompositionColorGradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], startIndex: UInt32, items: Annotated[SZArray[win32more.Windows.UI.Composition.CompositionColorGradientStop], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionColorGradientStop], items: Annotated[SZArray[win32more.Windows.UI.Composition.CompositionColorGradientStop], 'In']) -> Void: ...
    Size = property(get_Size, None)
CompositionColorSpace = Int32
CompositionColorSpace_Auto: CompositionColorSpace = 0
CompositionColorSpace_Hsl: CompositionColorSpace = 1
CompositionColorSpace_Rgb: CompositionColorSpace = 2
CompositionColorSpace_HslLinear: CompositionColorSpace = 3
CompositionColorSpace_RgbLinear: CompositionColorSpace = 4
class CompositionCommitBatch(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionCommitBatch
    _classid_ = 'Windows.UI.Composition.CompositionCommitBatch'
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.UI.Composition.ICompositionCommitBatch) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsEnded(self: win32more.Windows.UI.Composition.ICompositionCommitBatch) -> Boolean: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.UI.Composition.ICompositionCommitBatch, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head, win32more.Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.UI.Composition.ICompositionCommitBatch, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
CompositionCompositeMode = Int32
CompositionCompositeMode_Inherit: CompositionCompositeMode = 0
CompositionCompositeMode_SourceOver: CompositionCompositeMode = 1
CompositionCompositeMode_DestinationInvert: CompositionCompositeMode = 2
CompositionCompositeMode_MinBlend: CompositionCompositeMode = 3
class CompositionContainerShape(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionShape
    default_interface: win32more.Windows.UI.Composition.ICompositionContainerShape
    _classid_ = 'Windows.UI.Composition.CompositionContainerShape'
    @winrt_mixinmethod
    def get_Shapes(self: win32more.Windows.UI.Composition.ICompositionContainerShape) -> win32more.Windows.UI.Composition.CompositionShapeCollection: ...
    Shapes = property(get_Shapes, None)
class CompositionDrawingSurface(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionDrawingSurface
    _classid_ = 'Windows.UI.Composition.CompositionDrawingSurface'
    @winrt_mixinmethod
    def get_AlphaMode(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface) -> win32more.Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SizeInt32(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface2) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def Resize(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface2, sizePixels: win32more.Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_mixinmethod
    def Scroll(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface2, offset: win32more.Windows.Graphics.PointInt32) -> Void: ...
    @winrt_mixinmethod
    def ScrollRect(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface2, offset: win32more.Windows.Graphics.PointInt32, scrollRect: win32more.Windows.Graphics.RectInt32) -> Void: ...
    @winrt_mixinmethod
    def ScrollWithClip(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface2, offset: win32more.Windows.Graphics.PointInt32, clipRect: win32more.Windows.Graphics.RectInt32) -> Void: ...
    @winrt_mixinmethod
    def ScrollRectWithClip(self: win32more.Windows.UI.Composition.ICompositionDrawingSurface2, offset: win32more.Windows.Graphics.PointInt32, clipRect: win32more.Windows.Graphics.RectInt32, scrollRect: win32more.Windows.Graphics.RectInt32) -> Void: ...
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
    SizeInt32 = property(get_SizeInt32, None)
CompositionDropShadowSourcePolicy = Int32
CompositionDropShadowSourcePolicy_Default: CompositionDropShadowSourcePolicy = 0
CompositionDropShadowSourcePolicy_InheritFromVisualContent: CompositionDropShadowSourcePolicy = 1
class CompositionEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionEasingFunction
    _classid_ = 'Windows.UI.Composition.CompositionEasingFunction'
    @winrt_classmethod
    def CreateCubicBezierEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, controlPoint1: win32more.Windows.Foundation.Numerics.Vector2, controlPoint2: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_classmethod
    def CreateLinearEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_classmethod
    def CreateStepEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
    @winrt_classmethod
    def CreateStepEasingFunctionWithStepCount(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, stepCount: Int32) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
    @winrt_classmethod
    def CreateBackEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, amplitude: Single) -> win32more.Windows.UI.Composition.BackEasingFunction: ...
    @winrt_classmethod
    def CreateBounceEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, bounces: Int32, bounciness: Single) -> win32more.Windows.UI.Composition.BounceEasingFunction: ...
    @winrt_classmethod
    def CreateCircleEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode) -> win32more.Windows.UI.Composition.CircleEasingFunction: ...
    @winrt_classmethod
    def CreateElasticEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, oscillations: Int32, springiness: Single) -> win32more.Windows.UI.Composition.ElasticEasingFunction: ...
    @winrt_classmethod
    def CreateExponentialEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, exponent: Single) -> win32more.Windows.UI.Composition.ExponentialEasingFunction: ...
    @winrt_classmethod
    def CreatePowerEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, power: Single) -> win32more.Windows.UI.Composition.PowerEasingFunction: ...
    @winrt_classmethod
    def CreateSineEasingFunction(cls: Windows.UI.Composition.ICompositionEasingFunctionStatics, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode) -> win32more.Windows.UI.Composition.SineEasingFunction: ...
CompositionEasingFunctionMode = Int32
CompositionEasingFunctionMode_In: CompositionEasingFunctionMode = 0
CompositionEasingFunctionMode_Out: CompositionEasingFunctionMode = 1
CompositionEasingFunctionMode_InOut: CompositionEasingFunctionMode = 2
class CompositionEffectBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionEffectBrush
    _classid_ = 'Windows.UI.Composition.CompositionEffectBrush'
    @winrt_mixinmethod
    def GetSourceParameter(self: win32more.Windows.UI.Composition.ICompositionEffectBrush, name: WinRT_String) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def SetSourceParameter(self: win32more.Windows.UI.Composition.ICompositionEffectBrush, name: WinRT_String, source: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
class CompositionEffectFactory(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionEffectFactory
    _classid_ = 'Windows.UI.Composition.CompositionEffectFactory'
    @winrt_mixinmethod
    def CreateBrush(self: win32more.Windows.UI.Composition.ICompositionEffectFactory) -> win32more.Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.UI.Composition.ICompositionEffectFactory) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_LoadStatus(self: win32more.Windows.UI.Composition.ICompositionEffectFactory) -> win32more.Windows.UI.Composition.CompositionEffectFactoryLoadStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    LoadStatus = property(get_LoadStatus, None)
CompositionEffectFactoryLoadStatus = Int32
CompositionEffectFactoryLoadStatus_Success: CompositionEffectFactoryLoadStatus = 0
CompositionEffectFactoryLoadStatus_EffectTooComplex: CompositionEffectFactoryLoadStatus = 1
CompositionEffectFactoryLoadStatus_Pending: CompositionEffectFactoryLoadStatus = 2
CompositionEffectFactoryLoadStatus_Other: CompositionEffectFactoryLoadStatus = -1
class CompositionEffectSourceParameter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.ICompositionEffectSourceParameter
    _classid_ = 'Windows.UI.Composition.CompositionEffectSourceParameter'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Composition.ICompositionEffectSourceParameterFactory, name: WinRT_String) -> win32more.Windows.UI.Composition.CompositionEffectSourceParameter: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.UI.Composition.ICompositionEffectSourceParameter) -> WinRT_String: ...
    Name = property(get_Name, None)
class CompositionEllipseGeometry(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionGeometry
    default_interface: win32more.Windows.UI.Composition.ICompositionEllipseGeometry
    _classid_ = 'Windows.UI.Composition.CompositionEllipseGeometry'
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.UI.Composition.ICompositionEllipseGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Center(self: win32more.Windows.UI.Composition.ICompositionEllipseGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Radius(self: win32more.Windows.UI.Composition.ICompositionEllipseGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Radius(self: win32more.Windows.UI.Composition.ICompositionEllipseGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class CompositionGeometricClip(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionClip
    default_interface: win32more.Windows.UI.Composition.ICompositionGeometricClip
    _classid_ = 'Windows.UI.Composition.CompositionGeometricClip'
    @winrt_mixinmethod
    def get_Geometry(self: win32more.Windows.UI.Composition.ICompositionGeometricClip) -> win32more.Windows.UI.Composition.CompositionGeometry: ...
    @winrt_mixinmethod
    def put_Geometry(self: win32more.Windows.UI.Composition.ICompositionGeometricClip, value: win32more.Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_mixinmethod
    def get_ViewBox(self: win32more.Windows.UI.Composition.ICompositionGeometricClip) -> win32more.Windows.UI.Composition.CompositionViewBox: ...
    @winrt_mixinmethod
    def put_ViewBox(self: win32more.Windows.UI.Composition.ICompositionGeometricClip, value: win32more.Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Geometry = property(get_Geometry, put_Geometry)
    ViewBox = property(get_ViewBox, put_ViewBox)
class CompositionGeometry(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionGeometry
    _classid_ = 'Windows.UI.Composition.CompositionGeometry'
    @winrt_mixinmethod
    def get_TrimEnd(self: win32more.Windows.UI.Composition.ICompositionGeometry) -> Single: ...
    @winrt_mixinmethod
    def put_TrimEnd(self: win32more.Windows.UI.Composition.ICompositionGeometry, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TrimOffset(self: win32more.Windows.UI.Composition.ICompositionGeometry) -> Single: ...
    @winrt_mixinmethod
    def put_TrimOffset(self: win32more.Windows.UI.Composition.ICompositionGeometry, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TrimStart(self: win32more.Windows.UI.Composition.ICompositionGeometry) -> Single: ...
    @winrt_mixinmethod
    def put_TrimStart(self: win32more.Windows.UI.Composition.ICompositionGeometry, value: Single) -> Void: ...
    TrimEnd = property(get_TrimEnd, put_TrimEnd)
    TrimOffset = property(get_TrimOffset, put_TrimOffset)
    TrimStart = property(get_TrimStart, put_TrimStart)
CompositionGetValueStatus = Int32
CompositionGetValueStatus_Succeeded: CompositionGetValueStatus = 0
CompositionGetValueStatus_TypeMismatch: CompositionGetValueStatus = 1
CompositionGetValueStatus_NotFound: CompositionGetValueStatus = 2
class CompositionGradientBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionGradientBrush
    _classid_ = 'Windows.UI.Composition.CompositionGradientBrush'
    @winrt_mixinmethod
    def get_AnchorPoint(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_ColorStops(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.UI.Composition.CompositionColorGradientStopCollection: ...
    @winrt_mixinmethod
    def get_ExtendMode(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.UI.Composition.CompositionGradientExtendMode: ...
    @winrt_mixinmethod
    def put_ExtendMode(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: win32more.Windows.UI.Composition.CompositionGradientExtendMode) -> Void: ...
    @winrt_mixinmethod
    def get_InterpolationSpace(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_mixinmethod
    def put_InterpolationSpace(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: win32more.Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionGradientBrush) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionGradientBrush, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_MappingMode(self: win32more.Windows.UI.Composition.ICompositionGradientBrush2) -> win32more.Windows.UI.Composition.CompositionMappingMode: ...
    @winrt_mixinmethod
    def put_MappingMode(self: win32more.Windows.UI.Composition.ICompositionGradientBrush2, value: win32more.Windows.UI.Composition.CompositionMappingMode) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    ColorStops = property(get_ColorStops, None)
    ExtendMode = property(get_ExtendMode, put_ExtendMode)
    InterpolationSpace = property(get_InterpolationSpace, put_InterpolationSpace)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    MappingMode = property(get_MappingMode, put_MappingMode)
CompositionGradientExtendMode = Int32
CompositionGradientExtendMode_Clamp: CompositionGradientExtendMode = 0
CompositionGradientExtendMode_Wrap: CompositionGradientExtendMode = 1
CompositionGradientExtendMode_Mirror: CompositionGradientExtendMode = 2
class CompositionGraphicsDevice(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionGraphicsDevice
    _classid_ = 'Windows.UI.Composition.CompositionGraphicsDevice'
    @winrt_mixinmethod
    def CreateDrawingSurface(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice, sizePixels: win32more.Windows.Foundation.Size, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_mixinmethod
    def add_RenderingDeviceReplaced(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Composition.CompositionGraphicsDevice, win32more.Windows.UI.Composition.RenderingDeviceReplacedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RenderingDeviceReplaced(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateDrawingSurface2(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice2, sizePixels: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_mixinmethod
    def CreateVirtualDrawingSurface(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice2, sizePixels: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionVirtualDrawingSurface: ...
    @winrt_mixinmethod
    def CreateMipmapSurface(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice3, sizePixels: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionMipmapSurface: ...
    @winrt_mixinmethod
    def Trim(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice3) -> Void: ...
    @winrt_mixinmethod
    def CaptureAsync(self: win32more.Windows.UI.Composition.ICompositionGraphicsDevice4, captureVisual: win32more.Windows.UI.Composition.Visual, size: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode, sdrBoost: Single) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Composition.ICompositionSurface]: ...
class CompositionLight(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionLight
    _classid_ = 'Windows.UI.Composition.CompositionLight'
    @winrt_mixinmethod
    def get_Targets(self: win32more.Windows.UI.Composition.ICompositionLight) -> win32more.Windows.UI.Composition.VisualUnorderedCollection: ...
    @winrt_mixinmethod
    def get_ExclusionsFromTargets(self: win32more.Windows.UI.Composition.ICompositionLight2) -> win32more.Windows.UI.Composition.VisualUnorderedCollection: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.UI.Composition.ICompositionLight3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.UI.Composition.ICompositionLight3, value: Boolean) -> Void: ...
    Targets = property(get_Targets, None)
    ExclusionsFromTargets = property(get_ExclusionsFromTargets, None)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class CompositionLineGeometry(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionGeometry
    default_interface: win32more.Windows.UI.Composition.ICompositionLineGeometry
    _classid_ = 'Windows.UI.Composition.CompositionLineGeometry'
    @winrt_mixinmethod
    def get_Start(self: win32more.Windows.UI.Composition.ICompositionLineGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Start(self: win32more.Windows.UI.Composition.ICompositionLineGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_End(self: win32more.Windows.UI.Composition.ICompositionLineGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_End(self: win32more.Windows.UI.Composition.ICompositionLineGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Start = property(get_Start, put_Start)
    End = property(get_End, put_End)
class CompositionLinearGradientBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionGradientBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionLinearGradientBrush
    _classid_ = 'Windows.UI.Composition.CompositionLinearGradientBrush'
    @winrt_mixinmethod
    def get_EndPoint(self: win32more.Windows.UI.Composition.ICompositionLinearGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_EndPoint(self: win32more.Windows.UI.Composition.ICompositionLinearGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_StartPoint(self: win32more.Windows.UI.Composition.ICompositionLinearGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_StartPoint(self: win32more.Windows.UI.Composition.ICompositionLinearGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
CompositionMappingMode = Int32
CompositionMappingMode_Absolute: CompositionMappingMode = 0
CompositionMappingMode_Relative: CompositionMappingMode = 1
class CompositionMaskBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionMaskBrush
    _classid_ = 'Windows.UI.Composition.CompositionMaskBrush'
    @winrt_mixinmethod
    def get_Mask(self: win32more.Windows.UI.Composition.ICompositionMaskBrush) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Mask(self: win32more.Windows.UI.Composition.ICompositionMaskBrush, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Composition.ICompositionMaskBrush) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.UI.Composition.ICompositionMaskBrush, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    Mask = property(get_Mask, put_Mask)
    Source = property(get_Source, put_Source)
class CompositionMipmapSurface(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionMipmapSurface
    _classid_ = 'Windows.UI.Composition.CompositionMipmapSurface'
    @winrt_mixinmethod
    def get_LevelCount(self: win32more.Windows.UI.Composition.ICompositionMipmapSurface) -> UInt32: ...
    @winrt_mixinmethod
    def get_AlphaMode(self: win32more.Windows.UI.Composition.ICompositionMipmapSurface) -> win32more.Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_mixinmethod
    def get_PixelFormat(self: win32more.Windows.UI.Composition.ICompositionMipmapSurface) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_SizeInt32(self: win32more.Windows.UI.Composition.ICompositionMipmapSurface) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def GetDrawingSurfaceForLevel(self: win32more.Windows.UI.Composition.ICompositionMipmapSurface, level: UInt32) -> win32more.Windows.UI.Composition.CompositionDrawingSurface: ...
    LevelCount = property(get_LevelCount, None)
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    SizeInt32 = property(get_SizeInt32, None)
class CompositionNineGridBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionNineGridBrush
    _classid_ = 'Windows.UI.Composition.CompositionNineGridBrush'
    @winrt_mixinmethod
    def get_BottomInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_BottomInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_BottomInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_BottomInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_IsCenterHollow(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCenterHollow(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LeftInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_LeftInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LeftInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_LeftInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RightInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_RightInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_TopInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_TopInset(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush) -> Single: ...
    @winrt_mixinmethod
    def put_TopInsetScale(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsets(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, inset: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsetsWithValues(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsetScales(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, scale: Single) -> Void: ...
    @winrt_mixinmethod
    def SetInsetScalesWithValues(self: win32more.Windows.UI.Composition.ICompositionNineGridBrush, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    BottomInsetScale = property(get_BottomInsetScale, put_BottomInsetScale)
    IsCenterHollow = property(get_IsCenterHollow, put_IsCenterHollow)
    LeftInset = property(get_LeftInset, put_LeftInset)
    LeftInsetScale = property(get_LeftInsetScale, put_LeftInsetScale)
    RightInset = property(get_RightInset, put_RightInset)
    RightInsetScale = property(get_RightInsetScale, put_RightInsetScale)
    Source = property(get_Source, put_Source)
    TopInset = property(get_TopInset, put_TopInset)
    TopInsetScale = property(get_TopInsetScale, put_TopInsetScale)
class CompositionObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.ICompositionObject
    _classid_ = 'Windows.UI.Composition.CompositionObject'
    @winrt_mixinmethod
    def get_Compositor(self: win32more.Windows.UI.Composition.ICompositionObject) -> win32more.Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: win32more.Windows.UI.Composition.ICompositionObject) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.UI.Composition.ICompositionObject) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_mixinmethod
    def StartAnimation(self: win32more.Windows.UI.Composition.ICompositionObject, propertyName: WinRT_String, animation: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_mixinmethod
    def StopAnimation(self: win32more.Windows.UI.Composition.ICompositionObject, propertyName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.UI.Composition.ICompositionObject2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Comment(self: win32more.Windows.UI.Composition.ICompositionObject2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ImplicitAnimations(self: win32more.Windows.UI.Composition.ICompositionObject2) -> win32more.Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_mixinmethod
    def put_ImplicitAnimations(self: win32more.Windows.UI.Composition.ICompositionObject2, value: win32more.Windows.UI.Composition.ImplicitAnimationCollection) -> Void: ...
    @winrt_mixinmethod
    def StartAnimationGroup(self: win32more.Windows.UI.Composition.ICompositionObject2, value: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def StopAnimationGroup(self: win32more.Windows.UI.Composition.ICompositionObject2, value: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Windows.UI.Composition.ICompositionObject3) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def TryGetAnimationController(self: win32more.Windows.UI.Composition.ICompositionObject4, propertyName: WinRT_String) -> win32more.Windows.UI.Composition.AnimationController: ...
    @winrt_mixinmethod
    def StartAnimationWithController(self: win32more.Windows.UI.Composition.ICompositionObject5, propertyName: WinRT_String, animation: win32more.Windows.UI.Composition.CompositionAnimation, animationController: win32more.Windows.UI.Composition.AnimationController) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfo(self: win32more.Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, propertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_classmethod
    def StartAnimationWithIAnimationObject(cls: Windows.UI.Composition.ICompositionObjectStatics, target: win32more.Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, animation: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_classmethod
    def StartAnimationGroupWithIAnimationObject(cls: Windows.UI.Composition.ICompositionObjectStatics, target: win32more.Windows.UI.Composition.IAnimationObject, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    Compositor = property(get_Compositor, None)
    Dispatcher = property(get_Dispatcher, None)
    Properties = property(get_Properties, None)
    Comment = property(get_Comment, put_Comment)
    ImplicitAnimations = property(get_ImplicitAnimations, put_ImplicitAnimations)
    DispatcherQueue = property(get_DispatcherQueue, None)
class CompositionPath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.ICompositionPath
    _classid_ = 'Windows.UI.Composition.CompositionPath'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Composition.ICompositionPathFactory, source: win32more.Windows.Graphics.IGeometrySource2D) -> win32more.Windows.UI.Composition.CompositionPath: ...
class CompositionPathGeometry(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionGeometry
    default_interface: win32more.Windows.UI.Composition.ICompositionPathGeometry
    _classid_ = 'Windows.UI.Composition.CompositionPathGeometry'
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.UI.Composition.ICompositionPathGeometry) -> win32more.Windows.UI.Composition.CompositionPath: ...
    @winrt_mixinmethod
    def put_Path(self: win32more.Windows.UI.Composition.ICompositionPathGeometry, value: win32more.Windows.UI.Composition.CompositionPath) -> Void: ...
    Path = property(get_Path, put_Path)
class CompositionProjectedShadow(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionProjectedShadow
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadow'
    @winrt_mixinmethod
    def get_BlurRadiusMultiplier(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow) -> Single: ...
    @winrt_mixinmethod
    def put_BlurRadiusMultiplier(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Casters(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow) -> win32more.Windows.UI.Composition.CompositionProjectedShadowCasterCollection: ...
    @winrt_mixinmethod
    def get_LightSource(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow) -> win32more.Windows.UI.Composition.CompositionLight: ...
    @winrt_mixinmethod
    def put_LightSource(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow, value: win32more.Windows.UI.Composition.CompositionLight) -> Void: ...
    @winrt_mixinmethod
    def get_MaxBlurRadius(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow) -> Single: ...
    @winrt_mixinmethod
    def put_MaxBlurRadius(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinBlurRadius(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow) -> Single: ...
    @winrt_mixinmethod
    def put_MinBlurRadius(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Receivers(self: win32more.Windows.UI.Composition.ICompositionProjectedShadow) -> win32more.Windows.UI.Composition.CompositionProjectedShadowReceiverUnorderedCollection: ...
    BlurRadiusMultiplier = property(get_BlurRadiusMultiplier, put_BlurRadiusMultiplier)
    Casters = property(get_Casters, None)
    LightSource = property(get_LightSource, put_LightSource)
    MaxBlurRadius = property(get_MaxBlurRadius, put_MaxBlurRadius)
    MinBlurRadius = property(get_MinBlurRadius, put_MinBlurRadius)
    Receivers = property(get_Receivers, None)
class CompositionProjectedShadowCaster(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionProjectedShadowCaster
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowCaster'
    @winrt_mixinmethod
    def get_Brush(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCaster) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Brush(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCaster, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_CastingVisual(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCaster) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CastingVisual(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCaster, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    Brush = property(get_Brush, put_Brush)
    CastingVisual = property(get_CastingVisual, put_CastingVisual)
class _CompositionProjectedShadowCasterCollection_Meta_(ComPtr.__class__):
    pass
class CompositionProjectedShadowCasterCollection(ComPtr, metaclass=_CompositionProjectedShadowCasterCollection_Meta_):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowCasterCollection'
    @winrt_mixinmethod
    def get_Count(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection) -> Int32: ...
    @winrt_mixinmethod
    def InsertAbove(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster, reference: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def InsertAtBottom(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def InsertAtTop(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def InsertBelow(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster, reference: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection, caster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowCasterCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.CompositionProjectedShadowCaster]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.CompositionProjectedShadowCaster]: ...
    @winrt_classmethod
    def get_MaxRespectedCasters(cls: Windows.UI.Composition.ICompositionProjectedShadowCasterCollectionStatics) -> Int32: ...
    Count = property(get_Count, None)
    _CompositionProjectedShadowCasterCollection_Meta_.MaxRespectedCasters = property(get_MaxRespectedCasters.__wrapped__, None)
class CompositionProjectedShadowReceiver(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiver
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowReceiver'
    @winrt_mixinmethod
    def get_ReceivingVisual(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiver) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_ReceivingVisual(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiver, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    ReceivingVisual = property(get_ReceivingVisual, put_ReceivingVisual)
class CompositionProjectedShadowReceiverUnorderedCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection
    _classid_ = 'Windows.UI.Composition.CompositionProjectedShadowReceiverUnorderedCollection'
    @winrt_mixinmethod
    def Add(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection, value: win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_mixinmethod
    def get_Count(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection) -> Int32: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection, value: win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: win32more.Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver]: ...
    Count = property(get_Count, None)
class CompositionPropertySet(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionPropertySet
    _classid_ = 'Windows.UI.Composition.CompositionPropertySet'
    @winrt_mixinmethod
    def InsertColor(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def InsertMatrix3x2(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def InsertMatrix4x4(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def InsertQuaternion(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def InsertScalar(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: Single) -> Void: ...
    @winrt_mixinmethod
    def InsertVector2(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def InsertVector3(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def InsertVector4(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def TryGetColor(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(win32more.Windows.UI.Color_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetMatrix3x2(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Matrix3x2_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetMatrix4x4(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetQuaternion(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Quaternion_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetScalar(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(Single)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetVector2(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Vector2_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetVector3(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Vector3_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def TryGetVector4(self: win32more.Windows.UI.Composition.ICompositionPropertySet, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Vector4_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_mixinmethod
    def InsertBoolean(self: win32more.Windows.UI.Composition.ICompositionPropertySet2, propertyName: WinRT_String, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def TryGetBoolean(self: win32more.Windows.UI.Composition.ICompositionPropertySet2, propertyName: WinRT_String, value: POINTER(Boolean)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
class CompositionRadialGradientBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionGradientBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionRadialGradientBrush
    _classid_ = 'Windows.UI.Composition.CompositionRadialGradientBrush'
    @winrt_mixinmethod
    def get_EllipseCenter(self: win32more.Windows.UI.Composition.ICompositionRadialGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_EllipseCenter(self: win32more.Windows.UI.Composition.ICompositionRadialGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_EllipseRadius(self: win32more.Windows.UI.Composition.ICompositionRadialGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_EllipseRadius(self: win32more.Windows.UI.Composition.ICompositionRadialGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_GradientOriginOffset(self: win32more.Windows.UI.Composition.ICompositionRadialGradientBrush) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_GradientOriginOffset(self: win32more.Windows.UI.Composition.ICompositionRadialGradientBrush, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    EllipseCenter = property(get_EllipseCenter, put_EllipseCenter)
    EllipseRadius = property(get_EllipseRadius, put_EllipseRadius)
    GradientOriginOffset = property(get_GradientOriginOffset, put_GradientOriginOffset)
class CompositionRectangleGeometry(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionGeometry
    default_interface: win32more.Windows.UI.Composition.ICompositionRectangleGeometry
    _classid_ = 'Windows.UI.Composition.CompositionRectangleGeometry'
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionRectangleGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionRectangleGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Composition.ICompositionRectangleGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.UI.Composition.ICompositionRectangleGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class CompositionRoundedRectangleGeometry(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionGeometry
    default_interface: win32more.Windows.UI.Composition.ICompositionRoundedRectangleGeometry
    _classid_ = 'Windows.UI.Composition.CompositionRoundedRectangleGeometry'
    @winrt_mixinmethod
    def get_CornerRadius(self: win32more.Windows.UI.Composition.ICompositionRoundedRectangleGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CornerRadius(self: win32more.Windows.UI.Composition.ICompositionRoundedRectangleGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionRoundedRectangleGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionRoundedRectangleGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Composition.ICompositionRoundedRectangleGeometry) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.UI.Composition.ICompositionRoundedRectangleGeometry, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    CornerRadius = property(get_CornerRadius, put_CornerRadius)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class CompositionScopedBatch(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionScopedBatch
    _classid_ = 'Windows.UI.Composition.CompositionScopedBatch'
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Windows.UI.Composition.ICompositionScopedBatch) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsEnded(self: win32more.Windows.UI.Composition.ICompositionScopedBatch) -> Boolean: ...
    @winrt_mixinmethod
    def End(self: win32more.Windows.UI.Composition.ICompositionScopedBatch) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Windows.UI.Composition.ICompositionScopedBatch) -> Void: ...
    @winrt_mixinmethod
    def Suspend(self: win32more.Windows.UI.Composition.ICompositionScopedBatch) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.UI.Composition.ICompositionScopedBatch, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head, win32more.Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.UI.Composition.ICompositionScopedBatch, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
class CompositionShadow(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionShadow
    _classid_ = 'Windows.UI.Composition.CompositionShadow'
class CompositionShape(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionShape
    _classid_ = 'Windows.UI.Composition.CompositionShape'
    @winrt_mixinmethod
    def get_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionShape) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionShape, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionShape) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionShape, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionShape) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionShape) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.ICompositionShape) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Composition.ICompositionShape, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionShape) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionShape, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class CompositionShapeCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape]
    _classid_ = 'Windows.UI.Composition.CompositionShapeCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], index: UInt32) -> win32more.Windows.UI.Composition.CompositionShape: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Composition.CompositionShape]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], value: win32more.Windows.UI.Composition.CompositionShape, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], index: UInt32, value: win32more.Windows.UI.Composition.CompositionShape) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], index: UInt32, value: win32more.Windows.UI.Composition.CompositionShape) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], value: win32more.Windows.UI.Composition.CompositionShape) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], startIndex: UInt32, items: Annotated[SZArray[win32more.Windows.UI.Composition.CompositionShape], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.CompositionShape], items: Annotated[SZArray[win32more.Windows.UI.Composition.CompositionShape], 'In']) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.CompositionShape]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.CompositionShape]: ...
    Size = property(get_Size, None)
class CompositionSpriteShape(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionShape
    default_interface: win32more.Windows.UI.Composition.ICompositionSpriteShape
    _classid_ = 'Windows.UI.Composition.CompositionSpriteShape'
    @winrt_mixinmethod
    def get_FillBrush(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_FillBrush(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Geometry(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionGeometry: ...
    @winrt_mixinmethod
    def put_Geometry(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: win32more.Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_mixinmethod
    def get_IsStrokeNonScaling(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStrokeNonScaling(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeBrush(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_StrokeBrush(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashArray(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionStrokeDashArray: ...
    @winrt_mixinmethod
    def get_StrokeDashCap(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_mixinmethod
    def put_StrokeDashCap(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: win32more.Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashOffset(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> Single: ...
    @winrt_mixinmethod
    def put_StrokeDashOffset(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeEndCap(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_mixinmethod
    def put_StrokeEndCap(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: win32more.Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeLineJoin(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionStrokeLineJoin: ...
    @winrt_mixinmethod
    def put_StrokeLineJoin(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: win32more.Windows.UI.Composition.CompositionStrokeLineJoin) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeMiterLimit(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> Single: ...
    @winrt_mixinmethod
    def put_StrokeMiterLimit(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeStartCap(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> win32more.Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_mixinmethod
    def put_StrokeStartCap(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: win32more.Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: win32more.Windows.UI.Composition.ICompositionSpriteShape) -> Single: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: win32more.Windows.UI.Composition.ICompositionSpriteShape, value: Single) -> Void: ...
    FillBrush = property(get_FillBrush, put_FillBrush)
    Geometry = property(get_Geometry, put_Geometry)
    IsStrokeNonScaling = property(get_IsStrokeNonScaling, put_IsStrokeNonScaling)
    StrokeBrush = property(get_StrokeBrush, put_StrokeBrush)
    StrokeDashArray = property(get_StrokeDashArray, None)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeEndCap = property(get_StrokeEndCap, put_StrokeEndCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeStartCap = property(get_StrokeStartCap, put_StrokeStartCap)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
CompositionStretch = Int32
CompositionStretch_None: CompositionStretch = 0
CompositionStretch_Fill: CompositionStretch = 1
CompositionStretch_Uniform: CompositionStretch = 2
CompositionStretch_UniformToFill: CompositionStretch = 3
CompositionStrokeCap = Int32
CompositionStrokeCap_Flat: CompositionStrokeCap = 0
CompositionStrokeCap_Square: CompositionStrokeCap = 1
CompositionStrokeCap_Round: CompositionStrokeCap = 2
CompositionStrokeCap_Triangle: CompositionStrokeCap = 3
class CompositionStrokeDashArray(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.Foundation.Collections.IVector[Single]
    _classid_ = 'Windows.UI.Composition.CompositionStrokeDashArray'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[Single], index: UInt32) -> Single: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[Single]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[Single]) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[Single], value: Single, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[Single], index: UInt32, value: Single) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[Single], index: UInt32, value: Single) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[Single], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[Single], value: Single) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[Single]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[Single]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[Single], startIndex: UInt32, items: Annotated[SZArray[Single], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[Single], items: Annotated[SZArray[Single], 'In']) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[Single]) -> win32more.Windows.Foundation.Collections.IIterator[Single]: ...
    Size = property(get_Size, None)
CompositionStrokeLineJoin = Int32
CompositionStrokeLineJoin_Miter: CompositionStrokeLineJoin = 0
CompositionStrokeLineJoin_Bevel: CompositionStrokeLineJoin = 1
CompositionStrokeLineJoin_Round: CompositionStrokeLineJoin = 2
CompositionStrokeLineJoin_MiterOrBevel: CompositionStrokeLineJoin = 3
class CompositionSurfaceBrush(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionBrush
    default_interface: win32more.Windows.UI.Composition.ICompositionSurfaceBrush
    _classid_ = 'Windows.UI.Composition.CompositionSurfaceBrush'
    @winrt_mixinmethod
    def get_BitmapInterpolationMode(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush) -> win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_mixinmethod
    def put_BitmapInterpolationMode(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush, value: win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush) -> Single: ...
    @winrt_mixinmethod
    def put_HorizontalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush) -> win32more.Windows.UI.Composition.CompositionStretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush, value: win32more.Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_mixinmethod
    def get_Surface(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush) -> win32more.Windows.UI.Composition.ICompositionSurface: ...
    @winrt_mixinmethod
    def put_Surface(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush, value: win32more.Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush) -> Single: ...
    @winrt_mixinmethod
    def put_VerticalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AnchorPoint(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush2, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_SnapToPixels(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush3) -> Boolean: ...
    @winrt_mixinmethod
    def put_SnapToPixels(self: win32more.Windows.UI.Composition.ICompositionSurfaceBrush3, value: Boolean) -> Void: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Stretch = property(get_Stretch, put_Stretch)
    Surface = property(get_Surface, put_Surface)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    SnapToPixels = property(get_SnapToPixels, put_SnapToPixels)
class CompositionTarget(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionTarget
    _classid_ = 'Windows.UI.Composition.CompositionTarget'
    @winrt_mixinmethod
    def get_Root(self: win32more.Windows.UI.Composition.ICompositionTarget) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_Root(self: win32more.Windows.UI.Composition.ICompositionTarget, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    Root = property(get_Root, put_Root)
class CompositionTransform(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionTransform
    _classid_ = 'Windows.UI.Composition.CompositionTransform'
class CompositionViewBox(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionViewBox
    _classid_ = 'Windows.UI.Composition.CompositionViewBox'
    @winrt_mixinmethod
    def get_HorizontalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionViewBox) -> Single: ...
    @winrt_mixinmethod
    def put_HorizontalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionViewBox, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ICompositionViewBox) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ICompositionViewBox, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Composition.ICompositionViewBox) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.UI.Composition.ICompositionViewBox, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: win32more.Windows.UI.Composition.ICompositionViewBox) -> win32more.Windows.UI.Composition.CompositionStretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: win32more.Windows.UI.Composition.ICompositionViewBox, value: win32more.Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_mixinmethod
    def get_VerticalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionViewBox) -> Single: ...
    @winrt_mixinmethod
    def put_VerticalAlignmentRatio(self: win32more.Windows.UI.Composition.ICompositionViewBox, value: Single) -> Void: ...
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
    Stretch = property(get_Stretch, put_Stretch)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
class CompositionVirtualDrawingSurface(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionDrawingSurface
    default_interface: win32more.Windows.UI.Composition.ICompositionVirtualDrawingSurface
    _classid_ = 'Windows.UI.Composition.CompositionVirtualDrawingSurface'
    @winrt_mixinmethod
    def Trim(self: win32more.Windows.UI.Composition.ICompositionVirtualDrawingSurface, rects: Annotated[SZArray[win32more.Windows.Graphics.RectInt32], 'In']) -> Void: ...
class CompositionVisualSurface(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.ICompositionVisualSurface
    _classid_ = 'Windows.UI.Composition.CompositionVisualSurface'
    @winrt_mixinmethod
    def get_SourceVisual(self: win32more.Windows.UI.Composition.ICompositionVisualSurface) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_SourceVisual(self: win32more.Windows.UI.Composition.ICompositionVisualSurface, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_SourceOffset(self: win32more.Windows.UI.Composition.ICompositionVisualSurface) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_SourceOffset(self: win32more.Windows.UI.Composition.ICompositionVisualSurface, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_SourceSize(self: win32more.Windows.UI.Composition.ICompositionVisualSurface) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_SourceSize(self: win32more.Windows.UI.Composition.ICompositionVisualSurface, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    SourceVisual = property(get_SourceVisual, put_SourceVisual)
    SourceOffset = property(get_SourceOffset, put_SourceOffset)
    SourceSize = property(get_SourceSize, put_SourceSize)
class _Compositor_Meta_(ComPtr.__class__):
    pass
class Compositor(ComPtr, metaclass=_Compositor_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.ICompositor
    _classid_ = 'Windows.UI.Composition.Compositor'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def CreateColorKeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.ColorKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateColorBrush(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_mixinmethod
    def CreateColorBrushWithColor(self: win32more.Windows.UI.Composition.ICompositor, color: win32more.Windows.UI.Color) -> win32more.Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_mixinmethod
    def CreateContainerVisual(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.ContainerVisual: ...
    @winrt_mixinmethod
    def CreateCubicBezierEasingFunction(self: win32more.Windows.UI.Composition.ICompositor, controlPoint1: win32more.Windows.Foundation.Numerics.Vector2, controlPoint2: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_mixinmethod
    def CreateEffectFactory(self: win32more.Windows.UI.Composition.ICompositor, graphicsEffect: win32more.Windows.Graphics.Effects.IGraphicsEffect) -> win32more.Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_mixinmethod
    def CreateEffectFactoryWithProperties(self: win32more.Windows.UI.Composition.ICompositor, graphicsEffect: win32more.Windows.Graphics.Effects.IGraphicsEffect, animatableProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_mixinmethod
    def CreateExpressionAnimation(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def CreateExpressionAnimationWithExpression(self: win32more.Windows.UI.Composition.ICompositor, expression: WinRT_String) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_mixinmethod
    def CreateInsetClip(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.InsetClip: ...
    @winrt_mixinmethod
    def CreateInsetClipWithInsets(self: win32more.Windows.UI.Composition.ICompositor, leftInset: Single, topInset: Single, rightInset: Single, bottomInset: Single) -> win32more.Windows.UI.Composition.InsetClip: ...
    @winrt_mixinmethod
    def CreateLinearEasingFunction(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_mixinmethod
    def CreatePropertySet(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_mixinmethod
    def CreateQuaternionKeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.QuaternionKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateScalarKeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.ScalarKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateScopedBatch(self: win32more.Windows.UI.Composition.ICompositor, batchType: win32more.Windows.UI.Composition.CompositionBatchTypes) -> win32more.Windows.UI.Composition.CompositionScopedBatch: ...
    @winrt_mixinmethod
    def CreateSpriteVisual(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.SpriteVisual: ...
    @winrt_mixinmethod
    def CreateSurfaceBrush(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_mixinmethod
    def CreateSurfaceBrushWithSurface(self: win32more.Windows.UI.Composition.ICompositor, surface: win32more.Windows.UI.Composition.ICompositionSurface) -> win32more.Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_mixinmethod
    def CreateTargetForCurrentView(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.CompositionTarget: ...
    @winrt_mixinmethod
    def CreateVector2KeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.Vector2KeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateVector3KeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.Vector3KeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateVector4KeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor) -> win32more.Windows.UI.Composition.Vector4KeyFrameAnimation: ...
    @winrt_mixinmethod
    def GetCommitBatch(self: win32more.Windows.UI.Composition.ICompositor, batchType: win32more.Windows.UI.Composition.CompositionBatchTypes) -> win32more.Windows.UI.Composition.CompositionCommitBatch: ...
    @winrt_mixinmethod
    def CreateAmbientLight(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.AmbientLight: ...
    @winrt_mixinmethod
    def CreateAnimationGroup(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.CompositionAnimationGroup: ...
    @winrt_mixinmethod
    def CreateBackdropBrush(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_mixinmethod
    def CreateDistantLight(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.DistantLight: ...
    @winrt_mixinmethod
    def CreateDropShadow(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.DropShadow: ...
    @winrt_mixinmethod
    def CreateImplicitAnimationCollection(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_mixinmethod
    def CreateLayerVisual(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.LayerVisual: ...
    @winrt_mixinmethod
    def CreateMaskBrush(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.CompositionMaskBrush: ...
    @winrt_mixinmethod
    def CreateNineGridBrush(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.CompositionNineGridBrush: ...
    @winrt_mixinmethod
    def CreatePointLight(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.PointLight: ...
    @winrt_mixinmethod
    def CreateSpotLight(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.SpotLight: ...
    @winrt_mixinmethod
    def CreateStepEasingFunction(self: win32more.Windows.UI.Composition.ICompositor2) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
    @winrt_mixinmethod
    def CreateStepEasingFunctionWithStepCount(self: win32more.Windows.UI.Composition.ICompositor2, stepCount: Int32) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
    @winrt_mixinmethod
    def CreateHostBackdropBrush(self: win32more.Windows.UI.Composition.ICompositor3) -> win32more.Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_mixinmethod
    def CreateColorGradientStop(self: win32more.Windows.UI.Composition.ICompositor4) -> win32more.Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_mixinmethod
    def CreateColorGradientStopWithOffsetAndColor(self: win32more.Windows.UI.Composition.ICompositor4, offset: Single, color: win32more.Windows.UI.Color) -> win32more.Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_mixinmethod
    def CreateLinearGradientBrush(self: win32more.Windows.UI.Composition.ICompositor4) -> win32more.Windows.UI.Composition.CompositionLinearGradientBrush: ...
    @winrt_mixinmethod
    def CreateSpringScalarAnimation(self: win32more.Windows.UI.Composition.ICompositor4) -> win32more.Windows.UI.Composition.SpringScalarNaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateSpringVector2Animation(self: win32more.Windows.UI.Composition.ICompositor4) -> win32more.Windows.UI.Composition.SpringVector2NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateSpringVector3Animation(self: win32more.Windows.UI.Composition.ICompositor4) -> win32more.Windows.UI.Composition.SpringVector3NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.UI.Composition.ICompositor5) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Comment(self: win32more.Windows.UI.Composition.ICompositor5, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalPlaybackRate(self: win32more.Windows.UI.Composition.ICompositor5) -> Single: ...
    @winrt_mixinmethod
    def put_GlobalPlaybackRate(self: win32more.Windows.UI.Composition.ICompositor5, value: Single) -> Void: ...
    @winrt_mixinmethod
    def CreateBounceScalarAnimation(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.BounceScalarNaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateBounceVector2Animation(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.BounceVector2NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateBounceVector3Animation(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.BounceVector3NaturalMotionAnimation: ...
    @winrt_mixinmethod
    def CreateContainerShape(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionContainerShape: ...
    @winrt_mixinmethod
    def CreateEllipseGeometry(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionEllipseGeometry: ...
    @winrt_mixinmethod
    def CreateLineGeometry(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionLineGeometry: ...
    @winrt_mixinmethod
    def CreatePathGeometry(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_mixinmethod
    def CreatePathGeometryWithPath(self: win32more.Windows.UI.Composition.ICompositor5, path: win32more.Windows.UI.Composition.CompositionPath) -> win32more.Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_mixinmethod
    def CreatePathKeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.PathKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateRectangleGeometry(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionRectangleGeometry: ...
    @winrt_mixinmethod
    def CreateRoundedRectangleGeometry(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionRoundedRectangleGeometry: ...
    @winrt_mixinmethod
    def CreateShapeVisual(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.ShapeVisual: ...
    @winrt_mixinmethod
    def CreateSpriteShape(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_mixinmethod
    def CreateSpriteShapeWithGeometry(self: win32more.Windows.UI.Composition.ICompositor5, geometry: win32more.Windows.UI.Composition.CompositionGeometry) -> win32more.Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_mixinmethod
    def CreateViewBox(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.UI.Composition.CompositionViewBox: ...
    @winrt_mixinmethod
    def RequestCommitAsync(self: win32more.Windows.UI.Composition.ICompositor5) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateGeometricClip(self: win32more.Windows.UI.Composition.ICompositor6) -> win32more.Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_mixinmethod
    def CreateGeometricClipWithGeometry(self: win32more.Windows.UI.Composition.ICompositor6, geometry: win32more.Windows.UI.Composition.CompositionGeometry) -> win32more.Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_mixinmethod
    def CreateRedirectVisual(self: win32more.Windows.UI.Composition.ICompositor6) -> win32more.Windows.UI.Composition.RedirectVisual: ...
    @winrt_mixinmethod
    def CreateRedirectVisualWithSourceVisual(self: win32more.Windows.UI.Composition.ICompositor6, source: win32more.Windows.UI.Composition.Visual) -> win32more.Windows.UI.Composition.RedirectVisual: ...
    @winrt_mixinmethod
    def CreateBooleanKeyFrameAnimation(self: win32more.Windows.UI.Composition.ICompositor6) -> win32more.Windows.UI.Composition.BooleanKeyFrameAnimation: ...
    @winrt_mixinmethod
    def CreateProjectedShadowCaster(self: win32more.Windows.UI.Composition.ICompositorWithProjectedShadow) -> win32more.Windows.UI.Composition.CompositionProjectedShadowCaster: ...
    @winrt_mixinmethod
    def CreateProjectedShadow(self: win32more.Windows.UI.Composition.ICompositorWithProjectedShadow) -> win32more.Windows.UI.Composition.CompositionProjectedShadow: ...
    @winrt_mixinmethod
    def CreateProjectedShadowReceiver(self: win32more.Windows.UI.Composition.ICompositorWithProjectedShadow) -> win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver: ...
    @winrt_mixinmethod
    def CreateRadialGradientBrush(self: win32more.Windows.UI.Composition.ICompositorWithRadialGradient) -> win32more.Windows.UI.Composition.CompositionRadialGradientBrush: ...
    @winrt_mixinmethod
    def CreateVisualSurface(self: win32more.Windows.UI.Composition.ICompositorWithVisualSurface) -> win32more.Windows.UI.Composition.CompositionVisualSurface: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Windows.UI.Composition.ICompositor7) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_mixinmethod
    def CreateAnimationPropertyInfo(self: win32more.Windows.UI.Composition.ICompositor7) -> win32more.Windows.UI.Composition.AnimationPropertyInfo: ...
    @winrt_mixinmethod
    def CreateRectangleClip(self: win32more.Windows.UI.Composition.ICompositor7) -> win32more.Windows.UI.Composition.RectangleClip: ...
    @winrt_mixinmethod
    def CreateRectangleClipWithSides(self: win32more.Windows.UI.Composition.ICompositor7, left: Single, top: Single, right: Single, bottom: Single) -> win32more.Windows.UI.Composition.RectangleClip: ...
    @winrt_mixinmethod
    def CreateRectangleClipWithSidesAndRadius(self: win32more.Windows.UI.Composition.ICompositor7, left: Single, top: Single, right: Single, bottom: Single, topLeftRadius: win32more.Windows.Foundation.Numerics.Vector2, topRightRadius: win32more.Windows.Foundation.Numerics.Vector2, bottomRightRadius: win32more.Windows.Foundation.Numerics.Vector2, bottomLeftRadius: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.UI.Composition.RectangleClip: ...
    @winrt_mixinmethod
    def TryCreateBlurredWallpaperBackdropBrush(self: win32more.Windows.UI.Composition.ICompositorWithBlurredWallpaperBackdropBrush) -> win32more.Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_mixinmethod
    def CreateAnimationController(self: win32more.Windows.UI.Composition.ICompositor8) -> win32more.Windows.UI.Composition.AnimationController: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def get_MaxGlobalPlaybackRate(cls: Windows.UI.Composition.ICompositorStatics) -> Single: ...
    @winrt_classmethod
    def get_MinGlobalPlaybackRate(cls: Windows.UI.Composition.ICompositorStatics) -> Single: ...
    Comment = property(get_Comment, put_Comment)
    GlobalPlaybackRate = property(get_GlobalPlaybackRate, put_GlobalPlaybackRate)
    DispatcherQueue = property(get_DispatcherQueue, None)
    _Compositor_Meta_.MaxGlobalPlaybackRate = property(get_MaxGlobalPlaybackRate.__wrapped__, None)
    _Compositor_Meta_.MinGlobalPlaybackRate = property(get_MinGlobalPlaybackRate.__wrapped__, None)
class ContainerVisual(ComPtr):
    extends: win32more.Windows.UI.Composition.Visual
    default_interface: win32more.Windows.UI.Composition.IContainerVisual
    _classid_ = 'Windows.UI.Composition.ContainerVisual'
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Composition.IContainerVisual) -> win32more.Windows.UI.Composition.VisualCollection: ...
    Children = property(get_Children, None)
class CubicBezierEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.ICubicBezierEasingFunction
    _classid_ = 'Windows.UI.Composition.CubicBezierEasingFunction'
    @winrt_mixinmethod
    def get_ControlPoint1(self: win32more.Windows.UI.Composition.ICubicBezierEasingFunction) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def get_ControlPoint2(self: win32more.Windows.UI.Composition.ICubicBezierEasingFunction) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    ControlPoint1 = property(get_ControlPoint1, None)
    ControlPoint2 = property(get_ControlPoint2, None)
class DelegatedInkTrailVisual(ComPtr):
    extends: win32more.Windows.UI.Composition.Visual
    default_interface: win32more.Windows.UI.Composition.IDelegatedInkTrailVisual
    _classid_ = 'Windows.UI.Composition.DelegatedInkTrailVisual'
    @winrt_mixinmethod
    def AddTrailPoints(self: win32more.Windows.UI.Composition.IDelegatedInkTrailVisual, inkPoints: Annotated[SZArray[win32more.Windows.UI.Composition.InkTrailPoint], 'In']) -> UInt32: ...
    @winrt_mixinmethod
    def AddTrailPointsWithPrediction(self: win32more.Windows.UI.Composition.IDelegatedInkTrailVisual, inkPoints: Annotated[SZArray[win32more.Windows.UI.Composition.InkTrailPoint], 'In'], predictedInkPoints: Annotated[SZArray[win32more.Windows.UI.Composition.InkTrailPoint], 'In']) -> UInt32: ...
    @winrt_mixinmethod
    def RemoveTrailPoints(self: win32more.Windows.UI.Composition.IDelegatedInkTrailVisual, generationId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def StartNewTrail(self: win32more.Windows.UI.Composition.IDelegatedInkTrailVisual, color: win32more.Windows.UI.Color) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.IDelegatedInkTrailVisualStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.DelegatedInkTrailVisual: ...
    @winrt_classmethod
    def CreateForSwapChain(cls: Windows.UI.Composition.IDelegatedInkTrailVisualStatics, compositor: win32more.Windows.UI.Composition.Compositor, swapChain: win32more.Windows.UI.Composition.ICompositionSurface) -> win32more.Windows.UI.Composition.DelegatedInkTrailVisual: ...
class DistantLight(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionLight
    default_interface: win32more.Windows.UI.Composition.IDistantLight
    _classid_ = 'Windows.UI.Composition.DistantLight'
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Composition.IDistantLight) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Composition.IDistantLight, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_CoordinateSpace(self: win32more.Windows.UI.Composition.IDistantLight) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CoordinateSpace(self: win32more.Windows.UI.Composition.IDistantLight, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.Composition.IDistantLight) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Windows.UI.Composition.IDistantLight, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Intensity(self: win32more.Windows.UI.Composition.IDistantLight2) -> Single: ...
    @winrt_mixinmethod
    def put_Intensity(self: win32more.Windows.UI.Composition.IDistantLight2, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
    Intensity = property(get_Intensity, put_Intensity)
class DropShadow(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionShadow
    default_interface: win32more.Windows.UI.Composition.IDropShadow
    _classid_ = 'Windows.UI.Composition.DropShadow'
    @winrt_mixinmethod
    def get_BlurRadius(self: win32more.Windows.UI.Composition.IDropShadow) -> Single: ...
    @winrt_mixinmethod
    def put_BlurRadius(self: win32more.Windows.UI.Composition.IDropShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Composition.IDropShadow) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Composition.IDropShadow, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Mask(self: win32more.Windows.UI.Composition.IDropShadow) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Mask(self: win32more.Windows.UI.Composition.IDropShadow, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.IDropShadow) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.IDropShadow, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Windows.UI.Composition.IDropShadow) -> Single: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Windows.UI.Composition.IDropShadow, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_SourcePolicy(self: win32more.Windows.UI.Composition.IDropShadow2) -> win32more.Windows.UI.Composition.CompositionDropShadowSourcePolicy: ...
    @winrt_mixinmethod
    def put_SourcePolicy(self: win32more.Windows.UI.Composition.IDropShadow2, value: win32more.Windows.UI.Composition.CompositionDropShadowSourcePolicy) -> Void: ...
    BlurRadius = property(get_BlurRadius, put_BlurRadius)
    Color = property(get_Color, put_Color)
    Mask = property(get_Mask, put_Mask)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
    SourcePolicy = property(get_SourcePolicy, put_SourcePolicy)
class ElasticEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.IElasticEasingFunction
    _classid_ = 'Windows.UI.Composition.ElasticEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Composition.IElasticEasingFunction) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Oscillations(self: win32more.Windows.UI.Composition.IElasticEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def get_Springiness(self: win32more.Windows.UI.Composition.IElasticEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Oscillations = property(get_Oscillations, None)
    Springiness = property(get_Springiness, None)
class ExponentialEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.IExponentialEasingFunction
    _classid_ = 'Windows.UI.Composition.ExponentialEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Composition.IExponentialEasingFunction) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Exponent(self: win32more.Windows.UI.Composition.IExponentialEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Exponent = property(get_Exponent, None)
class ExpressionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionAnimation
    default_interface: win32more.Windows.UI.Composition.IExpressionAnimation
    _classid_ = 'Windows.UI.Composition.ExpressionAnimation'
    @winrt_mixinmethod
    def get_Expression(self: win32more.Windows.UI.Composition.IExpressionAnimation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Expression(self: win32more.Windows.UI.Composition.IExpressionAnimation, value: WinRT_String) -> Void: ...
    Expression = property(get_Expression, put_Expression)
class IAmbientLight(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAmbientLight'
    _iid_ = Guid('{a48130a1-b7c4-46f7-b9bf-daf43a44e6ee}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class IAmbientLight2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAmbientLight2'
    _iid_ = Guid('{3b64a6bf-5f97-4c94-86e5-042dd386b27d}')
    @winrt_commethod(6)
    def get_Intensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_Intensity(self, value: Single) -> Void: ...
    Intensity = property(get_Intensity, put_Intensity)
class IAnimationController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationController'
    _iid_ = Guid('{c934efd2-0722-4f5f-a4e2-9510f3d43bf7}')
    @winrt_commethod(6)
    def get_PlaybackRate(self) -> Single: ...
    @winrt_commethod(7)
    def put_PlaybackRate(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Progress(self) -> Single: ...
    @winrt_commethod(9)
    def put_Progress(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_ProgressBehavior(self) -> win32more.Windows.UI.Composition.AnimationControllerProgressBehavior: ...
    @winrt_commethod(11)
    def put_ProgressBehavior(self, value: win32more.Windows.UI.Composition.AnimationControllerProgressBehavior) -> Void: ...
    @winrt_commethod(12)
    def Pause(self) -> Void: ...
    @winrt_commethod(13)
    def Resume(self) -> Void: ...
    PlaybackRate = property(get_PlaybackRate, put_PlaybackRate)
    Progress = property(get_Progress, put_Progress)
    ProgressBehavior = property(get_ProgressBehavior, put_ProgressBehavior)
class IAnimationControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationControllerStatics'
    _iid_ = Guid('{e71164df-651b-4800-b9e5-6a3bcfed3365}')
    @winrt_commethod(6)
    def get_MaxPlaybackRate(self) -> Single: ...
    @winrt_commethod(7)
    def get_MinPlaybackRate(self) -> Single: ...
    MaxPlaybackRate = property(get_MaxPlaybackRate, None)
    MinPlaybackRate = property(get_MinPlaybackRate, None)
class IAnimationObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationObject'
    _iid_ = Guid('{e7141e0a-04b8-4fc5-a4dc-195392e57807}')
    @winrt_commethod(6)
    def PopulatePropertyInfo(self, propertyName: WinRT_String, propertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
class IAnimationPropertyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationPropertyInfo'
    _iid_ = Guid('{f4716f05-ed77-4e3c-b328-5c3985b3738f}')
    @winrt_commethod(6)
    def get_AccessMode(self) -> win32more.Windows.UI.Composition.AnimationPropertyAccessMode: ...
    @winrt_commethod(7)
    def put_AccessMode(self, value: win32more.Windows.UI.Composition.AnimationPropertyAccessMode) -> Void: ...
    AccessMode = property(get_AccessMode, put_AccessMode)
class IAnimationPropertyInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IAnimationPropertyInfo2'
    _iid_ = Guid('{591720b4-7472-5218-8b39-dffe615ae6da}')
    @winrt_commethod(6)
    def GetResolvedCompositionObject(self) -> win32more.Windows.UI.Composition.CompositionObject: ...
    @winrt_commethod(7)
    def GetResolvedCompositionObjectProperty(self) -> WinRT_String: ...
class IBackEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBackEasingFunction'
    _iid_ = Guid('{b8560da4-5e3c-545d-b263-7987a2bd27cb}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Amplitude(self) -> Single: ...
    Mode = property(get_Mode, None)
    Amplitude = property(get_Amplitude, None)
class IBooleanKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBooleanKeyFrameAnimation'
    _iid_ = Guid('{95e23a08-d1f4-4972-9770-3efe68d82e14}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Boolean) -> Void: ...
class IBounceEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceEasingFunction'
    _iid_ = Guid('{e7fdb44b-aad5-5174-9421-eef8b75a6a43}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Bounces(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Bounciness(self) -> Single: ...
    Mode = property(get_Mode, None)
    Bounces = property(get_Bounces, None)
    Bounciness = property(get_Bounciness, None)
class IBounceScalarNaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceScalarNaturalMotionAnimation'
    _iid_ = Guid('{baa30dcc-a633-4618-9b06-7f7c72c87cff}')
    @winrt_commethod(6)
    def get_Acceleration(self) -> Single: ...
    @winrt_commethod(7)
    def put_Acceleration(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Restitution(self) -> Single: ...
    @winrt_commethod(9)
    def put_Restitution(self, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class IBounceVector2NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceVector2NaturalMotionAnimation'
    _iid_ = Guid('{da344196-2154-4b3c-88aa-47361204eccd}')
    @winrt_commethod(6)
    def get_Acceleration(self) -> Single: ...
    @winrt_commethod(7)
    def put_Acceleration(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Restitution(self) -> Single: ...
    @winrt_commethod(9)
    def put_Restitution(self, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class IBounceVector3NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IBounceVector3NaturalMotionAnimation'
    _iid_ = Guid('{47dabc31-10d3-4518-86f1-09caf742d113}')
    @winrt_commethod(6)
    def get_Acceleration(self) -> Single: ...
    @winrt_commethod(7)
    def put_Acceleration(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Restitution(self) -> Single: ...
    @winrt_commethod(9)
    def put_Restitution(self, value: Single) -> Void: ...
    Acceleration = property(get_Acceleration, put_Acceleration)
    Restitution = property(get_Restitution, put_Restitution)
class ICircleEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICircleEasingFunction'
    _iid_ = Guid('{1e07222a-6f82-5a28-8748-2e92fc46ee2b}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class IColorKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IColorKeyFrameAnimation'
    _iid_ = Guid('{93adb5e9-8e05-4593-84a3-dca152781e56}')
    @winrt_commethod(6)
    def get_InterpolationColorSpace(self) -> win32more.Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_commethod(7)
    def put_InterpolationColorSpace(self, value: win32more.Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_commethod(8)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(9)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: win32more.Windows.UI.Color, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    InterpolationColorSpace = property(get_InterpolationColorSpace, put_InterpolationColorSpace)
class ICompositionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation'
    _iid_ = Guid('{464c4c2c-1caa-4061-9b40-e13fde1503ca}')
    @winrt_commethod(6)
    def ClearAllParameters(self) -> Void: ...
    @winrt_commethod(7)
    def ClearParameter(self, key: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def SetColorParameter(self, key: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(9)
    def SetMatrix3x2Parameter(self, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(10)
    def SetMatrix4x4Parameter(self, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_commethod(11)
    def SetQuaternionParameter(self, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(12)
    def SetReferenceParameter(self, key: WinRT_String, compositionObject: win32more.Windows.UI.Composition.CompositionObject) -> Void: ...
    @winrt_commethod(13)
    def SetScalarParameter(self, key: WinRT_String, value: Single) -> Void: ...
    @winrt_commethod(14)
    def SetVector2Parameter(self, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(15)
    def SetVector3Parameter(self, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(16)
    def SetVector4Parameter(self, key: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
class ICompositionAnimation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation2'
    _iid_ = Guid('{369b603e-a80f-4948-93e3-ed23fb38c6cb}')
    @winrt_commethod(6)
    def SetBooleanParameter(self, key: WinRT_String, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Target(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Target(self, value: WinRT_String) -> Void: ...
    Target = property(get_Target, put_Target)
class ICompositionAnimation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation3'
    _iid_ = Guid('{d51e030d-7da4-4bd7-bc2d-f4517529f43a}')
    @winrt_commethod(6)
    def get_InitialValueExpressions(self) -> win32more.Windows.UI.Composition.InitialValueExpressionCollection: ...
    InitialValueExpressions = property(get_InitialValueExpressions, None)
class ICompositionAnimation4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimation4'
    _iid_ = Guid('{770137be-76bc-4e23-bfed-fe9cc20f6ec9}')
    @winrt_commethod(6)
    def SetExpressionReferenceParameter(self, parameterName: WinRT_String, source: win32more.Windows.UI.Composition.IAnimationObject) -> Void: ...
class ICompositionAnimationBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimationBase'
    _iid_ = Guid('{1c2c2999-e818-48d3-a6dd-d78c82f8ace9}')
class ICompositionAnimationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimationFactory'
    _iid_ = Guid('{10f6c4fb-6e51-4c25-bbd3-586a9bec3ef4}')
class ICompositionAnimationGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionAnimationGroup'
    _iid_ = Guid('{5e7cc90c-cd14-4e07-8a55-c72527aabdac}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def Add(self, value: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(8)
    def Remove(self, value: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ICompositionBackdropBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBackdropBrush'
    _iid_ = Guid('{c5acae58-3898-499e-8d7f-224e91286a5d}')
class ICompositionBatchCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBatchCompletedEventArgs'
    _iid_ = Guid('{0d00dad0-9464-450a-a562-2e2698b0a812}')
class ICompositionBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBrush'
    _iid_ = Guid('{ab0d7608-30c0-40e9-b568-b60a6bd1fb46}')
class ICompositionBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionBrushFactory'
    _iid_ = Guid('{da53fb4c-4650-47c4-ad76-765379607ed6}')
class ICompositionCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionCapabilities'
    _iid_ = Guid('{8253353e-b517-48bc-b1e8-4b3561a2e181}')
    @winrt_commethod(6)
    def AreEffectsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def AreEffectsFast(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Composition.CompositionCapabilities, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICompositionCapabilitiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionCapabilitiesStatics'
    _iid_ = Guid('{f7b7a86e-6416-49e5-8ddf-afe949e20562}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Composition.CompositionCapabilities: ...
class ICompositionClip(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionClip'
    _iid_ = Guid('{1ccd2a52-cfc7-4ace-9983-146bb8eb6a3c}')
class ICompositionClip2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionClip2'
    _iid_ = Guid('{5893e069-3516-40e1-89e0-5ba924927235}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_CenterPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_CenterPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(13)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(15)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(17)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(18)
    def get_TransformMatrix(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(19)
    def put_TransformMatrix(self, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionClipFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionClipFactory'
    _iid_ = Guid('{b9484caf-20c7-4aed-ac4a-9c78ba1302cf}')
class ICompositionColorBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionColorBrush'
    _iid_ = Guid('{2b264c5e-bf35-4831-8642-cf70c20fff2f}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class ICompositionColorGradientStop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionColorGradientStop'
    _iid_ = Guid('{6f00ca92-c801-4e41-9a8f-a53e20f57778}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Single: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
class ICompositionColorGradientStopCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionColorGradientStopCollection'
    _iid_ = Guid('{9f1d20ec-7b04-4b1d-90bc-9fa32c0cfd26}')
class ICompositionCommitBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionCommitBatch'
    _iid_ = Guid('{0d00dad0-ca07-4400-8c8e-cb5db08559cc}')
    @winrt_commethod(6)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsEnded(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_Completed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head, win32more.Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Completed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
class ICompositionContainerShape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionContainerShape'
    _iid_ = Guid('{4f5e859b-2e5b-44a8-982c-aa0f69c16059}')
    @winrt_commethod(6)
    def get_Shapes(self) -> win32more.Windows.UI.Composition.CompositionShapeCollection: ...
    Shapes = property(get_Shapes, None)
class ICompositionDrawingSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionDrawingSurface'
    _iid_ = Guid('{a166c300-fad0-4d11-9e67-e433162ff49e}')
    @winrt_commethod(6)
    def get_AlphaMode(self) -> win32more.Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_commethod(7)
    def get_PixelFormat(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(8)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    Size = property(get_Size, None)
class ICompositionDrawingSurface2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionDrawingSurface2'
    _iid_ = Guid('{fad0e88b-e354-44e8-8e3d-c4880d5a213f}')
    @winrt_commethod(6)
    def get_SizeInt32(self) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_commethod(7)
    def Resize(self, sizePixels: win32more.Windows.Graphics.SizeInt32) -> Void: ...
    @winrt_commethod(8)
    def Scroll(self, offset: win32more.Windows.Graphics.PointInt32) -> Void: ...
    @winrt_commethod(9)
    def ScrollRect(self, offset: win32more.Windows.Graphics.PointInt32, scrollRect: win32more.Windows.Graphics.RectInt32) -> Void: ...
    @winrt_commethod(10)
    def ScrollWithClip(self, offset: win32more.Windows.Graphics.PointInt32, clipRect: win32more.Windows.Graphics.RectInt32) -> Void: ...
    @winrt_commethod(11)
    def ScrollRectWithClip(self, offset: win32more.Windows.Graphics.PointInt32, clipRect: win32more.Windows.Graphics.RectInt32, scrollRect: win32more.Windows.Graphics.RectInt32) -> Void: ...
    SizeInt32 = property(get_SizeInt32, None)
class ICompositionDrawingSurfaceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionDrawingSurfaceFactory'
    _iid_ = Guid('{9497b00a-312d-46b9-9db3-412fd79464c8}')
class ICompositionEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEasingFunction'
    _iid_ = Guid('{5145e356-bf79-4ea8-8cc2-6b5b472e6c9a}')
class ICompositionEasingFunctionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEasingFunctionFactory'
    _iid_ = Guid('{60840774-3da0-4949-8200-7206c00190a0}')
class ICompositionEasingFunctionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEasingFunctionStatics'
    _iid_ = Guid('{17a766b6-2936-53ea-b5af-c642f4a61083}')
    @winrt_commethod(6)
    def CreateCubicBezierEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, controlPoint1: win32more.Windows.Foundation.Numerics.Vector2, controlPoint2: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_commethod(7)
    def CreateLinearEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_commethod(8)
    def CreateStepEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
    @winrt_commethod(9)
    def CreateStepEasingFunctionWithStepCount(self, owner: win32more.Windows.UI.Composition.Compositor, stepCount: Int32) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
    @winrt_commethod(10)
    def CreateBackEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, amplitude: Single) -> win32more.Windows.UI.Composition.BackEasingFunction: ...
    @winrt_commethod(11)
    def CreateBounceEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, bounces: Int32, bounciness: Single) -> win32more.Windows.UI.Composition.BounceEasingFunction: ...
    @winrt_commethod(12)
    def CreateCircleEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode) -> win32more.Windows.UI.Composition.CircleEasingFunction: ...
    @winrt_commethod(13)
    def CreateElasticEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, oscillations: Int32, springiness: Single) -> win32more.Windows.UI.Composition.ElasticEasingFunction: ...
    @winrt_commethod(14)
    def CreateExponentialEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, exponent: Single) -> win32more.Windows.UI.Composition.ExponentialEasingFunction: ...
    @winrt_commethod(15)
    def CreatePowerEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode, power: Single) -> win32more.Windows.UI.Composition.PowerEasingFunction: ...
    @winrt_commethod(16)
    def CreateSineEasingFunction(self, owner: win32more.Windows.UI.Composition.Compositor, mode: win32more.Windows.UI.Composition.CompositionEasingFunctionMode) -> win32more.Windows.UI.Composition.SineEasingFunction: ...
class ICompositionEffectBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectBrush'
    _iid_ = Guid('{bf7f795e-83cc-44bf-a447-3e3c071789ec}')
    @winrt_commethod(6)
    def GetSourceParameter(self, name: WinRT_String) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def SetSourceParameter(self, name: WinRT_String, source: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
class ICompositionEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectFactory'
    _iid_ = Guid('{be5624af-ba7e-4510-9850-41c0b4ff74df}')
    @winrt_commethod(6)
    def CreateBrush(self) -> win32more.Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_LoadStatus(self) -> win32more.Windows.UI.Composition.CompositionEffectFactoryLoadStatus: ...
    ExtendedError = property(get_ExtendedError, None)
    LoadStatus = property(get_LoadStatus, None)
class ICompositionEffectSourceParameter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectSourceParameter'
    _iid_ = Guid('{858ab13a-3292-4e4e-b3bb-2b6c6544a6ee}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class ICompositionEffectSourceParameterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEffectSourceParameterFactory'
    _iid_ = Guid('{b3d9f276-aba3-4724-acf3-d0397464db1c}')
    @winrt_commethod(6)
    def Create(self, name: WinRT_String) -> win32more.Windows.UI.Composition.CompositionEffectSourceParameter: ...
class ICompositionEllipseGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionEllipseGeometry'
    _iid_ = Guid('{4801f884-f6ad-4b93-afa9-897b64e57b1f}')
    @winrt_commethod(6)
    def get_Center(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_Center(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Radius(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Radius(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Center = property(get_Center, put_Center)
    Radius = property(get_Radius, put_Radius)
class ICompositionGeometricClip(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGeometricClip'
    _iid_ = Guid('{c840b581-81c9-4444-a2c1-ccaece3a50e5}')
    @winrt_commethod(6)
    def get_Geometry(self) -> win32more.Windows.UI.Composition.CompositionGeometry: ...
    @winrt_commethod(7)
    def put_Geometry(self, value: win32more.Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_commethod(8)
    def get_ViewBox(self) -> win32more.Windows.UI.Composition.CompositionViewBox: ...
    @winrt_commethod(9)
    def put_ViewBox(self, value: win32more.Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Geometry = property(get_Geometry, put_Geometry)
    ViewBox = property(get_ViewBox, put_ViewBox)
class ICompositionGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGeometry'
    _iid_ = Guid('{e985217c-6a17-4207-abd8-5fd3dd612a9d}')
    @winrt_commethod(6)
    def get_TrimEnd(self) -> Single: ...
    @winrt_commethod(7)
    def put_TrimEnd(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_TrimOffset(self) -> Single: ...
    @winrt_commethod(9)
    def put_TrimOffset(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_TrimStart(self) -> Single: ...
    @winrt_commethod(11)
    def put_TrimStart(self, value: Single) -> Void: ...
    TrimEnd = property(get_TrimEnd, put_TrimEnd)
    TrimOffset = property(get_TrimOffset, put_TrimOffset)
    TrimStart = property(get_TrimStart, put_TrimStart)
class ICompositionGeometryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGeometryFactory'
    _iid_ = Guid('{bffebfe1-8c25-480b-9f56-fed6b288055d}')
class ICompositionGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGradientBrush'
    _iid_ = Guid('{1d9709e0-ffc6-4c0e-a9ab-34144d4c9098}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_CenterPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_CenterPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_ColorStops(self) -> win32more.Windows.UI.Composition.CompositionColorGradientStopCollection: ...
    @winrt_commethod(11)
    def get_ExtendMode(self) -> win32more.Windows.UI.Composition.CompositionGradientExtendMode: ...
    @winrt_commethod(12)
    def put_ExtendMode(self, value: win32more.Windows.UI.Composition.CompositionGradientExtendMode) -> Void: ...
    @winrt_commethod(13)
    def get_InterpolationSpace(self) -> win32more.Windows.UI.Composition.CompositionColorSpace: ...
    @winrt_commethod(14)
    def put_InterpolationSpace(self, value: win32more.Windows.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_commethod(15)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(16)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(17)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(18)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(19)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(20)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(21)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(22)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(23)
    def get_TransformMatrix(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(24)
    def put_TransformMatrix(self, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    ColorStops = property(get_ColorStops, None)
    ExtendMode = property(get_ExtendMode, put_ExtendMode)
    InterpolationSpace = property(get_InterpolationSpace, put_InterpolationSpace)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionGradientBrush2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGradientBrush2'
    _iid_ = Guid('{899dd5a1-b4c7-4b33-a1b6-264addc26d10}')
    @winrt_commethod(6)
    def get_MappingMode(self) -> win32more.Windows.UI.Composition.CompositionMappingMode: ...
    @winrt_commethod(7)
    def put_MappingMode(self, value: win32more.Windows.UI.Composition.CompositionMappingMode) -> Void: ...
    MappingMode = property(get_MappingMode, put_MappingMode)
class ICompositionGradientBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGradientBrushFactory'
    _iid_ = Guid('{56d765d7-f189-48c9-9c8d-94daf1bec010}')
class ICompositionGraphicsDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice'
    _iid_ = Guid('{fb22c6e1-80a2-4667-9936-dbeaf6eefe95}')
    @winrt_commethod(6)
    def CreateDrawingSurface(self, sizePixels: win32more.Windows.Foundation.Size, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_commethod(7)
    def add_RenderingDeviceReplaced(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Composition.CompositionGraphicsDevice, win32more.Windows.UI.Composition.RenderingDeviceReplacedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_RenderingDeviceReplaced(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICompositionGraphicsDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice2'
    _iid_ = Guid('{0fb8bdf6-c0f0-4bcc-9fb8-084982490d7d}')
    @winrt_commethod(6)
    def CreateDrawingSurface2(self, sizePixels: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionDrawingSurface: ...
    @winrt_commethod(7)
    def CreateVirtualDrawingSurface(self, sizePixels: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionVirtualDrawingSurface: ...
class ICompositionGraphicsDevice3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice3'
    _iid_ = Guid('{37f67514-d3ef-49d1-b69d-0d8eabeb3626}')
    @winrt_commethod(6)
    def CreateMipmapSurface(self, sizePixels: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode) -> win32more.Windows.UI.Composition.CompositionMipmapSurface: ...
    @winrt_commethod(7)
    def Trim(self) -> Void: ...
class ICompositionGraphicsDevice4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionGraphicsDevice4'
    _iid_ = Guid('{5a73bff9-a97f-4cf5-ba46-98ef358e71b1}')
    @winrt_commethod(6)
    def CaptureAsync(self, captureVisual: win32more.Windows.UI.Composition.Visual, size: win32more.Windows.Graphics.SizeInt32, pixelFormat: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, alphaMode: win32more.Windows.Graphics.DirectX.DirectXAlphaMode, sdrBoost: Single) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Composition.ICompositionSurface]: ...
class ICompositionLight(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLight'
    _iid_ = Guid('{41a6d7c2-2e5d-4bc1-b09e-8f0a03e3d8d3}')
    @winrt_commethod(6)
    def get_Targets(self) -> win32more.Windows.UI.Composition.VisualUnorderedCollection: ...
    Targets = property(get_Targets, None)
class ICompositionLight2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLight2'
    _iid_ = Guid('{a7bcda72-f35d-425d-9b98-23f4205f6669}')
    @winrt_commethod(6)
    def get_ExclusionsFromTargets(self) -> win32more.Windows.UI.Composition.VisualUnorderedCollection: ...
    ExclusionsFromTargets = property(get_ExclusionsFromTargets, None)
class ICompositionLight3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLight3'
    _iid_ = Guid('{4b0b00e4-df07-4959-b7a4-4f7e4233f838}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class ICompositionLightFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLightFactory'
    _iid_ = Guid('{069cf306-da3c-4b44-838a-5e03d51ace55}')
class ICompositionLineGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLineGeometry'
    _iid_ = Guid('{dd7615a4-0c9a-4b67-8dce-440a5bf9cdec}')
    @winrt_commethod(6)
    def get_Start(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_Start(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_End(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_End(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Start = property(get_Start, put_Start)
    End = property(get_End, put_End)
class ICompositionLinearGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionLinearGradientBrush'
    _iid_ = Guid('{983bc519-a9db-413c-a2d8-2a9056fc525e}')
    @winrt_commethod(6)
    def get_EndPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_EndPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_StartPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_StartPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
class ICompositionMaskBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionMaskBrush'
    _iid_ = Guid('{522cf09e-be6b-4f41-be49-f9226d471b4a}')
    @winrt_commethod(6)
    def get_Mask(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_Mask(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(8)
    def get_Source(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(9)
    def put_Source(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    Mask = property(get_Mask, put_Mask)
    Source = property(get_Source, put_Source)
class ICompositionMipmapSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionMipmapSurface'
    _iid_ = Guid('{4863675c-cf4a-4b1c-9ece-c5ec0c2b2fe6}')
    @winrt_commethod(6)
    def get_LevelCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_AlphaMode(self) -> win32more.Windows.Graphics.DirectX.DirectXAlphaMode: ...
    @winrt_commethod(8)
    def get_PixelFormat(self) -> win32more.Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(9)
    def get_SizeInt32(self) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_commethod(10)
    def GetDrawingSurfaceForLevel(self, level: UInt32) -> win32more.Windows.UI.Composition.CompositionDrawingSurface: ...
    LevelCount = property(get_LevelCount, None)
    AlphaMode = property(get_AlphaMode, None)
    PixelFormat = property(get_PixelFormat, None)
    SizeInt32 = property(get_SizeInt32, None)
class ICompositionNineGridBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionNineGridBrush'
    _iid_ = Guid('{f25154e4-bc8c-4be7-b80f-8685b83c0186}')
    @winrt_commethod(6)
    def get_BottomInset(self) -> Single: ...
    @winrt_commethod(7)
    def put_BottomInset(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_BottomInsetScale(self) -> Single: ...
    @winrt_commethod(9)
    def put_BottomInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_IsCenterHollow(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsCenterHollow(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_LeftInset(self) -> Single: ...
    @winrt_commethod(13)
    def put_LeftInset(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_LeftInsetScale(self) -> Single: ...
    @winrt_commethod(15)
    def put_LeftInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_RightInset(self) -> Single: ...
    @winrt_commethod(17)
    def put_RightInset(self, value: Single) -> Void: ...
    @winrt_commethod(18)
    def get_RightInsetScale(self) -> Single: ...
    @winrt_commethod(19)
    def put_RightInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_Source(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(21)
    def put_Source(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(22)
    def get_TopInset(self) -> Single: ...
    @winrt_commethod(23)
    def put_TopInset(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_TopInsetScale(self) -> Single: ...
    @winrt_commethod(25)
    def put_TopInsetScale(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def SetInsets(self, inset: Single) -> Void: ...
    @winrt_commethod(27)
    def SetInsetsWithValues(self, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    @winrt_commethod(28)
    def SetInsetScales(self, scale: Single) -> Void: ...
    @winrt_commethod(29)
    def SetInsetScalesWithValues(self, left: Single, top: Single, right: Single, bottom: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    BottomInsetScale = property(get_BottomInsetScale, put_BottomInsetScale)
    IsCenterHollow = property(get_IsCenterHollow, put_IsCenterHollow)
    LeftInset = property(get_LeftInset, put_LeftInset)
    LeftInsetScale = property(get_LeftInsetScale, put_LeftInsetScale)
    RightInset = property(get_RightInset, put_RightInset)
    RightInsetScale = property(get_RightInsetScale, put_RightInsetScale)
    Source = property(get_Source, put_Source)
    TopInset = property(get_TopInset, put_TopInset)
    TopInsetScale = property(get_TopInsetScale, put_TopInsetScale)
class ICompositionObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject'
    _iid_ = Guid('{bcb4ad45-7609-4550-934f-16002a68fded}')
    @winrt_commethod(6)
    def get_Compositor(self) -> win32more.Windows.UI.Composition.Compositor: ...
    @winrt_commethod(7)
    def get_Dispatcher(self) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_commethod(8)
    def get_Properties(self) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_commethod(9)
    def StartAnimation(self, propertyName: WinRT_String, animation: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(10)
    def StopAnimation(self, propertyName: WinRT_String) -> Void: ...
    Compositor = property(get_Compositor, None)
    Dispatcher = property(get_Dispatcher, None)
    Properties = property(get_Properties, None)
class ICompositionObject2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject2'
    _iid_ = Guid('{ef874ea1-5cff-4b68-9e30-a1519d08ba03}')
    @winrt_commethod(6)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Comment(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_ImplicitAnimations(self) -> win32more.Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_commethod(9)
    def put_ImplicitAnimations(self, value: win32more.Windows.UI.Composition.ImplicitAnimationCollection) -> Void: ...
    @winrt_commethod(10)
    def StartAnimationGroup(self, value: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(11)
    def StopAnimationGroup(self, value: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    Comment = property(get_Comment, put_Comment)
    ImplicitAnimations = property(get_ImplicitAnimations, put_ImplicitAnimations)
class ICompositionObject3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject3'
    _iid_ = Guid('{4bc27925-dacd-4cf2-98b1-986b76e7ebe6}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class ICompositionObject4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject4'
    _iid_ = Guid('{0bb3784c-346b-4a7c-966b-7310966553d5}')
    @winrt_commethod(6)
    def TryGetAnimationController(self, propertyName: WinRT_String) -> win32more.Windows.UI.Composition.AnimationController: ...
class ICompositionObject5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObject5'
    _iid_ = Guid('{1d7f391b-a130-5265-a62b-60b8e668965a}')
    @winrt_commethod(6)
    def StartAnimationWithController(self, propertyName: WinRT_String, animation: win32more.Windows.UI.Composition.CompositionAnimation, animationController: win32more.Windows.UI.Composition.AnimationController) -> Void: ...
class ICompositionObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObjectFactory'
    _iid_ = Guid('{51205c5e-558a-4f2a-8d39-37bfe1e20ddd}')
class ICompositionObjectStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionObjectStatics'
    _iid_ = Guid('{c1ed052f-1ba2-44ba-a904-6a882a0a5adb}')
    @winrt_commethod(6)
    def StartAnimationWithIAnimationObject(self, target: win32more.Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, animation: win32more.Windows.UI.Composition.CompositionAnimation) -> Void: ...
    @winrt_commethod(7)
    def StartAnimationGroupWithIAnimationObject(self, target: win32more.Windows.UI.Composition.IAnimationObject, animation: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
class ICompositionPath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPath'
    _iid_ = Guid('{66da1d5f-2e10-4f22-8a06-0a8151919e60}')
class ICompositionPathFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPathFactory'
    _iid_ = Guid('{9c1e8c6a-0f33-4751-9437-eb3fb9d3ab07}')
    @winrt_commethod(6)
    def Create(self, source: win32more.Windows.Graphics.IGeometrySource2D) -> win32more.Windows.UI.Composition.CompositionPath: ...
class ICompositionPathGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPathGeometry'
    _iid_ = Guid('{0b6a417e-2c77-4c23-af5e-6304c147bb61}')
    @winrt_commethod(6)
    def get_Path(self) -> win32more.Windows.UI.Composition.CompositionPath: ...
    @winrt_commethod(7)
    def put_Path(self, value: win32more.Windows.UI.Composition.CompositionPath) -> Void: ...
    Path = property(get_Path, put_Path)
class ICompositionProjectedShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadow'
    _iid_ = Guid('{285b8e72-4328-523f-bcf2-5557c52c3b25}')
    @winrt_commethod(6)
    def get_BlurRadiusMultiplier(self) -> Single: ...
    @winrt_commethod(7)
    def put_BlurRadiusMultiplier(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Casters(self) -> win32more.Windows.UI.Composition.CompositionProjectedShadowCasterCollection: ...
    @winrt_commethod(9)
    def get_LightSource(self) -> win32more.Windows.UI.Composition.CompositionLight: ...
    @winrt_commethod(10)
    def put_LightSource(self, value: win32more.Windows.UI.Composition.CompositionLight) -> Void: ...
    @winrt_commethod(11)
    def get_MaxBlurRadius(self) -> Single: ...
    @winrt_commethod(12)
    def put_MaxBlurRadius(self, value: Single) -> Void: ...
    @winrt_commethod(13)
    def get_MinBlurRadius(self) -> Single: ...
    @winrt_commethod(14)
    def put_MinBlurRadius(self, value: Single) -> Void: ...
    @winrt_commethod(15)
    def get_Receivers(self) -> win32more.Windows.UI.Composition.CompositionProjectedShadowReceiverUnorderedCollection: ...
    BlurRadiusMultiplier = property(get_BlurRadiusMultiplier, put_BlurRadiusMultiplier)
    Casters = property(get_Casters, None)
    LightSource = property(get_LightSource, put_LightSource)
    MaxBlurRadius = property(get_MaxBlurRadius, put_MaxBlurRadius)
    MinBlurRadius = property(get_MinBlurRadius, put_MinBlurRadius)
    Receivers = property(get_Receivers, None)
class ICompositionProjectedShadowCaster(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowCaster'
    _iid_ = Guid('{b1d7d426-1e36-5a62-be56-a16112fdd148}')
    @winrt_commethod(6)
    def get_Brush(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_Brush(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(8)
    def get_CastingVisual(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(9)
    def put_CastingVisual(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    Brush = property(get_Brush, put_Brush)
    CastingVisual = property(get_CastingVisual, put_CastingVisual)
class ICompositionProjectedShadowCasterCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowCasterCollection'
    _iid_ = Guid('{d2525c0c-e07f-58a3-ac91-37f73ee91740}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def InsertAbove(self, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster, reference: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(8)
    def InsertAtBottom(self, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(9)
    def InsertAtTop(self, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(10)
    def InsertBelow(self, newCaster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster, reference: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(11)
    def Remove(self, caster: win32more.Windows.UI.Composition.CompositionProjectedShadowCaster) -> Void: ...
    @winrt_commethod(12)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ICompositionProjectedShadowCasterCollectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowCasterCollectionStatics'
    _iid_ = Guid('{56fbb136-e94f-5299-ab5b-6e15e38bd899}')
    @winrt_commethod(6)
    def get_MaxRespectedCasters(self) -> Int32: ...
    MaxRespectedCasters = property(get_MaxRespectedCasters, None)
class ICompositionProjectedShadowReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowReceiver'
    _iid_ = Guid('{1377985a-6a49-536a-9be4-a96a8e5298a9}')
    @winrt_commethod(6)
    def get_ReceivingVisual(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_ReceivingVisual(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    ReceivingVisual = property(get_ReceivingVisual, put_ReceivingVisual)
class ICompositionProjectedShadowReceiverUnorderedCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionProjectedShadowReceiverUnorderedCollection'
    _iid_ = Guid('{02b3e3b7-27d2-599f-ac4b-ab787cdde6fd}')
    @winrt_commethod(6)
    def Add(self, value: win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_commethod(7)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(8)
    def Remove(self, value: win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ICompositionPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPropertySet'
    _iid_ = Guid('{c9d6d202-5f67-4453-9117-9eadd430d3c2}')
    @winrt_commethod(6)
    def InsertColor(self, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(7)
    def InsertMatrix3x2(self, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(8)
    def InsertMatrix4x4(self, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_commethod(9)
    def InsertQuaternion(self, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(10)
    def InsertScalar(self, propertyName: WinRT_String, value: Single) -> Void: ...
    @winrt_commethod(11)
    def InsertVector2(self, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def InsertVector3(self, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(13)
    def InsertVector4(self, propertyName: WinRT_String, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(14)
    def TryGetColor(self, propertyName: WinRT_String, value: POINTER(win32more.Windows.UI.Color_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(15)
    def TryGetMatrix3x2(self, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Matrix3x2_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(16)
    def TryGetMatrix4x4(self, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Matrix4x4_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(17)
    def TryGetQuaternion(self, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Quaternion_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(18)
    def TryGetScalar(self, propertyName: WinRT_String, value: POINTER(Single)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(19)
    def TryGetVector2(self, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Vector2_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(20)
    def TryGetVector3(self, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Vector3_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
    @winrt_commethod(21)
    def TryGetVector4(self, propertyName: WinRT_String, value: POINTER(win32more.Windows.Foundation.Numerics.Vector4_head)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
class ICompositionPropertySet2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionPropertySet2'
    _iid_ = Guid('{de80731e-a211-4455-8880-7d0f3f6a44fd}')
    @winrt_commethod(6)
    def InsertBoolean(self, propertyName: WinRT_String, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def TryGetBoolean(self, propertyName: WinRT_String, value: POINTER(Boolean)) -> win32more.Windows.UI.Composition.CompositionGetValueStatus: ...
class ICompositionRadialGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionRadialGradientBrush'
    _iid_ = Guid('{3d3b50c5-e3fa-4ce2-b9fc-3ee12561788f}')
    @winrt_commethod(6)
    def get_EllipseCenter(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_EllipseCenter(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_EllipseRadius(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_EllipseRadius(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_GradientOriginOffset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_GradientOriginOffset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    EllipseCenter = property(get_EllipseCenter, put_EllipseCenter)
    EllipseRadius = property(get_EllipseRadius, put_EllipseRadius)
    GradientOriginOffset = property(get_GradientOriginOffset, put_GradientOriginOffset)
class ICompositionRectangleGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionRectangleGeometry'
    _iid_ = Guid('{0cd51428-5356-4246-aecf-7a0b76975400}')
    @winrt_commethod(6)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Size(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Size(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class ICompositionRoundedRectangleGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionRoundedRectangleGeometry'
    _iid_ = Guid('{8770c822-1d50-4b8b-b013-7c9a0e46935f}')
    @winrt_commethod(6)
    def get_CornerRadius(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_CornerRadius(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Size(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Size(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    CornerRadius = property(get_CornerRadius, put_CornerRadius)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
class ICompositionScopedBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionScopedBatch'
    _iid_ = Guid('{0d00dad0-fb07-46fd-8c72-6280d1a3d1dd}')
    @winrt_commethod(6)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsEnded(self) -> Boolean: ...
    @winrt_commethod(8)
    def End(self) -> Void: ...
    @winrt_commethod(9)
    def Resume(self) -> Void: ...
    @winrt_commethod(10)
    def Suspend(self) -> Void: ...
    @winrt_commethod(11)
    def add_Completed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head, win32more.Windows.UI.Composition.CompositionBatchCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Completed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsActive = property(get_IsActive, None)
    IsEnded = property(get_IsEnded, None)
class ICompositionShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShadow'
    _iid_ = Guid('{329e52e2-4335-49cc-b14a-37782d10f0c4}')
class ICompositionShadowFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShadowFactory'
    _iid_ = Guid('{221f492f-dcba-4b91-999e-1dc217a01530}')
class ICompositionShape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShape'
    _iid_ = Guid('{b47ce2f7-9a88-42c4-9e87-2e500ca8688c}')
    @winrt_commethod(6)
    def get_CenterPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_CenterPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(11)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(13)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(15)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(16)
    def get_TransformMatrix(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(17)
    def put_TransformMatrix(self, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionShapeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionShapeFactory'
    _iid_ = Guid('{1dfc36d0-b05a-44ef-82b0-12118bcd4cd0}')
class ICompositionSpriteShape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSpriteShape'
    _iid_ = Guid('{401b61bb-0007-4363-b1f3-6bcc003fb83e}')
    @winrt_commethod(6)
    def get_FillBrush(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_FillBrush(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(8)
    def get_Geometry(self) -> win32more.Windows.UI.Composition.CompositionGeometry: ...
    @winrt_commethod(9)
    def put_Geometry(self, value: win32more.Windows.UI.Composition.CompositionGeometry) -> Void: ...
    @winrt_commethod(10)
    def get_IsStrokeNonScaling(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsStrokeNonScaling(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeBrush(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(13)
    def put_StrokeBrush(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(14)
    def get_StrokeDashArray(self) -> win32more.Windows.UI.Composition.CompositionStrokeDashArray: ...
    @winrt_commethod(15)
    def get_StrokeDashCap(self) -> win32more.Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_commethod(16)
    def put_StrokeDashCap(self, value: win32more.Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_commethod(17)
    def get_StrokeDashOffset(self) -> Single: ...
    @winrt_commethod(18)
    def put_StrokeDashOffset(self, value: Single) -> Void: ...
    @winrt_commethod(19)
    def get_StrokeEndCap(self) -> win32more.Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_commethod(20)
    def put_StrokeEndCap(self, value: win32more.Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_commethod(21)
    def get_StrokeLineJoin(self) -> win32more.Windows.UI.Composition.CompositionStrokeLineJoin: ...
    @winrt_commethod(22)
    def put_StrokeLineJoin(self, value: win32more.Windows.UI.Composition.CompositionStrokeLineJoin) -> Void: ...
    @winrt_commethod(23)
    def get_StrokeMiterLimit(self) -> Single: ...
    @winrt_commethod(24)
    def put_StrokeMiterLimit(self, value: Single) -> Void: ...
    @winrt_commethod(25)
    def get_StrokeStartCap(self) -> win32more.Windows.UI.Composition.CompositionStrokeCap: ...
    @winrt_commethod(26)
    def put_StrokeStartCap(self, value: win32more.Windows.UI.Composition.CompositionStrokeCap) -> Void: ...
    @winrt_commethod(27)
    def get_StrokeThickness(self) -> Single: ...
    @winrt_commethod(28)
    def put_StrokeThickness(self, value: Single) -> Void: ...
    FillBrush = property(get_FillBrush, put_FillBrush)
    Geometry = property(get_Geometry, put_Geometry)
    IsStrokeNonScaling = property(get_IsStrokeNonScaling, put_IsStrokeNonScaling)
    StrokeBrush = property(get_StrokeBrush, put_StrokeBrush)
    StrokeDashArray = property(get_StrokeDashArray, None)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeEndCap = property(get_StrokeEndCap, put_StrokeEndCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeStartCap = property(get_StrokeStartCap, put_StrokeStartCap)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
class ICompositionSupportsSystemBackdrop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSupportsSystemBackdrop'
    _iid_ = Guid('{397dafe4-b6c2-5bb9-951d-f5707de8b7bc}')
    @winrt_commethod(6)
    def get_SystemBackdrop(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_SystemBackdrop(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    SystemBackdrop = property(get_SystemBackdrop, put_SystemBackdrop)
class ICompositionSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurface'
    _iid_ = Guid('{1527540d-42c7-47a6-a408-668f79a90dfb}')
class ICompositionSurfaceBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceBrush'
    _iid_ = Guid('{ad016d79-1e4c-4c0d-9c29-83338c87c162}')
    @winrt_commethod(6)
    def get_BitmapInterpolationMode(self) -> win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_commethod(7)
    def put_BitmapInterpolationMode(self, value: win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_commethod(8)
    def get_HorizontalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(9)
    def put_HorizontalAlignmentRatio(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_Stretch(self) -> win32more.Windows.UI.Composition.CompositionStretch: ...
    @winrt_commethod(11)
    def put_Stretch(self, value: win32more.Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_commethod(12)
    def get_Surface(self) -> win32more.Windows.UI.Composition.ICompositionSurface: ...
    @winrt_commethod(13)
    def put_Surface(self, value: win32more.Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_commethod(14)
    def get_VerticalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(15)
    def put_VerticalAlignmentRatio(self, value: Single) -> Void: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Stretch = property(get_Stretch, put_Stretch)
    Surface = property(get_Surface, put_Surface)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
class ICompositionSurfaceBrush2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceBrush2'
    _iid_ = Guid('{d27174d5-64f5-4692-9dc7-71b61d7e5880}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_CenterPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_CenterPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(13)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(15)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(17)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(18)
    def get_TransformMatrix(self) -> win32more.Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(19)
    def put_TransformMatrix(self, value: win32more.Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Offset = property(get_Offset, put_Offset)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    Scale = property(get_Scale, put_Scale)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class ICompositionSurfaceBrush3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceBrush3'
    _iid_ = Guid('{550bb289-1fe0-42e5-8195-1eefa87ff08e}')
    @winrt_commethod(6)
    def get_SnapToPixels(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SnapToPixels(self, value: Boolean) -> Void: ...
    SnapToPixels = property(get_SnapToPixels, put_SnapToPixels)
class ICompositionSurfaceFacade(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionSurfaceFacade'
    _iid_ = Guid('{e01622c8-2332-55c7-8868-a7312c5c229d}')
    @winrt_commethod(6)
    def GetRealSurface(self) -> win32more.Windows.UI.Composition.ICompositionSurface: ...
class ICompositionTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTarget'
    _iid_ = Guid('{a1bea8ba-d726-4663-8129-6b5e7927ffa6}')
    @winrt_commethod(6)
    def get_Root(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_Root(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    Root = property(get_Root, put_Root)
class ICompositionTargetFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTargetFactory'
    _iid_ = Guid('{93cd9d2b-8516-4b14-a8ce-f49e2119ec42}')
class ICompositionTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTransform'
    _iid_ = Guid('{7cd54529-fbed-4112-abc5-185906dd927c}')
class ICompositionTransformFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionTransformFactory'
    _iid_ = Guid('{aaaeca26-c149-517a-8f72-6bff7a65ce08}')
class ICompositionViewBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionViewBox'
    _iid_ = Guid('{b440bf07-068f-4537-84c6-4ecbe019e1f4}')
    @winrt_commethod(6)
    def get_HorizontalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_HorizontalAlignmentRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_Size(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_Size(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_Stretch(self) -> win32more.Windows.UI.Composition.CompositionStretch: ...
    @winrt_commethod(13)
    def put_Stretch(self, value: win32more.Windows.UI.Composition.CompositionStretch) -> Void: ...
    @winrt_commethod(14)
    def get_VerticalAlignmentRatio(self) -> Single: ...
    @winrt_commethod(15)
    def put_VerticalAlignmentRatio(self, value: Single) -> Void: ...
    HorizontalAlignmentRatio = property(get_HorizontalAlignmentRatio, put_HorizontalAlignmentRatio)
    Offset = property(get_Offset, put_Offset)
    Size = property(get_Size, put_Size)
    Stretch = property(get_Stretch, put_Stretch)
    VerticalAlignmentRatio = property(get_VerticalAlignmentRatio, put_VerticalAlignmentRatio)
class ICompositionVirtualDrawingSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionVirtualDrawingSurface'
    _iid_ = Guid('{a9c384db-8740-4f94-8b9d-b68521e7863d}')
    @winrt_commethod(6)
    def Trim(self, rects: Annotated[SZArray[win32more.Windows.Graphics.RectInt32], 'In']) -> Void: ...
class ICompositionVirtualDrawingSurfaceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionVirtualDrawingSurfaceFactory'
    _iid_ = Guid('{6766106c-d56b-4a49-b1df-5076a0620768}')
class ICompositionVisualSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositionVisualSurface'
    _iid_ = Guid('{b224d803-4f6e-4a3f-8cae-3dc1cda74fc6}')
    @winrt_commethod(6)
    def get_SourceVisual(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_SourceVisual(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def get_SourceOffset(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_SourceOffset(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_SourceSize(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_SourceSize(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    SourceVisual = property(get_SourceVisual, put_SourceVisual)
    SourceOffset = property(get_SourceOffset, put_SourceOffset)
    SourceSize = property(get_SourceSize, put_SourceSize)
class ICompositor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor'
    _iid_ = Guid('{b403ca50-7f8c-4e83-985f-cc45060036d8}')
    @winrt_commethod(6)
    def CreateColorKeyFrameAnimation(self) -> win32more.Windows.UI.Composition.ColorKeyFrameAnimation: ...
    @winrt_commethod(7)
    def CreateColorBrush(self) -> win32more.Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_commethod(8)
    def CreateColorBrushWithColor(self, color: win32more.Windows.UI.Color) -> win32more.Windows.UI.Composition.CompositionColorBrush: ...
    @winrt_commethod(9)
    def CreateContainerVisual(self) -> win32more.Windows.UI.Composition.ContainerVisual: ...
    @winrt_commethod(10)
    def CreateCubicBezierEasingFunction(self, controlPoint1: win32more.Windows.Foundation.Numerics.Vector2, controlPoint2: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.UI.Composition.CubicBezierEasingFunction: ...
    @winrt_commethod(11)
    def CreateEffectFactory(self, graphicsEffect: win32more.Windows.Graphics.Effects.IGraphicsEffect) -> win32more.Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_commethod(12)
    def CreateEffectFactoryWithProperties(self, graphicsEffect: win32more.Windows.Graphics.Effects.IGraphicsEffect, animatableProperties: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.UI.Composition.CompositionEffectFactory: ...
    @winrt_commethod(13)
    def CreateExpressionAnimation(self) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(14)
    def CreateExpressionAnimationWithExpression(self, expression: WinRT_String) -> win32more.Windows.UI.Composition.ExpressionAnimation: ...
    @winrt_commethod(15)
    def CreateInsetClip(self) -> win32more.Windows.UI.Composition.InsetClip: ...
    @winrt_commethod(16)
    def CreateInsetClipWithInsets(self, leftInset: Single, topInset: Single, rightInset: Single, bottomInset: Single) -> win32more.Windows.UI.Composition.InsetClip: ...
    @winrt_commethod(17)
    def CreateLinearEasingFunction(self) -> win32more.Windows.UI.Composition.LinearEasingFunction: ...
    @winrt_commethod(18)
    def CreatePropertySet(self) -> win32more.Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_commethod(19)
    def CreateQuaternionKeyFrameAnimation(self) -> win32more.Windows.UI.Composition.QuaternionKeyFrameAnimation: ...
    @winrt_commethod(20)
    def CreateScalarKeyFrameAnimation(self) -> win32more.Windows.UI.Composition.ScalarKeyFrameAnimation: ...
    @winrt_commethod(21)
    def CreateScopedBatch(self, batchType: win32more.Windows.UI.Composition.CompositionBatchTypes) -> win32more.Windows.UI.Composition.CompositionScopedBatch: ...
    @winrt_commethod(22)
    def CreateSpriteVisual(self) -> win32more.Windows.UI.Composition.SpriteVisual: ...
    @winrt_commethod(23)
    def CreateSurfaceBrush(self) -> win32more.Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_commethod(24)
    def CreateSurfaceBrushWithSurface(self, surface: win32more.Windows.UI.Composition.ICompositionSurface) -> win32more.Windows.UI.Composition.CompositionSurfaceBrush: ...
    @winrt_commethod(25)
    def CreateTargetForCurrentView(self) -> win32more.Windows.UI.Composition.CompositionTarget: ...
    @winrt_commethod(26)
    def CreateVector2KeyFrameAnimation(self) -> win32more.Windows.UI.Composition.Vector2KeyFrameAnimation: ...
    @winrt_commethod(27)
    def CreateVector3KeyFrameAnimation(self) -> win32more.Windows.UI.Composition.Vector3KeyFrameAnimation: ...
    @winrt_commethod(28)
    def CreateVector4KeyFrameAnimation(self) -> win32more.Windows.UI.Composition.Vector4KeyFrameAnimation: ...
    @winrt_commethod(29)
    def GetCommitBatch(self, batchType: win32more.Windows.UI.Composition.CompositionBatchTypes) -> win32more.Windows.UI.Composition.CompositionCommitBatch: ...
class ICompositor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor2'
    _iid_ = Guid('{735081dc-5e24-45da-a38f-e32cc349a9a0}')
    @winrt_commethod(6)
    def CreateAmbientLight(self) -> win32more.Windows.UI.Composition.AmbientLight: ...
    @winrt_commethod(7)
    def CreateAnimationGroup(self) -> win32more.Windows.UI.Composition.CompositionAnimationGroup: ...
    @winrt_commethod(8)
    def CreateBackdropBrush(self) -> win32more.Windows.UI.Composition.CompositionBackdropBrush: ...
    @winrt_commethod(9)
    def CreateDistantLight(self) -> win32more.Windows.UI.Composition.DistantLight: ...
    @winrt_commethod(10)
    def CreateDropShadow(self) -> win32more.Windows.UI.Composition.DropShadow: ...
    @winrt_commethod(11)
    def CreateImplicitAnimationCollection(self) -> win32more.Windows.UI.Composition.ImplicitAnimationCollection: ...
    @winrt_commethod(12)
    def CreateLayerVisual(self) -> win32more.Windows.UI.Composition.LayerVisual: ...
    @winrt_commethod(13)
    def CreateMaskBrush(self) -> win32more.Windows.UI.Composition.CompositionMaskBrush: ...
    @winrt_commethod(14)
    def CreateNineGridBrush(self) -> win32more.Windows.UI.Composition.CompositionNineGridBrush: ...
    @winrt_commethod(15)
    def CreatePointLight(self) -> win32more.Windows.UI.Composition.PointLight: ...
    @winrt_commethod(16)
    def CreateSpotLight(self) -> win32more.Windows.UI.Composition.SpotLight: ...
    @winrt_commethod(17)
    def CreateStepEasingFunction(self) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
    @winrt_commethod(18)
    def CreateStepEasingFunctionWithStepCount(self, stepCount: Int32) -> win32more.Windows.UI.Composition.StepEasingFunction: ...
class ICompositor3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor3'
    _iid_ = Guid('{c9dd8ef0-6eb1-4e3c-a658-675d9c64d4ab}')
    @winrt_commethod(6)
    def CreateHostBackdropBrush(self) -> win32more.Windows.UI.Composition.CompositionBackdropBrush: ...
class ICompositor4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor4'
    _iid_ = Guid('{ae47e78a-7910-4425-a482-a05b758adce9}')
    @winrt_commethod(6)
    def CreateColorGradientStop(self) -> win32more.Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_commethod(7)
    def CreateColorGradientStopWithOffsetAndColor(self, offset: Single, color: win32more.Windows.UI.Color) -> win32more.Windows.UI.Composition.CompositionColorGradientStop: ...
    @winrt_commethod(8)
    def CreateLinearGradientBrush(self) -> win32more.Windows.UI.Composition.CompositionLinearGradientBrush: ...
    @winrt_commethod(9)
    def CreateSpringScalarAnimation(self) -> win32more.Windows.UI.Composition.SpringScalarNaturalMotionAnimation: ...
    @winrt_commethod(10)
    def CreateSpringVector2Animation(self) -> win32more.Windows.UI.Composition.SpringVector2NaturalMotionAnimation: ...
    @winrt_commethod(11)
    def CreateSpringVector3Animation(self) -> win32more.Windows.UI.Composition.SpringVector3NaturalMotionAnimation: ...
class ICompositor5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor5'
    _iid_ = Guid('{48ea31ad-7fcd-4076-a79c-90cc4b852c9b}')
    @winrt_commethod(6)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Comment(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_GlobalPlaybackRate(self) -> Single: ...
    @winrt_commethod(9)
    def put_GlobalPlaybackRate(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def CreateBounceScalarAnimation(self) -> win32more.Windows.UI.Composition.BounceScalarNaturalMotionAnimation: ...
    @winrt_commethod(11)
    def CreateBounceVector2Animation(self) -> win32more.Windows.UI.Composition.BounceVector2NaturalMotionAnimation: ...
    @winrt_commethod(12)
    def CreateBounceVector3Animation(self) -> win32more.Windows.UI.Composition.BounceVector3NaturalMotionAnimation: ...
    @winrt_commethod(13)
    def CreateContainerShape(self) -> win32more.Windows.UI.Composition.CompositionContainerShape: ...
    @winrt_commethod(14)
    def CreateEllipseGeometry(self) -> win32more.Windows.UI.Composition.CompositionEllipseGeometry: ...
    @winrt_commethod(15)
    def CreateLineGeometry(self) -> win32more.Windows.UI.Composition.CompositionLineGeometry: ...
    @winrt_commethod(16)
    def CreatePathGeometry(self) -> win32more.Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_commethod(17)
    def CreatePathGeometryWithPath(self, path: win32more.Windows.UI.Composition.CompositionPath) -> win32more.Windows.UI.Composition.CompositionPathGeometry: ...
    @winrt_commethod(18)
    def CreatePathKeyFrameAnimation(self) -> win32more.Windows.UI.Composition.PathKeyFrameAnimation: ...
    @winrt_commethod(19)
    def CreateRectangleGeometry(self) -> win32more.Windows.UI.Composition.CompositionRectangleGeometry: ...
    @winrt_commethod(20)
    def CreateRoundedRectangleGeometry(self) -> win32more.Windows.UI.Composition.CompositionRoundedRectangleGeometry: ...
    @winrt_commethod(21)
    def CreateShapeVisual(self) -> win32more.Windows.UI.Composition.ShapeVisual: ...
    @winrt_commethod(22)
    def CreateSpriteShape(self) -> win32more.Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_commethod(23)
    def CreateSpriteShapeWithGeometry(self, geometry: win32more.Windows.UI.Composition.CompositionGeometry) -> win32more.Windows.UI.Composition.CompositionSpriteShape: ...
    @winrt_commethod(24)
    def CreateViewBox(self) -> win32more.Windows.UI.Composition.CompositionViewBox: ...
    @winrt_commethod(25)
    def RequestCommitAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Comment = property(get_Comment, put_Comment)
    GlobalPlaybackRate = property(get_GlobalPlaybackRate, put_GlobalPlaybackRate)
class ICompositor6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor6'
    _iid_ = Guid('{7a38b2bd-cec8-4eeb-830f-d8d07aedebc3}')
    @winrt_commethod(6)
    def CreateGeometricClip(self) -> win32more.Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_commethod(7)
    def CreateGeometricClipWithGeometry(self, geometry: win32more.Windows.UI.Composition.CompositionGeometry) -> win32more.Windows.UI.Composition.CompositionGeometricClip: ...
    @winrt_commethod(8)
    def CreateRedirectVisual(self) -> win32more.Windows.UI.Composition.RedirectVisual: ...
    @winrt_commethod(9)
    def CreateRedirectVisualWithSourceVisual(self, source: win32more.Windows.UI.Composition.Visual) -> win32more.Windows.UI.Composition.RedirectVisual: ...
    @winrt_commethod(10)
    def CreateBooleanKeyFrameAnimation(self) -> win32more.Windows.UI.Composition.BooleanKeyFrameAnimation: ...
class ICompositor7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor7'
    _iid_ = Guid('{d3483fad-9a12-53ba-bfc8-88b7ff7977c6}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_commethod(7)
    def CreateAnimationPropertyInfo(self) -> win32more.Windows.UI.Composition.AnimationPropertyInfo: ...
    @winrt_commethod(8)
    def CreateRectangleClip(self) -> win32more.Windows.UI.Composition.RectangleClip: ...
    @winrt_commethod(9)
    def CreateRectangleClipWithSides(self, left: Single, top: Single, right: Single, bottom: Single) -> win32more.Windows.UI.Composition.RectangleClip: ...
    @winrt_commethod(10)
    def CreateRectangleClipWithSidesAndRadius(self, left: Single, top: Single, right: Single, bottom: Single, topLeftRadius: win32more.Windows.Foundation.Numerics.Vector2, topRightRadius: win32more.Windows.Foundation.Numerics.Vector2, bottomRightRadius: win32more.Windows.Foundation.Numerics.Vector2, bottomLeftRadius: win32more.Windows.Foundation.Numerics.Vector2) -> win32more.Windows.UI.Composition.RectangleClip: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class ICompositor8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositor8'
    _iid_ = Guid('{9a0bdee2-fe7b-5f62-a366-9cf8effe2112}')
    @winrt_commethod(6)
    def CreateAnimationController(self) -> win32more.Windows.UI.Composition.AnimationController: ...
class ICompositorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorStatics'
    _iid_ = Guid('{080db93e-121e-4d97-8b74-1dfcf91987ea}')
    @winrt_commethod(6)
    def get_MaxGlobalPlaybackRate(self) -> Single: ...
    @winrt_commethod(7)
    def get_MinGlobalPlaybackRate(self) -> Single: ...
    MaxGlobalPlaybackRate = property(get_MaxGlobalPlaybackRate, None)
    MinGlobalPlaybackRate = property(get_MinGlobalPlaybackRate, None)
class ICompositorWithBlurredWallpaperBackdropBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithBlurredWallpaperBackdropBrush'
    _iid_ = Guid('{0d8fb190-f122-5b8d-9fdd-543b0d8eb7f3}')
    @winrt_commethod(6)
    def TryCreateBlurredWallpaperBackdropBrush(self) -> win32more.Windows.UI.Composition.CompositionBackdropBrush: ...
class ICompositorWithProjectedShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithProjectedShadow'
    _iid_ = Guid('{a2e6330e-8a60-5a38-bb85-b44ea901677c}')
    @winrt_commethod(6)
    def CreateProjectedShadowCaster(self) -> win32more.Windows.UI.Composition.CompositionProjectedShadowCaster: ...
    @winrt_commethod(7)
    def CreateProjectedShadow(self) -> win32more.Windows.UI.Composition.CompositionProjectedShadow: ...
    @winrt_commethod(8)
    def CreateProjectedShadowReceiver(self) -> win32more.Windows.UI.Composition.CompositionProjectedShadowReceiver: ...
class ICompositorWithRadialGradient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithRadialGradient'
    _iid_ = Guid('{98b9c1a7-8e71-4b53-b4a8-69ba5d19dc5b}')
    @winrt_commethod(6)
    def CreateRadialGradientBrush(self) -> win32more.Windows.UI.Composition.CompositionRadialGradientBrush: ...
class ICompositorWithVisualSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICompositorWithVisualSurface'
    _iid_ = Guid('{cfa1658b-0123-4551-8891-89bdcc40322b}')
    @winrt_commethod(6)
    def CreateVisualSurface(self) -> win32more.Windows.UI.Composition.CompositionVisualSurface: ...
class IContainerVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IContainerVisual'
    _iid_ = Guid('{02f6bc74-ed20-4773-afe6-d49b4a93db32}')
    @winrt_commethod(6)
    def get_Children(self) -> win32more.Windows.UI.Composition.VisualCollection: ...
    Children = property(get_Children, None)
class IContainerVisualFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IContainerVisualFactory'
    _iid_ = Guid('{0363a65b-c7da-4d9a-95f4-69b5c8df670b}')
class ICubicBezierEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ICubicBezierEasingFunction'
    _iid_ = Guid('{32350666-c1e8-44f9-96b8-c98acf0ae698}')
    @winrt_commethod(6)
    def get_ControlPoint1(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def get_ControlPoint2(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    ControlPoint1 = property(get_ControlPoint1, None)
    ControlPoint2 = property(get_ControlPoint2, None)
class IDelegatedInkTrailVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDelegatedInkTrailVisual'
    _iid_ = Guid('{856e60b1-e1ab-5b23-8e3d-d513f221c998}')
    @winrt_commethod(6)
    def AddTrailPoints(self, inkPoints: Annotated[SZArray[win32more.Windows.UI.Composition.InkTrailPoint], 'In']) -> UInt32: ...
    @winrt_commethod(7)
    def AddTrailPointsWithPrediction(self, inkPoints: Annotated[SZArray[win32more.Windows.UI.Composition.InkTrailPoint], 'In'], predictedInkPoints: Annotated[SZArray[win32more.Windows.UI.Composition.InkTrailPoint], 'In']) -> UInt32: ...
    @winrt_commethod(8)
    def RemoveTrailPoints(self, generationId: UInt32) -> Void: ...
    @winrt_commethod(9)
    def StartNewTrail(self, color: win32more.Windows.UI.Color) -> Void: ...
class IDelegatedInkTrailVisualStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDelegatedInkTrailVisualStatics'
    _iid_ = Guid('{0daf6bd5-42c6-555c-9267-e0ac663af836}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.DelegatedInkTrailVisual: ...
    @winrt_commethod(7)
    def CreateForSwapChain(self, compositor: win32more.Windows.UI.Composition.Compositor, swapChain: win32more.Windows.UI.Composition.ICompositionSurface) -> win32more.Windows.UI.Composition.DelegatedInkTrailVisual: ...
class IDistantLight(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDistantLight'
    _iid_ = Guid('{318cfafc-5ce3-4b55-ab5d-07a00353ac99}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_CoordinateSpace(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(9)
    def put_CoordinateSpace(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(10)
    def get_Direction(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_Direction(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    Color = property(get_Color, put_Color)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
class IDistantLight2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDistantLight2'
    _iid_ = Guid('{dbcdaa1c-294b-48d7-b60e-76df64aa392b}')
    @winrt_commethod(6)
    def get_Intensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_Intensity(self, value: Single) -> Void: ...
    Intensity = property(get_Intensity, put_Intensity)
class IDropShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDropShadow'
    _iid_ = Guid('{cb977c07-a154-4851-85e7-a8924c84fad8}')
    @winrt_commethod(6)
    def get_BlurRadius(self) -> Single: ...
    @winrt_commethod(7)
    def put_BlurRadius(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_Mask(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(11)
    def put_Mask(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(12)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_Opacity(self) -> Single: ...
    @winrt_commethod(15)
    def put_Opacity(self, value: Single) -> Void: ...
    BlurRadius = property(get_BlurRadius, put_BlurRadius)
    Color = property(get_Color, put_Color)
    Mask = property(get_Mask, put_Mask)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
class IDropShadow2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IDropShadow2'
    _iid_ = Guid('{6c4218bc-15b9-4c2d-8d4a-0767df11977a}')
    @winrt_commethod(6)
    def get_SourcePolicy(self) -> win32more.Windows.UI.Composition.CompositionDropShadowSourcePolicy: ...
    @winrt_commethod(7)
    def put_SourcePolicy(self, value: win32more.Windows.UI.Composition.CompositionDropShadowSourcePolicy) -> Void: ...
    SourcePolicy = property(get_SourcePolicy, put_SourcePolicy)
class IElasticEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IElasticEasingFunction'
    _iid_ = Guid('{66de6285-054e-5594-8475-c22cb51f1bd5}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Oscillations(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Springiness(self) -> Single: ...
    Mode = property(get_Mode, None)
    Oscillations = property(get_Oscillations, None)
    Springiness = property(get_Springiness, None)
class IExponentialEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IExponentialEasingFunction'
    _iid_ = Guid('{6f7d1a51-98d2-5638-a34a-00486554c750}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Exponent(self) -> Single: ...
    Mode = property(get_Mode, None)
    Exponent = property(get_Exponent, None)
class IExpressionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IExpressionAnimation'
    _iid_ = Guid('{6acc5431-7d3d-4bf3-abb6-f44bdc4888c1}')
    @winrt_commethod(6)
    def get_Expression(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Expression(self, value: WinRT_String) -> Void: ...
    Expression = property(get_Expression, put_Expression)
class IImplicitAnimationCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IImplicitAnimationCollection'
    _iid_ = Guid('{0598a3ff-0a92-4c9d-a427-b25519250dbf}')
class IInsetClip(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IInsetClip'
    _iid_ = Guid('{1e73e647-84c7-477a-b474-5880e0442e15}')
    @winrt_commethod(6)
    def get_BottomInset(self) -> Single: ...
    @winrt_commethod(7)
    def put_BottomInset(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_LeftInset(self) -> Single: ...
    @winrt_commethod(9)
    def put_LeftInset(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_RightInset(self) -> Single: ...
    @winrt_commethod(11)
    def put_RightInset(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_TopInset(self) -> Single: ...
    @winrt_commethod(13)
    def put_TopInset(self, value: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    LeftInset = property(get_LeftInset, put_LeftInset)
    RightInset = property(get_RightInset, put_RightInset)
    TopInset = property(get_TopInset, put_TopInset)
class IKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimation'
    _iid_ = Guid('{126e7f22-3ae9-4540-9a8a-deae8a4a4a84}')
    @winrt_commethod(6)
    def get_DelayTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_DelayTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_IterationBehavior(self) -> win32more.Windows.UI.Composition.AnimationIterationBehavior: ...
    @winrt_commethod(11)
    def put_IterationBehavior(self, value: win32more.Windows.UI.Composition.AnimationIterationBehavior) -> Void: ...
    @winrt_commethod(12)
    def get_IterationCount(self) -> Int32: ...
    @winrt_commethod(13)
    def put_IterationCount(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_KeyFrameCount(self) -> Int32: ...
    @winrt_commethod(15)
    def get_StopBehavior(self) -> win32more.Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_commethod(16)
    def put_StopBehavior(self, value: win32more.Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    @winrt_commethod(17)
    def InsertExpressionKeyFrame(self, normalizedProgressKey: Single, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def InsertExpressionKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: WinRT_String, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    DelayTime = property(get_DelayTime, put_DelayTime)
    Duration = property(get_Duration, put_Duration)
    IterationBehavior = property(get_IterationBehavior, put_IterationBehavior)
    IterationCount = property(get_IterationCount, put_IterationCount)
    KeyFrameCount = property(get_KeyFrameCount, None)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
class IKeyFrameAnimation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimation2'
    _iid_ = Guid('{f4b488bb-2940-4ec0-a41a-eb6d801a2f18}')
    @winrt_commethod(6)
    def get_Direction(self) -> win32more.Windows.UI.Composition.AnimationDirection: ...
    @winrt_commethod(7)
    def put_Direction(self, value: win32more.Windows.UI.Composition.AnimationDirection) -> Void: ...
    Direction = property(get_Direction, put_Direction)
class IKeyFrameAnimation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimation3'
    _iid_ = Guid('{845bf0b4-d8de-462f-8753-c80d43c6ff5a}')
    @winrt_commethod(6)
    def get_DelayBehavior(self) -> win32more.Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_commethod(7)
    def put_DelayBehavior(self, value: win32more.Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
class IKeyFrameAnimationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IKeyFrameAnimationFactory'
    _iid_ = Guid('{bf0803f8-712a-4fc1-8c87-970859ed8d2e}')
class ILayerVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ILayerVisual'
    _iid_ = Guid('{af843985-0444-4887-8e83-b40b253f822c}')
    @winrt_commethod(6)
    def get_Effect(self) -> win32more.Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_commethod(7)
    def put_Effect(self, value: win32more.Windows.UI.Composition.CompositionEffectBrush) -> Void: ...
    Effect = property(get_Effect, put_Effect)
class ILayerVisual2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ILayerVisual2'
    _iid_ = Guid('{98f9aeeb-6f23-49f1-90b1-1f59a14fbce3}')
    @winrt_commethod(6)
    def get_Shadow(self) -> win32more.Windows.UI.Composition.CompositionShadow: ...
    @winrt_commethod(7)
    def put_Shadow(self, value: win32more.Windows.UI.Composition.CompositionShadow) -> Void: ...
    Shadow = property(get_Shadow, put_Shadow)
class ILinearEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ILinearEasingFunction'
    _iid_ = Guid('{9400975a-c7a6-46b3-acf7-1a268a0a117d}')
class INaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.INaturalMotionAnimation'
    _iid_ = Guid('{438de12d-769b-4821-a949-284a6547e873}')
    @winrt_commethod(6)
    def get_DelayBehavior(self) -> win32more.Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_commethod(7)
    def put_DelayBehavior(self, value: win32more.Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    @winrt_commethod(8)
    def get_DelayTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_DelayTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StopBehavior(self) -> win32more.Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_commethod(11)
    def put_StopBehavior(self, value: win32more.Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
    DelayTime = property(get_DelayTime, put_DelayTime)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
class INaturalMotionAnimationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.INaturalMotionAnimationFactory'
    _iid_ = Guid('{f53acb06-cf6a-4387-a3fe-5221f3e7e0e0}')
class IPathKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPathKeyFrameAnimation'
    _iid_ = Guid('{9d0d18c9-1576-4b3f-be60-1d5031f5e71b}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, path: win32more.Windows.UI.Composition.CompositionPath) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, path: win32more.Windows.UI.Composition.CompositionPath, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IPointLight(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPointLight'
    _iid_ = Guid('{b18545b3-0c5a-4ab0-bedc-4f3546948272}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_ConstantAttenuation(self) -> Single: ...
    @winrt_commethod(9)
    def put_ConstantAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_CoordinateSpace(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(11)
    def put_CoordinateSpace(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(12)
    def get_LinearAttenuation(self) -> Single: ...
    @winrt_commethod(13)
    def put_LinearAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(15)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(16)
    def get_QuadraticAttenuation(self) -> Single: ...
    @winrt_commethod(17)
    def put_QuadraticAttenuation(self, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
class IPointLight2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPointLight2'
    _iid_ = Guid('{efe98f2c-0678-4f69-b164-a810d995bcb7}')
    @winrt_commethod(6)
    def get_Intensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_Intensity(self, value: Single) -> Void: ...
    Intensity = property(get_Intensity, put_Intensity)
class IPointLight3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPointLight3'
    _iid_ = Guid('{4c0a8367-d4e9-468a-87ae-7ba43ab29485}')
    @winrt_commethod(6)
    def get_MinAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(7)
    def put_MinAttenuationCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_MaxAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(9)
    def put_MaxAttenuationCutoff(self, value: Single) -> Void: ...
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class IPowerEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IPowerEasingFunction'
    _iid_ = Guid('{c3ff53d6-138b-5815-891a-b7f615ccc563}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_commethod(7)
    def get_Power(self) -> Single: ...
    Mode = property(get_Mode, None)
    Power = property(get_Power, None)
class IQuaternionKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IQuaternionKeyFrameAnimation'
    _iid_ = Guid('{404e5835-ecf6-4240-8520-671279cf36bc}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Quaternion, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IRectangleClip(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IRectangleClip'
    _iid_ = Guid('{b3e7549e-00b4-5b53-8be8-353f6c433101}')
    @winrt_commethod(6)
    def get_Bottom(self) -> Single: ...
    @winrt_commethod(7)
    def put_Bottom(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_BottomLeftRadius(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(9)
    def put_BottomLeftRadius(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(10)
    def get_BottomRightRadius(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_BottomRightRadius(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(12)
    def get_Left(self) -> Single: ...
    @winrt_commethod(13)
    def put_Left(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_Right(self) -> Single: ...
    @winrt_commethod(15)
    def put_Right(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_Top(self) -> Single: ...
    @winrt_commethod(17)
    def put_Top(self, value: Single) -> Void: ...
    @winrt_commethod(18)
    def get_TopLeftRadius(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(19)
    def put_TopLeftRadius(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(20)
    def get_TopRightRadius(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(21)
    def put_TopRightRadius(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Bottom = property(get_Bottom, put_Bottom)
    BottomLeftRadius = property(get_BottomLeftRadius, put_BottomLeftRadius)
    BottomRightRadius = property(get_BottomRightRadius, put_BottomRightRadius)
    Left = property(get_Left, put_Left)
    Right = property(get_Right, put_Right)
    Top = property(get_Top, put_Top)
    TopLeftRadius = property(get_TopLeftRadius, put_TopLeftRadius)
    TopRightRadius = property(get_TopRightRadius, put_TopRightRadius)
class IRedirectVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IRedirectVisual'
    _iid_ = Guid('{8cc6e340-8b75-5422-b06f-09ffe9f8617e}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_Source(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    Source = property(get_Source, put_Source)
class IRenderingDeviceReplacedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IRenderingDeviceReplacedEventArgs'
    _iid_ = Guid('{3a31ac7d-28bf-4e7a-8524-71679d480f38}')
    @winrt_commethod(6)
    def get_GraphicsDevice(self) -> win32more.Windows.UI.Composition.CompositionGraphicsDevice: ...
    GraphicsDevice = property(get_GraphicsDevice, None)
class IScalarKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IScalarKeyFrameAnimation'
    _iid_ = Guid('{ae288fa9-252c-4b95-a725-bf85e38000a1}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: Single) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: Single, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IScalarNaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IScalarNaturalMotionAnimation'
    _iid_ = Guid('{94a94581-bf92-495b-b5bd-d2c659430737}')
    @winrt_commethod(6)
    def get_FinalValue(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(7)
    def put_FinalValue(self, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_commethod(8)
    def get_InitialValue(self) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_commethod(9)
    def put_InitialValue(self, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_commethod(10)
    def get_InitialVelocity(self) -> Single: ...
    @winrt_commethod(11)
    def put_InitialVelocity(self, value: Single) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class IScalarNaturalMotionAnimationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IScalarNaturalMotionAnimationFactory'
    _iid_ = Guid('{835aa4fc-671c-41dd-af48-ae8def8b1529}')
class IShapeVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IShapeVisual'
    _iid_ = Guid('{f2bd13c3-ba7e-4b0f-9126-ffb7536b8176}')
    @winrt_commethod(6)
    def get_Shapes(self) -> win32more.Windows.UI.Composition.CompositionShapeCollection: ...
    @winrt_commethod(7)
    def get_ViewBox(self) -> win32more.Windows.UI.Composition.CompositionViewBox: ...
    @winrt_commethod(8)
    def put_ViewBox(self, value: win32more.Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Shapes = property(get_Shapes, None)
    ViewBox = property(get_ViewBox, put_ViewBox)
class ISineEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISineEasingFunction'
    _iid_ = Guid('{f1b518bf-9563-5474-bd13-44b2df4b1d58}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class ISpotLight(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpotLight'
    _iid_ = Guid('{5a9fe273-44a1-4f95-a422-8fa5116bdb44}')
    @winrt_commethod(6)
    def get_ConstantAttenuation(self) -> Single: ...
    @winrt_commethod(7)
    def put_ConstantAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_CoordinateSpace(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(9)
    def put_CoordinateSpace(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(10)
    def get_Direction(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_Direction(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(12)
    def get_InnerConeAngle(self) -> Single: ...
    @winrt_commethod(13)
    def put_InnerConeAngle(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_InnerConeAngleInDegrees(self) -> Single: ...
    @winrt_commethod(15)
    def put_InnerConeAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_InnerConeColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(17)
    def put_InnerConeColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(18)
    def get_LinearAttenuation(self) -> Single: ...
    @winrt_commethod(19)
    def put_LinearAttenuation(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(21)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(22)
    def get_OuterConeAngle(self) -> Single: ...
    @winrt_commethod(23)
    def put_OuterConeAngle(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_OuterConeAngleInDegrees(self) -> Single: ...
    @winrt_commethod(25)
    def put_OuterConeAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def get_OuterConeColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(27)
    def put_OuterConeColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(28)
    def get_QuadraticAttenuation(self) -> Single: ...
    @winrt_commethod(29)
    def put_QuadraticAttenuation(self, value: Single) -> Void: ...
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
    InnerConeAngle = property(get_InnerConeAngle, put_InnerConeAngle)
    InnerConeAngleInDegrees = property(get_InnerConeAngleInDegrees, put_InnerConeAngleInDegrees)
    InnerConeColor = property(get_InnerConeColor, put_InnerConeColor)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    OuterConeAngle = property(get_OuterConeAngle, put_OuterConeAngle)
    OuterConeAngleInDegrees = property(get_OuterConeAngleInDegrees, put_OuterConeAngleInDegrees)
    OuterConeColor = property(get_OuterConeColor, put_OuterConeColor)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
class ISpotLight2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpotLight2'
    _iid_ = Guid('{64ee615e-0686-4dea-a9e8-bc3a8c701459}')
    @winrt_commethod(6)
    def get_InnerConeIntensity(self) -> Single: ...
    @winrt_commethod(7)
    def put_InnerConeIntensity(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_OuterConeIntensity(self) -> Single: ...
    @winrt_commethod(9)
    def put_OuterConeIntensity(self, value: Single) -> Void: ...
    InnerConeIntensity = property(get_InnerConeIntensity, put_InnerConeIntensity)
    OuterConeIntensity = property(get_OuterConeIntensity, put_OuterConeIntensity)
class ISpotLight3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpotLight3'
    _iid_ = Guid('{e4d03eea-131f-480e-859e-b82705b74360}')
    @winrt_commethod(6)
    def get_MinAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(7)
    def put_MinAttenuationCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_MaxAttenuationCutoff(self) -> Single: ...
    @winrt_commethod(9)
    def put_MaxAttenuationCutoff(self, value: Single) -> Void: ...
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class ISpringScalarNaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpringScalarNaturalMotionAnimation'
    _iid_ = Guid('{0572a95f-37f9-4fbe-b87b-5cd03a89501c}')
    @winrt_commethod(6)
    def get_DampingRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_DampingRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Period(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Period(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class ISpringVector2NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpringVector2NaturalMotionAnimation'
    _iid_ = Guid('{23f494b5-ee73-4f0f-a423-402b946df4b3}')
    @winrt_commethod(6)
    def get_DampingRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_DampingRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Period(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Period(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class ISpringVector3NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpringVector3NaturalMotionAnimation'
    _iid_ = Guid('{6c8749df-d57b-4794-8e2d-cecb11e194e5}')
    @winrt_commethod(6)
    def get_DampingRatio(self) -> Single: ...
    @winrt_commethod(7)
    def put_DampingRatio(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_Period(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Period(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class ISpriteVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpriteVisual'
    _iid_ = Guid('{08e05581-1ad1-4f97-9757-402d76e4233b}')
    @winrt_commethod(6)
    def get_Brush(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_Brush(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    Brush = property(get_Brush, put_Brush)
class ISpriteVisual2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.ISpriteVisual2'
    _iid_ = Guid('{588c9664-997a-4850-91fe-53cb58f81ce9}')
    @winrt_commethod(6)
    def get_Shadow(self) -> win32more.Windows.UI.Composition.CompositionShadow: ...
    @winrt_commethod(7)
    def put_Shadow(self, value: win32more.Windows.UI.Composition.CompositionShadow) -> Void: ...
    Shadow = property(get_Shadow, put_Shadow)
class IStepEasingFunction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IStepEasingFunction'
    _iid_ = Guid('{d0caa74b-560c-4a0b-a5f6-206ca8c3ecd6}')
    @winrt_commethod(6)
    def get_FinalStep(self) -> Int32: ...
    @winrt_commethod(7)
    def put_FinalStep(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_InitialStep(self) -> Int32: ...
    @winrt_commethod(9)
    def put_InitialStep(self, value: Int32) -> Void: ...
    @winrt_commethod(10)
    def get_IsFinalStepSingleFrame(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsFinalStepSingleFrame(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsInitialStepSingleFrame(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsInitialStepSingleFrame(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_StepCount(self) -> Int32: ...
    @winrt_commethod(15)
    def put_StepCount(self, value: Int32) -> Void: ...
    FinalStep = property(get_FinalStep, put_FinalStep)
    InitialStep = property(get_InitialStep, put_InitialStep)
    IsFinalStepSingleFrame = property(get_IsFinalStepSingleFrame, put_IsFinalStepSingleFrame)
    IsInitialStepSingleFrame = property(get_IsInitialStepSingleFrame, put_IsInitialStepSingleFrame)
    StepCount = property(get_StepCount, put_StepCount)
class IVector2KeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector2KeyFrameAnimation'
    _iid_ = Guid('{df414515-4e29-4f11-b55e-bf2a6eb36294}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector2, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IVector2NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector2NaturalMotionAnimation'
    _iid_ = Guid('{0f3e0b7d-e512-479d-a00c-77c93a30a395}')
    @winrt_commethod(6)
    def get_FinalValue(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]: ...
    @winrt_commethod(7)
    def put_FinalValue(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_commethod(8)
    def get_InitialValue(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]: ...
    @winrt_commethod(9)
    def put_InitialValue(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_commethod(10)
    def get_InitialVelocity(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_InitialVelocity(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class IVector2NaturalMotionAnimationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector2NaturalMotionAnimationFactory'
    _iid_ = Guid('{8c74ff61-0761-48a2-bddb-6afcc52b89d8}')
class IVector3KeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector3KeyFrameAnimation'
    _iid_ = Guid('{c8039daa-a281-43c2-a73d-b68e3c533c40}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector3, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IVector3NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector3NaturalMotionAnimation'
    _iid_ = Guid('{9c17042c-e2ca-45ad-969e-4e78b7b9ad41}')
    @winrt_commethod(6)
    def get_FinalValue(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def put_FinalValue(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(8)
    def get_InitialValue(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(9)
    def put_InitialValue(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_commethod(10)
    def get_InitialVelocity(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(11)
    def put_InitialVelocity(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class IVector3NaturalMotionAnimationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector3NaturalMotionAnimationFactory'
    _iid_ = Guid('{21a81d2f-0880-457b-ac87-b609018c876d}')
class IVector4KeyFrameAnimation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVector4KeyFrameAnimation'
    _iid_ = Guid('{2457945b-addd-4385-9606-b6a3d5e4e1b9}')
    @winrt_commethod(6)
    def InsertKeyFrame(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(7)
    def InsertKeyFrameWithEasingFunction(self, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector4, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class IVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual'
    _iid_ = Guid('{117e202d-a859-4c89-873b-c2aa566788e3}')
    @winrt_commethod(6)
    def get_AnchorPoint(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(7)
    def put_AnchorPoint(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(8)
    def get_BackfaceVisibility(self) -> win32more.Windows.UI.Composition.CompositionBackfaceVisibility: ...
    @winrt_commethod(9)
    def put_BackfaceVisibility(self, value: win32more.Windows.UI.Composition.CompositionBackfaceVisibility) -> Void: ...
    @winrt_commethod(10)
    def get_BorderMode(self) -> win32more.Windows.UI.Composition.CompositionBorderMode: ...
    @winrt_commethod(11)
    def put_BorderMode(self, value: win32more.Windows.UI.Composition.CompositionBorderMode) -> Void: ...
    @winrt_commethod(12)
    def get_CenterPoint(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_CenterPoint(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_Clip(self) -> win32more.Windows.UI.Composition.CompositionClip: ...
    @winrt_commethod(15)
    def put_Clip(self, value: win32more.Windows.UI.Composition.CompositionClip) -> Void: ...
    @winrt_commethod(16)
    def get_CompositeMode(self) -> win32more.Windows.UI.Composition.CompositionCompositeMode: ...
    @winrt_commethod(17)
    def put_CompositeMode(self, value: win32more.Windows.UI.Composition.CompositionCompositeMode) -> Void: ...
    @winrt_commethod(18)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_Offset(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(21)
    def put_Offset(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(22)
    def get_Opacity(self) -> Single: ...
    @winrt_commethod(23)
    def put_Opacity(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_Orientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(25)
    def put_Orientation(self, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(26)
    def get_Parent(self) -> win32more.Windows.UI.Composition.ContainerVisual: ...
    @winrt_commethod(27)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(28)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(29)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(30)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(31)
    def get_RotationAxis(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(32)
    def put_RotationAxis(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(33)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(34)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(35)
    def get_Size(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(36)
    def put_Size(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_commethod(37)
    def get_TransformMatrix(self) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_commethod(38)
    def put_TransformMatrix(self, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    BackfaceVisibility = property(get_BackfaceVisibility, put_BackfaceVisibility)
    BorderMode = property(get_BorderMode, put_BorderMode)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Clip = property(get_Clip, put_Clip)
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
    IsVisible = property(get_IsVisible, put_IsVisible)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
    Orientation = property(get_Orientation, put_Orientation)
    Parent = property(get_Parent, None)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Size = property(get_Size, put_Size)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
class IVisual2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual2'
    _iid_ = Guid('{3052b611-56c3-4c3e-8bf3-f6e1ad473f06}')
    @winrt_commethod(6)
    def get_ParentForTransform(self) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def put_ParentForTransform(self, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def get_RelativeOffsetAdjustment(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def put_RelativeOffsetAdjustment(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(10)
    def get_RelativeSizeAdjustment(self) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_commethod(11)
    def put_RelativeSizeAdjustment(self, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    ParentForTransform = property(get_ParentForTransform, put_ParentForTransform)
    RelativeOffsetAdjustment = property(get_RelativeOffsetAdjustment, put_RelativeOffsetAdjustment)
    RelativeSizeAdjustment = property(get_RelativeSizeAdjustment, put_RelativeSizeAdjustment)
class IVisual3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual3'
    _iid_ = Guid('{30be580d-f4b6-4ab7-80dd-3738cbac9f2c}')
    @winrt_commethod(6)
    def get_IsHitTestVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsHitTestVisible(self, value: Boolean) -> Void: ...
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
class IVisual4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisual4'
    _iid_ = Guid('{9476bf11-e24b-5bf9-9ebe-6274109b2711}')
    @winrt_commethod(6)
    def get_IsPixelSnappingEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPixelSnappingEnabled(self, value: Boolean) -> Void: ...
    IsPixelSnappingEnabled = property(get_IsPixelSnappingEnabled, put_IsPixelSnappingEnabled)
class IVisualCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualCollection'
    _iid_ = Guid('{8b745505-fd3e-4a98-84a8-e949468c6bcb}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def InsertAbove(self, newChild: win32more.Windows.UI.Composition.Visual, sibling: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def InsertAtBottom(self, newChild: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def InsertAtTop(self, newChild: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(10)
    def InsertBelow(self, newChild: win32more.Windows.UI.Composition.Visual, sibling: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(11)
    def Remove(self, child: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(12)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class IVisualElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualElement'
    _iid_ = Guid('{01e64612-1d82-42f4-8e3f-a722ded33fc7}')
class IVisualElement2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualElement2'
    _iid_ = Guid('{993ae8a0-6057-5e40-918c-e06e0b7e7c64}')
    @winrt_commethod(6)
    def GetVisualInternal(self) -> win32more.Windows.UI.Composition.Visual: ...
class IVisualFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualFactory'
    _iid_ = Guid('{ad0ff93e-b502-4eb5-87b4-9a38a71d0137}')
class IVisualUnorderedCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.IVisualUnorderedCollection'
    _iid_ = Guid('{338faa70-54c8-40a7-8029-c9ceeb0aa250}')
    @winrt_commethod(6)
    def get_Count(self) -> Int32: ...
    @winrt_commethod(7)
    def Add(self, newVisual: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def Remove(self, visual: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def RemoveAll(self) -> Void: ...
    Count = property(get_Count, None)
class ImplicitAnimationCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.IImplicitAnimationCollection
    _classid_ = 'Windows.UI.Composition.ImplicitAnimationCollection'
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase]]: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String) -> win32more.Windows.UI.Composition.ICompositionAnimationBase: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String, value: win32more.Windows.UI.Composition.ICompositionAnimationBase) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.ICompositionAnimationBase]) -> Void: ...
    Size = property(get_Size, None)
class InitialValueExpressionCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]
    _classid_ = 'Windows.UI.Composition.InitialValueExpressionCollection'
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String, value: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    Size = property(get_Size, None)
class InkTrailPoint(EasyCastStructure):
    Point: win32more.Windows.Foundation.Point
    Radius: Single
class InsetClip(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionClip
    default_interface: win32more.Windows.UI.Composition.IInsetClip
    _classid_ = 'Windows.UI.Composition.InsetClip'
    @winrt_mixinmethod
    def get_BottomInset(self: win32more.Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_BottomInset(self: win32more.Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_LeftInset(self: win32more.Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_LeftInset(self: win32more.Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightInset(self: win32more.Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_RightInset(self: win32more.Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopInset(self: win32more.Windows.UI.Composition.IInsetClip) -> Single: ...
    @winrt_mixinmethod
    def put_TopInset(self: win32more.Windows.UI.Composition.IInsetClip, value: Single) -> Void: ...
    BottomInset = property(get_BottomInset, put_BottomInset)
    LeftInset = property(get_LeftInset, put_LeftInset)
    RightInset = property(get_RightInset, put_RightInset)
    TopInset = property(get_TopInset, put_TopInset)
class KeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionAnimation
    default_interface: win32more.Windows.UI.Composition.IKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.KeyFrameAnimation'
    @winrt_mixinmethod
    def get_DelayTime(self: win32more.Windows.UI.Composition.IKeyFrameAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DelayTime(self: win32more.Windows.UI.Composition.IKeyFrameAnimation, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.UI.Composition.IKeyFrameAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.UI.Composition.IKeyFrameAnimation, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IterationBehavior(self: win32more.Windows.UI.Composition.IKeyFrameAnimation) -> win32more.Windows.UI.Composition.AnimationIterationBehavior: ...
    @winrt_mixinmethod
    def put_IterationBehavior(self: win32more.Windows.UI.Composition.IKeyFrameAnimation, value: win32more.Windows.UI.Composition.AnimationIterationBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_IterationCount(self: win32more.Windows.UI.Composition.IKeyFrameAnimation) -> Int32: ...
    @winrt_mixinmethod
    def put_IterationCount(self: win32more.Windows.UI.Composition.IKeyFrameAnimation, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_KeyFrameCount(self: win32more.Windows.UI.Composition.IKeyFrameAnimation) -> Int32: ...
    @winrt_mixinmethod
    def get_StopBehavior(self: win32more.Windows.UI.Composition.IKeyFrameAnimation) -> win32more.Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_mixinmethod
    def put_StopBehavior(self: win32more.Windows.UI.Composition.IKeyFrameAnimation, value: win32more.Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    @winrt_mixinmethod
    def InsertExpressionKeyFrame(self: win32more.Windows.UI.Composition.IKeyFrameAnimation, normalizedProgressKey: Single, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def InsertExpressionKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IKeyFrameAnimation, normalizedProgressKey: Single, value: WinRT_String, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.Composition.IKeyFrameAnimation2) -> win32more.Windows.UI.Composition.AnimationDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Windows.UI.Composition.IKeyFrameAnimation2, value: win32more.Windows.UI.Composition.AnimationDirection) -> Void: ...
    @winrt_mixinmethod
    def get_DelayBehavior(self: win32more.Windows.UI.Composition.IKeyFrameAnimation3) -> win32more.Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_mixinmethod
    def put_DelayBehavior(self: win32more.Windows.UI.Composition.IKeyFrameAnimation3, value: win32more.Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    DelayTime = property(get_DelayTime, put_DelayTime)
    Duration = property(get_Duration, put_Duration)
    IterationBehavior = property(get_IterationBehavior, put_IterationBehavior)
    IterationCount = property(get_IterationCount, put_IterationCount)
    KeyFrameCount = property(get_KeyFrameCount, None)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
    Direction = property(get_Direction, put_Direction)
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
class LayerVisual(ComPtr):
    extends: win32more.Windows.UI.Composition.ContainerVisual
    default_interface: win32more.Windows.UI.Composition.ILayerVisual
    _classid_ = 'Windows.UI.Composition.LayerVisual'
    @winrt_mixinmethod
    def get_Effect(self: win32more.Windows.UI.Composition.ILayerVisual) -> win32more.Windows.UI.Composition.CompositionEffectBrush: ...
    @winrt_mixinmethod
    def put_Effect(self: win32more.Windows.UI.Composition.ILayerVisual, value: win32more.Windows.UI.Composition.CompositionEffectBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Shadow(self: win32more.Windows.UI.Composition.ILayerVisual2) -> win32more.Windows.UI.Composition.CompositionShadow: ...
    @winrt_mixinmethod
    def put_Shadow(self: win32more.Windows.UI.Composition.ILayerVisual2, value: win32more.Windows.UI.Composition.CompositionShadow) -> Void: ...
    Effect = property(get_Effect, put_Effect)
    Shadow = property(get_Shadow, put_Shadow)
class LinearEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.ILinearEasingFunction
    _classid_ = 'Windows.UI.Composition.LinearEasingFunction'
class NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionAnimation
    default_interface: win32more.Windows.UI.Composition.INaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DelayBehavior(self: win32more.Windows.UI.Composition.INaturalMotionAnimation) -> win32more.Windows.UI.Composition.AnimationDelayBehavior: ...
    @winrt_mixinmethod
    def put_DelayBehavior(self: win32more.Windows.UI.Composition.INaturalMotionAnimation, value: win32more.Windows.UI.Composition.AnimationDelayBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_DelayTime(self: win32more.Windows.UI.Composition.INaturalMotionAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DelayTime(self: win32more.Windows.UI.Composition.INaturalMotionAnimation, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StopBehavior(self: win32more.Windows.UI.Composition.INaturalMotionAnimation) -> win32more.Windows.UI.Composition.AnimationStopBehavior: ...
    @winrt_mixinmethod
    def put_StopBehavior(self: win32more.Windows.UI.Composition.INaturalMotionAnimation, value: win32more.Windows.UI.Composition.AnimationStopBehavior) -> Void: ...
    DelayBehavior = property(get_DelayBehavior, put_DelayBehavior)
    DelayTime = property(get_DelayTime, put_DelayTime)
    StopBehavior = property(get_StopBehavior, put_StopBehavior)
class PathKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IPathKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.PathKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IPathKeyFrameAnimation, normalizedProgressKey: Single, path: win32more.Windows.UI.Composition.CompositionPath) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IPathKeyFrameAnimation, normalizedProgressKey: Single, path: win32more.Windows.UI.Composition.CompositionPath, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class PointLight(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionLight
    default_interface: win32more.Windows.UI.Composition.IPointLight
    _classid_ = 'Windows.UI.Composition.PointLight'
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Composition.IPointLight) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Composition.IPointLight, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ConstantAttenuation(self: win32more.Windows.UI.Composition.IPointLight) -> Single: ...
    @winrt_mixinmethod
    def put_ConstantAttenuation(self: win32more.Windows.UI.Composition.IPointLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_CoordinateSpace(self: win32more.Windows.UI.Composition.IPointLight) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CoordinateSpace(self: win32more.Windows.UI.Composition.IPointLight, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_LinearAttenuation(self: win32more.Windows.UI.Composition.IPointLight) -> Single: ...
    @winrt_mixinmethod
    def put_LinearAttenuation(self: win32more.Windows.UI.Composition.IPointLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.IPointLight) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.IPointLight, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_QuadraticAttenuation(self: win32more.Windows.UI.Composition.IPointLight) -> Single: ...
    @winrt_mixinmethod
    def put_QuadraticAttenuation(self: win32more.Windows.UI.Composition.IPointLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Intensity(self: win32more.Windows.UI.Composition.IPointLight2) -> Single: ...
    @winrt_mixinmethod
    def put_Intensity(self: win32more.Windows.UI.Composition.IPointLight2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinAttenuationCutoff(self: win32more.Windows.UI.Composition.IPointLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MinAttenuationCutoff(self: win32more.Windows.UI.Composition.IPointLight3, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MaxAttenuationCutoff(self: win32more.Windows.UI.Composition.IPointLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MaxAttenuationCutoff(self: win32more.Windows.UI.Composition.IPointLight3, value: Single) -> Void: ...
    Color = property(get_Color, put_Color)
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
    Intensity = property(get_Intensity, put_Intensity)
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class PowerEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.IPowerEasingFunction
    _classid_ = 'Windows.UI.Composition.PowerEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Composition.IPowerEasingFunction) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    @winrt_mixinmethod
    def get_Power(self: win32more.Windows.UI.Composition.IPowerEasingFunction) -> Single: ...
    Mode = property(get_Mode, None)
    Power = property(get_Power, None)
class QuaternionKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IQuaternionKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.QuaternionKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IQuaternionKeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IQuaternionKeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Quaternion, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class RectangleClip(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionClip
    default_interface: win32more.Windows.UI.Composition.IRectangleClip
    _classid_ = 'Windows.UI.Composition.RectangleClip'
    @winrt_mixinmethod
    def get_Bottom(self: win32more.Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Bottom(self: win32more.Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_BottomLeftRadius(self: win32more.Windows.UI.Composition.IRectangleClip) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_BottomLeftRadius(self: win32more.Windows.UI.Composition.IRectangleClip, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_BottomRightRadius(self: win32more.Windows.UI.Composition.IRectangleClip) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_BottomRightRadius(self: win32more.Windows.UI.Composition.IRectangleClip, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_Left(self: win32more.Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Left(self: win32more.Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Right(self: win32more.Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Right(self: win32more.Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Top(self: win32more.Windows.UI.Composition.IRectangleClip) -> Single: ...
    @winrt_mixinmethod
    def put_Top(self: win32more.Windows.UI.Composition.IRectangleClip, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopLeftRadius(self: win32more.Windows.UI.Composition.IRectangleClip) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_TopLeftRadius(self: win32more.Windows.UI.Composition.IRectangleClip, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TopRightRadius(self: win32more.Windows.UI.Composition.IRectangleClip) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_TopRightRadius(self: win32more.Windows.UI.Composition.IRectangleClip, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    Bottom = property(get_Bottom, put_Bottom)
    BottomLeftRadius = property(get_BottomLeftRadius, put_BottomLeftRadius)
    BottomRightRadius = property(get_BottomRightRadius, put_BottomRightRadius)
    Left = property(get_Left, put_Left)
    Right = property(get_Right, put_Right)
    Top = property(get_Top, put_Top)
    TopLeftRadius = property(get_TopLeftRadius, put_TopLeftRadius)
    TopRightRadius = property(get_TopRightRadius, put_TopRightRadius)
class RedirectVisual(ComPtr):
    extends: win32more.Windows.UI.Composition.ContainerVisual
    default_interface: win32more.Windows.UI.Composition.IRedirectVisual
    _classid_ = 'Windows.UI.Composition.RedirectVisual'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Composition.IRedirectVisual) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.UI.Composition.IRedirectVisual, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    Source = property(get_Source, put_Source)
class RenderingDeviceReplacedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.IRenderingDeviceReplacedEventArgs
    _classid_ = 'Windows.UI.Composition.RenderingDeviceReplacedEventArgs'
    @winrt_mixinmethod
    def get_GraphicsDevice(self: win32more.Windows.UI.Composition.IRenderingDeviceReplacedEventArgs) -> win32more.Windows.UI.Composition.CompositionGraphicsDevice: ...
    GraphicsDevice = property(get_GraphicsDevice, None)
class ScalarKeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IScalarKeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.ScalarKeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IScalarKeyFrameAnimation, normalizedProgressKey: Single, value: Single) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IScalarKeyFrameAnimation, normalizedProgressKey: Single, value: Single, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class ScalarNaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.NaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.IScalarNaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.ScalarNaturalMotionAnimation'
    @winrt_mixinmethod
    def get_FinalValue(self: win32more.Windows.UI.Composition.IScalarNaturalMotionAnimation) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_FinalValue(self: win32more.Windows.UI.Composition.IScalarNaturalMotionAnimation, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: win32more.Windows.UI.Composition.IScalarNaturalMotionAnimation) -> win32more.Windows.Foundation.IReference[Single]: ...
    @winrt_mixinmethod
    def put_InitialValue(self: win32more.Windows.UI.Composition.IScalarNaturalMotionAnimation, value: win32more.Windows.Foundation.IReference[Single]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialVelocity(self: win32more.Windows.UI.Composition.IScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_InitialVelocity(self: win32more.Windows.UI.Composition.IScalarNaturalMotionAnimation, value: Single) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class ShapeVisual(ComPtr):
    extends: win32more.Windows.UI.Composition.ContainerVisual
    default_interface: win32more.Windows.UI.Composition.IShapeVisual
    _classid_ = 'Windows.UI.Composition.ShapeVisual'
    @winrt_mixinmethod
    def get_Shapes(self: win32more.Windows.UI.Composition.IShapeVisual) -> win32more.Windows.UI.Composition.CompositionShapeCollection: ...
    @winrt_mixinmethod
    def get_ViewBox(self: win32more.Windows.UI.Composition.IShapeVisual) -> win32more.Windows.UI.Composition.CompositionViewBox: ...
    @winrt_mixinmethod
    def put_ViewBox(self: win32more.Windows.UI.Composition.IShapeVisual, value: win32more.Windows.UI.Composition.CompositionViewBox) -> Void: ...
    Shapes = property(get_Shapes, None)
    ViewBox = property(get_ViewBox, put_ViewBox)
class SineEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.ISineEasingFunction
    _classid_ = 'Windows.UI.Composition.SineEasingFunction'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.UI.Composition.ISineEasingFunction) -> win32more.Windows.UI.Composition.CompositionEasingFunctionMode: ...
    Mode = property(get_Mode, None)
class SpotLight(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionLight
    default_interface: win32more.Windows.UI.Composition.ISpotLight
    _classid_ = 'Windows.UI.Composition.SpotLight'
    @winrt_mixinmethod
    def get_ConstantAttenuation(self: win32more.Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_ConstantAttenuation(self: win32more.Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_CoordinateSpace(self: win32more.Windows.UI.Composition.ISpotLight) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_CoordinateSpace(self: win32more.Windows.UI.Composition.ISpotLight, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.Composition.ISpotLight) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Direction(self: win32more.Windows.UI.Composition.ISpotLight, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeAngle(self: win32more.Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_InnerConeAngle(self: win32more.Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeAngleInDegrees(self: win32more.Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_InnerConeAngleInDegrees(self: win32more.Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeColor(self: win32more.Windows.UI.Composition.ISpotLight) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_InnerConeColor(self: win32more.Windows.UI.Composition.ISpotLight, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_LinearAttenuation(self: win32more.Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_LinearAttenuation(self: win32more.Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.ISpotLight) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.ISpotLight, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeAngle(self: win32more.Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_OuterConeAngle(self: win32more.Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeAngleInDegrees(self: win32more.Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_OuterConeAngleInDegrees(self: win32more.Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeColor(self: win32more.Windows.UI.Composition.ISpotLight) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_OuterConeColor(self: win32more.Windows.UI.Composition.ISpotLight, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_QuadraticAttenuation(self: win32more.Windows.UI.Composition.ISpotLight) -> Single: ...
    @winrt_mixinmethod
    def put_QuadraticAttenuation(self: win32more.Windows.UI.Composition.ISpotLight, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InnerConeIntensity(self: win32more.Windows.UI.Composition.ISpotLight2) -> Single: ...
    @winrt_mixinmethod
    def put_InnerConeIntensity(self: win32more.Windows.UI.Composition.ISpotLight2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_OuterConeIntensity(self: win32more.Windows.UI.Composition.ISpotLight2) -> Single: ...
    @winrt_mixinmethod
    def put_OuterConeIntensity(self: win32more.Windows.UI.Composition.ISpotLight2, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MinAttenuationCutoff(self: win32more.Windows.UI.Composition.ISpotLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MinAttenuationCutoff(self: win32more.Windows.UI.Composition.ISpotLight3, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MaxAttenuationCutoff(self: win32more.Windows.UI.Composition.ISpotLight3) -> Single: ...
    @winrt_mixinmethod
    def put_MaxAttenuationCutoff(self: win32more.Windows.UI.Composition.ISpotLight3, value: Single) -> Void: ...
    ConstantAttenuation = property(get_ConstantAttenuation, put_ConstantAttenuation)
    CoordinateSpace = property(get_CoordinateSpace, put_CoordinateSpace)
    Direction = property(get_Direction, put_Direction)
    InnerConeAngle = property(get_InnerConeAngle, put_InnerConeAngle)
    InnerConeAngleInDegrees = property(get_InnerConeAngleInDegrees, put_InnerConeAngleInDegrees)
    InnerConeColor = property(get_InnerConeColor, put_InnerConeColor)
    LinearAttenuation = property(get_LinearAttenuation, put_LinearAttenuation)
    Offset = property(get_Offset, put_Offset)
    OuterConeAngle = property(get_OuterConeAngle, put_OuterConeAngle)
    OuterConeAngleInDegrees = property(get_OuterConeAngleInDegrees, put_OuterConeAngleInDegrees)
    OuterConeColor = property(get_OuterConeColor, put_OuterConeColor)
    QuadraticAttenuation = property(get_QuadraticAttenuation, put_QuadraticAttenuation)
    InnerConeIntensity = property(get_InnerConeIntensity, put_InnerConeIntensity)
    OuterConeIntensity = property(get_OuterConeIntensity, put_OuterConeIntensity)
    MinAttenuationCutoff = property(get_MinAttenuationCutoff, put_MinAttenuationCutoff)
    MaxAttenuationCutoff = property(get_MaxAttenuationCutoff, put_MaxAttenuationCutoff)
class SpringScalarNaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.ScalarNaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.ISpringScalarNaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.SpringScalarNaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DampingRatio(self: win32more.Windows.UI.Composition.ISpringScalarNaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_DampingRatio(self: win32more.Windows.UI.Composition.ISpringScalarNaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Period(self: win32more.Windows.UI.Composition.ISpringScalarNaturalMotionAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Period(self: win32more.Windows.UI.Composition.ISpringScalarNaturalMotionAnimation, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class SpringVector2NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.Vector2NaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.ISpringVector2NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.SpringVector2NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DampingRatio(self: win32more.Windows.UI.Composition.ISpringVector2NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_DampingRatio(self: win32more.Windows.UI.Composition.ISpringVector2NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Period(self: win32more.Windows.UI.Composition.ISpringVector2NaturalMotionAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Period(self: win32more.Windows.UI.Composition.ISpringVector2NaturalMotionAnimation, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class SpringVector3NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.Vector3NaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.ISpringVector3NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.SpringVector3NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_DampingRatio(self: win32more.Windows.UI.Composition.ISpringVector3NaturalMotionAnimation) -> Single: ...
    @winrt_mixinmethod
    def put_DampingRatio(self: win32more.Windows.UI.Composition.ISpringVector3NaturalMotionAnimation, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Period(self: win32more.Windows.UI.Composition.ISpringVector3NaturalMotionAnimation) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Period(self: win32more.Windows.UI.Composition.ISpringVector3NaturalMotionAnimation, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    DampingRatio = property(get_DampingRatio, put_DampingRatio)
    Period = property(get_Period, put_Period)
class SpriteVisual(ComPtr):
    extends: win32more.Windows.UI.Composition.ContainerVisual
    default_interface: win32more.Windows.UI.Composition.ISpriteVisual
    _classid_ = 'Windows.UI.Composition.SpriteVisual'
    @winrt_mixinmethod
    def get_Brush(self: win32more.Windows.UI.Composition.ISpriteVisual) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_Brush(self: win32more.Windows.UI.Composition.ISpriteVisual, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def get_Shadow(self: win32more.Windows.UI.Composition.ISpriteVisual2) -> win32more.Windows.UI.Composition.CompositionShadow: ...
    @winrt_mixinmethod
    def put_Shadow(self: win32more.Windows.UI.Composition.ISpriteVisual2, value: win32more.Windows.UI.Composition.CompositionShadow) -> Void: ...
    Brush = property(get_Brush, put_Brush)
    Shadow = property(get_Shadow, put_Shadow)
class StepEasingFunction(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionEasingFunction
    default_interface: win32more.Windows.UI.Composition.IStepEasingFunction
    _classid_ = 'Windows.UI.Composition.StepEasingFunction'
    @winrt_mixinmethod
    def get_FinalStep(self: win32more.Windows.UI.Composition.IStepEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def put_FinalStep(self: win32more.Windows.UI.Composition.IStepEasingFunction, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_InitialStep(self: win32more.Windows.UI.Composition.IStepEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def put_InitialStep(self: win32more.Windows.UI.Composition.IStepEasingFunction, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_IsFinalStepSingleFrame(self: win32more.Windows.UI.Composition.IStepEasingFunction) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsFinalStepSingleFrame(self: win32more.Windows.UI.Composition.IStepEasingFunction, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsInitialStepSingleFrame(self: win32more.Windows.UI.Composition.IStepEasingFunction) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInitialStepSingleFrame(self: win32more.Windows.UI.Composition.IStepEasingFunction, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StepCount(self: win32more.Windows.UI.Composition.IStepEasingFunction) -> Int32: ...
    @winrt_mixinmethod
    def put_StepCount(self: win32more.Windows.UI.Composition.IStepEasingFunction, value: Int32) -> Void: ...
    FinalStep = property(get_FinalStep, put_FinalStep)
    InitialStep = property(get_InitialStep, put_InitialStep)
    IsFinalStepSingleFrame = property(get_IsFinalStepSingleFrame, put_IsFinalStepSingleFrame)
    IsInitialStepSingleFrame = property(get_IsInitialStepSingleFrame, put_IsInitialStepSingleFrame)
    StepCount = property(get_StepCount, put_StepCount)
class Vector2KeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IVector2KeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.Vector2KeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IVector2KeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IVector2KeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector2, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class Vector2NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.NaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.IVector2NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.Vector2NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_FinalValue(self: win32more.Windows.UI.Composition.IVector2NaturalMotionAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]: ...
    @winrt_mixinmethod
    def put_FinalValue(self: win32more.Windows.UI.Composition.IVector2NaturalMotionAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: win32more.Windows.UI.Composition.IVector2NaturalMotionAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]: ...
    @winrt_mixinmethod
    def put_InitialValue(self: win32more.Windows.UI.Composition.IVector2NaturalMotionAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector2]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialVelocity(self: win32more.Windows.UI.Composition.IVector2NaturalMotionAnimation) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_InitialVelocity(self: win32more.Windows.UI.Composition.IVector2NaturalMotionAnimation, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class Vector3KeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IVector3KeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.Vector3KeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IVector3KeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IVector3KeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector3, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class Vector3NaturalMotionAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.NaturalMotionAnimation
    default_interface: win32more.Windows.UI.Composition.IVector3NaturalMotionAnimation
    _classid_ = 'Windows.UI.Composition.Vector3NaturalMotionAnimation'
    @winrt_mixinmethod
    def get_FinalValue(self: win32more.Windows.UI.Composition.IVector3NaturalMotionAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def put_FinalValue(self: win32more.Windows.UI.Composition.IVector3NaturalMotionAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: win32more.Windows.UI.Composition.IVector3NaturalMotionAnimation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def put_InitialValue(self: win32more.Windows.UI.Composition.IVector3NaturalMotionAnimation, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]) -> Void: ...
    @winrt_mixinmethod
    def get_InitialVelocity(self: win32more.Windows.UI.Composition.IVector3NaturalMotionAnimation) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_InitialVelocity(self: win32more.Windows.UI.Composition.IVector3NaturalMotionAnimation, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    FinalValue = property(get_FinalValue, put_FinalValue)
    InitialValue = property(get_InitialValue, put_InitialValue)
    InitialVelocity = property(get_InitialVelocity, put_InitialVelocity)
class Vector4KeyFrameAnimation(ComPtr):
    extends: win32more.Windows.UI.Composition.KeyFrameAnimation
    default_interface: win32more.Windows.UI.Composition.IVector4KeyFrameAnimation
    _classid_ = 'Windows.UI.Composition.Vector4KeyFrameAnimation'
    @winrt_mixinmethod
    def InsertKeyFrame(self: win32more.Windows.UI.Composition.IVector4KeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def InsertKeyFrameWithEasingFunction(self: win32more.Windows.UI.Composition.IVector4KeyFrameAnimation, normalizedProgressKey: Single, value: win32more.Windows.Foundation.Numerics.Vector4, easingFunction: win32more.Windows.UI.Composition.CompositionEasingFunction) -> Void: ...
class Visual(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.IVisual
    _classid_ = 'Windows.UI.Composition.Visual'
    @winrt_mixinmethod
    def get_AnchorPoint(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_AnchorPoint(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_BackfaceVisibility(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.UI.Composition.CompositionBackfaceVisibility: ...
    @winrt_mixinmethod
    def put_BackfaceVisibility(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.UI.Composition.CompositionBackfaceVisibility) -> Void: ...
    @winrt_mixinmethod
    def get_BorderMode(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.UI.Composition.CompositionBorderMode: ...
    @winrt_mixinmethod
    def put_BorderMode(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.UI.Composition.CompositionBorderMode) -> Void: ...
    @winrt_mixinmethod
    def get_CenterPoint(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_CenterPoint(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Clip(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.UI.Composition.CompositionClip: ...
    @winrt_mixinmethod
    def put_Clip(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.UI.Composition.CompositionClip) -> Void: ...
    @winrt_mixinmethod
    def get_CompositeMode(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.UI.Composition.CompositionCompositeMode: ...
    @winrt_mixinmethod
    def put_CompositeMode(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.UI.Composition.CompositionCompositeMode) -> Void: ...
    @winrt_mixinmethod
    def get_IsVisible(self: win32more.Windows.UI.Composition.IVisual) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVisible(self: win32more.Windows.UI.Composition.IVisual, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Windows.UI.Composition.IVisual) -> Single: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Windows.UI.Composition.IVisual, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.UI.Composition.ContainerVisual: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Windows.UI.Composition.IVisual) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Windows.UI.Composition.IVisual, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.IVisual) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.IVisual, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAxis(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RotationAxis(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_TransformMatrix(self: win32more.Windows.UI.Composition.IVisual) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_mixinmethod
    def put_TransformMatrix(self: win32more.Windows.UI.Composition.IVisual, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    @winrt_mixinmethod
    def get_ParentForTransform(self: win32more.Windows.UI.Composition.IVisual2) -> win32more.Windows.UI.Composition.Visual: ...
    @winrt_mixinmethod
    def put_ParentForTransform(self: win32more.Windows.UI.Composition.IVisual2, value: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeOffsetAdjustment(self: win32more.Windows.UI.Composition.IVisual2) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RelativeOffsetAdjustment(self: win32more.Windows.UI.Composition.IVisual2, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeSizeAdjustment(self: win32more.Windows.UI.Composition.IVisual2) -> win32more.Windows.Foundation.Numerics.Vector2: ...
    @winrt_mixinmethod
    def put_RelativeSizeAdjustment(self: win32more.Windows.UI.Composition.IVisual2, value: win32more.Windows.Foundation.Numerics.Vector2) -> Void: ...
    @winrt_mixinmethod
    def get_IsHitTestVisible(self: win32more.Windows.UI.Composition.IVisual3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHitTestVisible(self: win32more.Windows.UI.Composition.IVisual3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPixelSnappingEnabled(self: win32more.Windows.UI.Composition.IVisual4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPixelSnappingEnabled(self: win32more.Windows.UI.Composition.IVisual4, value: Boolean) -> Void: ...
    AnchorPoint = property(get_AnchorPoint, put_AnchorPoint)
    BackfaceVisibility = property(get_BackfaceVisibility, put_BackfaceVisibility)
    BorderMode = property(get_BorderMode, put_BorderMode)
    CenterPoint = property(get_CenterPoint, put_CenterPoint)
    Clip = property(get_Clip, put_Clip)
    CompositeMode = property(get_CompositeMode, put_CompositeMode)
    IsVisible = property(get_IsVisible, put_IsVisible)
    Offset = property(get_Offset, put_Offset)
    Opacity = property(get_Opacity, put_Opacity)
    Orientation = property(get_Orientation, put_Orientation)
    Parent = property(get_Parent, None)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Size = property(get_Size, put_Size)
    TransformMatrix = property(get_TransformMatrix, put_TransformMatrix)
    ParentForTransform = property(get_ParentForTransform, put_ParentForTransform)
    RelativeOffsetAdjustment = property(get_RelativeOffsetAdjustment, put_RelativeOffsetAdjustment)
    RelativeSizeAdjustment = property(get_RelativeSizeAdjustment, put_RelativeSizeAdjustment)
    IsHitTestVisible = property(get_IsHitTestVisible, put_IsHitTestVisible)
    IsPixelSnappingEnabled = property(get_IsPixelSnappingEnabled, put_IsPixelSnappingEnabled)
class VisualCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.IVisualCollection
    _classid_ = 'Windows.UI.Composition.VisualCollection'
    @winrt_mixinmethod
    def get_Count(self: win32more.Windows.UI.Composition.IVisualCollection) -> Int32: ...
    @winrt_mixinmethod
    def InsertAbove(self: win32more.Windows.UI.Composition.IVisualCollection, newChild: win32more.Windows.UI.Composition.Visual, sibling: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def InsertAtBottom(self: win32more.Windows.UI.Composition.IVisualCollection, newChild: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def InsertAtTop(self: win32more.Windows.UI.Composition.IVisualCollection, newChild: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def InsertBelow(self: win32more.Windows.UI.Composition.IVisualCollection, newChild: win32more.Windows.UI.Composition.Visual, sibling: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Composition.IVisualCollection, child: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: win32more.Windows.UI.Composition.IVisualCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Visual]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.Visual]: ...
    Count = property(get_Count, None)
class VisualUnorderedCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.IVisualUnorderedCollection
    _classid_ = 'Windows.UI.Composition.VisualUnorderedCollection'
    @winrt_mixinmethod
    def get_Count(self: win32more.Windows.UI.Composition.IVisualUnorderedCollection) -> Int32: ...
    @winrt_mixinmethod
    def Add(self: win32more.Windows.UI.Composition.IVisualUnorderedCollection, newVisual: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Composition.IVisualUnorderedCollection, visual: win32more.Windows.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def RemoveAll(self: win32more.Windows.UI.Composition.IVisualUnorderedCollection) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Visual]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.Visual]: ...
    Count = property(get_Count, None)
make_head(_module, 'AmbientLight')
make_head(_module, 'AnimationController')
make_head(_module, 'AnimationPropertyInfo')
make_head(_module, 'BackEasingFunction')
make_head(_module, 'BooleanKeyFrameAnimation')
make_head(_module, 'BounceEasingFunction')
make_head(_module, 'BounceScalarNaturalMotionAnimation')
make_head(_module, 'BounceVector2NaturalMotionAnimation')
make_head(_module, 'BounceVector3NaturalMotionAnimation')
make_head(_module, 'CircleEasingFunction')
make_head(_module, 'ColorKeyFrameAnimation')
make_head(_module, 'CompositionAnimation')
make_head(_module, 'CompositionAnimationGroup')
make_head(_module, 'CompositionBackdropBrush')
make_head(_module, 'CompositionBatchCompletedEventArgs')
make_head(_module, 'CompositionBrush')
make_head(_module, 'CompositionCapabilities')
make_head(_module, 'CompositionClip')
make_head(_module, 'CompositionColorBrush')
make_head(_module, 'CompositionColorGradientStop')
make_head(_module, 'CompositionColorGradientStopCollection')
make_head(_module, 'CompositionCommitBatch')
make_head(_module, 'CompositionContainerShape')
make_head(_module, 'CompositionDrawingSurface')
make_head(_module, 'CompositionEasingFunction')
make_head(_module, 'CompositionEffectBrush')
make_head(_module, 'CompositionEffectFactory')
make_head(_module, 'CompositionEffectSourceParameter')
make_head(_module, 'CompositionEllipseGeometry')
make_head(_module, 'CompositionGeometricClip')
make_head(_module, 'CompositionGeometry')
make_head(_module, 'CompositionGradientBrush')
make_head(_module, 'CompositionGraphicsDevice')
make_head(_module, 'CompositionLight')
make_head(_module, 'CompositionLineGeometry')
make_head(_module, 'CompositionLinearGradientBrush')
make_head(_module, 'CompositionMaskBrush')
make_head(_module, 'CompositionMipmapSurface')
make_head(_module, 'CompositionNineGridBrush')
make_head(_module, 'CompositionObject')
make_head(_module, 'CompositionPath')
make_head(_module, 'CompositionPathGeometry')
make_head(_module, 'CompositionProjectedShadow')
make_head(_module, 'CompositionProjectedShadowCaster')
make_head(_module, 'CompositionProjectedShadowCasterCollection')
make_head(_module, 'CompositionProjectedShadowReceiver')
make_head(_module, 'CompositionProjectedShadowReceiverUnorderedCollection')
make_head(_module, 'CompositionPropertySet')
make_head(_module, 'CompositionRadialGradientBrush')
make_head(_module, 'CompositionRectangleGeometry')
make_head(_module, 'CompositionRoundedRectangleGeometry')
make_head(_module, 'CompositionScopedBatch')
make_head(_module, 'CompositionShadow')
make_head(_module, 'CompositionShape')
make_head(_module, 'CompositionShapeCollection')
make_head(_module, 'CompositionSpriteShape')
make_head(_module, 'CompositionStrokeDashArray')
make_head(_module, 'CompositionSurfaceBrush')
make_head(_module, 'CompositionTarget')
make_head(_module, 'CompositionTransform')
make_head(_module, 'CompositionViewBox')
make_head(_module, 'CompositionVirtualDrawingSurface')
make_head(_module, 'CompositionVisualSurface')
make_head(_module, 'Compositor')
make_head(_module, 'ContainerVisual')
make_head(_module, 'CubicBezierEasingFunction')
make_head(_module, 'DelegatedInkTrailVisual')
make_head(_module, 'DistantLight')
make_head(_module, 'DropShadow')
make_head(_module, 'ElasticEasingFunction')
make_head(_module, 'ExponentialEasingFunction')
make_head(_module, 'ExpressionAnimation')
make_head(_module, 'IAmbientLight')
make_head(_module, 'IAmbientLight2')
make_head(_module, 'IAnimationController')
make_head(_module, 'IAnimationControllerStatics')
make_head(_module, 'IAnimationObject')
make_head(_module, 'IAnimationPropertyInfo')
make_head(_module, 'IAnimationPropertyInfo2')
make_head(_module, 'IBackEasingFunction')
make_head(_module, 'IBooleanKeyFrameAnimation')
make_head(_module, 'IBounceEasingFunction')
make_head(_module, 'IBounceScalarNaturalMotionAnimation')
make_head(_module, 'IBounceVector2NaturalMotionAnimation')
make_head(_module, 'IBounceVector3NaturalMotionAnimation')
make_head(_module, 'ICircleEasingFunction')
make_head(_module, 'IColorKeyFrameAnimation')
make_head(_module, 'ICompositionAnimation')
make_head(_module, 'ICompositionAnimation2')
make_head(_module, 'ICompositionAnimation3')
make_head(_module, 'ICompositionAnimation4')
make_head(_module, 'ICompositionAnimationBase')
make_head(_module, 'ICompositionAnimationFactory')
make_head(_module, 'ICompositionAnimationGroup')
make_head(_module, 'ICompositionBackdropBrush')
make_head(_module, 'ICompositionBatchCompletedEventArgs')
make_head(_module, 'ICompositionBrush')
make_head(_module, 'ICompositionBrushFactory')
make_head(_module, 'ICompositionCapabilities')
make_head(_module, 'ICompositionCapabilitiesStatics')
make_head(_module, 'ICompositionClip')
make_head(_module, 'ICompositionClip2')
make_head(_module, 'ICompositionClipFactory')
make_head(_module, 'ICompositionColorBrush')
make_head(_module, 'ICompositionColorGradientStop')
make_head(_module, 'ICompositionColorGradientStopCollection')
make_head(_module, 'ICompositionCommitBatch')
make_head(_module, 'ICompositionContainerShape')
make_head(_module, 'ICompositionDrawingSurface')
make_head(_module, 'ICompositionDrawingSurface2')
make_head(_module, 'ICompositionDrawingSurfaceFactory')
make_head(_module, 'ICompositionEasingFunction')
make_head(_module, 'ICompositionEasingFunctionFactory')
make_head(_module, 'ICompositionEasingFunctionStatics')
make_head(_module, 'ICompositionEffectBrush')
make_head(_module, 'ICompositionEffectFactory')
make_head(_module, 'ICompositionEffectSourceParameter')
make_head(_module, 'ICompositionEffectSourceParameterFactory')
make_head(_module, 'ICompositionEllipseGeometry')
make_head(_module, 'ICompositionGeometricClip')
make_head(_module, 'ICompositionGeometry')
make_head(_module, 'ICompositionGeometryFactory')
make_head(_module, 'ICompositionGradientBrush')
make_head(_module, 'ICompositionGradientBrush2')
make_head(_module, 'ICompositionGradientBrushFactory')
make_head(_module, 'ICompositionGraphicsDevice')
make_head(_module, 'ICompositionGraphicsDevice2')
make_head(_module, 'ICompositionGraphicsDevice3')
make_head(_module, 'ICompositionGraphicsDevice4')
make_head(_module, 'ICompositionLight')
make_head(_module, 'ICompositionLight2')
make_head(_module, 'ICompositionLight3')
make_head(_module, 'ICompositionLightFactory')
make_head(_module, 'ICompositionLineGeometry')
make_head(_module, 'ICompositionLinearGradientBrush')
make_head(_module, 'ICompositionMaskBrush')
make_head(_module, 'ICompositionMipmapSurface')
make_head(_module, 'ICompositionNineGridBrush')
make_head(_module, 'ICompositionObject')
make_head(_module, 'ICompositionObject2')
make_head(_module, 'ICompositionObject3')
make_head(_module, 'ICompositionObject4')
make_head(_module, 'ICompositionObject5')
make_head(_module, 'ICompositionObjectFactory')
make_head(_module, 'ICompositionObjectStatics')
make_head(_module, 'ICompositionPath')
make_head(_module, 'ICompositionPathFactory')
make_head(_module, 'ICompositionPathGeometry')
make_head(_module, 'ICompositionProjectedShadow')
make_head(_module, 'ICompositionProjectedShadowCaster')
make_head(_module, 'ICompositionProjectedShadowCasterCollection')
make_head(_module, 'ICompositionProjectedShadowCasterCollectionStatics')
make_head(_module, 'ICompositionProjectedShadowReceiver')
make_head(_module, 'ICompositionProjectedShadowReceiverUnorderedCollection')
make_head(_module, 'ICompositionPropertySet')
make_head(_module, 'ICompositionPropertySet2')
make_head(_module, 'ICompositionRadialGradientBrush')
make_head(_module, 'ICompositionRectangleGeometry')
make_head(_module, 'ICompositionRoundedRectangleGeometry')
make_head(_module, 'ICompositionScopedBatch')
make_head(_module, 'ICompositionShadow')
make_head(_module, 'ICompositionShadowFactory')
make_head(_module, 'ICompositionShape')
make_head(_module, 'ICompositionShapeFactory')
make_head(_module, 'ICompositionSpriteShape')
make_head(_module, 'ICompositionSupportsSystemBackdrop')
make_head(_module, 'ICompositionSurface')
make_head(_module, 'ICompositionSurfaceBrush')
make_head(_module, 'ICompositionSurfaceBrush2')
make_head(_module, 'ICompositionSurfaceBrush3')
make_head(_module, 'ICompositionSurfaceFacade')
make_head(_module, 'ICompositionTarget')
make_head(_module, 'ICompositionTargetFactory')
make_head(_module, 'ICompositionTransform')
make_head(_module, 'ICompositionTransformFactory')
make_head(_module, 'ICompositionViewBox')
make_head(_module, 'ICompositionVirtualDrawingSurface')
make_head(_module, 'ICompositionVirtualDrawingSurfaceFactory')
make_head(_module, 'ICompositionVisualSurface')
make_head(_module, 'ICompositor')
make_head(_module, 'ICompositor2')
make_head(_module, 'ICompositor3')
make_head(_module, 'ICompositor4')
make_head(_module, 'ICompositor5')
make_head(_module, 'ICompositor6')
make_head(_module, 'ICompositor7')
make_head(_module, 'ICompositor8')
make_head(_module, 'ICompositorStatics')
make_head(_module, 'ICompositorWithBlurredWallpaperBackdropBrush')
make_head(_module, 'ICompositorWithProjectedShadow')
make_head(_module, 'ICompositorWithRadialGradient')
make_head(_module, 'ICompositorWithVisualSurface')
make_head(_module, 'IContainerVisual')
make_head(_module, 'IContainerVisualFactory')
make_head(_module, 'ICubicBezierEasingFunction')
make_head(_module, 'IDelegatedInkTrailVisual')
make_head(_module, 'IDelegatedInkTrailVisualStatics')
make_head(_module, 'IDistantLight')
make_head(_module, 'IDistantLight2')
make_head(_module, 'IDropShadow')
make_head(_module, 'IDropShadow2')
make_head(_module, 'IElasticEasingFunction')
make_head(_module, 'IExponentialEasingFunction')
make_head(_module, 'IExpressionAnimation')
make_head(_module, 'IImplicitAnimationCollection')
make_head(_module, 'IInsetClip')
make_head(_module, 'IKeyFrameAnimation')
make_head(_module, 'IKeyFrameAnimation2')
make_head(_module, 'IKeyFrameAnimation3')
make_head(_module, 'IKeyFrameAnimationFactory')
make_head(_module, 'ILayerVisual')
make_head(_module, 'ILayerVisual2')
make_head(_module, 'ILinearEasingFunction')
make_head(_module, 'INaturalMotionAnimation')
make_head(_module, 'INaturalMotionAnimationFactory')
make_head(_module, 'IPathKeyFrameAnimation')
make_head(_module, 'IPointLight')
make_head(_module, 'IPointLight2')
make_head(_module, 'IPointLight3')
make_head(_module, 'IPowerEasingFunction')
make_head(_module, 'IQuaternionKeyFrameAnimation')
make_head(_module, 'IRectangleClip')
make_head(_module, 'IRedirectVisual')
make_head(_module, 'IRenderingDeviceReplacedEventArgs')
make_head(_module, 'IScalarKeyFrameAnimation')
make_head(_module, 'IScalarNaturalMotionAnimation')
make_head(_module, 'IScalarNaturalMotionAnimationFactory')
make_head(_module, 'IShapeVisual')
make_head(_module, 'ISineEasingFunction')
make_head(_module, 'ISpotLight')
make_head(_module, 'ISpotLight2')
make_head(_module, 'ISpotLight3')
make_head(_module, 'ISpringScalarNaturalMotionAnimation')
make_head(_module, 'ISpringVector2NaturalMotionAnimation')
make_head(_module, 'ISpringVector3NaturalMotionAnimation')
make_head(_module, 'ISpriteVisual')
make_head(_module, 'ISpriteVisual2')
make_head(_module, 'IStepEasingFunction')
make_head(_module, 'IVector2KeyFrameAnimation')
make_head(_module, 'IVector2NaturalMotionAnimation')
make_head(_module, 'IVector2NaturalMotionAnimationFactory')
make_head(_module, 'IVector3KeyFrameAnimation')
make_head(_module, 'IVector3NaturalMotionAnimation')
make_head(_module, 'IVector3NaturalMotionAnimationFactory')
make_head(_module, 'IVector4KeyFrameAnimation')
make_head(_module, 'IVisual')
make_head(_module, 'IVisual2')
make_head(_module, 'IVisual3')
make_head(_module, 'IVisual4')
make_head(_module, 'IVisualCollection')
make_head(_module, 'IVisualElement')
make_head(_module, 'IVisualElement2')
make_head(_module, 'IVisualFactory')
make_head(_module, 'IVisualUnorderedCollection')
make_head(_module, 'ImplicitAnimationCollection')
make_head(_module, 'InitialValueExpressionCollection')
make_head(_module, 'InkTrailPoint')
make_head(_module, 'InsetClip')
make_head(_module, 'KeyFrameAnimation')
make_head(_module, 'LayerVisual')
make_head(_module, 'LinearEasingFunction')
make_head(_module, 'NaturalMotionAnimation')
make_head(_module, 'PathKeyFrameAnimation')
make_head(_module, 'PointLight')
make_head(_module, 'PowerEasingFunction')
make_head(_module, 'QuaternionKeyFrameAnimation')
make_head(_module, 'RectangleClip')
make_head(_module, 'RedirectVisual')
make_head(_module, 'RenderingDeviceReplacedEventArgs')
make_head(_module, 'ScalarKeyFrameAnimation')
make_head(_module, 'ScalarNaturalMotionAnimation')
make_head(_module, 'ShapeVisual')
make_head(_module, 'SineEasingFunction')
make_head(_module, 'SpotLight')
make_head(_module, 'SpringScalarNaturalMotionAnimation')
make_head(_module, 'SpringVector2NaturalMotionAnimation')
make_head(_module, 'SpringVector3NaturalMotionAnimation')
make_head(_module, 'SpriteVisual')
make_head(_module, 'StepEasingFunction')
make_head(_module, 'Vector2KeyFrameAnimation')
make_head(_module, 'Vector2NaturalMotionAnimation')
make_head(_module, 'Vector3KeyFrameAnimation')
make_head(_module, 'Vector3NaturalMotionAnimation')
make_head(_module, 'Vector4KeyFrameAnimation')
make_head(_module, 'Visual')
make_head(_module, 'VisualCollection')
make_head(_module, 'VisualUnorderedCollection')
