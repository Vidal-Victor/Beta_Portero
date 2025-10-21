from enum import IntFlag

import comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 as __wrapper_module__
from comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 import (
    DISPID_SVSInputWordPosition, ISpeechAudioStatus,
    DISPID_SVSVisemeId, SVEWordBoundary, SSTTTextBuffer,
    SpeechCategoryVoices, SPGS_EXCLUSIVE, STSF_AppData,
    SPCT_SUB_DICTATION, SPEVENTSOURCEINFO, SPINTERFERENCE_NONE,
    SAFTADPCM_44kHzMono, SPEI_ADAPTATION, SP_VISEME_4,
    SREPropertyNumChange, DISPID_SVAudioOutput, eLEXTYPE_PRIVATE6,
    SAFT12kHz8BitMono, DISPID_SRRRecoContext, SAFT44kHz8BitMono,
    DISPID_SVSyncronousSpeakTimeout, SAFT11kHz8BitMono,
    DISPID_SRSCurrentStreamPosition, SPEI_START_INPUT_STREAM,
    SpeechPropertyComplexResponseSpeed, DISPID_SOTMatchesAttributes,
    SVF_Emphasis, eLEXTYPE_MORPHOLOGY, DISPID_SDKOpenKey,
    SDKLLocalMachine, DISPID_SBSRead, SPRECOCONTEXTSTATUS,
    SpSharedRecognizer, SpMMAudioOut, SREHypothesis, SGDSInactive,
    SPDKL_CurrentConfig, SPLO_STATIC, SWTDeleted,
    DISPID_SRCRecognizer, DISPID_SPISaveToMemory,
    DISPID_SRGetPropertyString, DISPID_SLPs_NewEnum, SPRST_NUM_STATES,
    SPSSuppressWord, SVEPrivate, DISPID_SRCEFalseRecognition,
    SpMemoryStream, ISpRecognizer2, SRAORetainAudio,
    DISPID_SWFEExtraData, DISPID_SPIEnginePrivateData,
    SPSInterjection, UINT_PTR, DISPID_SDKCreateKey,
    DISPID_SVEVoiceChange, SPXRO_SML, ISpRecoResult,
    SpeechGrammarTagWildcard, SpeechVoiceCategoryTTSRate,
    SAFT48kHz16BitStereo, SPAR_Medium, DISPID_SRRPhraseInfo,
    DISPID_SRRSpeakAudio, _lcid, SVP_15, SPEI_SR_RETAINEDAUDIO,
    DISPID_SRCEHypothesis, DISPID_SRSetPropertyNumber,
    DISPID_SCSBaseStream, DISPID_SGRs_NewEnum, DISPID_SLPPartOfSpeech,
    SPAO_RETAIN_AUDIO, STSF_LocalAppData, DISPID_SVEStreamEnd,
    DISPID_SRCVoicePurgeEvent, SAFT11kHz16BitStereo,
    SPPS_Interjection, SPWORDPRONUNCIATION, SPCT_DICTATION,
    DISPID_SRIsUISupported, SLTUser, SPLO_DYNAMIC,
    DISPID_SPEAudioSizeBytes, DISPID_SRGSetTextSelection,
    DISPID_SRState, SpeechCategoryRecognizers,
    SpeechAudioFormatGUIDText, DISPID_SAFGetWaveFormatEx,
    DISPID_SPIProperties, DISPID_SRGetPropertyNumber,
    DISPID_SRCEventInterests, SPEI_MAX_TTS, SVEEndInputStream, SVP_3,
    SpeechTokenKeyFiles, DISPID_SRCCmdMaxAlternates, DISPID_SVVoice,
    DISPID_SPACommit, DISPID_SRRGetXMLResult, HRESULT, SRERecognition,
    __MIDL___MIDL_itf_sapi_0000_0020_0002,
    ISpeechLexiconPronunciations, SAFT8kHz8BitMono, SVP_1,
    eLEXTYPE_PRIVATE15, SAFT8kHz16BitMono, DISPID_SRRAlternates,
    SWPKnownWordPronounceable, SPEI_PROPERTY_NUM_CHANGE,
    SGDSActiveWithAutoPause, SREStateChange, SPGS_DISABLED,
    SAFT8kHz8BitStereo, SPPS_Noncontent, SAFTCCITT_ALaw_8kHzStereo,
    DISPID_SRCAudioInInterferenceStatus, SPSNotOverriden,
    SPGS_ENABLED, SPEI_RESERVED2, DISPID_SRGRules, ISpeechRecoResult,
    SPSHORTCUTPAIR, SLOStatic, SPCT_SUB_COMMAND, SPPS_LMA,
    SSSPTRelativeToCurrentPosition, eLEXTYPE_RESERVED7, SPAS_RUN,
    SRESoundStart, SPINTERFERENCE_LATENCY_WARNING,
    DISPID_SVAlertBoundary, SpObjectToken,
    DISPID_SLRemovePronunciationByPhoneIds, Speech_StreamPos_Asap,
    SVP_18, SPXRO_Alternates_SML, ISpObjectWithToken,
    DISPID_SPIRetainedSizeBytes, DISPID_SWFEBlockAlign,
    SpeechRegistryLocalMachineRoot, SPINTERFERENCE_TOOFAST,
    ISpPhoneConverter, DISPID_SRCRequestedUIType, ISpeechPhraseRules,
    DISPID_SPPBRestorePhraseFromMemory, SP_VISEME_6, SRTStandard,
    GUID, ISpeechGrammarRuleStateTransitions,
    DISPID_SPEActualConfidence, SpeechVoiceSkipTypeSentence,
    DISPID_SRGSetWordSequenceData, DISPID_SRGId,
    SAFTCCITT_ALaw_22kHzStereo, SAFTADPCM_22kHzStereo, SINoSignal,
    SAFT12kHz8BitStereo, ISpeechRecognizer,
    DISPID_SLGetGenerationChange, ISpShortcut, eLEXTYPE_VENDORLEXICON,
    SPSVerb, DISPID_SPILanguageId, DISPID_SRGState, WSTRING,
    SpeechTokenIdUserLexicon, SGDSActive, STCInprocServer,
    SVSFUnusedFlags, SGSDisabled, SPSHT_Unknown, DISPID_SPARecoResult,
    SVSFPersistXML, SVP_13, eLEXTYPE_RESERVED4, SPFM_OPEN_READONLY,
    SPEI_RECO_OTHER_CONTEXT, SPEI_START_SR_STREAM,
    DISPID_SPEAudioSizeTime, ISpeechVoiceStatus, SP_VISEME_8,
    SPEI_WORD_BOUNDARY, SREStreamStart,
    DISPID_SGRSAddSpecialTransition, SAFTCCITT_ALaw_11kHzMono,
    DISPID_SPANumberOfElementsInResult, SPBO_NONE, WAVEFORMATEX,
    DISPID_SPPConfidence, SAFT32kHz8BitStereo, SAFT32kHz16BitMono,
    DISPID_SOTId, DISPID_SGRAddResource, eLEXTYPE_PRIVATE2,
    SECFIgnoreWidth, DISPID_SRSAudioStatus,
    DISPID_SRCEPropertyNumberChange, SPWT_DISPLAY,
    DISPID_SREmulateRecognition, SpeechPropertyAdaptationOn,
    DISPID_SRCEPropertyStringChange, SPEI_SOUND_START,
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet,
    DISPID_SRRTOffsetFromStart, wireHWND, DISPID_SPRulesCount,
    SPCS_ENABLED, SPINTERFERENCE_NOSIGNAL, SP_VISEME_5,
    DISPID_SOTCGetDataKey, DISPID_SLWs_NewEnum, DISPID_SPPParent,
    DISPID_SRSCurrentStreamNumber, eLEXTYPE_PRIVATE12, ISpVoice,
    DISPID_SVRate, SAFTCCITT_uLaw_44kHzMono, SPBO_AHEAD,
    SAFT44kHz8BitStereo, eLEXTYPE_PRIVATE10, SpNullPhoneConverter,
    SPPHRASE, DISPID_SVSLastResult, ISpDataKey, STCRemoteServer,
    DISPID_SRCState, SPEI_SR_AUDIO_LEVEL, DISPID_SRCEStartStream,
    DISPID_SVWaitUntilDone, SPSLMA, DISPID_SPRuleChildren,
    DISPID_SPCLangId, SSTTDictation, SVP_8, IEnumString,
    ISpeechGrammarRule, ISpeechCustomStream,
    SAFTCCITT_uLaw_44kHzStereo, SPSHT_NotOverriden,
    SpeechUserTraining, SVSFVoiceMask, DISPID_SRAudioInputStream,
    SPFM_NUM_MODES, ISpNotifySource, DISPID_SLWPronunciations,
    DISPID_SRRAudio, SAFTADPCM_8kHzMono, DISPID_SRGCommit,
    DISPID_SVAudioOutputStream, SITooFast, DISPID_SRProfile,
    DISPID_SBSWrite, SRAExport, SP_VISEME_0,
    SAFTCCITT_uLaw_22kHzStereo, SVEStartInputStream, SpStream,
    SRARoot, SPEI_HYPOTHESIS, DISPID_SOTsItem, ISpeechGrammarRules,
    SpWaveFormatEx, DISPID_SRGCmdSetRuleState,
    DISPID_SOTGetStorageFileName, SPPS_RESERVED4, SPFM_CREATE,
    SPEI_TTS_PRIVATE, SPVOICESTATUS, SASStop,
    DISPID_SRGDictationUnload, DISPID_SVSLastStreamNumberQueued,
    ISpPhoneticAlphabetSelection, DISPID_SPEDisplayText,
    SVSFNLPSpeakPunc, DISPID_SAEventHandle, SDTAll,
    Speech_Default_Weight, STCAll, SPSHORTCUTPAIRLIST,
    ISpeechGrammarRuleStateTransition, ISpeechPhraseRule,
    SREInterference, SGRSTTDictation, DISPID_SPEsItem,
    Speech_StreamPos_RealTime, SpeechAllElements, SVEViseme,
    ISpRecoContext, ISpRecoGrammar, DISPID_SPRNumberOfElements,
    SPINTERFERENCE_NOISE, DISPID_SPELexicalForm,
    DISPID_SVSLastBookmarkId, DISPID_SRRSetTextFeedback, SPCT_SLEEP,
    DISPID_SPIElements, DISPID_SPRs_NewEnum,
    DISPID_SRGCmdLoadFromProprietaryGrammar,
    SPEI_PROPERTY_STRING_CHANGE, SAFT48kHz16BitMono,
    SPEI_SENTENCE_BOUNDARY, ISpRecoCategory, SpCompressedLexicon,
    DISPID_SPPValue, ISpeechPhraseAlternate, SPINTERFERENCE_TOOLOUD,
    DISPID_SVEWord, DISPID_SRIsShared, SPSMF_SRGS_SAPIPROPERTIES,
    DISPID_SABufferNotifySize, SLTApp, DISPID_SRCERecognition,
    SAFT22kHz8BitMono, eLEXTYPE_PRIVATE19, DISPID_SPAPhraseInfo,
    DISPID_SPPName, eLEXTYPE_PRIVATE16, DISPID_SABIBufferSize,
    SpeechCategoryAppLexicons, SAFT16kHz8BitMono, DISPID_SGRSRule,
    SP_VISEME_7, DISPID_SDKSetStringValue, SpPhoneConverter,
    DISPID_SPEAudioTimeOffset, eLEXTYPE_RESERVED10,
    SAFTADPCM_8kHzStereo, SPRECORESULTTIMES, SpeechTokenKeyAttributes,
    ISpNotifyTranslator, DISPID_SRCVoice, SPRST_ACTIVE,
    SECFIgnoreCase, DISPID_SRGDictationLoad, DISPID_SOTRemove,
    ISpObjectTokenCategory, DISPIDSPTSI_ActiveOffset,
    SDA_Two_Trailing_Spaces, DISPID_SPIStartTime, SP_VISEME_2,
    SP_VISEME_1, SECHighConfidence, SpeechAudioFormatGUIDWave,
    DISPID_SOTCDefault, SAFTCCITT_uLaw_11kHzMono, DISPID_SPIGrammarId,
    DISPID_SRGDictationSetState, SVSFPurgeBeforeSpeak,
    DISPID_SRCEAdaptation, SFTSREngine, SAFTGSM610_8kHzMono,
    SRERecoOtherContext, SITooQuiet, DISPID_SOTs_NewEnum,
    SPPS_Unknown, SRAInterpreter, SVP_11, DISPID_SPERetainedSizeBytes,
    SRAONone, DISPID_SOTCategory, SVP_9, SpShortcut, ISpEventSource,
    eLEXTYPE_RESERVED9, SDA_Consume_Leading_Spaces, SPVPRI_NORMAL,
    SAFTGSM610_11kHzMono, SECFIgnoreKanaType, SPAS_PAUSE,
    ISpRecoContext2, SPRS_ACTIVE_WITH_AUTO_PAUSE,
    DISPID_SVSLastBookmark, DISPID_SLWType, DISPID_SOTGetDescription,
    DISPID_SVIsUISupported, typelib_path, SVESentenceBoundary,
    SPEI_INTERFERENCE, ISpeechRecoResultDispatch, SPVPRI_ALERT,
    SVSFIsFilename, SPAS_STOP, DISPID_SRGetFormat, SP_VISEME_15,
    ISpeechRecoResult2, SAFT22kHz16BitStereo, ISpeechLexiconWord,
    LONG_PTR, ISpeechLexicon, DISPID_SRRAudioFormat, DISPID_SRRTimes,
    DISPID_SVEAudioLevel, DISPID_SASetState, SECFEmulateResult,
    DISPID_SRSClsidEngine, DISPID_SLGetPronunciations,
    STCInprocHandler, SpeechMicTraining, SPAR_Unknown,
    ISpeechPhraseElements, DISPID_SRGCmdSetRuleIdState,
    DISPID_SRCEAudioLevel, SREFalseRecognition, ISpProperties,
    DISPID_SPEEngineConfidence, SPCT_COMMAND, DISPID_SFSOpen,
    SAFT24kHz8BitMono, DISPID_SWFEAvgBytesPerSec, SDTDisplayText,
    eLEXTYPE_LETTERTOSOUND, SpStreamFormatConverter,
    ISpeechPhraseProperty, DISPID_SRCRetainedAudio,
    DISPID_SPPChildren, SPEI_VISEME, DISPID_SRRSaveToMemory,
    DISPID_SOTDataKey, SP_VISEME_13, DISPID_SLGenerationId,
    DISPID_SOTCreateInstance, DISPID_SASCurrentSeekPosition,
    DISPID_SRCESoundEnd, DISPID_SRSSupportedLanguages,
    DISPID_SGRsItem, SDTPronunciation, ISpeechVoice, SDTLexicalForm,
    SASClosed, eLEXTYPE_RESERVED8, SPINTERFERENCE_TOOSLOW,
    DISPID_SAStatus, DISPID_SGRSTsCount, SpMMAudioIn, SRSActive,
    DISPID_SGRSTPropertyId, SAFTCCITT_ALaw_8kHzMono,
    DISPID_SVSInputSentenceLength, SRSEIsSpeaking, DISPID_SLWLangId,
    DISPID_SLWsCount, SDA_One_Trailing_Space, DISPID_SLGetWords,
    SPRST_INACTIVE, SAFTCCITT_uLaw_8kHzMono,
    DISPID_SRGCmdLoadFromObject, DISPIDSPTSI_SelectionLength,
    ISpeechTextSelectionInformation, SAFT32kHz16BitStereo,
    DISPID_SASNonBlockingIO, SRESoundEnd,
    DISPID_SRCCreateResultFromMemory, SPWORDPRONUNCIATIONLIST,
    SREStreamEnd, DISPID_SGRSTPropertyValue, DISPID_SLWWord,
    SAFTCCITT_ALaw_44kHzMono, SDKLDefaultLocation,
    DISPID_SGRsCommitAndSave, DISPID_SVEViseme,
    DISPID_SOTIsUISupported, SREAudioLevel, SPBINARYGRAMMAR,
    SPPS_Noun, DISPID_SRCEInterference, SINone, SAFT44kHz16BitStereo,
    IInternetSecurityManager, DISPID_SLPsCount, SDTReplacement,
    SDTProperty, SAFT44kHz16BitMono, DISPID_SGRName, DISPID_SBSSeek,
    ISpObjectToken, SREPropertyStringChange, SPAS_CLOSED,
    DISPID_SRGIsPronounceable, SPSMF_UPS, SVSFParseMask,
    SPPHRASEPROPERTY, DISPID_SPIAudioSizeTime, DISPID_SRCEPhraseStart,
    DISPID_SDKGetBinaryValue, DISPID_SRGCmdLoadFromResource,
    SPEI_END_INPUT_STREAM, SDKLCurrentUser, DISPID_SLPType,
    SREAllEvents, SVP_6, SVEPhoneme, DISPID_SPAStartElementInResult,
    SPINTERFERENCE_LATENCY_TRUNCATE_END, SP_VISEME_3, SPSHT_EMAIL,
    SpVoice, tagSPPROPERTYINFO, _ISpeechRecoContextEvents,
    ISpeechResourceLoader, SAFT24kHz16BitMono, SVPNormal,
    SGRSTTWildcard, SASPause, SASRun, SVF_None,
    DISPID_SRCEEnginePrivate, DISPID_SGRSAddRuleTransition,
    ISpRecognizer, ISequentialStream, ISpEventSink,
    ISpeechObjectTokens, SpFileStream, SAFTGSM610_44kHzMono,
    DISPID_SGRId, SPEI_RESERVED5, SP_VISEME_11, _ISpeechVoiceEvents,
    SVSFlagsAsync, SPEI_MIN_SR, SPBO_PAUSE, STSF_FlagCreate, SDTAudio,
    eLEXTYPE_PRIVATE20, DISPID_SRSNumberOfActiveRules,
    SECFNoSpecialChars, SpeechRegistryUserRoot, SRADefaultToActive,
    SPINTERFERENCE_TOOQUIET, eWORDTYPE_DELETED, DISPID_SPCPhoneToId,
    eWORDTYPE_ADDED, DISPID_SPIGetText, SPAO_NONE,
    DISPIDSPTSI_ActiveLength, DISPID_SGRSTType, ISpeechFileStream,
    SPEI_TTS_AUDIO_LEVEL, SGRSTTEpsilon,
    DISPID_SLAddPronunciationByPhoneIds, SAFT24kHz8BitStereo,
    ISpeechRecognizerStatus, VARIANT_BOOL, SPPS_NotOverriden, SPSNoun,
    DISPID_SRCCreateGrammar, DISPID_SRCResume, SAFTGSM610_22kHzMono,
    SVP_21, DISPID_SVGetVoices, SPAUDIOSTATUS, DISPID_SGRsCount,
    ISpeechPhraseReplacement, SPPS_RESERVED2, DISPID_SVSRunningState,
    SP_VISEME_16, DISPID_SLRemovePronunciation,
    SpeechGrammarTagUnlimitedDictation, ISpeechRecoGrammar,
    SpeechTokenValueCLSID, SpeechDictationTopicSpelling,
    SpeechCategoryAudioIn, _ULARGE_INTEGER, DISPID_SLAddPronunciation,
    SBOPause, SPEI_MIN_TTS, DISPID_SASState, DISPID_SDKSetLongValue,
    DISPID_SGRSTs_NewEnum, DISPID_SRStatus,
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE, SSSPTRelativeToStart,
    DISPID_SDKDeleteKey, SGRSTTRule, DISPID_SVSInputWordLength,
    DISPID_SDKGetStringValue, DISPID_SLPLangId, SAFTADPCM_44kHzStereo,
    DISPID_SRGRecoContext, SpMMAudioEnum, SPWT_LEXICAL,
    DISPID_SOTRemoveStorageFileName, IEnumSpObjectTokens,
    DISPID_SABufferInfo, SRATopLevel, IServiceProvider,
    DISPID_SRCEBookmark, DISPID_SOTSetId, SPSModifier, ISpAudio,
    SPWORDLIST, SpAudioFormat, DISPID_SGRSTWeight, DISPID_SAVolume,
    ISpRecognizer3, DISPID_SMSADeviceId, DISPID_SPPFirstElement,
    SpNotifyTranslator, ULONG_PTR, DISPID_SVSpeak,
    Speech_Max_Word_Length, eLEXTYPE_PRIVATE11, SDTAlternates,
    ISpeechPhoneConverter, DISPID_SMSSetData, eLEXTYPE_PRIVATE3,
    SP_VISEME_18, SPSMF_SAPI_PROPERTIES, SPPHRASEELEMENT,
    SpeechCategoryPhoneConverters, SVF_Stressed,
    SPWT_LEXICAL_NO_SPECIAL_CHARS, DISPID_SPRuleName,
    DISPID_SPEs_NewEnum, SPPS_RESERVED3, SGDSActiveUserDelimited,
    SVSFParseSsml, SFTInput, DISPID_SOTsCount, DISPID_SPPId,
    SPEI_VOICE_CHANGE, DISPID_SVSpeakStream, DISPID_SPPsCount,
    DISPID_SRCSetAdaptationData, SPRST_INACTIVE_WITH_PURGE,
    SPWF_INPUT, ISpSerializeState, SPSEMANTICERRORINFO, SP_VISEME_14,
    SPEI_MAX_SR, SRTEmulated, SPEI_PHRASE_START, SAFT48kHz8BitMono,
    SAFT16kHz8BitStereo, DISPID_SGRsFindRule,
    ISpPhoneticAlphabetConverter, DISPID_SRGCmdLoadFromFile,
    SPEI_RECO_STATE_CHANGE, SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN,
    SAFTNoAssignedFormat, SpeechGrammarTagDictation, SVP_4,
    ISpLexicon, SITooSlow, SpSharedRecoContext,
    DISPID_SPRuleFirstElement, COMMETHOD, DISPID_SRCPause, ISpStream,
    eLEXTYPE_APP, SRTReSent, DISPID_SVVolume, SWTAdded,
    ISpeechRecoContext, SVSFParseAutodetect,
    DISPID_SRCERecognitionForOtherContext, SPWORD,
    DISPID_SPPNumberOfElements, DISPMETHOD, SRCS_Disabled,
    DISPID_SPRulesItem, SpeechCategoryRecoProfiles,
    SAFT12kHz16BitStereo, DISPID_SABIEventBias, DISPID_SRRTLength,
    SP_VISEME_12, SVSFIsXML, SITooLoud, DISPID_SVSkip, ISpNotifySink,
    __MIDL_IWinTypes_0009, DISPID_SPRuleNumberOfElements,
    DISPID_SGRSTRule, SVP_14, DISPID_SPRuleConfidence, SVP_19,
    SpeechRecoProfileProperties, SpCustomStream, DISPID_SPRuleParent,
    SAFTADPCM_11kHzStereo, SpeechAudioVolume, SPTEXTSELECTIONINFO,
    SVEVoiceChange, DISPID_SRCRetainedAudioFormat, SVP_20,
    DISPID_SMSAMMHandle, SVEAllEvents, DISPID_SPRDisplayAttributes,
    ISpeechDataKey, ISpXMLRecoResult, CoClass, DISPID_SPIReplacements,
    SVP_16, DISPID_SOTCEnumerateTokens, DISPID_SOTCSetId, SpLexicon,
    DISPID_SOTCId, DISPID_SGRSTText, DISPID_SGRSTransitions,
    DISPID_SPAs_NewEnum, SpeechPropertyResourceUsage,
    DISPID_SPPEngineConfidence, helpstring, DISPID_SLPPhoneIds,
    ISpeechGrammarRuleState, SVEBookmark, SRAImport, DISPID_SPEsCount,
    SPEI_SR_BOOKMARK, SPRS_ACTIVE, SPRECOGNIZERSTATUS, SPCS_DISABLED,
    DISPID_SVStatus, SPEI_REQUEST_UI, DISPID_SGRSTsItem,
    DISPID_SVEEnginePrivate, SAFT24kHz16BitStereo, SPPS_Verb,
    DISPID_SDKSetBinaryValue, SpPhraseInfoBuilder,
    SpInProcRecoContext, DISPID_SRCERequestUI, ISpeechBaseStream,
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE, SWPUnknownWordUnpronounceable,
    DISPID_SRRTTickCount, SAFT32kHz8BitMono, ISpPhrase,
    DISPID_SGRAddState, DISPID_SWFEBitsPerSample,
    IInternetSecurityMgrSite, SPRULE, SpUnCompressedLexicon,
    SGLexicalNoSpecialChars, SDKLCurrentConfig,
    ISpeechObjectTokenCategory, ISpeechMemoryStream, SDTRule,
    DISPID_SGRClear, SPAR_Low, SPEI_TTS_BOOKMARK, SAFTText,
    SRSInactive, DISPID_SLPsItem, DISPID_SPERetainedStreamOffset,
    eLEXTYPE_PRIVATE5, SAFT8kHz16BitStereo, SP_VISEME_21,
    SVSFParseSapi, ISpeechLexiconPronunciation, ISpeechAudioFormat,
    DISPID_SPEAudioStreamOffset, ISpStreamFormat, SPFM_CREATE_ALWAYS,
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C, SRTAutopause,
    SPDKL_CurrentUser, SSFMCreate, SAFT16kHz16BitMono,
    DISPID_SDKDeleteValue, SECNormalConfidence, SpeechAddRemoveWord,
    DISPID_SWFEChannels, ISpeechPhraseAlternates, eLEXTYPE_PRIVATE7,
    ISpeechRecoResultTimes, DISPID_SPIAudioStreamPosition,
    DISPID_SVEventInterests, ISpGrammarBuilder,
    DISPID_SRCreateRecoContext,
    DISPID_SRAllowVoiceFormatMatchingOnNextSet, SREPrivate,
    eLEXTYPE_PRIVATE18, DISPID_SVResume, DISPID_SRGReset,
    SAFTCCITT_ALaw_22kHzMono, SPEVENT, DISPID_SDKEnumValues,
    SSTTWildcard, SPSMF_SRGS_SEMANTICINTERPRETATION_MS,
    SpResourceManager, tagSTATSTG, SPEI_END_SR_STREAM, SVPOver,
    SSFMCreateForWrite, SRADynamic, STCLocalServer, SPPS_SuppressWord,
    SPEI_SR_PRIVATE, DISPID_SGRSTNextState, DISPID_SADefaultFormat,
    DISPID_SASFreeBufferSpace, DISPID_SRRecognizer, _FILETIME,
    SAFTCCITT_ALaw_44kHzStereo, DISPID_SPAsItem, SBONone,
    DISPID_SPIRule, SPWF_SRENGINE, SGSExclusive,
    SAFTNonStandardFormat, DISPID_SOTGetAttribute, SINoise,
    SAFTCCITT_uLaw_8kHzStereo, DISPID_SVGetProfiles,
    eLEXTYPE_RESERVED6, SREAdaptation, ISpeechWaveFormatEx,
    SRCS_Enabled, SpeechTokenKeyUI, SAFTADPCM_11kHzMono,
    SPSERIALIZEDRESULT, IUnknown, eLEXTYPE_USER,
    DISPID_SASCurrentDevicePosition, SAFT48kHz8BitStereo,
    DISPID_SPERequiredConfidence, SVP_12, DISPID_SVPriority,
    DISPID_SVDisplayUI, SSSPTRelativeToEnd, ISpResourceManager,
    Library, SP_VISEME_10, SVSFNLPMask, ISpeechXMLRecoResult,
    DISPID_SGRAttributes, SRSEDone, SVSFIsNotXML,
    SpeechPropertyNormalConfidenceThreshold, DISPID_SGRsCommit,
    eLEXTYPE_PRIVATE14, DISPID_SPIGetDisplayAttributes,
    SPRS_ACTIVE_USER_DELIMITED, DISPID_SPEDisplayAttributes,
    DISPID_SMSALineId, __MIDL___MIDL_itf_sapi_0000_0020_0001,
    DISPID_SRSetPropertyString, SREPhraseStart, SPSUnknown,
    tagSPTEXTSELECTIONINFO, DISPID_SAFSetWaveFormatEx,
    SAFTCCITT_ALaw_11kHzStereo, DISPID_SRGetRecognizers,
    SPEI_RESERVED1, SECFDefault, SSFMOpenForRead,
    SAFTCCITT_uLaw_22kHzMono, DISPID_SRCBookmark,
    SpeechAudioProperties, SGSEnabled, SPSERIALIZEDPHRASE, SLODynamic,
    SRTSMLTimeout, SP_VISEME_20, SpeechCategoryAudioOut, SPVPRI_OVER,
    DISPID_SVEBookmark, DISPID_SRCEEndStream, DISPID_SMSGetData,
    DISPID_SPRuleEngineConfidence, SP_VISEME_9, DISPID_SVEStreamStart,
    SPFM_OPEN_READWRITE, SpInprocRecognizer,
    SpeechPropertyHighConfidenceThreshold, ISpeechPhraseElement,
    DISPID_SRRTStreamTime, DISPID_SPCIdToPhone,
    SpeechPropertyLowConfidenceThreshold, BSTR,
    SpeechPropertyResponseSpeed, SSFMOpenReadWrite, dispid,
    ISpeechPhraseInfoBuilder, SAFT12kHz16BitMono,
    ISpStreamFormatConverter, DISPID_SPIEngineId, ISpeechObjectToken,
    SVP_5, DISPID_SVGetAudioOutputs, SRSActiveAlways, SPEI_UNDEFINED,
    SAFTCCITT_uLaw_11kHzStereo, ISpRecoGrammar2, DISPID_SPPs_NewEnum,
    DISPID_SVSpeakCompleteEvent, DISPID_SOTDisplayUI,
    DISPID_SRRGetXMLErrorInfo, ISpeechLexiconWords, _check_version,
    SAFT11kHz16BitMono, SAFTTrueSpeech_8kHz1BitMono, DISPID_SAFType,
    SVP_2, SPAUDIOBUFFERINFO, DISPID_SLPSymbolic,
    DISPID_SPEPronunciation, SVSFDefault, SPSHT_OTHER, DISPID_SVPause,
    SVP_17, eLEXTYPE_PRIVATE13, DISPID_SGRsAdd,
    DISPID_SRRDiscardResultInfo, SPWT_PRONUNCIATION, SECLowConfidence,
    SPDKL_LocalMachine, DISPID_SPRules_NewEnum, SPPS_Modifier,
    ISpPhraseAlt, SVP_10, eLEXTYPE_PRIVATE1, SGRSTTWord,
    eLEXTYPE_PRIVATE9, SRTExtendableParse, ISpeechAudio, SVPAlert,
    eLEXTYPE_PRIVATE4, DISPID_SDKEnumKeys, IStream,
    DISPID_SGRSTPropertyName, DISPID_SABIMinNotification, SGLexical,
    DISPID_SRGCmdLoadFromMemory, DISPID_SRCERecognizerStateChange,
    DISPID_SWFEFormatTag, SRERequestUI, DISPID_SLWsItem,
    DISPID_SRCESoundStart, DISPID_SRAudioInput,
    DISPID_SWFESamplesPerSec, ISpeechPhraseInfo,
    SpPhoneticAlphabetConverter, SPSFunction, DISPID_SAFGuid,
    DISPID_SPIAudioSizeBytes, SGDisplay, ISpeechPhraseProperties,
    VARIANT, SDA_No_Trailing_Space, SPEI_RECOGNITION,
    DISPID_SRAllowAudioInputFormatChangesOnNextSet,
    DISPID_SVESentenceBoundary, SPPS_RESERVED1,
    DISPID_SDKGetlongValue, SPEI_SOUND_END, SPRST_ACTIVE_ALWAYS,
    DISPID_SPPsItem, Speech_Max_Pron_Length,
    DISPIDSPTSI_SelectionOffset, DISPID_SPRText, ISpeechMMSysAudio,
    SPPHRASEREPLACEMENT, DISPID_SVSCurrentStreamNumber, SVP_0,
    SVEAudioLevel, DISPID_SVEPhoneme, SAFT16kHz16BitStereo,
    ISpeechAudioBufferInfo, DISPID_SGRsDynamic, SPEI_RESERVED3,
    SP_VISEME_17, SpObjectTokenCategory, SRSInactiveWithPurge,
    SGRSTTTextBuffer, eLEXTYPE_USER_SHORTCUT, SGPronounciation,
    ISpMMSysAudio, SPEI_RESERVED6, DISPID_SGRInitialState,
    SAFT22kHz16BitMono, SVP_7, SWPUnknownWordPronounceable,
    eLEXTYPE_PRIVATE8, _LARGE_INTEGER, SP_VISEME_19,
    eLEXTYPE_PRIVATE17, SAFT22kHz8BitStereo, DISPID_SPRsCount,
    SPEI_ACTIVE_CATEGORY_CHANGED, STSF_CommonAppData,
    SPEI_FALSE_RECOGNITION, ISpeechPhraseReplacements,
    SAFTADPCM_22kHzMono, DISPID_SPAsCount, SPPS_Function, SPAR_High,
    DISPID_SVGetAudioInputs, DISPID_SPRsItem, SREBookmark,
    SPBO_TIME_UNITS, SpTextSelectionInformation,
    SPWP_KNOWN_WORD_PRONOUNCEABLE, DISPID_SBSFormat, _RemotableHandle,
    DISPID_SVSPhonemeId, SAFTExtendedAudioFormat, DISPID_SFSClose,
    SPDKL_DefaultLocation, DISPID_SRDisplayUI, DISPID_SPRFirstElement,
    SAFT11kHz8BitStereo, DISPID_SVSInputSentencePosition, SAFTDefault,
    SPRS_INACTIVE, SPPROPERTYINFO, SpeechEngineProperties,
    DISPID_SPRuleId, DISPID_SGRSAddWordTransition, SPEI_PHONEME,
    SPPHRASERULE
)


