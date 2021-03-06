import FWCore.ParameterSet.Config as cms

#
#    _____             __ _                        _   _
#   / ____|           / _(_)                      | | (_)
#   | |     ___  _ __ | |_ _  __ _ _   _ _ __ __ _| |_ _  ___  _ __
#   | |    / _ \| '_ \|  _| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \
#   | |___| (_) | | | | | | | (_| | |_| | | | (_| | |_| | (_) | | | |
#    \_____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
#                             __/ |
#                            |___/

# From which kind of dataset are you starting from?
MC = False
runFromAOD = False
runFromALCA = True

# Do you want to reReco ECAL RecHits (also from RAW if you have them) ? 
ECALRecalib = True
ECALFromRAW = False
ApplyInterCalib = True
#Switch to turn on/off application of LC. To be set to False when running from RAW and want to produce LC=1
ApplyLaser = True

# Do you want to produce also small E/p ntuples?
simpleNtupleEoverP = True

# Do you want to filter events? 
HLTFilter = False
HLTPath = "HLT_Ele"
HLTProcessName = "HLT"

ZSkim = False
WSkim = False

#electron cuts
ELECTRON_ET_CUT_MIN = 20.0
ELECTRON_CUTS = "(abs(superCluster.eta)<2.5) && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"

#mass cuts (for Zee selection)
MASS_CUT_MIN = 60.

#met, mt cuts (for Wenu selection)
W_ELECTRON_ET_CUT_MIN = 30.0
MET_CUT_MIN = 20.
MT_CUT_MIN = 50.


#    _____  __             _             _         _
#   / ____|/ _|           | |           | |       | |
#   | |    | |_ __ _   ___| |_ __ _ _ __| |_ ___  | |__   ___ _ __ ___
#   | |    |  _/ _` | / __| __/ _` | '__| __/ __| | '_ \ / _ \ '__/ _ \
#   | |____| || (_| | \__ \ || (_| | |  | |_\__ \ | | | |  __/ | |  __/
#    \_____|_| \__, | |___/\__\__,_|_|   \__|___/ |_| |_|\___|_|  \___|
#               __/ |
#              |___/
   

if (not runFromALCA):
    processName = 'ALCASKIM'
else:
    processName ='ALCARERECO'

process = cms.Process(processName)
#process.prescaler = cms.EDFilter("Prescaler",
#                                    prescaleFactor = cms.int32(prescale),
#                                    prescaleOffset = cms.int32(0)
#                                    )
# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
#process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
#process.load('Configuration.StandardSequences.L1Reco_cff')
#process.load('Configuration.StandardSequences.Reconstruction_cff')
#process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#from Calibration.EcalCalibAlgos.DoubleElectron_Jul05_ALCAELECTRON_cff import *
#from Calibration.EcalCalibAlgos.Cert_160404_172802_cff import *

readFiles = cms.untracked.vstring()

readFiles.extend( [
# MC Aod 
#"/store/mc/Summer11/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/0AD7EA94-A29C-E011-BC75-001A4BA81FB8.root"
# ALCA
"file:/data1/dimatteo/Run2011B-WElectron-PromptSkim-v1-ALCARECO-NOLC.root"    
# RAW-RECO
#"/store/data/Run2011A/DoubleElectron/RAW-RECO/ZElectron-PromptSkim-v4/0000/407132B4-EC93-E011-B11F-00248C0BE005.root"
# RelVal
#"/store/RelVal/CMSSW_4_2_8/RelValZEE/GEN-SIM-RECO/START42_V12-v1/0025/529A2B04-05BB-E011-837A-001A92811708.root"
] )

process.source = cms.Source("PoolSource",
                            fileNames = readFiles
)

#process.source.inputCommands = cms.untracked.vstring("drop *", "keep *_*_*_HLT")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

# Other statements
#
if (MC):
    process.GlobalTag.globaltag = 'START42_V12::All'
else:
    process.GlobalTag.globaltag = 'GR_R_42_V22::All' 


