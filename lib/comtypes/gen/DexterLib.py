from enum import IntFlag

import comtypes.gen._78530B68_61F9_11D2_8CAD_00A024580902_0_1_0 as __wrapper_module__
from comtypes.gen._78530B68_61F9_11D2_8CAD_00A024580902_0_1_0 import (
    Xml2Dex, IAMTimeline, GUID, BSTR, TIMELINE_MAJOR_TYPE_EFFECT,
    IXml2Dex, ISequentialStream, IAMTimelineComp, _FILETIME, CoClass,
    State_Running, DxtCompositor, IEnumPins, IAMTimelineTrack,
    IErrorLog, _lcid, _LARGE_INTEGER, TIMELINE_MAJOR_TYPE_SOURCE,
    IResize, COMMETHOD, IAMTimelineTransable, IDxtJpeg, AMTimelineSrc,
    AMTimelineTrack, IStream, __MIDL___MIDL_itf_qedit_0000_0000_0003,
    IEnumMediaTypes, DEXTER_VALUE, AMTimelineTrans,
    ISmartRenderEngine, _ULARGE_INTEGER, DxtAlphaSetter,
    SampleGrabber, IAMSetErrorLog, IDxtAlphaSetter, IFilterGraph,
    IMediaSample, AMTimelineEffect, AMTimelineComp, IBaseFilter,
    dispid, PropertySetter, DEXTER_PARAM, IRenderEngine,
    IGraphBuilder, IGrfCache, ColorSource, Library, IDxtCompositor,
    IUnknown, PINDIR_INPUT, WSTRING, IAMTimelineEffectable,
    AMTimelineGroup, ISampleGrabberCB,
    __MIDL___MIDL_itf_qedit_0000_0000_0002, IPropertySetter, IPin,
    AMTimelineObj, IAMTimelineTrans, TIMELINE_MAJOR_TYPE_TRACK,
    TIMELINE_MAJOR_TYPE_TRANSITION, IPersist, AudMixer,
    TIMELINE_MAJOR_TYPE_COMPOSITE, DxtKey, NullRenderer, typelib_path,
    IAMTimelineGroup, RenderEngine, IFindCompressorCB, ISampleGrabber,
    tagSTATSTG, ULONG_PTR, MediaLocator, _AMMediaType,
    IAMTimelineEffect, IAMTimelineVirtualTrack, IRenderEngine2,
    IDXEffect, SmartRenderEngine, _check_version,
    TIMELINE_MAJOR_TYPE_GROUP, _PinInfo, HRESULT, IAMTimelineSrc,
    IAMTimelineObj, State_Stopped, IPropertyBag, State_Paused,
    _FilterInfo, DxtJpeg, VARIANT, IReferenceClock, IAMErrorLog,
    MediaDet, LONG_PTR, AMTimeline, IMediaDet, helpstring,
    IMediaLocator, IPersistStream, IEnumFilters, IMediaFilter,
    PINDIR_OUTPUT, IAMTimelineSplittable, IDxtKey
)


class _FilterState(IntFlag):
    State_Stopped = 0
    State_Paused = 1
    State_Running = 2


class __MIDL___MIDL_itf_qedit_0000_0000_0007(IntFlag):
    TIMELINE_MAJOR_TYPE_COMPOSITE = 1
    TIMELINE_MAJOR_TYPE_TRACK = 2
    TIMELINE_MAJOR_TYPE_SOURCE = 4
    TIMELINE_MAJOR_TYPE_TRANSITION = 8
    TIMELINE_MAJOR_TYPE_EFFECT = 16
    TIMELINE_MAJOR_TYPE_GROUP = 128


class _PinDirection(IntFlag):
    PINDIR_INPUT = 0
    PINDIR_OUTPUT = 1


TIMELINE_MAJOR_TYPE = __MIDL___MIDL_itf_qedit_0000_0000_0007


__all__ = [
    'IAMTimeline', 'TIMELINE_MAJOR_TYPE_EFFECT', 'IAMTimelineComp',
    'DxtCompositor', 'IAMTimelineTrack', '_FilterState',
    'TIMELINE_MAJOR_TYPE_SOURCE', 'IResize', 'IAMTimelineTransable',
    'IDxtJpeg', 'AMTimelineSrc', 'AMTimelineTrack', 'IStream',
    '__MIDL___MIDL_itf_qedit_0000_0000_0003', 'IEnumMediaTypes',
    'AMTimelineTrans', 'ISmartRenderEngine', 'IAMSetErrorLog',
    'IMediaSample', 'AMTimelineComp', 'DEXTER_PARAM', 'IGraphBuilder',
    'ColorSource', 'IDxtCompositor', 'IAMTimelineEffectable',
    'ISampleGrabberCB', '__MIDL___MIDL_itf_qedit_0000_0000_0002',
    'IPropertySetter', 'IPin', 'IAMTimelineTrans', 'typelib_path',
    'IAMTimelineGroup', 'RenderEngine', 'IFindCompressorCB',
    'tagSTATSTG', '_AMMediaType', 'IAMTimelineEffect',
    'IRenderEngine2', 'IDXEffect', 'TIMELINE_MAJOR_TYPE_GROUP',
    '_PinInfo', 'IAMTimelineObj', '_FilterInfo', 'DxtJpeg',
    'IReferenceClock', 'IAMErrorLog', 'MediaDet', 'LONG_PTR',
    'IMediaLocator', 'IPersistStream', 'IEnumFilters',
    'PINDIR_OUTPUT', '_PinDirection', 'IDxtKey', 'Xml2Dex',
    'IXml2Dex', 'State_Running', 'IEnumPins',
    '__MIDL___MIDL_itf_qedit_0000_0000_0007', 'DEXTER_VALUE',
    'DxtAlphaSetter', 'SampleGrabber', 'IDxtAlphaSetter',
    'IFilterGraph', 'AMTimelineEffect', 'IBaseFilter',
    'PropertySetter', 'IRenderEngine', 'IGrfCache', 'Library',
    'PINDIR_INPUT', 'AMTimelineGroup', 'AMTimelineObj',
    'TIMELINE_MAJOR_TYPE_TRACK', 'TIMELINE_MAJOR_TYPE_TRANSITION',
    'AudMixer', 'TIMELINE_MAJOR_TYPE_COMPOSITE', 'DxtKey',
    'NullRenderer', 'ISampleGrabber', 'MediaLocator',
    'IAMTimelineVirtualTrack', 'SmartRenderEngine', 'IAMTimelineSrc',
    'State_Stopped', 'AMTimeline', 'IMediaDet', 'IMediaFilter',
    'TIMELINE_MAJOR_TYPE', 'State_Paused', 'IAMTimelineSplittable'
]

