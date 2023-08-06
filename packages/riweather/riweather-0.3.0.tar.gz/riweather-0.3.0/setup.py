# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['riweather', 'riweather.db']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pyproj>=3.4.1,<4.0.0',
 'pyshp>=2.3.1,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'shapely>=2.0.0,<3.0.0',
 'sqlalchemy>=1.4.45,<2.0.0']

extras_require = \
{'plots': ['matplotlib>=3.6.2,<4.0.0', 'folium>=0.14.0,<0.15.0']}

entry_points = \
{'console_scripts': ['riweather = riweather.cli:main']}

setup_kwargs = {
    'name': 'riweather',
    'version': '0.3.0',
    'description': 'Grab publicly available weather data',
    'long_description': '# riweather\n\n[![Tests](https://github.com/ensley-nexant/riweather/workflows/Tests/badge.svg)](https://github.com/ensley-nexant/riweather/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/ensley-nexant/riweather/branch/main/graph/badge.svg)](https://codecov.io/gh/ensley-nexant/riweather)\n[![Release](https://github.com/ensley-nexant/riweather/actions/workflows/release.yml/badge.svg)](https://github.com/ensley-nexant/riweather/actions/workflows/release.yml)\n\nGrab publicly available weather data\n',
    'author': 'John Ensley',
    'author_email': 'jensley@resource-innovations.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ensley-nexant/riweather',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
