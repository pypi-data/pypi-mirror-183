# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['waveglow']

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
 'tacotron2>=22.12.28,<23.0.0',
 'tensorboardX>=2.5.1,<3.0.0',
 'tensorflow>=2.11.0,<3.0.0']

entry_points = \
{'console_scripts': ['waveglow-inference = waveglow.inference:main',
                     'waveglow-train = waveglow.train:main']}

setup_kwargs = {
    'name': 'waveglow',
    'version': '22.12.28',
    'description': 'Waveglow library',
    'long_description': '# Waveglow library\n\nThis Waveglow library was changed to be used with vait library.\n\n\n## Instalation\n\n### 1) Install waveglow library\n\n(This will also install tacotron2 library)\n\n```shell\npip install waveglow==22.12.28\n```\n\n\n### 2) Install CUDA 11.3 or 11.6\n\n```shell\npip install -r requirements-cuda-11.3.txt\n# or\npip install -r requirements-cuda-11.6.txt\n```\n\n\n### 3) Install apex\n```shell\ngit clone https://github.com/NVIDIA/apex /home/${USER}/apex\ncd /home/${USER}/apex\npip install -v --disable-pip-version-check --no-cache-dir ./\ncd -\n```\n\n\n### 4) Download published model files\n\n```shell\nwget https://drive.google.com/open?id=1rpK8CzAAirq9sWZhe9nlfvxMF1dRgFbF\n```\n\n\n### 5) Download mel-spectrograms\n\n```shell\nwget https://drive.google.com/file/d/1g_VXK2lpP9J25dQFhQwx7doWl_p20fXA/view?usp=sharing\n```\n\n\n## Usage: Creating audio\n\n```shell\nwaveglow-inference -f <(ls mel_spectrograms/*.pt) -w waveglow_256channels_universal_v5.pt -o . --is_fp16 -s 0.6\n```\n\n\n## Usage: Training\n\n```shell\nmkdir checkpoints\nwaveglow-train -c config.json\n```\n',
    'author': 'Tadeusz Miszczyk',
    'author_email': '42252259+8tm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/8tm/waveglow',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
