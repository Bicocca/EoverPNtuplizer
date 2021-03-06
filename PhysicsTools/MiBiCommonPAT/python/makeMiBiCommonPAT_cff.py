import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.tools.metTools import *
from PhysicsTools.PatAlgos.tools.tauTools import *
from PhysicsTools.PatAlgos.tools.jetTools import *
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *

from PhysicsTools.PatAlgos.selectionLayer1.leptonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.photonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *



def makeMiBiCommonPAT(process, GlobalTag, MC=False, Filter=False, SavePAT=True):

    # Setup the process
    process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr.FwkReport.reportEvery = 10
    process.load('Configuration.StandardSequences.GeometryDB_cff')
    process.load("Configuration.StandardSequences.MagneticField_cff")
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.GlobalTag.globaltag = GlobalTag
    
    # Source
    process.source = cms.Source(
        "PoolSource",
        fileNames = cms.untracked.vstring()
    )
    
    # Out
    process.out = cms.OutputModule(
        "PoolOutputModule",
        fileName = cms.untracked.string('file:./MiBiCommonPAT.root'),
        outputCommands = cms.untracked.vstring(),
        SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('MiBiPathAK5PF','MiBiPathAK5Calo', 'MiBiPathPFlow', 'MiBiPathPhotons') ) if Filter else cms.untracked.PSet()
        )

    if SavePAT :
        process.e = cms.EndPath(process.out)


     

    process.load("PhysicsTools.NtupleUtils.AllPassFilter_cfi")

    #--------------------------
    # Counter1: All read events
    #process.AllEvents = process.AllPassFilter.clone()
    process.AllEvents = cms.EDProducer("EventCountProducer")
    


    #--------------------------
    # Counter2: Scraping filter
    process.scrapingFilter = cms.EDFilter("FilterOutScraping",
        applyfilter = cms.untracked.bool(True),
        debugOn = cms.untracked.bool(False),
        numtrack = cms.untracked.uint32(10),
        thresh = cms.untracked.double(0.25)
    )
    
    #process.NonScrapedEvents = process.AllPassFilter.clone()
    process.NonScrapedEvents = cms.EDProducer("EventCountProducer")
    
    
    
    #-----------------------------------
    # Counter3: Filter on primary vertex
    process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
        vertexCollection = cms.InputTag('offlinePrimaryVertices'),
        minimumNDOF = cms.uint32(4) ,
        maxAbsZ = cms.double(24),
        maxd0 = cms.double(2)
    )
    
    #process.GoodVtxEvents = process.AllPassFilter.clone()
    process.GoodVtxEvents = cms.EDProducer("EventCountProducer")
    
    



    
    #------------------
    #Load PAT sequences
    process.load("PhysicsTools.PatAlgos.patSequences_cff")
    process.load("PhysicsTools.PatAlgos.tools.pfTools")
    postfix = "PFlow"
    usePF2PAT(process, runPF2PAT=True, jetAlgo='AK5', runOnMC=MC, postfix=postfix)  
    
    if not MC:
     removeMCMatching(process, ['All'])
    
    process.patJets.addTagInfos = cms.bool(False)    #bugfix related to btagging
    
    
    ### tau ###
    process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
    switchToPFTauHPS(process, 
        pfTauLabelOld = 'shrinkingConePFTauProducer',
        pfTauLabelNew = 'hpsPFTauProducer'
        )

    process.patCandidates.replace(process.makePatTaus,
        process.makePatTaus+
        getattr(process,"makePatTaus"+postfix)
        )   
    
    process.patCandidateSummary.candidates.append(cms.InputTag("patTaus"+postfix))
    
    setattr(process,"selectedPatTaus"+postfix,process.selectedPatTaus.clone())
    getattr(process,"selectedPatTaus"+postfix).src = 'patTaus'+postfix
    process.selectedPatCandidates.replace(process.selectedPatTaus,
        process.selectedPatTaus+
        getattr(process,"selectedPatTaus"+postfix)
    )
    process.selectedPatCandidateSummary.candidates.append(cms.InputTag("selectedPatTaus"+postfix))

    getattr(process,"patTaus"+postfix).embedIsolationTracks = cms.bool(True)
    getattr(process,"patTaus"+postfix).embedSignalTracks = cms.bool(True)
    getattr(process,"patTaus"+postfix).embedGenMatch = cms.bool(True)
    getattr(process,"patTaus"+postfix).embedLeadTrack = cms.bool(True)
    getattr(process,"patTaus"+postfix).embedLeadPFCand = True
    getattr(process,"patTaus"+postfix).embedLeadPFChargedHadrCand = True
    getattr(process,"patTaus"+postfix).embedLeadPFNeutralCand = True
    getattr(process,"patTaus"+postfix).embedSignalPFCands = True
    getattr(process,"patTaus"+postfix).embedSignalPFChargedHadrCands = True
    getattr(process,"patTaus"+postfix).embedSignalPFNeutralHadrCands = True
    getattr(process,"patTaus"+postfix).embedSignalPFGammaCands = True
    getattr(process,"patTaus"+postfix).embedIsolationPFCands = True
    getattr(process,"patTaus"+postfix).embedIsolationPFChargedHadrCands = True
    getattr(process,"patTaus"+postfix).embedIsolationPFNeutralHadrCands = True
    getattr(process,"patTaus"+postfix).embedIsolationPFGammaCands = True
    getattr(process,"patTaus"+postfix).embedGenJetMatch = cms.bool(True)
    getattr(process,"patTaus").embedIsolationTracks = cms.bool(True)
    getattr(process,"patTaus").embedSignalTracks = cms.bool(True)
    getattr(process,"patTaus").embedGenMatch = cms.bool(True)
    getattr(process,"patTaus").embedLeadTrack = cms.bool(True)
    getattr(process,"patTaus").embedLeadPFCand = True
    getattr(process,"patTaus").embedLeadPFChargedHadrCand = True
    getattr(process,"patTaus").embedLeadPFNeutralCand = True
    getattr(process,"patTaus").embedSignalPFCands = True
    getattr(process,"patTaus").embedSignalPFChargedHadrCands = True
    getattr(process,"patTaus").embedSignalPFNeutralHadrCands = True
    getattr(process,"patTaus").embedSignalPFGammaCands = True
    getattr(process,"patTaus").embedIsolationPFCands = True
    getattr(process,"patTaus").embedIsolationPFChargedHadrCands = True
    getattr(process,"patTaus").embedIsolationPFNeutralHadrCands = True
    getattr(process,"patTaus").embedIsolationPFGammaCands = True
    getattr(process,"patTaus").embedGenJetMatch = cms.bool(True)
   
    setattr(process,"hpsPFTauDiscriminationAgainstElectron2D",
      getattr(process,"hpsPFTauDiscriminationAgainstElectron").clone(
         ApplyCut_ElectronPreID_2D = cms.bool(True),
         ApplyCut_PFElectronMVA =  cms.bool(False)
      )
    )
    setattr(process,"hpsPFTauDiscriminationAgainstElectronCrackRem",
         getattr(process,"hpsPFTauDiscriminationAgainstElectron").clone(
           ApplyCut_EcalCrackCut = cms.bool(True),
           ApplyCut_PFElectronMVA =  cms.bool(False)
       )
    )
    
    setattr(process,"shrinkingConePFTauDiscriminationAgainstElectron2D",
        getattr(process,"shrinkingConePFTauDiscriminationAgainstElectron").clone(
           ApplyCut_ElectronPreID_2D = cms.bool(True),
           ApplyCut_PFElectronMVA =  cms.bool(False)
    )
    )
    setattr(process,"shrinkingConePFTauDiscriminationAgainstElectronCrackRem",
        getattr(process,"shrinkingConePFTauDiscriminationAgainstElectron").clone(
           ApplyCut_EcalCrackCut = cms.bool(True),
           ApplyCut_PFElectronMVA =  cms.bool(False)
         )
    )
    process.patHPSPFTauDiscrimination += process.hpsPFTauDiscriminationAgainstElectron2D
    process.patHPSPFTauDiscrimination += process.hpsPFTauDiscriminationAgainstElectronCrackRem
    process.patShrinkingConePFTauDiscrimination += process.shrinkingConePFTauDiscriminationAgainstElectron2D
    process.patShrinkingConePFTauDiscrimination += process.shrinkingConePFTauDiscriminationAgainstElectronCrackRem

    getattr(process,"makePatTaus"+postfix).replace(
        getattr(process,"patTaus"+postfix),
        process.patHPSPFTauDiscrimination + getattr(process,"patTaus"+postfix)
    )
    getattr(process,"makePatTaus").replace(
        getattr(process,"patTaus"),
        process.patShrinkingConePFTauDiscrimination + getattr(process,"patTaus")
    )
    
    
    #### electrons ####
    process.load("PhysicsTools.MiBiCommonPAT.simpleEleIdSequence_cff")

    process.patElectrons.addElectronID = cms.bool(True)
    process.patElectrons.electronIDSources = cms.PSet(
      simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
      simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
      simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
      simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
      simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
      simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
      simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
      simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
      simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
      simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
      simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
      simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),
    )
    
    process.patElectronsPFlow.addElectronID = cms.bool(True)
    process.patElectronsPFlow.electronIDSources = cms.PSet(
      simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
      simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
      simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
      simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
      simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
      simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
      simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
      simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
      simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
      simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
      simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
      simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),
    )
    
    process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
    process.makePatElectrons = cms.Sequence(
      process.patElectronIDs*
      process.patElectronIsolation*
      process.electronMatch*
      process.patElectrons
    )
    
    if not MC:
        process.makePatElectrons.remove(process.electronMatch)
    
    
    #### jets ####        
    process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
    process.load('RecoJets.Configuration.RecoJets_cff')
    process.load('RecoJets.Configuration.RecoPFJets_cff')
    process.kt6PFJets.doRhoFastjet = True
    process.kt6PFJets.Ghost_EtaMax = cms.double(5.0)
    process.kt6PFJets.Rho_EtaMax = cms.double(5.0)
    process.ak5PFJets.doAreaFastjet = True
    process.ak5PFJets.Rho_EtaMax = cms.double(5.0)
    
    process.patJetCorrFactors.rho = cms.InputTag("kt6PFJets","rho")
    
    # ---------------
    # add collections
    addTcMET(process, 'TC')
    addPfMET(process, 'PF')
    
    if not MC:    
        addJetCollection(
            process,
            cms.InputTag('ak5CaloJets'),
            'AK5',
            'Calo',
            doJTA        = True,
            doBTagging   = True,
            jetCorrLabel = ('AK5Calo', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'])),
            doType1MET   = True,
            doL1Cleaning = True,
            doL1Counters = False,
            genJetCollection=cms.InputTag("ak5GenJets"),
            doJetID      = True,
            jetIdLabel   = "ak5"
            )
        
        addJetCollection(
            process,
            cms.InputTag('ak5PFJets'),
            'AK5',
            'PF',
            doJTA        = True,
            doBTagging   = True,
            jetCorrLabel = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'])),
            doType1MET   = True,
            doL1Cleaning = True,
            doL1Counters = False,
            genJetCollection=cms.InputTag("ak5GenJets"),
            doJetID      = True,
            jetIdLabel   = "ak5"
            )
            
    if MC:    
        addJetCollection(
            process,
            cms.InputTag('ak5CaloJets'),
            'AK5',
            'Calo',
            doJTA        = True,
            doBTagging   = True,
            jetCorrLabel = ('AK5Calo', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])),
            doType1MET   = True,
            doL1Cleaning = True,
            doL1Counters = False,
            genJetCollection=cms.InputTag("ak5GenJets"),
            doJetID      = True,
            jetIdLabel   = "ak5"
            )
        
        addJetCollection(
            process,
            cms.InputTag('ak5PFJets'),
            'AK5',
            'PF',
            doJTA        = True,
            doBTagging   = True,
            jetCorrLabel = ('AK5PF', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute'])),
            doType1MET   = True,
            doL1Cleaning = True,
            doL1Counters = False,
            genJetCollection=cms.InputTag("ak5GenJets"),
            doJetID      = True,
            jetIdLabel   = "ak5"
            )
    
        
    
    #---------
    #PG PF2PAT sequence from /CMSSW/PhysicsTools/PatAlgos/test/patTuple_PATandPF2PAT_cfg.py
    # An empty postfix means that only PF2PAT is run,
    # otherwise both standard PAT and PF2PAT are run. In the latter case PF2PAT
    # collections have standard names + postfix (e.g. patElectronPFlow)  
    
    
    
    # -------------------
    # pat selection layer
    process.selectedPatElectrons.cut      = cms.string("pt > 20. & abs(eta) < 2.5")
    process.selectedPatElectronsPFlow.cut = cms.string("pt > 20. & abs(eta) < 2.5")    

    process.selectedPatMuons.cut      = cms.string("pt > 20. & abs(eta) < 2.5")
    process.selectedPatMuonsPFlow.cut = cms.string("pt > 20. & abs(eta) < 2.5")

    process.selectedPatJets.cut        = cms.string("pt > 15. & abs(eta) < 5")
    process.selectedPatJetsPFlow.cut   = cms.string("pt > 15. & abs(eta) < 5")    
    process.selectedPatJetsAK5Calo.cut = cms.string("pt > 15. & abs(eta) < 5")
    process.selectedPatJetsAK5PF.cut   = cms.string("pt > 15. & abs(eta) < 5")

    process.selectedPatPhotons.cut      = cms.string("pt > 10. & abs(eta) < 5")
    process.selectedPatPhotonsPFlow.cut = cms.string("pt > 10. & abs(eta) < 5")    
    
    # the HCAL Noise Filter
    #process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
    
    # the MiBiPAT path
    process.MiBiCommonPAT = cms.Sequence(
        process.AllEvents * # -> Counter
        process.scrapingFilter *
        process.NonScrapedEvents * # -> Counter
        process.primaryVertexFilter *
        process.GoodVtxEvents * # -> Counter
        getattr(process,"patPF2PATSequence"+postfix) *
        process.makePatElectrons* # -> EleID + EleIso + PatEle
        process.recoPFJets *
        process.patDefaultSequence
    )
    

    
    #----------------------
    # Lepton/Photon Filters
    process.load('PhysicsTools.PatAlgos.selectionLayer1.leptonCountFilter_cfi')
    process.LeptonsFilter = countPatLeptons.clone(
      electronSource = cms.InputTag("selectedPatElectrons"),
      muonSource     = cms.InputTag("selectedPatMuons"),
      minNumber      = cms.uint32(1)
     )

    
    process.LeptonsFilterPFlow = countPatLeptons.clone(
      electronSource = cms.InputTag("selectedPatElectronsPFlow"),
      muonSource     = cms.InputTag("selectedPatMuonsPFlow"),
      minNumber      = cms.uint32(1)
     )
    
    
    
    process.load('PhysicsTools.PatAlgos.selectionLayer1.photonCountFilter_cfi')
    process.PhotonsFilter = countPatPhotons.clone(
      src       = cms.InputTag("selectedPatPhotons"),
      minNumber = cms.uint32(2)
     )

    
    
    #------------
    # Jet Filters
    process.load('PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi')
    process.JetFilterAK5Calo = countPatJets.clone(
      src = cms.InputTag("selectedPatJetsAK5Calo"),
      minNumber      = cms.uint32(2)
    )
    
    
    process.JetFilterAK5PF = countPatJets.clone(
      src = cms.InputTag("selectedPatJetsAK5PF"),
      minNumber      = cms.uint32(2)
    )
    
     
    process.JetFilterPFlow = countPatJets.clone(
      src = cms.InputTag("selectedPatJetsPFlow"),
      minNumber      = cms.uint32(2)
    )
    
    
    
    #-----------
    # Sequences & Other counters
    process.LeptonsFilterEvents = cms.EDProducer("EventCountProducer")
    process.LeptonsFilterPFlowEvents = cms.EDProducer("EventCountProducer")
    process.JetFilterAK5CaloEvents = cms.EDProducer("EventCountProducer")
    process.JetFilterAK5PFEvents = cms.EDProducer("EventCountProducer")
    process.JetFilterPFlowEvents = cms.EDProducer("EventCountProducer")
    process.PhotonsFilterEvents = cms.EDProducer("EventCountProducer")
    
    process.OneLeptonTwoJetsAK5CaloSeq = cms.Sequence(
        process.LeptonsFilter*
        process.LeptonsFilterEvents*
        process.JetFilterAK5Calo*
        process.JetFilterAK5CaloEvents
       )

    
    process.OneLeptonTwoJetsAK5PFSeq = cms.Sequence(
        process.LeptonsFilter*
        #process.LeptonsFilterEvents*
        process.JetFilterAK5PF*
        process.JetFilterAK5PFEvents
        )
    
    
    process.OneLeptonTwoJetsPFlowSeq = cms.Sequence(
        process.LeptonsFilterPFlow*
        process.LeptonsFilterPFlowEvents*
        process.JetFilterPFlow*
        process.JetFilterPFlowEvents
        )

    process.TwoPhotonsSeq = cms.Sequence(
        process.PhotonsFilter*
        process.PhotonsFilterEvents
        )
    
    
    
    # the MiBiPAT
    process.MiBiPathAK5PF = cms.Path(process.MiBiCommonPAT*process.OneLeptonTwoJetsAK5PFSeq)
    process.MiBiPathAK5Calo = cms.Path(process.MiBiCommonPAT*process.OneLeptonTwoJetsAK5CaloSeq)
    process.MiBiPathPFlow = cms.Path(process.MiBiCommonPAT*process.OneLeptonTwoJetsPFlowSeq)
    process.MiBiPathPhotons = cms.Path(process.MiBiCommonPAT*process.TwoPhotonsSeq)
    
    process.out.outputCommands = cms.untracked.vstring(
        'drop *',
        'keep recoTracks_generalTracks__RECO',         # tracks
        'keep edmMergeableCounter_*_*_*',              # counters
        'keep *_selected*_*_*',                        # selected PAT objects
        'keep *TrackExtra*_*_*_*',                     # track extra objects
        'keep *_patMETs*_*_*',                         # All PAT objects
        'keep *_offlinePrimaryVertices*_*_*',          # Primary vertices: you want these to compute impact parameters
        'keep *_offlineBeamSpot_*_*',                  # Beam spot: you want this for the same reason
        'keep edmTriggerResults_TriggerResults_*_*',   # HLT info, per path (cheap)
        'keep *_genParticles_*_*',                     # HLT info, per path (cheap)
        'keep recoGsfElectronCores_*_*_*',             # refs for electrons
        'keep *_reducedEcalRecHitsEB_*_*',             # reduced recHits Barrel
        'keep *_reducedEcalRecHitsEE_*_*'              # reduced recHits Barrel
    )