class SpeechRunState(IntFlag):
    SRSEDone = 1
    SRSEIsSpeaking = 2


class SpeechBookmarkOptions(IntFlag):
    SBONone = 0
    SBOPause = 1


class SpeechRecognitionType(IntFlag):
    SRTStandard = 0
    SRTAutopause = 1
    SRTEmulated = 2
    SRTSMLTimeout = 4
    SRTExtendableParse = 8
    SRTReSent = 16


class SpeechInterference(IntFlag):
    SINone = 0
    SINoise = 1
    SINoSignal = 2
    SITooLoud = 3
    SITooQuiet = 4
    SITooFast = 5
    SITooSlow = 6


class SpeechRecognizerState(IntFlag):
    SRSInactive = 0
    SRSActive = 1
    SRSActiveAlways = 2
    SRSInactiveWithPurge = 3


class SPWAVEFORMATTYPE(IntFlag):
    SPWF_INPUT = 0
    SPWF_SRENGINE = 1


class SpeechStreamSeekPositionType(IntFlag):
    SSSPTRelativeToStart = 0
    SSSPTRelativeToCurrentPosition = 1
    SSSPTRelativeToEnd = 2


class SPVISEMES(IntFlag):
    SP_VISEME_0 = 0
    SP_VISEME_1 = 1
    SP_VISEME_2 = 2
    SP_VISEME_3 = 3
    SP_VISEME_4 = 4
    SP_VISEME_5 = 5
    SP_VISEME_6 = 6
    SP_VISEME_7 = 7
    SP_VISEME_8 = 8
    SP_VISEME_9 = 9
    SP_VISEME_10 = 10
    SP_VISEME_11 = 11
    SP_VISEME_12 = 12
    SP_VISEME_13 = 13
    SP_VISEME_14 = 14
    SP_VISEME_15 = 15
    SP_VISEME_16 = 16
    SP_VISEME_17 = 17
    SP_VISEME_18 = 18
    SP_VISEME_19 = 19
    SP_VISEME_20 = 20
    SP_VISEME_21 = 21


