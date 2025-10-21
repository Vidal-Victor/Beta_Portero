from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    OLE_YPOS_CONTAINER, GUID, OLE_YPOS_PIXELS, BSTR, VARIANT_BOOL,
    EXCEPINFO, CoClass, DISPMETHOD, _lcid, Unchecked,
    OLE_YPOS_HIMETRIC, COMMETHOD, OLE_XSIZE_CONTAINER, IFont, Font,
    OLE_OPTEXCLUSIVE, OLE_YSIZE_CONTAINER, OLE_XSIZE_HIMETRIC,
    IDispatch, FontEvents, DISPPROPERTY, OLE_CANCELBOOL,
    OLE_YSIZE_PIXELS, Picture, OLE_YSIZE_HIMETRIC,
    OLE_ENABLEDEFAULTBOOL, FONTUNDERSCORE, dispid, FONTSIZE,
    IPictureDisp, Library, IPicture, IUnknown, OLE_XPOS_PIXELS, Gray,
    OLE_XPOS_HIMETRIC, Color, VgaColor, IFontDisp, typelib_path,
    OLE_XSIZE_PIXELS, OLE_XPOS_CONTAINER, StdFont, FONTBOLD,
    FONTITALIC, Monochrome, StdPicture, _check_version, OLE_COLOR,
    FONTSTRIKETHROUGH, HRESULT, Checked, IEnumVARIANT, DISPPARAMS,
    Default, OLE_HANDLE, IFontEventsDisp, FONTNAME
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'OLE_YPOS_CONTAINER', 'OLE_YPOS_PIXELS', 'OLE_XPOS_PIXELS',
    'OLE_TRISTATE', 'Gray', 'OLE_XPOS_HIMETRIC', 'Color', 'VgaColor',
    'Unchecked', 'IFontDisp', 'typelib_path', 'OLE_XSIZE_PIXELS',
    'OLE_YPOS_HIMETRIC', 'OLE_XPOS_CONTAINER', 'StdFont',
    'OLE_XSIZE_CONTAINER', 'IFont', 'Font', 'OLE_OPTEXCLUSIVE',
    'OLE_YSIZE_CONTAINER', 'OLE_XSIZE_HIMETRIC', 'FONTBOLD',
    'LoadPictureConstants', 'FONTITALIC', 'FontEvents',
    'OLE_CANCELBOOL', 'OLE_YSIZE_PIXELS', 'Monochrome', 'Picture',
    'OLE_YSIZE_HIMETRIC', 'StdPicture', 'OLE_COLOR',
    'FONTSTRIKETHROUGH', 'OLE_ENABLEDEFAULTBOOL', 'Checked',
    'FONTUNDERSCORE', 'FONTNAME', 'Default', 'FONTSIZE',
    'IPictureDisp', 'OLE_HANDLE', 'IFontEventsDisp', 'Library',
    'IPicture'
]

