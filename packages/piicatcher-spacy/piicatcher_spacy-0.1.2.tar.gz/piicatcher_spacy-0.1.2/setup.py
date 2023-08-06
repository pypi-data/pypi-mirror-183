# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['piicatcher_spacy', 'piicatcher_spacy.detectors']

package_data = \
{'': ['*']}

install_requires = \
['piicatcher>=0.20.2,<0.21.0', 'spacy>=3.4.4,<4.0.0']

entry_points = \
{'piicatcher_detectors': ['spacy = piicatcher_spacy.detectors:SpacyDetector']}

setup_kwargs = {
    'name': 'piicatcher-spacy',
    'version': '0.1.2',
    'description': 'PIICatcher plugin that uses spacy to detect PII',
    'long_description': '# piicatcher_spacy\nPIICatcher plugin that uses spacy to detect PII\n',
    'author': 'Tokern',
    'author_email': 'piicatcher@tokern.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://tokern.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<=3.10.8',
}


setup(**setup_kwargs)
