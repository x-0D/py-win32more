from win32more import *
import win32more.System.WinRT.Graphics.Capture
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.WinRT.Graphics.Capture, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.WinRT.Graphics.Capture, name)
def _define_IGraphicsCaptureItemInterop_head():
    class IGraphicsCaptureItemInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('3628e81b-3cac-4c60-b7f4-23ce0e0c3356')
    return IGraphicsCaptureItemInterop
def _define_IGraphicsCaptureItemInterop():
    IGraphicsCaptureItemInterop = win32more.System.WinRT.Graphics.Capture.IGraphicsCaptureItemInterop_head
    IGraphicsCaptureItemInterop.CreateForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateForWindow', ((1, 'window'),(1, 'riid'),(1, 'result'),)))
    IGraphicsCaptureItemInterop.CreateForMonitor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HMONITOR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'CreateForMonitor', ((1, 'monitor'),(1, 'riid'),(1, 'result'),)))
    return IGraphicsCaptureItemInterop
__all__ = [
    "IGraphicsCaptureItemInterop",
]