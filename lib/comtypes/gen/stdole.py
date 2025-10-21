from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    VgaColor, Gray, IEnumVARIANT, OLE_YSIZE_CONTAINER, OLE_COLOR,
    FONTBOLD, HRESULT, OLE_XPOS_PIXELS, IFont, Checked,
    OLE_XPOS_HIMETRIC, OLE_XSIZE_PIXELS, Font, StdPicture,
    OLE_OPTEXCLUSIVE, FONTITALIC, Picture, DISPPARAMS,
    OLE_YPOS_HIMETRIC, OLE_CANCELBOOL, VARIANT_BOOL,
    OLE_XPOS_CONTAINER, OLE_YPOS_CONTAINER, StdFont, BSTR, _lcid,
    CoClass, FONTUNDERSCORE, FONTSIZE, FONTSTRIKETHROUGH, OLE_HANDLE,
    OLE_ENABLEDEFAULTBOOL, Monochrome, IUnknown, EXCEPINFO,
    OLE_XSIZE_CONTAINER, OLE_YSIZE_HIMETRIC, DISPPROPERTY, IPicture,
    Unchecked, Library, Color, IDispatch, IPictureDisp, typelib_path,
    _check_version, OLE_YSIZE_PIXELS, OLE_XSIZE_HIMETRIC,
    OLE_YPOS_PIXELS, IFontEventsDisp, Default, DISPMETHOD, FontEvents,
    dispid, COMMETHOD, IFontDisp, GUID, FONTNAME
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
    'VgaColor', 'Gray', 'Monochrome', 'OLE_YSIZE_CONTAINER',
    'OLE_XSIZE_CONTAINER', 'OLE_COLOR', 'OLE_YSIZE_HIMETRIC',
    'FONTBOLD', 'OLE_XPOS_PIXELS', 'IFont', 'IPicture', 'Checked',
    'OLE_XPOS_HIMETRIC', 'OLE_XSIZE_PIXELS', 'Font', 'Unchecked',
    'StdPicture', 'OLE_ENABLEDEFAULTBOOL', 'Picture', 'FONTITALIC',
    'OLE_OPTEXCLUSIVE', 'Library', 'OLE_YPOS_HIMETRIC',
    'OLE_CANCELBOOL', 'OLE_XPOS_CONTAINER', 'Color',
    'LoadPictureConstants', 'typelib_path', 'IPictureDisp',
    'OLE_TRISTATE', 'OLE_YPOS_CONTAINER', 'OLE_YSIZE_PIXELS',
    'StdFont', 'OLE_XSIZE_HIMETRIC', 'OLE_YPOS_PIXELS',
    'IFontEventsDisp', 'FONTUNDERSCORE', 'Default', 'FontEvents',
    'FONTSIZE', 'FONTSTRIKETHROUGH', 'OLE_HANDLE', 'IFontDisp',
    'FONTNAME'
]

