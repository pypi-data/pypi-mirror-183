# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['radtts', 'radtts.tts_text_processing']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'Unidecode>=1.3.6,<2.0.0',
 'audioread>=3.0.0,<4.0.0',
 'inflect>=6.0.2,<7.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'librosa>=0.9.2,<0.10.0',
 'matplotlib>=3.6.2,<4.0.0',
 'natsort>=8.2.0,<9.0.0',
 'pandas>=1.5.2,<2.0.0',
 'peakutils>=1.3.4,<2.0.0',
 'soundfile>=0.11.0,<0.12.0',
 'sox>=1.4.1,<2.0.0',
 'srt>=3.5.2,<4.0.0',
 'tgt>=1.4.4,<2.0.0',
 'webrtcvad>=2.0.10,<3.0.0']

entry_points = \
{'console_scripts': ['radtts-alignment = radtts.alignment:main',
                     'radtts-data = radtts.data:main',
                     'radtts-inference = radtts.inference:main',
                     'radtts-inference_voice_conversion = '
                     'radtts.inference_voice_conversion:main',
                     'radtts-train = radtts.train:main']}

setup_kwargs = {
    'name': 'radtts',
    'version': '22.12.28',
    'description': 'RADTTS library',
    'long_description': '# RADTTS library\n\nThis RADTTS library was changed to be used with vait library.\n\nOriginal code, README.md and additional information:\n\nhttps://github.com/NVIDIA/radtts\n\n\n## Instalation\n\n### 1) Install RADTTS library\n\n```shell\npip install radtts==22.12.28\n```\n\n\n### 2) Install CUDA 11.3 or 11.6\n\n```shell\npip install -r requirements-cuda-11.3.txt\n# or\npip install -r requirements-cuda-11.6.txt\n```\n\n### 3) Install maracas\n```shell\ngit clone https://github.com/jfsantos/maracas /home/${USER}/maracas\ncd /home/${USER}/maracas\npip install .\ncd -\n```\n\n## Usage: Training\n\n```shell\nradtts-train -c config_ljs_radtts.json -p train_config.output_directory=outdir\nradtts-train -c config_ljs_radtts.json -p train_config.output_directory=outdir_dir train_config.warmstart_checkpoint_path=model_path.pt model_config.include_modules="decatndur"\n```\n\n\n## Usage: Inferencing\n\n```shell\nradtts-inference -c CONFIG_PATH -r RADTTS_PATH -v HG_PATH -k HG_CONFIG_PATH -t TEXT_PATH -s ljs --speaker_attributes ljs --speaker_text ljs -o results/\nradtts-inference_voice_conversion --radtts_path RADTTS_PATH --radtts_config_path RADTTS_CONFIG_PATH --vocoder_path HG_PATH --vocoder_config_path HG_CONFIG_PATH --f0_mean=211.413 --f0_std=46.6595 --energy_mean=0.724884 --energy_std=0.0564605 --output_dir=results/ -p data_config.validation_files="{\'Dummy\': {\'basedir\': \'data/\', \'audiodir\':\'22khz\', \'filelist\': \'vc_audiopath_txt_speaker_emotion_duration_filelist.txt\'}}"\n```\n',
    'author': 'Tadeusz Miszczyk',
    'author_email': '42252259+8tm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/8tm/radtts',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
