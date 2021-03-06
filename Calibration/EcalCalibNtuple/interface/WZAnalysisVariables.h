#include "PhysicsTools/NtupleUtils/interface/treeReader.h"
#include "PhysicsTools/NtupleUtils/interface/ntpleUtils.h"

#include "TTree.h"



struct WZAnalysisVariables
{
  // tree definition
  TFile* m_outputRootFile;
  TTree* m_reducedTree;
  

   // event variables
  int dataFlag;
  int totEvents;
  float crossSection;
  int runId;
  int lumiId;
  int eventId;
  int eventNaiveId;
  int timeStampLow;
  int timeStampHigh;
 
  int isW;
  int isZ;


  // PU variables

  float PUit_TrueNumInteraction;
  int PUit_NumInteraction;
  int PUoot_early;
  int PUoot_late;

  float rhoForIsolation;
  float rhoForJets;
  
  
  // PV variables
  int PV_n;
  float PV_z;
  float PV_d0;
  float PV_SumPt;
  
  
  // 1st electron variables
  ROOT::Math::XYZTVector ele1;
  ROOT::Math::XYZTVector* p_ele1;
  float ele1_charge;
  float ele1_p;
  float ele1_pt;
  float ele1_eta;
  float ele1_phi;
  
  float ele1_sigmaIetaIeta;
  float ele1_DphiIn;
  float ele1_DetaIn;
  float ele1_HOverE;
  float ele1_tkIso;
  float ele1_emIso;
  float ele1_hadIso;

  float ele1_PFIso_ch;
  float ele1_PFIso_em;
  float ele1_PFIso_nh;
  float ele1_effAreaForIso; 

  float ele1_dxy_PV; 
  float ele1_dz_PV ;
  float ele1_sigmaP;

  float ele1_deltaEtaSuperClusterAtVtx;
  float ele1_deltaPhiSuperClusterAtVtx;

  float ele1_vtxFitConversion; 
  float ele1_ooemoop ;

  std::vector<float> ele1_recHit_E;
  std::vector<int> ele1_recHit_hashedIndex;
  std::vector<int> ele1_recHit_ieta;
  std::vector<int> ele1_recHit_iphi;
  std::vector<int> ele1_recHit_zside;
  std::vector<float> ele1_recHit_laserCorrection;
  std::vector<int> ele1_recHit_flag ;
  std::vector<int> ele1_recHit_alpha;

  float ele1_scERaw;
  float ele1_scEtRaw;
  float ele1_scE;
  float ele1_scEt;
  float ele1_scEta;
  float ele1_scPhi;
  float ele1_scLocalEta;
  float ele1_scLocalPhi;
  float ele1_scEtaWidth;
  float ele1_scPhiWidth;
  float ele1_scLaserCorr;
  float ele1_scCrackCorr;
  float ele1_scLocalContCorr;
  float ele1_scLocalContCorr_DK;
  float ele1_es;
  float ele1_fCorrection;
  float ele1_scE_regression;
  float ele1_scEerr_regression;
  float ele1_scERaw_PUcleaned;
  float ele1_scEtaWidth_PUcleaned;
  float ele1_scPhiWidth_PUcleaned;
  float ele1_fCorrection_PUcleaned;

  int ele1_bcN;
  float ele1_e3x3;
  float ele1_e5x5;
   
  
  int ele1_nPh;
  float ele1_ph_E;
  float ele1_ph_scEta;
  float ele1_ph_scPhi;
  float ele1_ph_R9;

  float ele1_seedE;
  int ele1_seedIeta;
  int ele1_seedIphi;
  int ele1_seedIx;
  int ele1_seedIy;
  int ele1_seedZside;
  float ele1_seedLaserAlpha;
  float ele1_seedLaserCorr;
  int   ele1_nRecHits;
  
  float ele1_tkP;
  float ele1_tkPt;
  
  float ele1_fbrem;
  float ele1_EOverP;
  
  int ele1_isEB;
  int ele1_isEBEEGap;
  int ele1_isEBEtaGap;
  int ele1_isEBPhiGap;
  int ele1_isEEDeeGap;
  int ele1_isEERingGap;

  // regression variables
  float ele1_eRegrInput_rawE;
  float ele1_eRegrInput_r9;
  float ele1_eRegrInput_eta;
  float ele1_eRegrInput_phi;
  float ele1_eRegrInput_r25;
  float ele1_eRegrInput_hoe;
  float ele1_eRegrInput_etaW;
  float ele1_eRegrInput_phiW;
  float ele1_eRegrInput_rho;

