# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eudata_server', 'eudata_server.backend.sdmx', 'eudata_server.tools']

package_data = \
{'': ['*'],
 'eudata_server': ['assets/css/*',
                   'assets/css/tippy/*',
                   'assets/js/*',
                   'assets/js/ag-grid/*',
                   'assets/political-compass/json/*',
                   'assets/sass/*',
                   'assets/sass/ag-theme-alpine-dark/sass/*',
                   'assets/sass/ag-theme-alpine/icons/*',
                   'assets/sass/ag-theme-alpine/sass/*',
                   'assets/sass/ag-theme-balham-dark/sass/*',
                   'assets/sass/ag-theme-balham-dark/sass/legacy/*',
                   'assets/sass/ag-theme-balham/icons/*',
                   'assets/sass/ag-theme-balham/sass/*',
                   'assets/sass/ag-theme-balham/sass/legacy/*',
                   'assets/sass/ag-theme-base/icons/*',
                   'assets/sass/ag-theme-base/sass/*',
                   'assets/sass/ag-theme-base/sass/legacy/*',
                   'assets/sass/ag-theme-base/sass/parts/*',
                   'assets/sass/ag-theme-blue/sass/*',
                   'assets/sass/ag-theme-blue/sass/legacy/*',
                   'assets/sass/ag-theme-bootstrap/sass/*',
                   'assets/sass/ag-theme-bootstrap/sass/legacy/*',
                   'assets/sass/ag-theme-classic/sass/*',
                   'assets/sass/ag-theme-dark/sass/*',
                   'assets/sass/ag-theme-dark/sass/legacy/*',
                   'assets/sass/ag-theme-fresh/sass/*',
                   'assets/sass/ag-theme-fresh/sass/legacy/*',
                   'assets/sass/ag-theme-material/icons/*',
                   'assets/sass/ag-theme-material/sass/*',
                   'assets/sass/ag-theme-material/sass/legacy/*',
                   'assets/sass/mixins/*',
                   'assets/sass/structural/*',
                   'assets/sass/webfont/*',
                   'assets/static/data/*',
                   'assets/static/images/*',
                   'assets/templates/*']}

install_requires = \
['fastapi[all]>=0.88.0,<0.89.0',
 'pandas>=1.5.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['rhttps = eudata_server.tools.https:cli',
                     'server = eudata_server.server:cli',
                     'srv = eudata_server.server:cli']}

setup_kwargs = {
    'name': 'eudata-server',
    'version': '0.1.23',
    'description': '',
    'long_description': "# Arno's super duper API\n\nThis is a super duper API that does super duper things.\n\n## Installation\n\nJust use pip if you're a regular user:\n\n```bash\npip install eudata-server\n```\n\nIf you want to develop, clone the repo and install the requirements\n\n### Sass\n\n[Sass](https://sass-lang.com/) is used to compile the CSS.\n\nIf you're on Windows I recommend using [Scoop](https://scoop.sh/):\n\n```powershell\nscoop install sass\n```\n\nIf you're on Linux, you can use the [homebrew package manager](brew.sh):\n\n```bash\nbrew install sass/sass/sass\n```\n\nA failsafe way to install Dart-Sass is to download the latest release as a zip/tar archive from [here](https://github.com/sass/dart-sass/releases/tag/1.57.1) and add it to your PATH.\n\n## Customization\n\n### Sass Customization\n\nThe Sass files are located in `eudata_server/static/sass`. For now the only file to compile is the grid theme file, `grid-theme.scss`.  \nTo compile it, run:\n\n```bash\nsass -w ./eudata_server/assets/sass/grid-theme.scss ./eudata_server/assets/css/grid-theme.css\n```\n\nOr if you're on Windows:\n\n```powershell\nsass -w .\\eudata_server\\assets\\sass\\grid-theme.scss .\\eudata_server\\assets\\css\\grid-theme.css\n```\n",
    'author': 'arnos-stuff',
    'author_email': 'bcda0276@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