class SpeechTokenContext(IntFlag):
    STCInprocServer = 1
    STCInprocHandler = 2
    STCLocalServer = 4
    STCRemoteServer = 16
    STCAll = 23


class SpeechTokenShellFolder(IntFlag):
    STSF_AppData = 26
    STSF_LocalAppData = 28
    STSF_CommonAppData = 35
    STSF_FlagCreate = 32768


class SpeechFormatType(IntFlag):
    SFTInput = 0
    SFTSREngine = 1


class SPXMLRESULTOPTIONS(IntFlag):
    SPXRO_SML = 0
    SPXRO_Alternates_SML = 1


class SPLOADOPTIONS(IntFlag):
    SPLO_STATIC = 0
    SPLO_DYNAMIC = 1


class SpeechRecoEvents(IntFlag):
    SREStreamEnd = 1
    SRESoundStart = 2
    SRESoundEnd = 4
    SREPhraseStart = 8
    SRERecognition = 16
    SREHypothesis = 32
    SREBookmark = 64
    SREPropertyNumChange = 128
    SREPropertyStringChange = 256
    SREFalseRecognition = 512
    SREInterference = 1024
    SRERequestUI = 2048
    SREStateChange = 4096
    SREAdaptation = 8192
    SREStreamStart = 16384
    SRERecoOtherContext = 32768
    SREAudioLevel = 65536
    SREPrivate = 262144
    SREAllEvents = 393215


class SpeechRecoContextState(IntFlag):
    SRCS_Disabled = 0
    SRCS_Enabled = 1


class SpeechDataKeyLocation(IntFlag):
    SDKLDefaultLocation = 0
    SDKLCurrentUser = 1
    SDKLLocalMachine = 2
    SDKLCurrentConfig = 5


class SpeechAudioState(IntFlag):
    SASClosed = 0
    SASStop = 1
    SASPause = 2
    SASRun = 3


class _SPAUDIOSTATE(IntFlag):
    SPAS_CLOSED = 0
    SPAS_STOP = 1
    SPAS_PAUSE = 2
    SPAS_RUN = 3


class SpeechVisemeType(IntFlag):
    SVP_0 = 0
    SVP_1 = 1
    SVP_2 = 2
    SVP_3 = 3
    SVP_4 = 4
    SVP_5 = 5
    SVP_6 = 6
    SVP_7 = 7
    SVP_8 = 8
    SVP_9 = 9
    SVP_10 = 10
    SVP_11 = 11
    SVP_12 = 12
    SVP_13 = 13
    SVP_14 = 14
    SVP_15 = 15
    SVP_16 = 16
    SVP_17 = 17
    SVP_18 = 18
    SVP_19 = 19
    SVP_20 = 20
    SVP_21 = 21


class SPSEMANTICFORMAT(IntFlag):
    SPSMF_SAPI_PROPERTIES = 0
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
    SPSMF_SRGS_SAPIPROPERTIES = 2
    SPSMF_UPS = 4
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8


class SPGRAMMARWORDTYPE(IntFlag):
    SPWT_DISPLAY = 0
    SPWT_LEXICAL = 1
    SPWT_PRONUNCIATION = 2
    SPWT_LEXICAL_NO_SPECIAL_CHARS = 3


class SpeechStreamFileMode(IntFlag):
    SSFMOpenForRead = 0
    SSFMOpenReadWrite = 1
    SSFMCreate = 2
    SSFMCreateForWrite = 3


class SpeechVisemeFeature(IntFlag):
    SVF_None = 0
    SVF_Stressed = 1
    SVF_Emphasis = 2


class SpeechSpecialTransitionType(IntFlag):
    SSTTWildcard = 1
    SSTTDictation = 2
    SSTTTextBuffer = 3


class SPRULESTATE(IntFlag):
    SPRS_INACTIVE = 0
    SPRS_ACTIVE = 1
    SPRS_ACTIVE_WITH_AUTO_PAUSE = 3
    SPRS_ACTIVE_USER_DELIMITED = 4


class SPWORDPRONOUNCEABLE(IntFlag):
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE = 0
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE = 1
    SPWP_KNOWN_WORD_PRONOUNCEABLE = 2


class SPGRAMMARSTATE(IntFlag):
    SPGS_DISABLED = 0
    SPGS_ENABLED = 1
    SPGS_EXCLUSIVE = 3


class SPINTERFERENCE(IntFlag):
    SPINTERFERENCE_NONE = 0
    SPINTERFERENCE_NOISE = 1
    SPINTERFERENCE_NOSIGNAL = 2
    SPINTERFERENCE_TOOLOUD = 3
    SPINTERFERENCE_TOOQUIET = 4
    SPINTERFERENCE_TOOFAST = 5
    SPINTERFERENCE_TOOSLOW = 6
    SPINTERFERENCE_LATENCY_WARNING = 7
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN = 8
    SPINTERFERENCE_LATENCY_TRUNCATE_END = 9


class SPAUDIOOPTIONS(IntFlag):
    SPAO_NONE = 0
    SPAO_RETAIN_AUDIO = 1


class SpeechVoiceEvents(IntFlag):
    SVEStartInputStream = 2
    SVEEndInputStream = 4
    SVEVoiceChange = 8
    SVEBookmark = 16
    SVEWordBoundary = 32
    SVEPhoneme = 64
    SVESentenceBoundary = 128
    SVEViseme = 256
    SVEAudioLevel = 512
    SVEPrivate = 32768
    SVEAllEvents = 33790


class SpeechVoicePriority(IntFlag):
    SVPNormal = 0
    SVPAlert = 1
    SVPOver = 2


class SpeechRuleState(IntFlag):
    SGDSInactive = 0
    SGDSActive = 1
    SGDSActiveWithAutoPause = 3
    SGDSActiveUserDelimited = 4


class SpeechWordPronounceable(IntFlag):
    SWPUnknownWordUnpronounceable = 0
    SWPUnknownWordPronounceable = 1
    SWPKnownWordPronounceable = 2


class SPBOOKMARKOPTIONS(IntFlag):
    SPBO_NONE = 0
    SPBO_PAUSE = 1
    SPBO_AHEAD = 2
    SPBO_TIME_UNITS = 4


class SPCONTEXTSTATE(IntFlag):
    SPCS_DISABLED = 0
    SPCS_ENABLED = 1


class SpeechEngineConfidence(IntFlag):
    SECLowConfidence = -1
    SECNormalConfidence = 0
    SECHighConfidence = 1


class SPADAPTATIONRELEVANCE(IntFlag):
    SPAR_Unknown = 0
    SPAR_Low = 1
    SPAR_Medium = 2
    SPAR_High = 3


class SPCATEGORYTYPE(IntFlag):
    SPCT_COMMAND = 0
    SPCT_DICTATION = 1
    SPCT_SLEEP = 2
    SPCT_SUB_COMMAND = 3
    SPCT_SUB_DICTATION = 4


class SpeechDisplayAttributes(IntFlag):
    SDA_No_Trailing_Space = 0
    SDA_One_Trailing_Space = 2
    SDA_Two_Trailing_Spaces = 4
    SDA_Consume_Leading_Spaces = 8


class SpeechDiscardType(IntFlag):
    SDTProperty = 1
    SDTReplacement = 2
    SDTRule = 4
    SDTDisplayText = 8
    SDTLexicalForm = 16
    SDTPronunciation = 32
    SDTAudio = 64
    SDTAlternates = 128
    SDTAll = 255


