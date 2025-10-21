from enum import IntFlag

import comtypes.gen._78530B68_61F9_11D2_8CAD_00A024580902_0_1_0 as __wrapper_module__
from comtypes.gen._78530B68_61F9_11D2_8CAD_00A024580902_0_1_0 import (
    SmartRenderEngine, __MIDL___MIDL_itf_qedit_0000_0000_0003,
    WSTRING, IMediaDet, IMediaLocator, SampleGrabber, _ULARGE_INTEGER,
    IAMTimelineSrc, IDxtJpeg, HRESULT, PINDIR_OUTPUT, IRenderEngine,
    IEnumMediaTypes, IPropertySetter, TIMELINE_MAJOR_TYPE_SOURCE,
    State_Paused, IAMTimelineTransable, State_Running,
    AMTimelineGroup, TIMELINE_MAJOR_TYPE_TRACK, ULONG_PTR, IDxtKey,
    IEnumFilters, IAMTimelineTrans, IAMTimelineTrack, AMTimelineTrack,
    IResize, IXml2Dex, _FILETIME, IReferenceClock, IStream,
    DxtCompositor, tagSTATSTG, ISampleGrabber, DEXTER_VALUE,
    IFilterGraph, TIMELINE_MAJOR_TYPE_TRANSITION, IAMTimeline, BSTR,
    PINDIR_INPUT, _lcid, VARIANT, IAMSetErrorLog,
    __MIDL___MIDL_itf_qedit_0000_0000_0002, CoClass, DxtJpeg,
    State_Stopped, AMTimelineObj, AMTimelineEffect, AudMixer,
    IDxtCompositor, IAMTimelineEffect, AMTimelineComp, IUnknown,
    IMediaSample, DxtAlphaSetter, DxtKey, GUID, _AMMediaType,
    TIMELINE_MAJOR_TYPE_EFFECT, _PinInfo, IMediaFilter, IPin,
    IAMErrorLog, MediaDet, IAMTimelineObj, IErrorLog, IGraphBuilder,
    IAMTimelineEffectable, TIMELINE_MAJOR_TYPE_COMPOSITE,
    IAMTimelineComp, IAMTimelineVirtualTrack, IFindCompressorCB,
    IPropertyBag, AMTimeline, _FilterInfo, Library, IBaseFilter,
    IEnumPins, IDxtAlphaSetter, IPersist, IGrfCache, NullRenderer,
    IRenderEngine2, Xml2Dex, ISampleGrabberCB, MediaLocator,
    typelib_path, _check_version, ColorSource, AMTimelineTrans,
    IAMTimelineGroup, AMTimelineSrc, RenderEngine, DEXTER_PARAM,
    IPersistStream, TIMELINE_MAJOR_TYPE_GROUP, _LARGE_INTEGER,
    ISequentialStream, PropertySetter, dispid, LONG_PTR, COMMETHOD,
    IAMTimelineSplittable, ISmartRenderEngine, IDXEffect, helpstring
)


class _PinDirection(IntFlag):
    PINDIR_INPUT = 0
    PINDIR_OUTPUT = 1


class __MIDL___MIDL_itf_qedit_0000_0000_0007(IntFlag):
    TIMELINE_MAJOR_TYPE_COMPOSITE = 1
    TIMELINE_MAJOR_TYPE_TRACK = 2
    TIMELINE_MAJOR_TYPE_SOURCE = 4
    TIMELINE_MAJOR_TYPE_TRANSITION = 8
    TIMELINE_MAJOR_TYPE_EFFECT = 16
    TIMELINE_MAJOR_TYPE_GROUP = 128


class _FilterState(IntFlag):
    State_Stopped = 0
    State_Paused = 1
    State_Running = 2


TIMELINE_MAJOR_TYPE = __MIDL___MIDL_itf_qedit_0000_0000_0007


__all__ = [
    'IMediaDet', 'IMediaLocator', 'SampleGrabber', 'PINDIR_OUTPUT',
    'TIMELINE_MAJOR_TYPE_SOURCE', 'State_Paused', 'State_Running',
    'AMTimelineGroup', 'TIMELINE_MAJOR_TYPE_TRACK', 'IDxtKey',
    'IAMTimelineTrans', 'IAMTimelineTrack', 'AMTimelineTrack',
    'IStream', 'ISampleGrabber', 'DEXTER_VALUE', 'IFilterGraph',
    'PINDIR_INPUT', '__MIDL___MIDL_itf_qedit_0000_0000_0002',
    'DxtJpeg', 'IAMTimelineEffect', 'IMediaSample', 'DxtAlphaSetter',
    '_AMMediaType', '_PinInfo', 'IMediaFilter', 'IPin', 'IAMErrorLog',
    '_PinDirection', 'MediaDet', 'IAMTimelineObj', 'IAMTimelineComp',
    'IAMTimelineVirtualTrack', 'AMTimeline', '_FilterInfo', 'Library',
    'IBaseFilter', 'IDxtAlphaSetter', 'IGrfCache', 'NullRenderer',
    'ISampleGrabberCB', 'ColorSource', 'AMTimelineTrans',
    'AMTimelineSrc', 'DEXTER_PARAM', 'IPersistStream',
    'PropertySetter', 'IDXEffect', 'SmartRenderEngine',
    '__MIDL___MIDL_itf_qedit_0000_0000_0003', 'IAMTimelineSrc',
    'IDxtJpeg', 'IRenderEngine', 'IEnumMediaTypes', '_FilterState',
    'IPropertySetter', 'IAMTimelineTransable', 'IEnumFilters',
    'IResize', 'IXml2Dex', 'IReferenceClock', 'DxtCompositor',
    'tagSTATSTG', 'TIMELINE_MAJOR_TYPE_TRANSITION', 'IAMSetErrorLog',
    'State_Stopped', 'AMTimelineObj', 'AMTimelineEffect', 'AudMixer',
    'IDxtCompositor', 'AMTimelineComp', 'DxtKey',
    'TIMELINE_MAJOR_TYPE_EFFECT',
    '__MIDL___MIDL_itf_qedit_0000_0000_0007', 'IGraphBuilder',
    'IAMTimelineEffectable', 'ISmartRenderEngine',
    'TIMELINE_MAJOR_TYPE_COMPOSITE', 'IFindCompressorCB', 'IEnumPins',
    'TIMELINE_MAJOR_TYPE', 'IRenderEngine2', 'Xml2Dex',
    'MediaLocator', 'typelib_path', 'IAMTimelineGroup',
    'RenderEngine', 'TIMELINE_MAJOR_TYPE_GROUP', 'LONG_PTR',
    'IAMTimelineSplittable', 'IAMTimeline'
]

