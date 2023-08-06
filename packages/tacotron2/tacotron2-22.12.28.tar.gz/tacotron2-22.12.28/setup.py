# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tacotron2', 'tacotron2.text']

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
 'tensorflow>=2.11.0,<3.0.0',
 'waveglow>=22.12.28,<23.0.0']

extras_require = \
{':python_version >= "3.8" and python_version < "3.11"': ['tensorflow-io-gcs-filesystem>=0.29.0,<0.30.0']}

entry_points = \
{'console_scripts': ['tacotron2-train = tacotron2.train:main']}

setup_kwargs = {
    'name': 'tacotron2',
    'version': '22.12.28',
    'description': 'Tacotron2 library',
    'long_description': '# Tacotron2 library\n\nThis Tacotron2 library was changed to be used with vait library.\n\nOriginal code, README.md and additional information:\n\nhttps://github.com/NVIDIA/tacotron2\n\n\n## Instalation\n\n### 1) Install tacotron2 library\n\n(This will also install waveglow library)\n\n```shell\npip install tacotron2==22.12.28\n```\n\n\n### 2) Install CUDA 11.3 or 11.6\n\n```shell\npip install -r requirements-cuda-11.3.txt\n# or\npip install -r requirements-cuda-11.6.txt\n```\n\n\n### 3) Install apex\n```shell\ngit clone https://github.com/NVIDIA/apex /home/${USER}/apex\ncd /home/${USER}/apex\npip install -v --disable-pip-version-check --no-cache-dir ./\ncd -\n```\n\n\n### 4) Download published model files\n\n```shell\nwget https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view?usp=sharing\n```\n\n\n## Usage: Training\n\n```shell\ntacotron2-train --output_directory=outdir --log_directory=logdir\ntacotron2-train --output_directory=outdir --log_directory=logdir -c tacotron2_statedict.pt --warm_start\n```\n',
    'author': 'Tadeusz Miszczyk',
    'author_email': '42252259+8tm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/8tm/tacotron2',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