  float ele1_eRegrInput_Deta_bC_sC;
  float ele1_eRegrInput_Dphi_bC_sC;
  float ele1_eRegrInput_bCE_Over_sCE;
  float ele1_eRegrInput_e3x3_Over_bCE;
  float ele1_eRegrInput_e5x5_Over_bCE;
  float ele1_eRegrInput_sigietaieta_bC1;
  float ele1_eRegrInput_sigiphiiphi_bC1;
  float ele1_eRegrInput_sigietaiphi_bC1;

  float ele1_eRegrInput_bEMax_Over_bCE;
  float ele1_eRegrInput_bE2nd_Over_bCE;
  float ele1_eRegrInput_bEtop_Over_bCE;
  float ele1_eRegrInput_bEbot_Over_bCE;
  float ele1_eRegrInput_bEleft_Over_bCE;
  float ele1_eRegrInput_bEright_Over_bCE;
  float ele1_eRegrInput_be2x5max_Over_bCE;
  float ele1_eRegrInput_be2x5top_Over_bCE;
  float ele1_eRegrInput_be2x5bottom_Over_bCE;
  float ele1_eRegrInput_be2x5left_Over_bCE;
  float ele1_eRegrInput_be2x5right_Over_bCE;

  float ele1_eRegrInput_seedbC_eta;
  float ele1_eRegrInput_seedbC_phi;
  float ele1_eRegrInput_seedbC_eta_p5;
  float ele1_eRegrInput_seedbC_phi_p2;
  float ele1_eRegrInput_seedbC_bieta;
  float ele1_eRegrInput_seedbC_phi_p20;
  float ele1_eRegrInput_seedbC_etacry;
  float ele1_eRegrInput_seedbC_phicry;
     
  float ele1_eRegrInput_ESoSC;
  float ele1_eRegrInput_nPV;
  float ele1_eRegrInput_SCsize;
  
 
  // 2nd electron variables
  ROOT::Math::XYZTVector ele2;
  ROOT::Math::XYZTVector* p_ele2;
  float ele2_charge;
  float ele2_p;
  float ele2_pt;
  float ele2_eta;
  float ele2_phi;
  
  float ele2_sigmaIetaIeta;
  float ele2_DphiIn;
  float ele2_DetaIn;
  float ele2_HOverE;
  float ele2_tkIso;
  float ele2_emIso;
  float ele2_hadIso;
 
  float ele2_PFIso_ch;
  float ele2_PFIso_em;
  float ele2_PFIso_nh;

  float ele2_effAreaForIso; 
  float ele2_dxy_PV; 
  float ele2_dz_PV ;
  float ele2_sigmaP;

  float ele2_deltaEtaSuperClusterAtVtx;
  float ele2_deltaPhiSuperClusterAtVtx;

  float ele2_ooemoop ;
  float ele2_vtxFitConversion; 
  

  float ele2_scERaw;
  float ele2_scEtRaw;
  float ele2_scE;
  float ele2_scEt;
  float ele2_scEta;
  float ele2_scPhi;
  float ele2_scLocalEta;
  float ele2_scLocalPhi;
  float ele2_scEtaWidth;
  float ele2_scPhiWidth;
  float ele2_scLaserCorr;
  float ele2_scCrackCorr;
  float ele2_scLocalContCorr;
  float ele2_scLocalContCorr_DK;
  float ele2_es;
  float ele2_fCorrection;
  float ele2_scE_regression;
  float ele2_scEerr_regression;
  float ele2_scERaw_PUcleaned;
  float ele2_scEtaWidth_PUcleaned;
  float ele2_scPhiWidth_PUcleaned;
  float ele2_fCorrection_PUcleaned;
  
  int ele2_bcN;
  float ele2_e3x3;
  float ele2_e5x5;

  int ele2_nPh;
  float ele2_ph_E;
  float ele2_ph_scEta;
  float ele2_ph_scPhi;
  float ele2_ph_R9;
  
  float ele2_seedE;
  int ele2_seedIeta;
  int ele2_seedIphi;
  int ele2_seedIx;
  int ele2_seedIy;
  int ele2_seedZside;
  float ele2_seedLaserAlpha;
  float ele2_seedLaserCorr;
  int   ele2_nRecHits;
  
  float ele2_tkP;
  float ele2_tkPt;
  
  float ele2_fbrem;
  float ele2_EOverP;
  
  int ele2_isEB;
  int ele2_isEBEEGap;
  int ele2_isEBEtaGap;
  int ele2_isEBPhiGap;
  int ele2_isEEDeeGap;
  int ele2_isEERingGap;
  
