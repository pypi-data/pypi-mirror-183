# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['earsegmentationai']

package_data = \
{'': ['*'], 'earsegmentationai': ['model_ear/*']}

install_requires = \
['albumentations>=1.3.0,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'imgviz>=1.6.2,<2.0.0',
 'numpy==1.24.1',
 'opencv-python==4.6.0.66',
 'pillow==9.3.0',
 'poethepoet>=0.17.1,<0.18.0',
 'requests>=2.28.1,<3.0.0',
 'segmentation-models-pytorch>=0.3.1,<0.4.0',
 'torch>=1.13.1,<2.0.0',
 'torchvision>=0.14.1,<0.15.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['obserware = earsegmentationai.main:main']}

setup_kwargs = {
    'name': 'earsegmentationai',
    'version': '1.0.0',
    'description': 'Pytorch based Ear Detection in picture and camera',
    'long_description': '# Efficient and Lightweight Ear Segmentation\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/umitkacar/Ear-segmentation-ai/main.svg)](https://results.pre-commit.ci/latest/github/umitkacar/Ear-segmentation-ai/main)\n<p>\n  <img alt="Python38" src="https://img.shields.io/badge/Python-3.8-3776AB.svg?logo=Python&logoColor=white"/>\n  <img alt="Python39" src="https://img.shields.io/badge/Python-3.9-3776AB.svg?logo=Python&logoColor=white"/>\n  <img alt="Python310" src="https://img.shields.io/badge/Python-3.10-3776AB.svg?logo=Python&logoColor=white"/>\n  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-v1.13.1-EE4C2C.svg?logo=PyTorch&logoColor=white"/>\n  <img alt="Torchvision" src="https://img.shields.io/badge/Torchvision-v0.14.1-EE4C2C.svg?logo=PyTorch&logoColor=white"/>\n  <img alt="Cuda" src="https://img.shields.io/badge/Cuda-Enabled-76B900.svg?logo=Nvidia&logoColor=white"/>\n  <img alt="Poetry" src="https://img.shields.io/badge/Poetry-60A5FA.svg?logo=Poetry&logoColor=white"/>\n  <img alt="Black" src="https://img.shields.io/badge/code%20style-black-black"/>\n  <img alt="Mypy" src="https://img.shields.io/badge/mypy-checked-blue"/>\n  <img alt="isort" src="https://img.shields.io/badge/isort-checked-yellow"/>\n</p>\n\n## Download Model 📂\n\n<p>\n<a href="https://drive.google.com/drive/folders/1l88PrrNESBDZ4Jd3QJSG9EbIe0CjXC_j?usp=sharing"><img alt="GoogleDrive" src="https://img.shields.io/badge/GoogleDrive-4285F4?logo=GoogleDrive&logoColor=white"></a>\n<a href="https://github.com/umitkacar/Ear-segmentation-ai/releases/download/v1.0.0/earsegmentation_model_v1_46.pth"><img alt="Github" src="https://img.shields.io/badge/Github Download-181717?logo=Github&logoColor=white"></a>\n</p>\n\n## ⚙️ Requirements ⚙️\n\n* Python 3.8 to Python3.10 (Virtualenv recommended)\n* Display Server for showing results\n* Optional: poetry\n* Optional: Nvidia CUDA for cuda usage\n\n## 🛠️ Installation 🛠️\n\n### Pip installation\n\n```bash\npip install -r requirements.txt\n```\n\n### Poetry installation\n\n```bash\npoetry shell\npoetry install\n```\n\n## Optional (If you have multiple python installation)\n\n```bash\npoetry env use $(which python3.10)\npoetry shell\npoetry install\n```\n\n## Usage\n\n```\nusage: earsegmentationai_cli.py [-h] -m {c,p} [-d [{cpu,cuda}]] [-fp FOLDERPATH] [-id [DEVICEID]]\n\noptions:\n  -h, --help            show this help message and exit\n  -m {c,p}, --mode {c,p}\n                        Select camera or picture mode\n  -d [{cpu,cuda}], --device [{cpu,cuda}]\n                        Run in gpu or cpu mode\n  -fp FOLDERPATH, --folderpath FOLDERPATH\n                        Folder path for image(s) for image mode only\n  -id [DEVICEID], --deviceId [DEVICEID]\n                        Camera deviceId /dev/videoX for camera mode only\n```\n\n## Webcam Mode 📷\n\n```bash\npython earsegmentationai_cli.py --mode c --device cpu\npython earsegmentationai_cli.py --mode c --device cuda\npython earsegmentationai_cli.py --mode c --deviceId 1 --device cuda\n```\n\n## Image Mode 🖼️\n\n```bash\npython earsegmentationai_cli.py --mode p --fp /path/xxx/\n```\n\n## Youtube Video 📸 ✨\n\n<p>\n<a href="https://www.youtube.com/watch?v=5Puxj7Q0EEo"><img alt="Youtube" src="https://img.shields.io/badge/Youtube-FF0000?logo=Youtube&logoColor=white"></a>\n</p>\n',
    'author': 'Umit KACAR',
    'author_email': 'umitkacar.phd@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/umitkacar/Ear-segmentation-ai',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