class SPLEXICONTYPE(IntFlag):
    eLEXTYPE_USER = 1
    eLEXTYPE_APP = 2
    eLEXTYPE_VENDORLEXICON = 4
    eLEXTYPE_LETTERTOSOUND = 8
    eLEXTYPE_MORPHOLOGY = 16
    eLEXTYPE_RESERVED4 = 32
    eLEXTYPE_USER_SHORTCUT = 64
    eLEXTYPE_RESERVED6 = 128
    eLEXTYPE_RESERVED7 = 256
    eLEXTYPE_RESERVED8 = 512
    eLEXTYPE_RESERVED9 = 1024
    eLEXTYPE_RESERVED10 = 2048
    eLEXTYPE_PRIVATE1 = 4096
    eLEXTYPE_PRIVATE2 = 8192
    eLEXTYPE_PRIVATE3 = 16384
    eLEXTYPE_PRIVATE4 = 32768
    eLEXTYPE_PRIVATE5 = 65536
    eLEXTYPE_PRIVATE6 = 131072
    eLEXTYPE_PRIVATE7 = 262144
    eLEXTYPE_PRIVATE8 = 524288
    eLEXTYPE_PRIVATE9 = 1048576
    eLEXTYPE_PRIVATE10 = 2097152
    eLEXTYPE_PRIVATE11 = 4194304
    eLEXTYPE_PRIVATE12 = 8388608
    eLEXTYPE_PRIVATE13 = 16777216
    eLEXTYPE_PRIVATE14 = 33554432
    eLEXTYPE_PRIVATE15 = 67108864
    eLEXTYPE_PRIVATE16 = 134217728
    eLEXTYPE_PRIVATE17 = 268435456
    eLEXTYPE_PRIVATE18 = 536870912
    eLEXTYPE_PRIVATE19 = 1073741824
    eLEXTYPE_PRIVATE20 = -2147483648


class SPPARTOFSPEECH(IntFlag):
    SPPS_NotOverriden = -1
    SPPS_Unknown = 0
    SPPS_Noun = 4096
    SPPS_Verb = 8192
    SPPS_Modifier = 12288
    SPPS_Function = 16384
    SPPS_Interjection = 20480
    SPPS_Noncontent = 24576
    SPPS_LMA = 28672
    SPPS_SuppressWord = 61440


class SpeechLexiconType(IntFlag):
    SLTUser = 1
    SLTApp = 2


class SpeechWordType(IntFlag):
    SWTAdded = 1
    SWTDeleted = 2


class SpeechLoadOption(IntFlag):
    SLOStatic = 0
    SLODynamic = 1


class SpeechPartOfSpeech(IntFlag):
    SPSNotOverriden = -1
    SPSUnknown = 0
    SPSNoun = 4096
    SPSVerb = 8192
    SPSModifier = 12288
    SPSFunction = 16384
    SPSInterjection = 20480
    SPSLMA = 28672
    SPSSuppressWord = 61440


class SPWORDTYPE(IntFlag):
    eWORDTYPE_ADDED = 1
    eWORDTYPE_DELETED = 2


class SPSHORTCUTTYPE(IntFlag):
    SPSHT_NotOverriden = -1
    SPSHT_Unknown = 0
    SPSHT_EMAIL = 4096
    SPSHT_OTHER = 8192
    SPPS_RESERVED1 = 12288
    SPPS_RESERVED2 = 16384
    SPPS_RESERVED3 = 20480
    SPPS_RESERVED4 = 61440


class SpeechAudioFormatType(IntFlag):
    SAFTDefault = -1
    SAFTNoAssignedFormat = 0
    SAFTText = 1
    SAFTNonStandardFormat = 2
    SAFTExtendedAudioFormat = 3
    SAFT8kHz8BitMono = 4
    SAFT8kHz8BitStereo = 5
    SAFT8kHz16BitMono = 6
    SAFT8kHz16BitStereo = 7
    SAFT11kHz8BitMono = 8
    SAFT11kHz8BitStereo = 9
    SAFT11kHz16BitMono = 10
    SAFT11kHz16BitStereo = 11
    SAFT12kHz8BitMono = 12
    SAFT12kHz8BitStereo = 13
    SAFT12kHz16BitMono = 14
    SAFT12kHz16BitStereo = 15
    SAFT16kHz8BitMono = 16
    SAFT16kHz8BitStereo = 17
    SAFT16kHz16BitMono = 18
    SAFT16kHz16BitStereo = 19
    SAFT22kHz8BitMono = 20
    SAFT22kHz8BitStereo = 21
    SAFT22kHz16BitMono = 22
    SAFT22kHz16BitStereo = 23
    SAFT24kHz8BitMono = 24
    SAFT24kHz8BitStereo = 25
    SAFT24kHz16BitMono = 26
    SAFT24kHz16BitStereo = 27
    SAFT32kHz8BitMono = 28
    SAFT32kHz8BitStereo = 29
    SAFT32kHz16BitMono = 30
    SAFT32kHz16BitStereo = 31
    SAFT44kHz8BitMono = 32
    SAFT44kHz8BitStereo = 33
    SAFT44kHz16BitMono = 34
    SAFT44kHz16BitStereo = 35
    SAFT48kHz8BitMono = 36
    SAFT48kHz8BitStereo = 37
    SAFT48kHz16BitMono = 38
    SAFT48kHz16BitStereo = 39
    SAFTTrueSpeech_8kHz1BitMono = 40
    SAFTCCITT_ALaw_8kHzMono = 41
    SAFTCCITT_ALaw_8kHzStereo = 42
    SAFTCCITT_ALaw_11kHzMono = 43
    SAFTCCITT_ALaw_11kHzStereo = 44
    SAFTCCITT_ALaw_22kHzMono = 45
    SAFTCCITT_ALaw_22kHzStereo = 46
    SAFTCCITT_ALaw_44kHzMono = 47
    SAFTCCITT_ALaw_44kHzStereo = 48
    SAFTCCITT_uLaw_8kHzMono = 49
    SAFTCCITT_uLaw_8kHzStereo = 50
    SAFTCCITT_uLaw_11kHzMono = 51
    SAFTCCITT_uLaw_11kHzStereo = 52
    SAFTCCITT_uLaw_22kHzMono = 53
    SAFTCCITT_uLaw_22kHzStereo = 54
    SAFTCCITT_uLaw_44kHzMono = 55
    SAFTCCITT_uLaw_44kHzStereo = 56
    SAFTADPCM_8kHzMono = 57
    SAFTADPCM_8kHzStereo = 58
    SAFTADPCM_11kHzMono = 59
    SAFTADPCM_11kHzStereo = 60
    SAFTADPCM_22kHzMono = 61
    SAFTADPCM_22kHzStereo = 62
    SAFTADPCM_44kHzMono = 63
    SAFTADPCM_44kHzStereo = 64
    SAFTGSM610_8kHzMono = 65
    SAFTGSM610_11kHzMono = 66
    SAFTGSM610_22kHzMono = 67
    SAFTGSM610_44kHzMono = 68


class DISPID_SpeechDataKey(IntFlag):
    DISPID_SDKSetBinaryValue = 1
    DISPID_SDKGetBinaryValue = 2
    DISPID_SDKSetStringValue = 3
    DISPID_SDKGetStringValue = 4
    DISPID_SDKSetLongValue = 5
    DISPID_SDKGetlongValue = 6
    DISPID_SDKOpenKey = 7
    DISPID_SDKCreateKey = 8
    DISPID_SDKDeleteKey = 9
    DISPID_SDKDeleteValue = 10
    DISPID_SDKEnumKeys = 11
    DISPID_SDKEnumValues = 12


class DISPID_SpeechObjectToken(IntFlag):
    DISPID_SOTId = 1
    DISPID_SOTDataKey = 2
    DISPID_SOTCategory = 3
    DISPID_SOTGetDescription = 4
    DISPID_SOTSetId = 5
    DISPID_SOTGetAttribute = 6
    DISPID_SOTCreateInstance = 7
    DISPID_SOTRemove = 8
    DISPID_SOTGetStorageFileName = 9
    DISPID_SOTRemoveStorageFileName = 10
    DISPID_SOTIsUISupported = 11
    DISPID_SOTDisplayUI = 12
    DISPID_SOTMatchesAttributes = 13


class DISPID_SpeechObjectTokens(IntFlag):
    DISPID_SOTsCount = 1
    DISPID_SOTsItem = 0
    DISPID_SOTs_NewEnum = -4


class SpeechGrammarState(IntFlag):
    SGSEnabled = 1
    SGSDisabled = 0
    SGSExclusive = 3


class DISPID_SpeechObjectTokenCategory(IntFlag):
    DISPID_SOTCId = 1
    DISPID_SOTCDefault = 2
    DISPID_SOTCSetId = 3
    DISPID_SOTCGetDataKey = 4
    DISPID_SOTCEnumerateTokens = 5


class DISPID_SpeechAudioFormat(IntFlag):
    DISPID_SAFType = 1
    DISPID_SAFGuid = 2
    DISPID_SAFGetWaveFormatEx = 3
    DISPID_SAFSetWaveFormatEx = 4


class DISPID_SpeechBaseStream(IntFlag):
    DISPID_SBSFormat = 1
    DISPID_SBSRead = 2
    DISPID_SBSWrite = 3
    DISPID_SBSSeek = 4


class SpeechVoiceSpeakFlags(IntFlag):
    SVSFDefault = 0
    SVSFlagsAsync = 1
    SVSFPurgeBeforeSpeak = 2
    SVSFIsFilename = 4
    SVSFIsXML = 8
    SVSFIsNotXML = 16
    SVSFPersistXML = 32
    SVSFNLPSpeakPunc = 64
    SVSFParseSapi = 128
    SVSFParseSsml = 256
    SVSFParseAutodetect = 0
    SVSFNLPMask = 64
    SVSFParseMask = 384
    SVSFVoiceMask = 511
    SVSFUnusedFlags = -512


class DISPID_SpeechAudio(IntFlag):
    DISPID_SAStatus = 200
    DISPID_SABufferInfo = 201
    DISPID_SADefaultFormat = 202
    DISPID_SAVolume = 203
    DISPID_SABufferNotifySize = 204
    DISPID_SAEventHandle = 205
    DISPID_SASetState = 206


class DISPID_SpeechMMSysAudio(IntFlag):
    DISPID_SMSADeviceId = 300
    DISPID_SMSALineId = 301
    DISPID_SMSAMMHandle = 302


class DISPID_SpeechFileStream(IntFlag):
    DISPID_SFSOpen = 100
    DISPID_SFSClose = 101


class DISPID_SpeechCustomStream(IntFlag):
    DISPID_SCSBaseStream = 100


class SpeechRuleAttributes(IntFlag):
    SRATopLevel = 1
    SRADefaultToActive = 2
    SRAExport = 4
    SRAImport = 8
    SRAInterpreter = 16
    SRADynamic = 32
    SRARoot = 64


class DISPID_SpeechMemoryStream(IntFlag):
    DISPID_SMSSetData = 100
    DISPID_SMSGetData = 101


class DISPID_SpeechAudioStatus(IntFlag):
    DISPID_SASFreeBufferSpace = 1
    DISPID_SASNonBlockingIO = 2
    DISPID_SASState = 3
    DISPID_SASCurrentSeekPosition = 4
    DISPID_SASCurrentDevicePosition = 5


class DISPID_SpeechAudioBufferInfo(IntFlag):
    DISPID_SABIMinNotification = 1
    DISPID_SABIBufferSize = 2
    DISPID_SABIEventBias = 3


class DISPID_SpeechWaveFormatEx(IntFlag):
    DISPID_SWFEFormatTag = 1
    DISPID_SWFEChannels = 2
    DISPID_SWFESamplesPerSec = 3
    DISPID_SWFEAvgBytesPerSec = 4
    DISPID_SWFEBlockAlign = 5
    DISPID_SWFEBitsPerSample = 6
    DISPID_SWFEExtraData = 7


class DISPID_SpeechVoice(IntFlag):
    DISPID_SVStatus = 1
    DISPID_SVVoice = 2
    DISPID_SVAudioOutput = 3
    DISPID_SVAudioOutputStream = 4
    DISPID_SVRate = 5
    DISPID_SVVolume = 6
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet = 7
    DISPID_SVEventInterests = 8
    DISPID_SVPriority = 9
    DISPID_SVAlertBoundary = 10
    DISPID_SVSyncronousSpeakTimeout = 11
    DISPID_SVSpeak = 12
    DISPID_SVSpeakStream = 13
    DISPID_SVPause = 14
    DISPID_SVResume = 15
    DISPID_SVSkip = 16
    DISPID_SVGetVoices = 17
    DISPID_SVGetAudioOutputs = 18
    DISPID_SVWaitUntilDone = 19
    DISPID_SVSpeakCompleteEvent = 20
    DISPID_SVIsUISupported = 21
    DISPID_SVDisplayUI = 22


class DISPID_SpeechVoiceStatus(IntFlag):
    DISPID_SVSCurrentStreamNumber = 1
    DISPID_SVSLastStreamNumberQueued = 2
    DISPID_SVSLastResult = 3
    DISPID_SVSRunningState = 4
    DISPID_SVSInputWordPosition = 5
    DISPID_SVSInputWordLength = 6
    DISPID_SVSInputSentencePosition = 7
    DISPID_SVSInputSentenceLength = 8
    DISPID_SVSLastBookmark = 9
    DISPID_SVSLastBookmarkId = 10
    DISPID_SVSPhonemeId = 11
    DISPID_SVSVisemeId = 12


class DISPID_SpeechVoiceEvent(IntFlag):
    DISPID_SVEStreamStart = 1
    DISPID_SVEStreamEnd = 2
    DISPID_SVEVoiceChange = 3
    DISPID_SVEBookmark = 4
    DISPID_SVEWord = 5
    DISPID_SVEPhoneme = 6
    DISPID_SVESentenceBoundary = 7
    DISPID_SVEViseme = 8
    DISPID_SVEAudioLevel = 9
    DISPID_SVEEnginePrivate = 10


class SPFILEMODE(IntFlag):
    SPFM_OPEN_READONLY = 0
    SPFM_OPEN_READWRITE = 1
    SPFM_CREATE = 2
    SPFM_CREATE_ALWAYS = 3
    SPFM_NUM_MODES = 4