  std::vector<float> ele2_recHit_E;
  std::vector<int> ele2_recHit_hashedIndex;
  std::vector<int> ele2_recHit_ieta;
  std::vector<int> ele2_recHit_iphi;
  std::vector<int> ele2_recHit_zside;
  std::vector<float> ele2_recHit_laserCorrection;
  std::vector<int> ele2_recHit_flag ;
  std::vector<int> ele2_recHit_alpha ;

    // Regression
  float ele2_eRegrInput_rawE;
  float ele2_eRegrInput_r9;
  float ele2_eRegrInput_eta;
  float ele2_eRegrInput_phi;
  float ele2_eRegrInput_r25;
  float ele2_eRegrInput_hoe;
  float ele2_eRegrInput_etaW;
  float ele2_eRegrInput_phiW;
  float ele2_eRegrInput_rho;
  float ele2_eRegrInput_Deta_bC_sC;
  float ele2_eRegrInput_Dphi_bC_sC;
  float ele2_eRegrInput_bCE_Over_sCE;
  float ele2_eRegrInput_e3x3_Over_bCE;
  float ele2_eRegrInput_e5x5_Over_bCE;
  float ele2_eRegrInput_sigietaieta_bC1;
  float ele2_eRegrInput_sigiphiiphi_bC1;
  float ele2_eRegrInput_sigietaiphi_bC1;

  float ele2_eRegrInput_bEMax_Over_bCE;
  float ele2_eRegrInput_bE2nd_Over_bCE;
  float ele2_eRegrInput_bEtop_Over_bCE;
  float ele2_eRegrInput_bEbot_Over_bCE;
  float ele2_eRegrInput_bEleft_Over_bCE;
  float ele2_eRegrInput_bEright_Over_bCE;
  float ele2_eRegrInput_be2x5max_Over_bCE;
  float ele2_eRegrInput_be2x5top_Over_bCE;
  float ele2_eRegrInput_be2x5bottom_Over_bCE;
  float ele2_eRegrInput_be2x5left_Over_bCE;
  float ele2_eRegrInput_be2x5right_Over_bCE;

  float ele2_eRegrInput_seedbC_eta;
  float ele2_eRegrInput_seedbC_phi;
  float ele2_eRegrInput_seedbC_eta_p5;
  float ele2_eRegrInput_seedbC_phi_p2;
  float ele2_eRegrInput_seedbC_bieta;
  float ele2_eRegrInput_seedbC_phi_p20;
  float ele2_eRegrInput_seedbC_etacry;
  float ele2_eRegrInput_seedbC_phicry;
     
  float ele2_eRegrInput_ESoSC;
  float ele2_eRegrInput_nPV;
  float ele2_eRegrInput_SCsize;
 
  
  // met variables
  ROOT::Math::XYZTVector met;
  ROOT::Math::XYZTVector* p_met;
  float met_et;
  float met_phi;

  float ele1Met_mt;
  float ele1Met_Dphi;
  
  
  // di-electron variables
  float ele1ele2_m;
  float ele1ele2_scM;
  float ele1ele2_scM_regression;

  // gen particle information

  float ele1_E_true ;
  float ele1_DR;

  float ele2_E_true ;
  float ele2_DR;
 

};



TFile* GetOutputRootFile(WZAnalysisVariables& vars);

void InitializeWZAnalysisTree(WZAnalysisVariables& vars, const std::string& outputRootFileName, bool isCalib);
void FillWZAnalysisTree(WZAnalysisVariables& vars);

void ClearWZAnalysisVariables(WZAnalysisVariables&, bool isCalib);
void DeleteWZAnalysisVariables(WZAnalysisVariables&);

void SetPUVariables(WZAnalysisVariables& vars, treeReader& reader, const int& dataFlag);
void SetPVVariables(WZAnalysisVariables& vars, treeReader& reader);

void SetElectron1Variables(WZAnalysisVariables& vars, treeReader& reader, const int& ele1It, bool isCalib);
void SetElectron2Variables(WZAnalysisVariables& vars, treeReader& reader, const int& ele2It, bool isCalib);
void SetMetVariables(WZAnalysisVariables& vars, treeReader& reader, int dataFlag, std::string dataRun);
void SetDiElectronVariables(WZAnalysisVariables& vars, treeReader& reader);

void SetPhotonMatchingEle(float* const var, treeReader& reader, const int& eleIt);
void SetGenLeptonInformation (WZAnalysisVariables& vars, treeReader& reader,const int & dataFlag, int isWZ);
