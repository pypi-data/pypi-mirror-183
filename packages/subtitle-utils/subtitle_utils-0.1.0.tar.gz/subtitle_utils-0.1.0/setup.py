# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['subtitle_utils']

package_data = \
{'': ['*']}

install_requires = \
['chardet>=5.1.0,<6.0.0',
 'loguru>=0.6.0,<0.7.0',
 'pathlib>=1.0.1,<2.0.0',
 'pyasstosrt>=1.3.1,<2.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pysrt>=1.1.2,<2.0.0',
 'pyvtt>=0.0.4,<0.0.5']

setup_kwargs = {
    'name': 'subtitle-utils',
    'version': '0.1.0',
    'description': 'Subtilte Conversion utils - ass2srt vtt2bcc srt2bcc ass2bcc and more',
    'long_description': '# subtitle_utils\n\n![cover](https://raw.githubusercontent.com/KimmyXYC/Subtitle-Conversion-TGBot/main/Data/cover.jpg)\n\n<p align="center">\n  <img src="https://img.shields.io/badge/Python-3.7|8|9|10-green" alt="Python" >\n</p>\n\nSubtilte Conversion utils - ass2srt vtt2bcc srt2bcc ass2bcc and more\n\n`pip install -U subtitle_utils`\n',
    'author': 'sudoskys',
    'author_email': 'coldlando@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sudoskys/subtitle_utils',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
