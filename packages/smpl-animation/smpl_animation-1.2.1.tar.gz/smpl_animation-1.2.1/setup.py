# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smpl_animation']

package_data = \
{'': ['*']}

install_requires = \
['ipywidgets', 'matplotlib', 'numpy', 'pillow']

setup_kwargs = {
    'name': 'smpl-animation',
    'version': '1.2.1',
    'description': 'SiMPLe plotting and fitting',
    'long_description': '# smpl_animation\nSimplified utilities in python.\n\n[![PyPI version][pypi image]][pypi link] [![PyPI version][pypi versions]][pypi link]  ![downloads](https://img.shields.io/pypi/dm/smpl_animation.svg)\n\n| [Stable][doc stable]        | [Test][doc test]           |\n| ------------- |:-------------:|\n| [![workflow][a s image]][a s link]   | [![test][a t image]][a t link]     |\n| [![Coverage Status][c s i]][c s l]   | [![Coverage Status][c t i]][c t l] |\n| [![Codacy Badge][cc s c i]][cc s c l] | [![Codacy Badge][cc c i]][cc c l]  |\n| [![Codacy Badge][cc s q i]][cc s q l] | [![Codacy Badge][cc q i]][cc q l]  |\n| [![Documentation][rtd s i]][rtd s l] | [![Documentation][rtd t i]][rtd t l]|\n\n## Documentation\n\n-   <https://smpl_animation.readthedocs.io/en/stable/>\n-   <https://apn-pucky.github.io/smpl_animation/index.html>\n\n## Versions\n\n### Stable\n\n```sh\npip install smpl_animation\n```\n\nOptional: --user or --upgrade\n\n### Dev\n\n```sh\npip install --index-url https://test.pypi.org/simple/ smpl_animation\n```\n\n[doc stable]: https://apn-pucky.github.io/smpl_animation/index.html\n[doc test]: https://apn-pucky.github.io/smpl_animation/test/index.html\n\n[pypi image]: https://badge.fury.io/py/smpl_animation.svg\n[pypi link]: https://pypi.org/project/smpl_animation/\n[pypi versions]: https://img.shields.io/pypi/pyversions/smpl_animation.svg\n\n[a s image]: https://github.com/APN-Pucky/smpl_animation/actions/workflows/stable.yml/badge.svg\n[a s link]: https://github.com/APN-Pucky/smpl_animation/actions/workflows/stable.yml\n[a t link]: https://github.com/APN-Pucky/smpl_animation/actions/workflows/test.yml\n[a t image]: https://github.com/APN-Pucky/smpl_animation/actions/workflows/test.yml/badge.svg\n\n[cc s q i]: https://app.codacy.com/project/badge/Grade/38630d0063814027bd4d0ffaa73790a2?branch=stable\n[cc s q l]: https://www.codacy.com/gh/APN-Pucky/smpl_animation/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/smpl&amp;utm_campaign=Badge_Grade?branch=stable\n[cc s c i]: https://app.codacy.com/project/badge/Coverage/38630d0063814027bd4d0ffaa73790a2?branch=stable\n[cc s c l]: https://www.codacy.com/gh/APN-Pucky/smpl_animation/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/smpl&utm_campaign=Badge_Coverage?branch=stable\n\n[cc q i]: https://app.codacy.com/project/badge/Grade/38630d0063814027bd4d0ffaa73790a2\n[cc q l]: https://www.codacy.com/gh/APN-Pucky/smpl_animation/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/smpl&amp;utm_campaign=Badge_Grade\n[cc c i]: https://app.codacy.com/project/badge/Coverage/38630d0063814027bd4d0ffaa73790a2\n[cc c l]: https://www.codacy.com/gh/APN-Pucky/smpl_animation/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/smpl&utm_campaign=Badge_Coverage\n\n[c s i]: https://coveralls.io/repos/github/APN-Pucky/smpl_animation/badge.svg?branch=stable\n[c s l]: https://coveralls.io/github/APN-Pucky/smpl_animation?branch=stable\n[c t l]: https://coveralls.io/github/APN-Pucky/smpl_animation?branch=master\n[c t i]: https://coveralls.io/repos/github/APN-Pucky/smpl_animation/badge.svg?branch=master\n\n[rtd s i]: https://readthedocs.org/projects/smpl_animation/badge/?version=stable\n[rtd s l]: https://smpl_animation.readthedocs.io/en/stable/?badge=stable\n[rtd t i]: https://readthedocs.org/projects/smpl_animation/badge/?version=latest\n[rtd t l]: https://smpl_animation.readthedocs.io/en/latest/?badge=latest\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/smpl_animation',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