class DISPID_SpeechRecognizer(IntFlag):
    DISPID_SRRecognizer = 1
    DISPID_SRAllowAudioInputFormatChangesOnNextSet = 2
    DISPID_SRAudioInput = 3
    DISPID_SRAudioInputStream = 4
    DISPID_SRIsShared = 5
    DISPID_SRState = 6
    DISPID_SRStatus = 7
    DISPID_SRProfile = 8
    DISPID_SREmulateRecognition = 9
    DISPID_SRCreateRecoContext = 10
    DISPID_SRGetFormat = 11
    DISPID_SRSetPropertyNumber = 12
    DISPID_SRGetPropertyNumber = 13
    DISPID_SRSetPropertyString = 14
    DISPID_SRGetPropertyString = 15
    DISPID_SRIsUISupported = 16
    DISPID_SRDisplayUI = 17
    DISPID_SRGetRecognizers = 18
    DISPID_SVGetAudioInputs = 19
    DISPID_SVGetProfiles = 20


class SpeechEmulationCompareFlags(IntFlag):
    SECFIgnoreCase = 1
    SECFIgnoreKanaType = 65536
    SECFIgnoreWidth = 131072
    SECFNoSpecialChars = 536870912
    SECFEmulateResult = 1073741824
    SECFDefault = 196609


class DISPID_SpeechRecognizerStatus(IntFlag):
    DISPID_SRSAudioStatus = 1
    DISPID_SRSCurrentStreamPosition = 2
    DISPID_SRSCurrentStreamNumber = 3
    DISPID_SRSNumberOfActiveRules = 4
    DISPID_SRSClsidEngine = 5
    DISPID_SRSSupportedLanguages = 6


class DISPID_SpeechRecoContext(IntFlag):
    DISPID_SRCRecognizer = 1
    DISPID_SRCAudioInInterferenceStatus = 2
    DISPID_SRCRequestedUIType = 3
    DISPID_SRCVoice = 4
    DISPID_SRAllowVoiceFormatMatchingOnNextSet = 5
    DISPID_SRCVoicePurgeEvent = 6
    DISPID_SRCEventInterests = 7
    DISPID_SRCCmdMaxAlternates = 8
    DISPID_SRCState = 9
    DISPID_SRCRetainedAudio = 10
    DISPID_SRCRetainedAudioFormat = 11
    DISPID_SRCPause = 12
    DISPID_SRCResume = 13
    DISPID_SRCCreateGrammar = 14
    DISPID_SRCCreateResultFromMemory = 15
    DISPID_SRCBookmark = 16
    DISPID_SRCSetAdaptationData = 17


class DISPIDSPRG(IntFlag):
    DISPID_SRGId = 1
    DISPID_SRGRecoContext = 2
    DISPID_SRGState = 3
    DISPID_SRGRules = 4
    DISPID_SRGReset = 5
    DISPID_SRGCommit = 6
    DISPID_SRGCmdLoadFromFile = 7
    DISPID_SRGCmdLoadFromObject = 8
    DISPID_SRGCmdLoadFromResource = 9
    DISPID_SRGCmdLoadFromMemory = 10
    DISPID_SRGCmdLoadFromProprietaryGrammar = 11
    DISPID_SRGCmdSetRuleState = 12
    DISPID_SRGCmdSetRuleIdState = 13
    DISPID_SRGDictationLoad = 14
    DISPID_SRGDictationUnload = 15
    DISPID_SRGDictationSetState = 16
    DISPID_SRGSetWordSequenceData = 17
    DISPID_SRGSetTextSelection = 18
    DISPID_SRGIsPronounceable = 19


class SPVPRIORITY(IntFlag):
    SPVPRI_NORMAL = 0
    SPVPRI_ALERT = 1
    SPVPRI_OVER = 2


class SPEVENTENUM(IntFlag):
    SPEI_UNDEFINED = 0
    SPEI_START_INPUT_STREAM = 1
    SPEI_END_INPUT_STREAM = 2
    SPEI_VOICE_CHANGE = 3
    SPEI_TTS_BOOKMARK = 4
    SPEI_WORD_BOUNDARY = 5
    SPEI_PHONEME = 6
    SPEI_SENTENCE_BOUNDARY = 7
    SPEI_VISEME = 8
    SPEI_TTS_AUDIO_LEVEL = 9
    SPEI_TTS_PRIVATE = 15
    SPEI_MIN_TTS = 1
    SPEI_MAX_TTS = 15
    SPEI_END_SR_STREAM = 34
    SPEI_SOUND_START = 35
    SPEI_SOUND_END = 36
    SPEI_PHRASE_START = 37
    SPEI_RECOGNITION = 38
    SPEI_HYPOTHESIS = 39
    SPEI_SR_BOOKMARK = 40
    SPEI_PROPERTY_NUM_CHANGE = 41
    SPEI_PROPERTY_STRING_CHANGE = 42
    SPEI_FALSE_RECOGNITION = 43
    SPEI_INTERFERENCE = 44
    SPEI_REQUEST_UI = 45
    SPEI_RECO_STATE_CHANGE = 46
    SPEI_ADAPTATION = 47
    SPEI_START_SR_STREAM = 48
    SPEI_RECO_OTHER_CONTEXT = 49
    SPEI_SR_AUDIO_LEVEL = 50
    SPEI_SR_RETAINEDAUDIO = 51
    SPEI_SR_PRIVATE = 52
    SPEI_ACTIVE_CATEGORY_CHANGED = 53
    SPEI_RESERVED5 = 54
    SPEI_RESERVED6 = 55
    SPEI_MIN_SR = 34
    SPEI_MAX_SR = 55
    SPEI_RESERVED1 = 30
    SPEI_RESERVED2 = 33
    SPEI_RESERVED3 = 63


class DISPID_SpeechRecoContextEvents(IntFlag):
    DISPID_SRCEStartStream = 1
    DISPID_SRCEEndStream = 2
    DISPID_SRCEBookmark = 3
    DISPID_SRCESoundStart = 4
    DISPID_SRCESoundEnd = 5
    DISPID_SRCEPhraseStart = 6
    DISPID_SRCERecognition = 7
    DISPID_SRCEHypothesis = 8
    DISPID_SRCEPropertyNumberChange = 9
    DISPID_SRCEPropertyStringChange = 10
    DISPID_SRCEFalseRecognition = 11
    DISPID_SRCEInterference = 12
    DISPID_SRCERequestUI = 13
    DISPID_SRCERecognizerStateChange = 14
    DISPID_SRCEAdaptation = 15
    DISPID_SRCERecognitionForOtherContext = 16
    DISPID_SRCEAudioLevel = 17
    DISPID_SRCEEnginePrivate = 18


class DISPID_SpeechGrammarRule(IntFlag):
    DISPID_SGRAttributes = 1
    DISPID_SGRInitialState = 2
    DISPID_SGRName = 3
    DISPID_SGRId = 4
    DISPID_SGRClear = 5
    DISPID_SGRAddResource = 6
    DISPID_SGRAddState = 7


class DISPID_SpeechGrammarRules(IntFlag):
    DISPID_SGRsCount = 1
    DISPID_SGRsDynamic = 2
    DISPID_SGRsAdd = 3
    DISPID_SGRsCommit = 4
    DISPID_SGRsCommitAndSave = 5
    DISPID_SGRsFindRule = 6
    DISPID_SGRsItem = 0
    DISPID_SGRs_NewEnum = -4


class DISPID_SpeechGrammarRuleState(IntFlag):
    DISPID_SGRSRule = 1
    DISPID_SGRSTransitions = 2
    DISPID_SGRSAddWordTransition = 3
    DISPID_SGRSAddRuleTransition = 4
    DISPID_SGRSAddSpecialTransition = 5


class DISPID_SpeechGrammarRuleStateTransitions(IntFlag):
    DISPID_SGRSTsCount = 1
    DISPID_SGRSTsItem = 0
    DISPID_SGRSTs_NewEnum = -4


class DISPID_SpeechGrammarRuleStateTransition(IntFlag):
    DISPID_SGRSTType = 1
    DISPID_SGRSTText = 2
    DISPID_SGRSTRule = 3
    DISPID_SGRSTWeight = 4
    DISPID_SGRSTPropertyName = 5
    DISPID_SGRSTPropertyId = 6
    DISPID_SGRSTPropertyValue = 7
    DISPID_SGRSTNextState = 8


class DISPIDSPTSI(IntFlag):
    DISPIDSPTSI_ActiveOffset = 1
    DISPIDSPTSI_ActiveLength = 2
    DISPIDSPTSI_SelectionOffset = 3
    DISPIDSPTSI_SelectionLength = 4


class DISPID_SpeechRecoResult(IntFlag):
    DISPID_SRRRecoContext = 1
    DISPID_SRRTimes = 2
    DISPID_SRRAudioFormat = 3
    DISPID_SRRPhraseInfo = 4
    DISPID_SRRAlternates = 5
    DISPID_SRRAudio = 6
    DISPID_SRRSpeakAudio = 7
    DISPID_SRRSaveToMemory = 8
    DISPID_SRRDiscardResultInfo = 9


class DISPID_SpeechXMLRecoResult(IntFlag):
    DISPID_SRRGetXMLResult = 10
    DISPID_SRRGetXMLErrorInfo = 11


class SpeechGrammarWordType(IntFlag):
    SGDisplay = 0
    SGLexical = 1
    SGPronounciation = 2
    SGLexicalNoSpecialChars = 3


class DISPID_SpeechRecoResult2(IntFlag):
    DISPID_SRRSetTextFeedback = 12


class SpeechGrammarRuleStateTransitionType(IntFlag):
    SGRSTTEpsilon = 0
    SGRSTTWord = 1
    SGRSTTRule = 2
    SGRSTTDictation = 3
    SGRSTTWildcard = 4
    SGRSTTTextBuffer = 5


class SPRECOSTATE(IntFlag):
    SPRST_INACTIVE = 0
    SPRST_ACTIVE = 1
    SPRST_ACTIVE_ALWAYS = 2
    SPRST_INACTIVE_WITH_PURGE = 3
    SPRST_NUM_STATES = 4


class DISPID_SpeechPhraseBuilder(IntFlag):
    DISPID_SPPBRestorePhraseFromMemory = 1


class DISPID_SpeechRecoResultTimes(IntFlag):
    DISPID_SRRTStreamTime = 1
    DISPID_SRRTLength = 2
    DISPID_SRRTTickCount = 3
    DISPID_SRRTOffsetFromStart = 4


class DISPID_SpeechPhraseAlternate(IntFlag):
    DISPID_SPARecoResult = 1
    DISPID_SPAStartElementInResult = 2
    DISPID_SPANumberOfElementsInResult = 3
    DISPID_SPAPhraseInfo = 4
    DISPID_SPACommit = 5


class DISPID_SpeechPhraseAlternates(IntFlag):
    DISPID_SPAsCount = 1
    DISPID_SPAsItem = 0
    DISPID_SPAs_NewEnum = -4


class DISPID_SpeechPhraseInfo(IntFlag):
    DISPID_SPILanguageId = 1
    DISPID_SPIGrammarId = 2
    DISPID_SPIStartTime = 3
    DISPID_SPIAudioStreamPosition = 4
    DISPID_SPIAudioSizeBytes = 5
    DISPID_SPIRetainedSizeBytes = 6
    DISPID_SPIAudioSizeTime = 7
    DISPID_SPIRule = 8
    DISPID_SPIProperties = 9
    DISPID_SPIElements = 10
    DISPID_SPIReplacements = 11
    DISPID_SPIEngineId = 12
    DISPID_SPIEnginePrivateData = 13
    DISPID_SPISaveToMemory = 14
    DISPID_SPIGetText = 15
    DISPID_SPIGetDisplayAttributes = 16


class DISPID_SpeechPhraseElement(IntFlag):
    DISPID_SPEAudioTimeOffset = 1
    DISPID_SPEAudioSizeTime = 2
    DISPID_SPEAudioStreamOffset = 3
    DISPID_SPEAudioSizeBytes = 4
    DISPID_SPERetainedStreamOffset = 5
    DISPID_SPERetainedSizeBytes = 6
    DISPID_SPEDisplayText = 7
    DISPID_SPELexicalForm = 8
    DISPID_SPEPronunciation = 9
    DISPID_SPEDisplayAttributes = 10
    DISPID_SPERequiredConfidence = 11
    DISPID_SPEActualConfidence = 12
    DISPID_SPEEngineConfidence = 13


class DISPID_SpeechPhraseElements(IntFlag):
    DISPID_SPEsCount = 1
    DISPID_SPEsItem = 0
    DISPID_SPEs_NewEnum = -4


class DISPID_SpeechPhraseReplacement(IntFlag):
    DISPID_SPRDisplayAttributes = 1
    DISPID_SPRText = 2
    DISPID_SPRFirstElement = 3
    DISPID_SPRNumberOfElements = 4


class DISPID_SpeechPhraseReplacements(IntFlag):
    DISPID_SPRsCount = 1
    DISPID_SPRsItem = 0
    DISPID_SPRs_NewEnum = -4


class DISPID_SpeechPhraseProperty(IntFlag):
    DISPID_SPPName = 1
    DISPID_SPPId = 2
    DISPID_SPPValue = 3
    DISPID_SPPFirstElement = 4
    DISPID_SPPNumberOfElements = 5
    DISPID_SPPEngineConfidence = 6
    DISPID_SPPConfidence = 7
    DISPID_SPPParent = 8
    DISPID_SPPChildren = 9


class DISPID_SpeechPhraseProperties(IntFlag):
    DISPID_SPPsCount = 1
    DISPID_SPPsItem = 0
    DISPID_SPPs_NewEnum = -4


class DISPID_SpeechPhraseRule(IntFlag):
    DISPID_SPRuleName = 1
    DISPID_SPRuleId = 2
    DISPID_SPRuleFirstElement = 3
    DISPID_SPRuleNumberOfElements = 4
    DISPID_SPRuleParent = 5
    DISPID_SPRuleChildren = 6
    DISPID_SPRuleConfidence = 7
    DISPID_SPRuleEngineConfidence = 8


class DISPID_SpeechPhraseRules(IntFlag):
    DISPID_SPRulesCount = 1
    DISPID_SPRulesItem = 0
    DISPID_SPRules_NewEnum = -4


class DISPID_SpeechLexicon(IntFlag):
    DISPID_SLGenerationId = 1
    DISPID_SLGetWords = 2
    DISPID_SLAddPronunciation = 3
    DISPID_SLAddPronunciationByPhoneIds = 4
    DISPID_SLRemovePronunciation = 5
    DISPID_SLRemovePronunciationByPhoneIds = 6
    DISPID_SLGetPronunciations = 7
    DISPID_SLGetGenerationChange = 8


class DISPID_SpeechLexiconWords(IntFlag):
    DISPID_SLWsCount = 1
    DISPID_SLWsItem = 0
    DISPID_SLWs_NewEnum = -4


