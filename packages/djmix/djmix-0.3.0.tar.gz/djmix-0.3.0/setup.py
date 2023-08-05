# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djmix',
 'djmix.models',
 'djmix.tools',
 'djmix.tools.alignment',
 'djmix.tools.cvxopt',
 'djmix.tools.cvxopt.optimizers',
 'djmix.tools.eq',
 'djmix.tools.features']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'yt-dlp']

extras_require = \
{'tools': ['librosa>=0.9.2,<0.10.0',
           'madmom>=0.16.1,<0.17.0',
           'joblib>=1.2.0,<2.0.0',
           'scikit-image>=0.19.3,<0.20.0',
           'pandas>=1.5.2,<2.0.0',
           'pytsmod>=0.3.6,<0.4.0',
           'pydub>=0.25.1,<0.26.0',
           'cvxpy>=1.2.2,<2.0.0',
           'matplotlib>=3.6.2,<4.0.0']}

setup_kwargs = {
    'name': 'djmix',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Taejun Kim',
    'author_email': 'taejun@kaist.ac.kr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
