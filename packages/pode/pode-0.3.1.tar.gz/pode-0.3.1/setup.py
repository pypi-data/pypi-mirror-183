# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pode']

package_data = \
{'': ['*']}

install_requires = \
['gon>=5.0.0,<6.0.0',
 'ground>=8.1.0,<9.0.0',
 'networkx>=2.8.8,<3.0.0',
 'sect>=6.1.0,<7.0.0']

setup_kwargs = {
    'name': 'pode',
    'version': '0.3.1',
    'description': 'Implementation of an algorithm for a polygon decomposition by Hert, S. and Lumelsky, V., 1998',
    'long_description': 'pode\n===========\n\n\n[![](https://travis-ci.org/LostFan123/pode.svg?branch=master)](https://travis-ci.org/LostFan123/pode "Travis CI")\n[![](https://dev.azure.com/skorobogatov/pode/_apis/build/status/LostFan123.pode?branchName=master)](https://dev.azure.com/skorobogatov/pode/_build/latest?definitionId=2&branchName=master "Azure Pipelines")\n[![](https://codecov.io/gh/LostFan123/pode/branch/master/graph/badge.svg)](https://codecov.io/gh/LostFan123/pode "Codecov")\n[![](https://img.shields.io/github/license/LostFan123/pode.svg)](https://github.com/LostFan123/pode/blob/master/LICENSE "License")\n[![](https://badge.fury.io/py/pode.svg)](https://badge.fury.io/py/pode "PyPI")\n\nSummary\n-------\n\n`pode` is a Python library that implements an algorithm of \n[Hert, S. and Lumelsky, V., 1998](https://www.worldscientific.com/doi/abs/10.1142/S0218195998000230)\nfor a polygon decomposition into separate parts depending on the area \nrequirements.\n\nMain features are\n- all calculations are robust for floating point numbers\n& precise for integral numbers (like `int`)\n- support for partition of convex/nonconvex polygons with/without holes\n- support for anchored partition, free partition, and a mixture of both \nwhere anchored polygon partition requires the resulting polygon parts to \ncontain specified points called "anchors" or "sites", and free partition does \nnot have any constraints on the resulting geometries. \n- most of the code is covered with property-based tests.\n---\n\nIn what follows\n- `python` is an alias for `python3.8` or any later\nversion (`python3.9` and so on).\n\nInstallation\n------------\n\nInstall the latest `pip` & `setuptools` packages versions:\n  ```bash\n  python -m pip install --upgrade pip setuptools\n  ```\n\n### User\n\nDownload and install the latest stable version from `PyPI` repository:\n  ```bash\n  python -m pip install --upgrade pode\n  ```\n\n### Developer\n\nDownload the latest version from `GitHub` repository\n```bash\ngit clone https://github.com/LostFan123/pode.git\ncd pode\n```\n\nInstall dependencies:\n  ```bash\n  poetry install\n  ```\n\nUsage\n-----\n```python\n>>> from pode import divide, Contour, Point, Polygon, Requirement\n>>> contour = Contour([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])\n>>> polygon = Polygon(contour)\n>>> requirements = [Requirement(0.5), Requirement(0.5, point=Point(1, 1))]\n>>> parts = divide(polygon, requirements)\nassert parts[0].area == parts[1].area < polygon.area\nassert Point(1, 1) in parts[1]\n```\nCurrently, the algorithm uses constrained Delaunay triangulation to form convex \nparts which are used internally for a convex-polygon partition.\nThis triangulation, however, affects the resulting partition. The resulting \nparts can have zigzag pattern separating different parts. In this way, the \nsolution can be far from being optimal in sense of the number of sides of the\nresulting polygons. Alternatively, we implemented a helper function that would \njoin neighboring triangles if they form a larger convex part. It can be \nimported as `from pode import joined_constrained_delaunay_triangles` and used\nas `divide(polygon, requirements, joined_constrained_delaunay_triangles)`. But, \nin the future, a better algorithm should be implemented, like \n[Greene, D.H., 1983](https://www.goodreads.com/book/show/477772.Advances_in_Computing_Research_Volume_1) \nor [Chazelle, B. and Dobkin, D., 1979](https://dl.acm.org/doi/abs/10.1145/800135.804396).\n\n\nDevelopment\n-----------\n\n### Bumping version\n\n#### Preparation\n\nInstall\n[bump2version](https://github.com/c4urself/bump2version#installation).\n\n#### Pre-release\n\nChoose which version number category to bump following [semver\nspecification](http://semver.org/).\n\nTest bumping version\n```bash\nbump2version --dry-run --verbose $CATEGORY\n```\n\nwhere `$CATEGORY` is the target version number category name, possible\nvalues are `patch`/`minor`/`major`.\n\nBump version\n```bash\nbump2version --verbose $CATEGORY\n```\n\nThis will set version to `major.minor.patch-alpha`. \n\n#### Release\n\nTest bumping version\n```bash\nbump2version --dry-run --verbose release\n```\n\nBump version\n```bash\nbump2version --verbose release\n```\n\nThis will set version to `major.minor.patch`.\n\n#### Notes\n\nTo avoid inconsistency between branches and pull requests,\nbumping version should be merged into `master` branch \nas separate pull request.\n\n### Running tests\n\nPlain:\n  ```bash\n  pytest\n  ```\n\nInside `Docker` container:\n  ```bash\n  docker-compose --file docker-compose.cpython.yml up\n  ```\n\n`Bash` script (e.g. can be used in `Git` hooks):\n  ```bash\n  ./run-tests.sh\n  ```\n  or\n  ```bash\n  ./run-tests.sh cpython\n  ```\n\n`PowerShell` script (e.g. can be used in `Git` hooks):\n  ```powershell\n  .\\run-tests.ps1\n  ```\n  or\n  ```powershell\n  .\\run-tests.ps1 cpython\n  ```\n',
    'author': 'GeorgySk',
    'author_email': 'skorobogatovgeorgy@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
