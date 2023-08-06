# Tacotron2 library

This Tacotron2 library was changed to be used with vait library.

Original code, README.md and additional information:

https://github.com/NVIDIA/tacotron2


## Instalation

### 1) Install tacotron2 library

(This will also install waveglow library)

```shell
pip install tacotron2==22.12.28
```


### 2) Install CUDA 11.3 or 11.6

```shell
pip install -r requirements-cuda-11.3.txt
# or
pip install -r requirements-cuda-11.6.txt
```


### 3) Install apex
```shell
git clone https://github.com/NVIDIA/apex /home/${USER}/apex
cd /home/${USER}/apex
pip install -v --disable-pip-version-check --no-cache-dir ./
cd -
```


### 4) Download published model files

```shell
wget https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view?usp=sharing
```


## Usage: Training

```shell
tacotron2-train --output_directory=outdir --log_directory=logdir
tacotron2-train --output_directory=outdir --log_directory=logdir -c tacotron2_statedict.pt --warm_start
```
