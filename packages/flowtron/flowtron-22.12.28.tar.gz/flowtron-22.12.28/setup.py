# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flowtron', 'flowtron.text']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'Unidecode>=1.3.6,<2.0.0',
 'inflect>=6.0.2,<7.0.0',
 'librosa>=0.9.2,<0.10.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.5,<2.0.0',
 'scipy>=1.9.3,<2.0.0',
 'tensorboardX>=2.5.1,<3.0.0',
 'waveglow>=22.12.28,<23.0.0']

extras_require = \
{':python_version >= "3.8" and python_version < "3.11"': ['tensorflow-io-gcs-filesystem>=0.29.0,<0.30.0']}

entry_points = \
{'console_scripts': ['flowtron-data = flowtron.data:main',
                     'flowtron-inference = flowtron.inference:main',
                     'flowtron-train = flowtron.train:main']}

setup_kwargs = {
    'name': 'flowtron',
    'version': '22.12.28',
    'description': 'Flowtron library',
    'long_description': '# Flowtron library\n\nThis Flowtron library was changed to be used with vait library.\n\nOriginal code, README.md and additional information:\n\nhttps://github.com/NVIDIA/flowtron\n\n\n## Instalation\n\n### 1) Install flowtron library\n\n(This will also install waveglow library)\n\n```shell\npip install flowtron==22.12.28\n```\n\n\n### 2) Install CUDA 11.3 or 11.6\n\n```shell\npip install -r requirements-cuda-11.3.txt\n# or\npip install -r requirements-cuda-11.6.txt\n```\n\n\n### 3) Install apex\n```shell\ngit clone https://github.com/NVIDIA/apex /home/${USER}/apex\ncd /home/${USER}/apex\npip install -v --disable-pip-version-check --no-cache-dir ./\ncd -\n```\n\n\n### 4) Download published model Flowtron LJS\n\n```shell\nwget https://drive.google.com/open?id=1Cjd6dK_eFz6DE0PKXKgKxrzTUqzzUDW-\n```\n### 5) Download published model Flowtron LibriTTS\n\n```shell\nwget https://drive.google.com/open?id=1KhJcPawFgmfvwV7tQAOeC253rYstLrs8\n```\n### 6) Download published model Flowtron LibriTTS2K\n\n```shell\nwget https://drive.google.com/open?id=1sKTImKkU0Cmlhjc_OeUDLrOLIXvUPwnO\n```\n\n\n## Usage: Training\n\n```shell\nflowtron-train -c config.json -p train_config.output_directory=outdir data_config.use_attn_prior=1\n```\n\n## Usage: Inferencing\n\n```shell\nflowtron-inference -c config.json -f models/flowtron_ljs.pt -w models/waveglow_256channels_v4.pt -t "It is well know that deep generative models have a rich latent space!" -i 0\n```\n',
    'author': 'Tadeusz Miszczyk',
    'author_email': '42252259+8tm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/8tm/flowtron',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