class DISPID_SpeechLexiconWord(IntFlag):
    DISPID_SLWLangId = 1
    DISPID_SLWType = 2
    DISPID_SLWWord = 3
    DISPID_SLWPronunciations = 4


class DISPID_SpeechLexiconProns(IntFlag):
    DISPID_SLPsCount = 1
    DISPID_SLPsItem = 0
    DISPID_SLPs_NewEnum = -4


class DISPID_SpeechLexiconPronunciation(IntFlag):
    DISPID_SLPType = 1
    DISPID_SLPLangId = 2
    DISPID_SLPPartOfSpeech = 3
    DISPID_SLPPhoneIds = 4
    DISPID_SLPSymbolic = 5


class DISPID_SpeechPhoneConverter(IntFlag):
    DISPID_SPCLangId = 1
    DISPID_SPCPhoneToId = 2
    DISPID_SPCIdToPhone = 3


class SPDATAKEYLOCATION(IntFlag):
    SPDKL_DefaultLocation = 0
    SPDKL_CurrentUser = 1
    SPDKL_LocalMachine = 2
    SPDKL_CurrentConfig = 5


class SpeechRetainedAudioOptions(IntFlag):
    SRAONone = 0
    SRAORetainAudio = 1


SPAUDIOSTATE = _SPAUDIOSTATE
SPSTREAMFORMATTYPE = SPWAVEFORMATTYPE


