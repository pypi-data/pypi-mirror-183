# Flowtron library

This Flowtron library was changed to be used with vait library.

Original code, README.md and additional information:

https://github.com/NVIDIA/flowtron


## Instalation

### 1) Install flowtron library

(This will also install waveglow library)

```shell
pip install flowtron==22.12.28
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


### 4) Download published model Flowtron LJS

```shell
wget https://drive.google.com/open?id=1Cjd6dK_eFz6DE0PKXKgKxrzTUqzzUDW-
```
### 5) Download published model Flowtron LibriTTS

```shell
wget https://drive.google.com/open?id=1KhJcPawFgmfvwV7tQAOeC253rYstLrs8
```
### 6) Download published model Flowtron LibriTTS2K

```shell
wget https://drive.google.com/open?id=1sKTImKkU0Cmlhjc_OeUDLrOLIXvUPwnO
```


## Usage: Training

```shell
flowtron-train -c config.json -p train_config.output_directory=outdir data_config.use_attn_prior=1
```

## Usage: Inferencing

```shell
flowtron-inference -c config.json -f models/flowtron_ljs.pt -w models/waveglow_256channels_v4.pt -t "It is well know that deep generative models have a rich latent space!" -i 0
```