process.GlobalTag.toGet = cms.VPSet(
        #cms.PSet(
            #record = cms.string("EcalLaserAPDPNRatiosRcd"),
            #tag = cms.string("EcalLaserAPDPNRatios_p1p2p3_v2_mc"),
            #connect =cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_ECAL")
            #),
cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
         tag = cms.string("EcalIntercalibConstants_V20111021_PiZeroEtaPhiSymm_relativeToPROMPTconstants"),
         connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_ECAL")
        )
#  ,cms.PSet(record = cms.string("EcalADCToGeVConstantRcd"),
#          tag = cms.string("EcalADCToGeVConstant_v10_offline"),
#          connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_ECAL")
#         )
,cms.PSet(record = cms.string("EcalLaserAPDPNRatiosRcd"),
#           tag = cms.string("EcalLaserAPDPNRatios_2011fit_noVPT_nolim_online"),
          #tag = cms.string("EcalLaserAPDPNRatios_test_20110625"),
          #tag = cms.string("EcalLaserAPDPNRatios_2011V3_online"),
          tag = cms.string("EcalLaserAPDPNRatios_data_20111122_158851_180363"),
         connect = cms.untracked.string("frontier://FrontierPrep/CMS_COND_ECAL")
         )
 #beam spot to arrive to very last runs after 167151
#   ,cms.PSet(record = cms.string("BeamSpotObjectsRcd"),
#          tag = cms.string("BeamSpotObjects_PCL_byLumi_v0_prompt"),
#          connect = cms.untracked.string("frontier://PromptProd/CMS_COND_31X_BEAMSPOT")
         )




##    _____ _           _                     ___    _
##   | ____| | ___  ___| |_ _ __ ___  _ __   |_ _|__| |
##   |  _| | |/ _ \/ __| __| '__/ _ \| '_ \   | |/ _` |
##   | |___| |  __/ (__| |_| | | (_) | | | |  | | (_| |
##   |_____|_|\___|\___|\__|_|  \___/|_| |_| |___\__,_|
##

process.selectedElectrons = cms.EDFilter("GsfElectronRefSelector",
                                 src = cms.InputTag( 'electronRecalibSCAssociator' ),
                                 cut = cms.string( ELECTRON_CUTS )
                             )

process.PassingWP90 = process.selectedElectrons.clone(
    cut = cms.string(
        process.selectedElectrons.cut.value() +
            " && (gsfTrack.trackerExpectedHitsInner.numberOfHits<=1)" #wrt std WP90 allowing 1 numberOfMissingExpectedHits
            " && (ecalEnergy*sin(superClusterPosition.theta)>" + str(ELECTRON_ET_CUT_MIN) + ")"
            " && ((isEB"
            " && ( dr03TkSumPt/p4.Pt <0.12 && dr03EcalRecHitSumEt/p4.Pt < 0.09 && dr03HcalTowerSumEt/p4.Pt  < 0.1 )"
            " && (sigmaIetaIeta<0.01)"
            " && ( -0.8<deltaPhiSuperClusterTrackAtVtx<0.8 )"
            " && ( -0.007<deltaEtaSuperClusterTrackAtVtx<0.007 )"
            " && (hadronicOverEm<0.12)"
            ")"
            " || (isEE"
            " && ( dr03TkSumPt/p4.Pt <0.07 && dr03EcalRecHitSumEt/p4.Pt < 0.07 && dr03HcalTowerSumEt/p4.Pt  < 0.07 )"
            " && (sigmaIetaIeta<0.03)"
            " && ( -0.7<deltaPhiSuperClusterTrackAtVtx<0.7 )"
            " && ( -0.009<deltaEtaSuperClusterTrackAtVtx<0.009 )"
            " && (hadronicOverEm<0.1) "
            "))"
            )
    )

process.ele_sequence = cms.Sequence(
    process.PassingWP90
    )


###############################
# ECAL Recalibration
###############################
process.electronRecalib = cms.Sequence()

