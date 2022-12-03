from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.Dxgi
import win32more.System.Com
import win32more.System.WinRT.Pdf
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
def _define_PdfCreateRenderer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.System.WinRT.Pdf.IPdfRendererNative_head))(('PdfCreateRenderer', windll['Windows.Data.Pdf.dll']), ((1, 'pDevice'),(1, 'ppRenderer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IPdfRendererNative_head():
    class IPdfRendererNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d9dcd91-d277-4947-85-27-07-a0-da-ed-a9-4a')
    return IPdfRendererNative
def _define_IPdfRendererNative():
    IPdfRendererNative = win32more.System.WinRT.Pdf.IPdfRendererNative_head
    IPdfRendererNative.RenderPageToSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Graphics.Dxgi.IDXGISurface_head,win32more.Foundation.POINT,POINTER(win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head))(3, 'RenderPageToSurface', ((1, 'pdfPage'),(1, 'pSurface'),(1, 'offset'),(1, 'pRenderParams'),)))
    IPdfRendererNative.RenderPageToDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Graphics.Direct2D.ID2D1DeviceContext_head,POINTER(win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head))(4, 'RenderPageToDeviceContext', ((1, 'pdfPage'),(1, 'pD2DDeviceContext'),(1, 'pRenderParams'),)))
    win32more.System.Com.IUnknown
    return IPdfRendererNative
def _define_PDF_RENDER_PARAMS_head():
    class PDF_RENDER_PARAMS(Structure):
        pass
    return PDF_RENDER_PARAMS
def _define_PDF_RENDER_PARAMS():
    PDF_RENDER_PARAMS = win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head
    PDF_RENDER_PARAMS._fields_ = [
        ('SourceRect', win32more.Graphics.Direct2D.Common.D2D_RECT_F),
        ('DestinationWidth', UInt32),
        ('DestinationHeight', UInt32),
        ('BackgroundColor', win32more.Graphics.Direct2D.Common.D2D_COLOR_F),
        ('IgnoreHighContrast', win32more.Foundation.BOOLEAN),
    ]
    return PDF_RENDER_PARAMS
def _define_PFN_PDF_CREATE_RENDERER():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.System.WinRT.Pdf.IPdfRendererNative_head))
__all__ = [
    "IPdfRendererNative",
    "PDF_RENDER_PARAMS",
    "PFN_PDF_CREATE_RENDERER",
    "PdfCreateRenderer",
]