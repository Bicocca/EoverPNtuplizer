#ifndef ZPeakFitUtils_h
#define ZPeakFitUtils_h

#include "TH1F.h"
#include "TF1.h"
#include "TArrow.h"

#include "RooMath.h"
#include "RooComplex.h"



void FitZPeak(TF1** fitFunc_voigtian, TF1** fitFunc_crystalBall, const std::string& fitFuncName,
              TH1F* histo);

double mySimpleVoigt(double *xx, double *s);
double myDoubleVoigt(double *xx, double *s);
double myTripleVoigt(double *xx, double *s);

double breitWigner(double* x, double* par);
double crystalBallLow(double* x, double* par);
double breitWigner_crystalBallLow(double* x, double* par);

void GetOLSigma(double& peak, double& sigmaOL,
                TF1* f, const double& prec = 0.01, TArrow** line = NULL);

#endif
