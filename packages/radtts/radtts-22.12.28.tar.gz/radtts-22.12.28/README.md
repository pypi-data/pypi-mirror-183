# RADTTS library

This RADTTS library was changed to be used with vait library.

Original code, README.md and additional information:

https://github.com/NVIDIA/radtts


## Instalation

### 1) Install RADTTS library

```shell
pip install radtts==22.12.28
```


### 2) Install CUDA 11.3 or 11.6

```shell
pip install -r requirements-cuda-11.3.txt
# or
pip install -r requirements-cuda-11.6.txt
```

### 3) Install maracas
```shell
git clone https://github.com/jfsantos/maracas /home/${USER}/maracas
cd /home/${USER}/maracas
pip install .
cd -
```

## Usage: Training

```shell
radtts-train -c config_ljs_radtts.json -p train_config.output_directory=outdir
radtts-train -c config_ljs_radtts.json -p train_config.output_directory=outdir_dir train_config.warmstart_checkpoint_path=model_path.pt model_config.include_modules="decatndur"
```


## Usage: Inferencing

```shell
radtts-inference -c CONFIG_PATH -r RADTTS_PATH -v HG_PATH -k HG_CONFIG_PATH -t TEXT_PATH -s ljs --speaker_attributes ljs --speaker_text ljs -o results/
radtts-inference_voice_conversion --radtts_path RADTTS_PATH --radtts_config_path RADTTS_CONFIG_PATH --vocoder_path HG_PATH --vocoder_config_path HG_CONFIG_PATH --f0_mean=211.413 --f0_std=46.6595 --energy_mean=0.724884 --energy_std=0.0564605 --output_dir=results/ -p data_config.validation_files="{'Dummy': {'basedir': 'data/', 'audiodir':'22khz', 'filelist': 'vc_audiopath_txt_speaker_emotion_duration_filelist.txt'}}"
```