if (ECALRecalib):
    process.load("Calibration.EcalCalibAlgos.electronRecalibSCAssociator_cfi")
            
    if (not ECALFromRAW):
        process.load("RecoLocalCalo.EcalRecProducers.ecalRecalibRecHit_cfi")
        process.ecalRecHit.doIntercalib = cms.bool(ApplyInterCalib)
        process.ecalRecHit.doLaserCorrection = cms.bool(ApplyLaser)
        if (runFromAOD):
            process.ecalRecHit.EBRecHitCollection = "reducedEcalRecHitsEB"
            process.ecalRecHit.EERecHitCollection = "reducedEcalRecHitsEE"
        elif (runFromALCA): 
            process.ecalRecHit.EBRecHitCollection = "alCaIsolatedElectrons:alcaBarrelHits"
            process.ecalRecHit.EERecHitCollection = "alCaIsolatedElectrons:alcaEndcapHits"

        process.ecalRecHit.EBRecalibRecHitCollection = "EcalRecHitsEB"
        process.ecalRecHit.EERecalibRecHitCollection = "EcalRecHitsEE"
        process.electronRecalib *= (process.ecalRecHit)
    else:
        #restarting from ECAL RAW to reconstruct amplitudes and energies
        process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
        process.load('RecoLocalCalo.Configuration.RecoLocalCalo_cff')
        process.ecalRecHit.laserCorrection=cms.bool(ApplyLaser)
        #no switch in standard recHit producer to apply new intercalibrations
        process.electronRecalib *= ( (process.ecalDigis+process.ecalPreshowerDigis) * process.ecalLocalRecoSequence)
        
    process.load("RecoEcal.Configuration.RecoEcal_cff")
    process.correctedHybridSuperClusters.corectedSuperClusterCollection = 'recalibSC'
    process.correctedMulti5x5SuperClustersWithPreshower.corectedSuperClusterCollection = 'endcapRecalibSC'

    if (runFromAOD):
        process.multi5x5SuperClustersWithPreshower.preshRecHitProducer = cms.InputTag("reducedEcalRecHitsES")
        process.multi5x5PreshowerClusterShape.preshRecHitProducer = cms.InputTag("reducedEcalRecHitsES")
    elif (runFromALCA):
        process.multi5x5SuperClustersWithPreshower.preshRecHitProducer = cms.InputTag("alCaIsolatedElectrons","alcaPreshowerHits")
        process.multi5x5PreshowerClusterShape.preshRecHitProducer = cms.InputTag("alCaIsolatedElectrons","alcaPreshowerHits")

    process.electronRecalibSCAssociator.scIslandCollection = cms.string('endcapRecalibSC')
    process.electronRecalibSCAssociator.scIslandProducer = cms.string('correctedMulti5x5SuperClustersWithPreshower')
    process.electronRecalibSCAssociator.scProducer = cms.string('correctedHybridSuperClusters')
    process.electronRecalibSCAssociator.scCollection = cms.string('recalibSC')
    process.electronRecalibSCAssociator.electronProducer = 'electronRecalibSCAssociator'
    process.electronRecalib *= (process.hybridClusteringSequence* process.multi5x5ClusteringSequence * process.multi5x5PreshowerClusteringSequence * process.electronRecalibSCAssociator)

if (runFromAOD):
    process.alCaIsolatedElectrons.esRecHitsLabel = cms.InputTag("reducedEcalRecHitsES")
elif (runFromALCA):
    process.alCaIsolatedElectrons.esRecHitsLabel = cms.InputTag("alCaIsolatedElectrons","alcaPreshowerHits")

if (ECALRecalib):
    process.alCaIsolatedElectrons.ebRecHitsLabel = cms.InputTag("ecalRecHit:EcalRecHitsEB")
    process.alCaIsolatedElectrons.eeRecHitsLabel = cms.InputTag("ecalRecHit:EcalRecHitsEE")
    process.alCaIsolatedElectrons.electronLabel = cms.InputTag("electronRecalibSCAssociator")        
elif (runFromAOD):
    process.alCaIsolatedElectrons.ebRecHitsLabel = cms.InputTag("reducedEcalRecHitsEB")
    process.alCaIsolatedElectrons.eeRecHitsLabel = cms.InputTag("reducedEcalRecHitsEE")