__all__ = [
    'DISPID_SVSInputWordPosition', 'ISpEventSink',
    'ISpeechObjectTokens', 'SpeechAudioState', 'SpFileStream',
    'SPAUDIOOPTIONS', 'SAFTGSM610_44kHzMono',
    'DISPID_SpeechMemoryStream', 'DISPID_SGRId', 'SPEI_RESERVED5',
    'SP_VISEME_11', '_ISpeechVoiceEvents', 'SVSFlagsAsync',
    'SPEI_MIN_SR', 'SPBO_PAUSE', 'STSF_FlagCreate',
    'ISpeechAudioStatus', 'DISPID_SVSVisemeId', 'SpeechTokenContext',
    'SVEWordBoundary', 'SDTAudio', 'eLEXTYPE_PRIVATE20',
    'DISPID_SRSNumberOfActiveRules', 'SECFNoSpecialChars',
    'SpeechVoiceEvents', 'SpeechRegistryUserRoot', 'SSTTTextBuffer',
    'SpeechCategoryVoices', 'SPGS_EXCLUSIVE', 'SRADefaultToActive',
    'STSF_AppData', 'SPWORDTYPE', 'SpeechRecognizerState',
    'SPINTERFERENCE_TOOQUIET', 'SPCT_SUB_DICTATION',
    'eWORDTYPE_DELETED', 'DISPID_SPCPhoneToId', 'SPEVENTSOURCEINFO',
    'SPINTERFERENCE_NONE', 'eWORDTYPE_ADDED', 'SAFTADPCM_44kHzMono',
    'DISPID_SPIGetText', 'SPEI_ADAPTATION', 'SPAO_NONE',
    'DISPIDSPTSI_ActiveLength', 'DISPID_SGRSTType',
    'ISpeechFileStream', 'SPEI_TTS_AUDIO_LEVEL', 'SGRSTTEpsilon',
    'SPSTREAMFORMATTYPE', 'DISPID_SLAddPronunciationByPhoneIds',
    'SAFT24kHz8BitStereo', 'SPBOOKMARKOPTIONS', 'SP_VISEME_4',
    'SREPropertyNumChange', 'DISPID_SVAudioOutput',
    'ISpeechRecognizerStatus', 'eLEXTYPE_PRIVATE6',
    'SAFT12kHz8BitMono', 'SPPS_NotOverriden', 'DISPID_SRRRecoContext',
    'SAFT44kHz8BitMono', 'DISPID_SVSyncronousSpeakTimeout',
    'DISPID_SpeechGrammarRuleState', 'SPSNoun', 'SAFT11kHz8BitMono',
    'SpeechWordType', 'DISPID_SRSCurrentStreamPosition',
    'DISPID_SRCResume', 'DISPID_SRCCreateGrammar',
    'SPEI_START_INPUT_STREAM', 'DISPID_SpeechPhraseElements',
    'SAFTGSM610_22kHzMono', 'SVP_21',
    'SpeechPropertyComplexResponseSpeed', 'DISPID_SVGetVoices',
    'SPAUDIOSTATUS', 'DISPID_SOTMatchesAttributes',
    'DISPID_SGRsCount', 'SVF_Emphasis', 'ISpeechPhraseReplacement',
    'eLEXTYPE_MORPHOLOGY', 'DISPID_SDKOpenKey', 'SDKLLocalMachine',
    'SPPS_RESERVED2', 'DISPID_SBSRead', 'SPRECOCONTEXTSTATUS',
    'SpSharedRecognizer', 'SpMMAudioOut', 'SPVISEMES',
    'SREHypothesis', 'SGDSInactive', 'SP_VISEME_16',
    'DISPID_SVSRunningState', 'DISPID_SpeechLexiconWord',
    'SPDKL_CurrentConfig', 'SPLO_STATIC', 'SWTDeleted',
    'DISPID_SLRemovePronunciation',
    'SpeechGrammarTagUnlimitedDictation', 'ISpeechRecoGrammar',
    'SpeechTokenValueCLSID', 'DISPID_SRCRecognizer', 'SPVPRIORITY',
    'DISPID_SPISaveToMemory', 'SpeechDictationTopicSpelling',
    'DISPID_SRGetPropertyString', 'SpeechCategoryAudioIn',
    'DISPID_SLPs_NewEnum', 'SPRST_NUM_STATES', 'SPSSuppressWord',
    'SVEPrivate', 'DISPID_SLAddPronunciation', 'SBOPause',
    'DISPID_SpeechDataKey', 'SPEI_MIN_TTS', 'DISPID_SASState',
    'DISPID_SDKSetLongValue', 'DISPID_SRCEFalseRecognition',
    'DISPID_SGRSTs_NewEnum', 'SpMemoryStream', 'ISpRecognizer2',
    'SRAORetainAudio', 'SPFILEMODE', 'DISPID_SpeechWaveFormatEx',
    'DISPID_SRStatus', 'SPWP_UNKNOWN_WORD_PRONOUNCEABLE',
    'SpeechRuleState', 'SSSPTRelativeToStart', 'DISPID_SWFEExtraData',
    'DISPID_SDKDeleteKey', 'DISPID_SPIEnginePrivateData',
    'SGRSTTRule', 'DISPID_SVSInputWordLength', 'SPSInterjection',
    'UINT_PTR', 'DISPID_SDKGetStringValue', 'DISPID_SLPLangId',
    'DISPID_SDKCreateKey', 'SAFTADPCM_44kHzStereo',
    'DISPID_SVEVoiceChange', 'SPXRO_SML', 'ISpRecoResult',
    'SpMMAudioEnum', 'DISPID_SRGRecoContext', 'SPWT_LEXICAL',
    'DISPID_SOTRemoveStorageFileName', 'SpeechGrammarTagWildcard',
    'SpeechVoiceCategoryTTSRate', 'SPLOADOPTIONS',
    'IEnumSpObjectTokens', 'DISPID_SABufferInfo',
    'SAFT48kHz16BitStereo', 'SRATopLevel', 'SPAR_Medium',
    'DISPID_SRRPhraseInfo', 'DISPID_SRRSpeakAudio', 'SVP_15',
    'SPEI_SR_RETAINEDAUDIO', 'DISPID_SRCEHypothesis',
    'DISPID_SRSetPropertyNumber', 'SpeechVoiceSpeakFlags',
    'DISPID_SRCEBookmark', 'DISPID_SCSBaseStream',
    'DISPID_SGRs_NewEnum', 'DISPID_SOTSetId', 'SPSModifier',
    'ISpAudio', 'DISPID_SLPPartOfSpeech', 'SPAO_RETAIN_AUDIO',
    'SPWORDLIST', 'STSF_LocalAppData', 'SpAudioFormat',
    'DISPID_SVEStreamEnd', 'DISPID_SRCVoicePurgeEvent',
    'SAFT11kHz16BitStereo', 'DISPID_SpeechAudioFormat',
    'DISPID_SAVolume', 'DISPID_SGRSTWeight', 'ISpRecognizer3',
    'SPPS_Interjection', 'SPWORDPRONUNCIATION', 'DISPID_SMSADeviceId',
    'SPCT_DICTATION', 'DISPID_SPPFirstElement',
    'DISPID_SRIsUISupported', 'SpNotifyTranslator', 'SLTUser',
    'SPLO_DYNAMIC', 'DISPID_SVSpeak', 'DISPID_SPEAudioSizeBytes',
    'DISPID_SRGSetTextSelection', 'SPINTERFERENCE',
    'Speech_Max_Word_Length', 'eLEXTYPE_PRIVATE11', 'SDTAlternates',
    'DISPID_SRState', 'DISPID_SMSSetData', 'eLEXTYPE_PRIVATE3',
    'SpeechAudioFormatGUIDText', 'ISpeechPhoneConverter',
    'SpeechCategoryRecognizers', 'SP_VISEME_18',
    'DISPID_SAFGetWaveFormatEx', 'SPRECOSTATE',
    'DISPID_SPIProperties', 'DISPID_SpeechPhoneConverter',
    'SPSMF_SAPI_PROPERTIES', 'SPPHRASEELEMENT',
    'SpeechCategoryPhoneConverters', 'DISPID_SRGetPropertyNumber',
    'SVF_Stressed', 'SPWT_LEXICAL_NO_SPECIAL_CHARS',
    'DISPID_SPRuleName', 'DISPID_SRCEventInterests',
    'DISPID_SPEs_NewEnum', 'SPPS_RESERVED3',
    'SpeechDisplayAttributes', 'SGDSActiveUserDelimited',
    'SVSFParseSsml', 'SPEI_MAX_TTS', 'SFTInput', 'SVEEndInputStream',
    'DISPID_SOTsCount', 'SpeechLoadOption', 'SPEI_VOICE_CHANGE',
    'SVP_3', 'DISPID_SVSpeakStream', 'SpeechTokenKeyFiles',
    'DISPID_SPPId', 'DISPID_SRCCmdMaxAlternates', 'DISPID_SVVoice',
    'DISPID_SPACommit', 'DISPID_SRRGetXMLResult', 'DISPID_SPPsCount',
    'SRERecognition', 'DISPID_SRCSetAdaptationData',
    'SPRST_INACTIVE_WITH_PURGE',
    '__MIDL___MIDL_itf_sapi_0000_0020_0002',
    'ISpeechLexiconPronunciations', 'SAFT8kHz8BitMono', 'SPWF_INPUT',
    'SVP_1', 'eLEXTYPE_PRIVATE15', 'SPSEMANTICERRORINFO',
    'SP_VISEME_14', 'SWPKnownWordPronounceable', 'SAFT8kHz16BitMono',
    'SPEI_PROPERTY_NUM_CHANGE', 'DISPID_SpeechGrammarRules',
    'DISPID_SRRAlternates', 'SGDSActiveWithAutoPause', 'SPEI_MAX_SR',
    'SRTEmulated', 'SREStateChange', 'DISPID_SpeechPhraseAlternate',
    'SPEI_PHRASE_START', 'SAFT48kHz8BitMono',
    'DISPID_SpeechGrammarRuleStateTransitions', 'SAFT16kHz8BitStereo',
    'DISPID_SGRsFindRule', 'SpeechGrammarWordType', 'SPGS_DISABLED',
    'SAFT8kHz8BitStereo', 'DISPID_SpeechRecoResultTimes',
    'ISpPhoneticAlphabetConverter', 'SpeechStreamFileMode',
    'SPPS_Noncontent', 'SAFTCCITT_ALaw_8kHzStereo',
    'DISPID_SpeechPhraseElement',
    'DISPID_SRCAudioInInterferenceStatus',
    'DISPID_SpeechPhraseBuilder', 'SPSNotOverriden',
    'DISPID_SRGCmdLoadFromFile', 'DISPIDSPRG',
    'SPEI_RECO_STATE_CHANGE', 'SpeechTokenShellFolder',
    'SPGS_ENABLED', 'SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN',
    'SAFTNoAssignedFormat', 'SpeechGrammarTagDictation',
    'SPEI_RESERVED2', 'SVP_4', 'DISPID_SRGRules', 'SITooSlow',
    'SpSharedRecoContext', 'ISpLexicon', 'DISPID_SPRuleFirstElement',
    'ISpeechRecoResult', 'DISPID_SRCPause', 'ISpStream',
    'eLEXTYPE_APP', 'SPSHORTCUTPAIR', 'SLOStatic', 'SPCT_SUB_COMMAND',
    'SRTReSent', 'SPPS_LMA', 'DISPID_SVVolume',
    'SSSPTRelativeToCurrentPosition', 'DISPID_SpeechVoiceEvent',
    'SWTAdded', 'eLEXTYPE_RESERVED7', 'ISpeechRecoContext',
    'SPAS_RUN', 'SVSFParseAutodetect',
    'DISPID_SRCERecognitionForOtherContext', 'SPWORD',
    'SRESoundStart', 'SPINTERFERENCE_LATENCY_WARNING',
    'DISPID_SPPNumberOfElements', 'DISPID_SVAlertBoundary',
    'SRCS_Disabled', 'DISPID_SpeechPhraseAlternates',
    'DISPID_SpeechAudioStatus', 'SpObjectToken',
    'DISPID_SLRemovePronunciationByPhoneIds', 'Speech_StreamPos_Asap',
    'DISPID_SPRulesItem', 'DISPID_SpeechLexiconWords', 'SVP_18',
    'SpeechCategoryRecoProfiles', 'DISPID_SpeechXMLRecoResult',
    'SAFT12kHz16BitStereo', 'DISPID_SABIEventBias',
    'DISPID_SRRTLength', 'SP_VISEME_12', 'SPXRO_Alternates_SML',
    'ISpObjectWithToken', 'SVSFIsXML', 'DISPID_SPIRetainedSizeBytes',
    'SITooLoud', 'SpeechRegistryLocalMachineRoot',
    'DISPID_SWFEBlockAlign', 'DISPID_SVSkip', 'ISpNotifySink',
    '__MIDL_IWinTypes_0009', 'DISPID_SPRuleNumberOfElements',
    'SPINTERFERENCE_TOOFAST', 'ISpPhoneConverter', 'DISPID_SGRSTRule',
    'SpeechRecognitionType', 'SVP_14', 'DISPID_SPRuleConfidence',
    'SVP_19', 'DISPID_SRCRequestedUIType',
    'SpeechRecoProfileProperties', 'ISpeechPhraseRules',
    'SpCustomStream', 'DISPID_SpeechObjectTokens',
    'DISPID_SPRuleParent', 'DISPID_SPPBRestorePhraseFromMemory',
    'SAFTADPCM_11kHzStereo', 'SpeechAudioVolume', 'SP_VISEME_6',
    'SRTStandard', 'SPTEXTSELECTIONINFO', 'SVEVoiceChange',
    'DISPID_SRCRetainedAudioFormat',
    'ISpeechGrammarRuleStateTransitions',
    'DISPID_SPEActualConfidence', 'SVP_20',
    'SpeechVoiceSkipTypeSentence', 'DISPID_SMSAMMHandle',
    'DISPID_SRGSetWordSequenceData', 'SpeechRecoContextState',
    'SVEAllEvents', 'SPWORDPRONOUNCEABLE',
    'DISPID_SPRDisplayAttributes', 'ISpeechDataKey',
    'ISpXMLRecoResult', 'DISPID_SRGId', 'SAFTCCITT_ALaw_22kHzStereo',
    'SAFTADPCM_22kHzStereo', 'SINoSignal', 'SAFT12kHz8BitStereo',
    'ISpeechRecognizer', 'SpeechAudioFormatType',
    'DISPID_SLGetGenerationChange', 'ISpShortcut',
    'DISPID_SPIReplacements', 'SVP_16', 'eLEXTYPE_VENDORLEXICON',
    'SPSVerb', 'DISPID_SPILanguageId', 'DISPID_SRGState',
    'SpeechTokenIdUserLexicon', 'SGDSActive',
    'DISPID_SOTCEnumerateTokens', 'DISPID_SOTCSetId', 'SpLexicon',
    'DISPID_SpeechPhraseInfo', 'STCInprocServer', 'SVSFUnusedFlags',
    'SGSDisabled', 'SPSHT_Unknown', 'DISPID_SOTCId',
    'DISPID_SPARecoResult', 'DISPID_SGRSTText',
    'DISPID_SGRSTransitions', '_SPAUDIOSTATE', 'SVSFPersistXML',
    'SVP_13', 'DISPID_SPAs_NewEnum', 'DISPID_SpeechCustomStream',
    'eLEXTYPE_RESERVED4', 'SpeechPropertyResourceUsage',
    'SpeechEngineConfidence', 'SPFM_OPEN_READONLY',
    'SPEI_START_SR_STREAM', 'SPEI_RECO_OTHER_CONTEXT',
    'ISpeechVoiceStatus', 'DISPID_SPEAudioSizeTime',
    'SpeechPartOfSpeech', 'DISPID_SPPEngineConfidence', 'SP_VISEME_8',
    'SPEI_WORD_BOUNDARY', 'SpeechLexiconType', 'DISPID_SLPPhoneIds',
    'ISpeechGrammarRuleState', 'SpeechStreamSeekPositionType',
    'SREStreamStart', 'SVEBookmark', 'DISPID_SpeechLexiconProns',
    'SRAImport', 'DISPID_SGRSAddSpecialTransition',
    'SAFTCCITT_ALaw_11kHzMono', 'DISPID_SPANumberOfElementsInResult',
    'SPBO_NONE', 'DISPID_SPEsCount', 'WAVEFORMATEX', 'SPSHORTCUTTYPE',
    'SPEI_SR_BOOKMARK', 'SPRS_ACTIVE', 'DISPID_SPPConfidence',
    'SAFT32kHz8BitStereo', 'SAFT32kHz16BitMono', 'SPRECOGNIZERSTATUS',
    'SPCS_DISABLED', 'DISPID_SOTId', 'DISPID_SVStatus',
    'eLEXTYPE_PRIVATE2', 'SECFIgnoreWidth', 'SPEI_REQUEST_UI',
    'DISPID_SGRAddResource', 'DISPID_SGRSTsItem',
    'DISPID_SVEEnginePrivate', 'SAFT24kHz16BitStereo',
    'DISPID_SRSAudioStatus', 'DISPID_SRCEPropertyNumberChange',
    'SPWT_DISPLAY', 'SpeechWordPronounceable', 'SPPS_Verb',
    'DISPID_SREmulateRecognition', 'SpeechPropertyAdaptationOn',
    'DISPID_SDKSetBinaryValue', 'DISPID_SRCEPropertyStringChange',
    'SPEI_SOUND_START',
    'DISPID_SVAllowAudioOuputFormatChangesOnNextSet',
    'DISPID_SRRTOffsetFromStart', 'SpPhraseInfoBuilder',
    'SpInProcRecoContext', 'DISPID_SRCERequestUI',
    'DISPID_SPRulesCount', 'ISpeechBaseStream',
    'SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE',
    'SWPUnknownWordUnpronounceable', 'SPCS_ENABLED',
    'SPWAVEFORMATTYPE', 'SpeechInterference', 'SAFT32kHz8BitMono',
    'DISPID_SRRTTickCount', 'SPINTERFERENCE_NOSIGNAL', 'SP_VISEME_5',
    'DISPID_SOTCGetDataKey', 'DISPID_SLWs_NewEnum',
    'DISPID_SPPParent', 'DISPID_SRGDictationUnload', 'ISpPhrase',
    'DISPID_SGRAddState', 'DISPID_SRSCurrentStreamNumber',
    'eLEXTYPE_PRIVATE12', 'DISPID_SWFEBitsPerSample',
    'IInternetSecurityMgrSite', 'ISpVoice', 'SPRULE',
    'SpUnCompressedLexicon', 'DISPID_SVRate',
    'DISPID_SpeechObjectTokenCategory', 'SAFTCCITT_uLaw_44kHzMono',
    'SDKLCurrentConfig', 'ISpeechObjectTokenCategory', 'SPBO_AHEAD',
    'SAFT44kHz8BitStereo', 'SDTRule', 'SGLexicalNoSpecialChars',
    'SpeechRecoEvents', 'eLEXTYPE_PRIVATE10', 'DISPID_SGRClear',
    'SpNullPhoneConverter', 'ISpeechMemoryStream', 'SPAR_Low',
    'SPEI_TTS_BOOKMARK', 'SAFTText', 'SPPHRASE', 'SRSInactive',
    'DISPID_SVSLastResult', 'DISPID_SLPsItem', 'STCRemoteServer',
    'ISpDataKey', 'DISPID_SpeechVoiceStatus', 'DISPID_SRCState',
    'SPEI_SR_AUDIO_LEVEL', 'DISPID_SRCEStartStream',
    'DISPID_SVWaitUntilDone', 'SPSLMA', 'DISPID_SPRuleChildren',
    'DISPID_SPCLangId', 'SSTTDictation',
    'DISPID_SPERetainedStreamOffset', 'eLEXTYPE_PRIVATE5', 'SVP_8',
    'SPCONTEXTSTATE', 'IEnumString', 'ISpeechGrammarRule',
    'SAFT8kHz16BitStereo', 'SPGRAMMARWORDTYPE',
    'SAFTCCITT_uLaw_44kHzStereo', 'ISpeechCustomStream',
    'SP_VISEME_21', 'SPSHT_NotOverriden', 'SpeechUserTraining',
    'SVSFParseSapi', 'SVSFVoiceMask', 'ISpeechAudioFormat',
    'DISPID_SRAudioInputStream', 'SPFM_NUM_MODES',
    'ISpeechLexiconPronunciation', 'ISpNotifySource',
    'DISPID_SPEAudioStreamOffset', 'DISPID_SLWPronunciations',
    'ISpStreamFormat', 'DISPID_SRRAudio', 'SPFM_CREATE_ALWAYS',
    'SAFTADPCM_8kHzMono', 'DISPID_SRGCommit',
    'DISPID_SpeechLexiconPronunciation',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_W3C', 'SRTAutopause',
    'DISPID_SVAudioOutputStream', 'SPDKL_CurrentUser', 'SITooFast',
    'SSFMCreate', 'SpeechVisemeFeature', 'SAFT16kHz16BitMono',
    'DISPID_SpeechVoice', 'DISPID_SRProfile', 'DISPID_SBSWrite',
    'SRAExport', 'SP_VISEME_0', 'SAFTCCITT_uLaw_22kHzStereo',
    'SVEStartInputStream', 'DISPID_SDKDeleteValue', 'SpStream',
    'SECNormalConfidence', 'SRARoot', 'SPEI_HYPOTHESIS',
    'SpeechAddRemoveWord', 'DISPID_SOTsItem', 'ISpeechGrammarRules',
    'DISPID_SWFEChannels', 'ISpeechPhraseAlternates',
    'eLEXTYPE_PRIVATE7', 'SpWaveFormatEx',
    'DISPID_SRGCmdSetRuleState', 'ISpeechRecoResultTimes',
    'DISPID_SOTGetStorageFileName', 'DISPID_SPIAudioStreamPosition',
    'DISPID_SVEventInterests', 'SPPS_RESERVED4', 'SPFM_CREATE',
    'SPEI_TTS_PRIVATE', 'ISpGrammarBuilder', 'SPVOICESTATUS',
    'SPDATAKEYLOCATION', 'SASStop', 'DISPID_SRCreateRecoContext',
    'DISPID_SRAllowVoiceFormatMatchingOnNextSet', 'SREPrivate',
    'eLEXTYPE_PRIVATE18', 'DISPID_SVResume', 'DISPID_SRGReset',
    'SAFTCCITT_ALaw_22kHzMono', 'SPEVENT', 'DISPID_SDKEnumValues',
    'SSTTWildcard', 'DISPID_SVSLastStreamNumberQueued',
    'SPSEMANTICFORMAT', 'SVSFNLPSpeakPunc', 'DISPID_SAEventHandle',
    'ISpPhoneticAlphabetSelection', 'DISPID_SPEDisplayText', 'SDTAll',
    'Speech_Default_Weight', 'STCAll', 'SPSHORTCUTPAIRLIST',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_MS',
    'ISpeechGrammarRuleStateTransition', 'SpResourceManager',
    'tagSTATSTG', 'SPEI_END_SR_STREAM', 'ISpeechPhraseRule',
    'SREInterference', 'SVPOver', 'SGRSTTDictation',
    'SSFMCreateForWrite', 'SRADynamic', 'DISPID_SPEsItem',
    'Speech_StreamPos_RealTime', 'STCLocalServer',
    'SPPS_SuppressWord', 'SPEI_SR_PRIVATE', 'DISPID_SGRSTNextState',
    'SpeechAllElements', 'DISPID_SADefaultFormat',
    'DISPID_SASFreeBufferSpace', 'DISPID_SRRecognizer',
    'SPLEXICONTYPE', 'SVEViseme', 'ISpRecoContext', 'ISpRecoGrammar',
    'SAFTCCITT_ALaw_44kHzStereo', 'SPXMLRESULTOPTIONS',
    'SPINTERFERENCE_NOISE', 'DISPID_SPELexicalForm',
    'DISPID_SPRNumberOfElements', 'DISPID_SpeechAudioBufferInfo',
    'DISPID_SVSLastBookmarkId', 'DISPID_SRRSetTextFeedback',
    'SPCT_SLEEP', 'DISPID_SPAsItem', 'DISPID_SPIElements', 'SBONone',
    'DISPID_SPRs_NewEnum', 'DISPID_SPIRule', 'SPWF_SRENGINE',
    'DISPID_SRGCmdLoadFromProprietaryGrammar',
    'SPEI_PROPERTY_STRING_CHANGE', 'SGSExclusive',
    'SAFT48kHz16BitMono', 'SAFTNonStandardFormat',
    'SPEI_SENTENCE_BOUNDARY', 'ISpRecoCategory',
    'DISPID_SOTGetAttribute', 'SPPARTOFSPEECH', 'SpCompressedLexicon',
    'SpeechBookmarkOptions', 'SINoise', 'DISPID_SPPValue',
    'ISpeechPhraseAlternate', 'SAFTCCITT_uLaw_8kHzStereo',
    'SPINTERFERENCE_TOOLOUD', 'eLEXTYPE_RESERVED6', 'SPAUDIOSTATE',
    'DISPID_SVGetProfiles', 'SPCATEGORYTYPE', 'DISPID_SVEWord',
    'SPSMF_SRGS_SAPIPROPERTIES', 'SREAdaptation',
    'ISpeechWaveFormatEx', 'DISPID_SABufferNotifySize',
    'SRCS_Enabled', 'SLTApp', 'SAFT22kHz8BitMono',
    'DISPID_SRIsShared', 'SpeechTokenKeyUI', 'SAFTADPCM_11kHzMono',
    'SPSERIALIZEDRESULT', 'DISPID_SRCERecognition',
    'DISPID_SpeechPhraseRules', 'eLEXTYPE_PRIVATE19', 'eLEXTYPE_USER',
    'DISPID_SASCurrentDevicePosition', 'SAFT48kHz8BitStereo',
    'DISPID_SPAPhraseInfo', 'DISPID_SPPName', 'eLEXTYPE_PRIVATE16',
    'DISPID_SPERequiredConfidence', 'SVP_12', 'DISPID_SABIBufferSize',
    'DISPID_SVPriority', 'DISPID_SVDisplayUI', 'SSSPTRelativeToEnd',
    'SpeechCategoryAppLexicons', 'Library', 'SAFT16kHz8BitMono',
    'DISPID_SpeechPhraseReplacements', 'SP_VISEME_10', 'SVSFNLPMask',
    'DISPID_SGRSRule', 'ISpeechXMLRecoResult', 'ISpResourceManager',
    'SP_VISEME_7', 'DISPID_SDKSetStringValue', 'SpeechGrammarState',
    'SpPhoneConverter', 'DISPID_SPEAudioTimeOffset',
    'SpeechVisemeType', 'eLEXTYPE_RESERVED10', 'SAFTADPCM_8kHzStereo',
    'DISPID_SGRAttributes', 'SRSEDone', 'SVSFIsNotXML',
    'SPRECORESULTTIMES', 'DISPIDSPTSI', 'SpeechTokenKeyAttributes',
    'ISpNotifyTranslator', 'SpeechPropertyNormalConfidenceThreshold',
    'DISPID_SRCVoice', 'DISPID_SpeechObjectToken',
    'DISPID_SGRsCommit', 'eLEXTYPE_PRIVATE14', 'SPRST_ACTIVE',
    'DISPID_SPIGetDisplayAttributes', 'SECFIgnoreCase',
    'SPRS_ACTIVE_USER_DELIMITED', 'DISPID_SPEDisplayAttributes',
    'DISPID_SMSALineId', '__MIDL___MIDL_itf_sapi_0000_0020_0001',
    'DISPID_SRSetPropertyString', 'SREPhraseStart', 'SPSUnknown',
    'SpeechGrammarRuleStateTransitionType', 'tagSPTEXTSELECTIONINFO',
    'DISPID_SRGDictationLoad', 'DISPID_SAFSetWaveFormatEx',
    'DISPID_SOTRemove', 'SAFTCCITT_ALaw_11kHzStereo',
    'DISPID_SRGetRecognizers', 'ISpObjectTokenCategory',
    'SPEI_RESERVED1', 'DISPIDSPTSI_ActiveOffset',
    'SDA_Two_Trailing_Spaces', 'DISPID_SPIStartTime', 'SP_VISEME_2',
    'SSFMOpenForRead', 'SP_VISEME_1', 'SAFTCCITT_uLaw_22kHzMono',
    'SECFDefault', 'DISPID_SRCBookmark', 'SpeechAudioProperties',
    'SECHighConfidence', 'SPSERIALIZEDPHRASE', 'SLODynamic',
    'SAFTCCITT_uLaw_11kHzMono', 'SpeechAudioFormatGUIDWave',
    'SGSEnabled', 'SRTSMLTimeout', 'SP_VISEME_20',
    'DISPID_SOTCDefault', 'SVSFPurgeBeforeSpeak',
    'SpeechCategoryAudioOut', 'DISPID_SRGDictationSetState',
    'DISPID_SpeechGrammarRule', 'SPVPRI_OVER', 'DISPID_SPIGrammarId',
    'DISPID_SRCEAdaptation', 'DISPID_SVEBookmark',
    'DISPID_SpeechLexicon', 'DISPID_SRCEEndStream',
    'DISPID_SMSGetData', 'SFTSREngine', 'SAFTGSM610_8kHzMono',
    'DISPID_SPRuleEngineConfidence', 'SP_VISEME_9',
    'DISPID_SVEStreamStart', 'SRERecoOtherContext',
    'SPFM_OPEN_READWRITE', 'SITooQuiet', 'SpInprocRecognizer',
    'SpeechPropertyHighConfidenceThreshold', 'DISPID_SOTs_NewEnum',
    'ISpeechPhraseElement', 'SPPS_Unknown', 'SRAInterpreter',
    'SVP_11', 'DISPID_SRRTStreamTime', 'DISPID_SPCIdToPhone',
    'DISPID_SPERetainedSizeBytes', 'SRAONone',
    'SpeechPropertyLowConfidenceThreshold', 'DISPID_SOTCategory',
    'SSFMOpenReadWrite', 'SpeechPropertyResponseSpeed', 'SVP_9',
    'SpShortcut', 'ISpEventSource', 'ISpeechPhraseInfoBuilder',
    'eLEXTYPE_RESERVED9', 'SAFT12kHz16BitMono',
    'ISpStreamFormatConverter', 'DISPID_SPIEngineId',
    'ISpeechObjectToken', 'SVP_5', 'DISPID_SpeechMMSysAudio',
    'DISPID_SVGetAudioOutputs', 'SPADAPTATIONRELEVANCE',
    'SDA_Consume_Leading_Spaces', 'SRSActiveAlways',
    'SAFTGSM610_11kHzMono', 'SPVPRI_NORMAL', 'SpeechVoicePriority',
    'SECFIgnoreKanaType', 'SPAS_PAUSE', 'ISpRecoContext2',
    'SPRS_ACTIVE_WITH_AUTO_PAUSE', 'DISPID_SVSLastBookmark',
    'SPEI_UNDEFINED', 'SAFTCCITT_uLaw_11kHzStereo', 'DISPID_SLWType',
    'ISpSerializeState', 'ISpRecoGrammar2', 'DISPID_SPPs_NewEnum',
    'DISPID_SOTGetDescription', 'DISPID_SVSpeakCompleteEvent',
    'DISPID_SVIsUISupported', 'typelib_path', 'DISPID_SOTDisplayUI',
    'SVESentenceBoundary', 'SPEI_INTERFERENCE',
    'ISpeechRecoResultDispatch', 'SPVPRI_ALERT', 'SVSFIsFilename',
    'DISPID_SRRGetXMLErrorInfo', 'ISpeechLexiconWords',
    'SAFT11kHz16BitMono', 'SPAS_STOP', 'DISPID_SRGetFormat',
    'SP_VISEME_15', 'ISpeechRecoResult2', 'SAFT22kHz16BitStereo',
    'ISpeechLexiconWord', 'LONG_PTR', 'SAFTTrueSpeech_8kHz1BitMono',
    'ISpeechLexicon', 'DISPID_SAFType', 'SVP_2', 'SPAUDIOBUFFERINFO',
    'DISPID_SRRTimes', 'DISPID_SRRAudioFormat', 'DISPID_SLPSymbolic',
    'DISPID_SVEAudioLevel', 'DISPID_SASetState', 'SECFEmulateResult',
    'DISPID_SRSClsidEngine', 'DISPID_SPEPronunciation',
    'DISPID_SLGetPronunciations', 'SVSFDefault', 'SPSHT_OTHER',
    'STCInprocHandler', 'DISPID_SVPause', 'SVP_17', 'SPAR_Unknown',
    'eLEXTYPE_PRIVATE13', 'SpeechMicTraining', 'DISPID_SGRsAdd',
    'ISpeechPhraseElements', 'DISPID_SRRDiscardResultInfo',
    'SPWT_PRONUNCIATION', 'DISPID_SRGCmdSetRuleIdState',
    'SECLowConfidence', 'DISPID_SRCEAudioLevel',
    'SREFalseRecognition', 'ISpProperties',
    'DISPID_SPEEngineConfidence', 'SPDKL_LocalMachine',
    'SPCT_COMMAND', 'DISPID_SpeechRecognizerStatus',
    'DISPID_SPRules_NewEnum', 'SPPS_Modifier', 'ISpPhraseAlt',
    'SVP_10', 'eLEXTYPE_PRIVATE1', 'DISPID_SFSOpen',
    'SAFT24kHz8BitMono', 'DISPID_SWFEAvgBytesPerSec', 'SGRSTTWord',
    'SDTDisplayText', 'eLEXTYPE_PRIVATE9', 'SRTExtendableParse',
    'ISpeechAudio', 'SVPAlert', 'eLEXTYPE_LETTERTOSOUND',
    'eLEXTYPE_PRIVATE4', 'DISPID_SDKEnumKeys', 'IStream',
    'DISPID_SGRSTPropertyName', 'SpStreamFormatConverter',
    'DISPID_SpeechRecoContextEvents', 'ISpeechPhraseProperty',
    'DISPID_SABIMinNotification', 'SGLexical',
    'DISPID_SRCRetainedAudio', 'DISPID_SRGCmdLoadFromMemory',
    'DISPID_SPPChildren', 'SPEI_VISEME',
    'DISPID_SRCERecognizerStateChange', 'DISPID_SWFEFormatTag',
    'DISPID_SpeechRecoContext', 'SRERequestUI', 'DISPID_SOTDataKey',
    'SP_VISEME_13', 'DISPID_SRCESoundStart', 'DISPID_SRRSaveToMemory',
    'DISPID_SLGenerationId', 'DISPID_SOTCreateInstance',
    'DISPID_SASCurrentSeekPosition', 'DISPID_SRAudioInput',
    'DISPID_SpeechFileStream', 'DISPID_SWFESamplesPerSec',
    'DISPID_SLWsItem', 'ISpeechPhraseInfo', 'DISPID_SRCESoundEnd',
    'SpPhoneticAlphabetConverter', 'SPSFunction', 'DISPID_SAFGuid',
    'DISPID_SRSSupportedLanguages', 'DISPID_SPIAudioSizeBytes',
    'DISPID_SGRsItem', 'SGDisplay', 'ISpeechPhraseProperties',
    'SDTPronunciation', 'SDA_No_Trailing_Space', 'ISpeechVoice',
    'SDTLexicalForm', 'SPEI_RECOGNITION',
    'SpeechSpecialTransitionType', 'DISPID_SpeechRecoResult',
    'SASClosed', 'eLEXTYPE_RESERVED8',
    'DISPID_SRAllowAudioInputFormatChangesOnNextSet',
    'DISPID_SVESentenceBoundary', 'SPINTERFERENCE_TOOSLOW',
    'DISPID_SpeechPhraseReplacement', 'SPPS_RESERVED1',
    'DISPID_SDKGetlongValue', 'DISPID_SAStatus', 'SPEI_SOUND_END',
    'SPRST_ACTIVE_ALWAYS', 'DISPID_SGRSTsCount', 'SpMMAudioIn',
    'DISPID_SPPsItem', 'Speech_Max_Pron_Length',
    'DISPIDSPTSI_SelectionOffset', 'SRSActive',
    'DISPID_SGRSTPropertyId', 'SAFTCCITT_ALaw_8kHzMono',
    'DISPID_SVSInputSentenceLength', 'DISPID_SpeechAudio',
    'SRSEIsSpeaking', 'ISpeechMMSysAudio', 'DISPID_SPRText',
    'DISPID_SLWLangId', 'DISPID_SLWsCount', 'SPPHRASEREPLACEMENT',
    'DISPID_SVSCurrentStreamNumber', 'SDA_One_Trailing_Space',
    'SVP_0', 'DISPID_SLGetWords', 'SPRST_INACTIVE',
    'SAFTCCITT_uLaw_8kHzMono', 'DISPID_SpeechPhraseProperties',
    'SPGRAMMARSTATE', 'SVEAudioLevel', 'DISPID_SVEPhoneme',
    'SpeechRetainedAudioOptions', 'DISPID_SpeechRecognizer',
    'DISPID_SpeechBaseStream', 'DISPID_SRGCmdLoadFromObject',
    'DISPIDSPTSI_SelectionLength', 'DISPID_SpeechPhraseProperty',
    'ISpeechTextSelectionInformation', 'SpeechDataKeyLocation',
    'SAFT32kHz16BitStereo', 'SAFT16kHz16BitStereo',
    'ISpeechAudioBufferInfo', 'DISPID_SASNonBlockingIO',
    'DISPID_SGRsDynamic', 'SRESoundEnd', 'SPEI_RESERVED3',
    'SP_VISEME_17', 'SpObjectTokenCategory', 'SRSInactiveWithPurge',
    'DISPID_SRCCreateResultFromMemory', 'DISPID_SpeechPhraseRule',
    'SGRSTTTextBuffer', 'SREStreamEnd', 'SPWORDPRONUNCIATIONLIST',
    'eLEXTYPE_USER_SHORTCUT', 'DISPID_SGRSTPropertyValue',
    'SGPronounciation', 'DISPID_SpeechRecoResult2', 'ISpMMSysAudio',
    'DISPID_SLWWord', 'SPEI_RESERVED6', 'SAFTCCITT_ALaw_44kHzMono',
    'DISPID_SGRInitialState', 'SDKLDefaultLocation', 'SVP_7',
    'SWPUnknownWordPronounceable', 'eLEXTYPE_PRIVATE8',
    'SAFT22kHz16BitMono', 'SpeechEmulationCompareFlags',
    'DISPID_SGRsCommitAndSave', 'DISPID_SVEViseme',
    'DISPID_SOTIsUISupported', 'SPEVENTENUM', 'SREAudioLevel',
    'SPBINARYGRAMMAR', 'SPPS_Noun', 'DISPID_SRCEInterference',
    'SINone', 'SP_VISEME_19', 'eLEXTYPE_PRIVATE17',
    'IInternetSecurityManager', 'SAFT44kHz16BitStereo',
    'SAFT22kHz8BitStereo', 'DISPID_SLPsCount', 'DISPID_SPRsCount',
    'SDTReplacement', 'SpeechDiscardType', 'STSF_CommonAppData',
    'SPEI_ACTIVE_CATEGORY_CHANGED', 'SDTProperty',
    'SAFT44kHz16BitMono', 'DISPID_SGRName', 'DISPID_SBSSeek',
    'ISpObjectToken', 'SREPropertyStringChange', 'SPAS_CLOSED',
    'DISPID_SRGIsPronounceable', 'SPEI_FALSE_RECOGNITION',
    'ISpeechPhraseReplacements', 'SPSMF_UPS', 'SVSFParseMask',
    'SPPHRASEPROPERTY', 'SAFTADPCM_22kHzMono',
    'DISPID_SPIAudioSizeTime', 'DISPID_SPAsCount', 'SPPS_Function',
    'SPAR_High', 'DISPID_SVGetAudioInputs', 'DISPID_SRCEPhraseStart',
    'DISPID_SDKGetBinaryValue', 'DISPID_SPRsItem', 'SREBookmark',
    'SPBO_TIME_UNITS', 'DISPID_SRGCmdLoadFromResource',
    'SDKLCurrentUser', 'SPEI_END_INPUT_STREAM', 'DISPID_SLPType',
    'SpTextSelectionInformation', 'SREAllEvents', 'SVP_6',
    'SPWP_KNOWN_WORD_PRONOUNCEABLE', 'DISPID_SBSFormat',
    '_RemotableHandle', 'SVEPhoneme',
    'DISPID_SPAStartElementInResult',
    'SPINTERFERENCE_LATENCY_TRUNCATE_END', 'DISPID_SVSPhonemeId',
    'SAFTExtendedAudioFormat', 'DISPID_SFSClose',
    'SPDKL_DefaultLocation', 'SP_VISEME_3', 'SPRULESTATE',
    'DISPID_SRDisplayUI', 'DISPID_SPRFirstElement',
    'DISPID_SpeechGrammarRuleStateTransition', 'SPSHT_EMAIL',
    'SpVoice', 'SAFT11kHz8BitStereo', 'tagSPPROPERTYINFO',
    'DISPID_SVSInputSentencePosition', '_ISpeechRecoContextEvents',
    'SAFTDefault', 'ISpeechResourceLoader', 'SPRS_INACTIVE',
    'SPPROPERTYINFO', 'SAFT24kHz16BitMono', 'SpeechRuleAttributes',
    'SpeechFormatType', 'SVPNormal', 'SpeechEngineProperties',
    'DISPID_SPRuleId', 'SGRSTTWildcard', 'SASPause', 'SASRun',
    'SVF_None', 'DISPID_SRCEEnginePrivate', 'SPEI_PHONEME',
    'DISPID_SGRSAddWordTransition', 'SpeechRunState', 'SPPHRASERULE',
    'DISPID_SGRSAddRuleTransition', 'ISpRecognizer'
]

