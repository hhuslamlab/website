# Installing Kaldi and MFA
This is a short guide to install [Kaldi](https://kaldi-asr.org/) and [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) for Linux and MacOS users.

## Kaldi installation
```sh
git clone https://github.com/kaldi-asr/kaldi.git kaldi
cd kaldi/tools
extras/check_dependencies.sh
extras/install_mkl.sh
make
extras/install_irstlm.sh
cd ../src/
./configure
make depend
make -j 4
```
Free Pro-tip by Akhilesh: You will run into errors at some point and all you have to do is to keep calm and read them. They mostly suggest you to install more softwares/tools and that is it.

## Montreal Forced Aligner installation
Download MFA (version 1.0.1) from [here](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/releases/tag/v1.0.1)

Linux users click on `montreal-forced-aligner_linux.tar.gz`

MacOS users click on `montreal-forced-aligner_macosx.zip`

Just unzip or untar and follow this [detailed guide](https://montreal-forced-aligner.readthedocs.io/en/latest/) for the usage.

## Authors
[**Akhilesh**](https://slam.phil.hhu.de/authors/akhilesh/)