elif (runFromALCA):
    process.alCaIsolatedElectrons.ebRecHitsLabel = cms.InputTag("alCaIsolatedElectrons:alcaBarrelHits")
    process.alCaIsolatedElectrons.eeRecHitsLabel = cms.InputTag("alCaIsolatedElectrons:alcaEndcapHits")
    
##    ____       _
##   |  _ \ __ _(_)_ __ ___
##   | |_) / _` | | '__/ __|
##   |  __/ (_| | | |  \__ \
##   |_|   \__,_|_|_|  |___/
##
##

process.filter = cms.Sequence()

if (ZSkim):
    process.tagGsf =  cms.EDProducer("CandViewShallowCloneCombiner",
                                     decay = cms.string("PassingWP90 PassingWP90"),
                                     checkCharge = cms.bool(False),
                                     cut   = cms.string("mass > " + str(MASS_CUT_MIN))
                                     )
    process.tagGsfCounter = cms.EDFilter("CandViewCountFilter",
                                         src = cms.InputTag("tagGsf"),
                                         minNumber = cms.uint32(1)
                                         )
    
    process.filter *= (process.tagGsf * process.tagGsfCounter)
elif (WSkim):
    MT="sqrt(2*daughter(0).pt*daughter(1).pt*(1 - cos(daughter(0).phi - daughter(1).phi)))"
    process.elecMet = cms.EDProducer("CandViewShallowCloneCombiner",
                             decay = cms.string("pfMet PassingWP90"), # charge coniugate states are implied
                             checkCharge = cms.bool(False),
                             cut   = cms.string(("daughter(0).pt > %f && daughter(0).pt > %f && "+MT+" > %f") % (MET_CUT_MIN, W_ELECTRON_ET_CUT_MIN, MT_CUT_MIN))
                             )
    process.elecMetCounter = cms.EDFilter("CandViewCountFilter",
                                  src = cms.InputTag("elecMet"),
                                  minNumber = cms.uint32(1)
                                  )
    process.filter *= (process.elecMet * process.elecMetCounter)

process.tagGsfSeq = cms.Sequence()

if (HLTFilter):
    import copy
    from HLTrigger.HLTfilters.hltHighLevel_cfi import *
    process.ZEEHltFilter = copy.deepcopy(hltHighLevel)
    process.ZEEHltFilter.throw = cms.bool(False)
    process.ZEEHltFilter.HLTPaths = ["HLT_Ele*"]
    process.tagGsfSeq *= process.ZEEHltFilter



#    process.tagGsfSeq *= process.ecalRecHit 
if (not runFromALCA):
    process.load('RecoJets.Configuration.RecoPFJets_cff')
    process.kt6PFJetsForRhoCorrection = process.kt6PFJets.clone(doRhoFastjet = True)
    process.kt6PFJetsForRhoCorrection.Rho_EtaMax = cms.double(2.5)
    process.tagGsfSeq *= (process.kt6PFJetsForRhoCorrection) 

process.tagGsfSeq *= (process.ele_sequence * process.filter * process.electronRecalib )

if ( (ECALRecalib) or (not runFromALCA) ):
    process.tagGsfSeq *= ( process.seqALCARECOEcalCalElectronRECO )

if (simpleNtupleEoverP):
    #--------------------------
    # HLT
    #--------------------------

    process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
    process.hltfilter = process.hltHighLevel.clone(
    # Single Ele
      HLTPaths = ['HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v*','HLT_Ele25_WP80_PFMT40_v1','HLT_Ele27_WP80_PFMT50_v1','HLT_Ele32_WP70_PFMT50_v*','HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v*','HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v8'],
        andOr = True,  # False = and, True=or
        throw = False
    )

    
    #--------------------------
    # Ntuple
    #--------------------------
    
    process.load("Calibration/EcalCalibNtuple/simpleNtupleEoverP_cfi")
    process.TFileService = cms.Service(
      "TFileService",
      fileName = cms.string("simpleNtuple.root")
    )
    process.tagGsfSeq *= ( process.hltfilter * process.simpleNtupleEoverP )
    
    
    
process.zFilterPath = cms.Path( process.tagGsfSeq )

process.schedule = cms.Schedule(process.zFilterPath)
