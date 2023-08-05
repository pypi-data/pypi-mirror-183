# pysepm-evo - Python Speech Enhancement Performance Measures (Quality and Intelligibility)
[![DOI](https://zenodo.org/badge/220233987.svg)](https://zenodo.org/badge/latestdoi/220233987)

PyPI released version of [pysepm](https://github.com/schmiph2/pysepm). Please note that this package doesn't include the usage pf `pesq`. To use SRMRpy, type the following:

    pip install https://github.com/jfsantos/SRMRpy/archive/master.zip#egg=SRMRpy

# Install with pip
Install pysepm-evo:
```
pip3 install pyseqm-evo
```
# Examples
Please find a Jupyter Notebook with examples for all implemented measures in the [examples folder](https://github.com/schmiph2/pysepm/tree/master/examples).

# Implemented Measures
## Speech Quality Measures
+ Segmental Signal-to-Noise Ratio (SNRseg)
+ Frequency-weighted Segmental SNR (fwSNRseg)
+ Log-likelihood Ratio (LLR)
+ Weighted Spectral Slope (WSS)
implementation by ludlows)
+ Composite Objective Speech Quality (composite)
+ Cepstrum Distance Objective Speech Quality Measure (CD)

## Speech Intelligibility Measures
+ Short-time objective intelligibility (STOI), ([pystoi](https://github.com/mpariente/pystoi) implementation by mpariente)
+ Coherence and speech intelligibility index (CSII)
+ Normalized-covariance measure (NCM)

## Dereverberation Measures (TODO)
+ Bark spectral distortion (BSD) 
+ Scale-invariant signal to distortion ratio (SI-SDR)
