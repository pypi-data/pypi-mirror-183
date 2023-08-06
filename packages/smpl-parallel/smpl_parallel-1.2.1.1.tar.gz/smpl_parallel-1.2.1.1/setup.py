# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smpl_parallel']

package_data = \
{'': ['*']}

install_requires = \
['smpl_doc']

setup_kwargs = {
    'name': 'smpl-parallel',
    'version': '1.2.1.1',
    'description': 'SiMPLe plotting and fitting',
    'long_description': '# smpl_parallel\nSimplified utilities in python.\n\n[![PyPI version][pypi image]][pypi link] [![PyPI version][pypi versions]][pypi link]  ![downloads](https://img.shields.io/pypi/dm/smpl_parallel.svg)\n\n [![test][a t image]][a t link]   [![Coverage Status][c t i]][c t l]  [![Codacy Badge][cc c i]][cc c l]   [![Codacy Badge][cc q i]][cc q l]  [![Documentation][rtd t i]][rtd t l]\n\n## Documentation\n\n-   <https://smpl_parallel.readthedocs.io/en/stable/>\n-   <https://apn-pucky.github.io/smpl_parallel/index.html>\n\n## Versions\n\n### Stable\n\n```sh\npip install smpl_parallel\n```\n\nOptional: --user or --upgrade\n\n### Dev\n\n```sh\npip install --index-url https://test.pypi.org/simple/ smpl_parallel\n```\n\n[doc stable]: https://apn-pucky.github.io/smpl_parallel/index.html\n[doc test]: https://apn-pucky.github.io/smpl_parallel/test/index.html\n\n[pypi image]: https://badge.fury.io/py/smpl_parallel.svg\n[pypi link]: https://pypi.org/project/smpl_parallel/\n[pypi versions]: https://img.shields.io/pypi/pyversions/smpl_parallel.svg\n\n[a s image]: https://github.com/APN-Pucky/smpl_parallel/actions/workflows/stable.yml/badge.svg\n[a s link]: https://github.com/APN-Pucky/smpl_parallel/actions/workflows/stable.yml\n[a t link]: https://github.com/APN-Pucky/smpl_parallel/actions/workflows/test.yml\n[a t image]: https://github.com/APN-Pucky/smpl_parallel/actions/workflows/test.yml/badge.svg\n\n[cc s q i]: https://app.codacy.com/project/badge/Grade/38630d0063814027bd4d0ffaa73790a2?branch=stable\n[cc s q l]: https://www.codacy.com/gh/APN-Pucky/smpl_parallel/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/smpl&amp;utm_campaign=Badge_Grade?branch=stable\n[cc s c i]: https://app.codacy.com/project/badge/Coverage/38630d0063814027bd4d0ffaa73790a2?branch=stable\n[cc s c l]: https://www.codacy.com/gh/APN-Pucky/smpl_parallel/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/smpl&utm_campaign=Badge_Coverage?branch=stable\n\n[cc q i]: https://app.codacy.com/project/badge/Grade/38630d0063814027bd4d0ffaa73790a2\n[cc q l]: https://www.codacy.com/gh/APN-Pucky/smpl_parallel/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=APN-Pucky/smpl&amp;utm_campaign=Badge_Grade\n[cc c i]: https://app.codacy.com/project/badge/Coverage/38630d0063814027bd4d0ffaa73790a2\n[cc c l]: https://www.codacy.com/gh/APN-Pucky/smpl_parallel/dashboard?utm_source=github.com&utm_medium=referral&utm_content=APN-Pucky/smpl&utm_campaign=Badge_Coverage\n\n[c s i]: https://coveralls.io/repos/github/APN-Pucky/smpl_parallel/badge.svg?branch=stable\n[c s l]: https://coveralls.io/github/APN-Pucky/smpl_parallel?branch=stable\n[c t l]: https://coveralls.io/github/APN-Pucky/smpl_parallel?branch=master\n[c t i]: https://coveralls.io/repos/github/APN-Pucky/smpl_parallel/badge.svg?branch=master\n\n[rtd s i]: https://readthedocs.org/projects/smpl_parallel/badge/?version=stable\n[rtd s l]: https://smpl_parallel.readthedocs.io/en/stable/?badge=stable\n[rtd t i]: https://readthedocs.org/projects/smpl_parallel/badge/?version=latest\n[rtd t l]: https://smpl_parallel.readthedocs.io/en/latest/?badge=latest\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/smpl_parallel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
