# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['traffic',
 'traffic.algorithms',
 'traffic.algorithms.onnx',
 'traffic.algorithms.onnx.holding_pattern',
 'traffic.console',
 'traffic.core',
 'traffic.data',
 'traffic.data.adsb',
 'traffic.data.basic',
 'traffic.data.datasets',
 'traffic.data.eurocontrol',
 'traffic.data.eurocontrol.aixm',
 'traffic.data.eurocontrol.b2b',
 'traffic.data.eurocontrol.b2b.xml',
 'traffic.data.eurocontrol.ddr',
 'traffic.data.faa',
 'traffic.data.samples',
 'traffic.data.samples.ambulances',
 'traffic.data.samples.calibration',
 'traffic.data.samples.collections',
 'traffic.data.samples.featured',
 'traffic.data.samples.firefighting',
 'traffic.data.samples.gliders',
 'traffic.data.samples.military',
 'traffic.data.samples.onground',
 'traffic.data.samples.performance',
 'traffic.data.samples.surveillance',
 'traffic.data.samples.surveys',
 'traffic.data.samples.tv_relay',
 'traffic.data.weather',
 'traffic.drawing',
 'traffic.plugins']

package_data = \
{'': ['*'], 'traffic.data.samples': ['airspaces/*']}

install_requires = \
['cartes>=0.7.4',
 'click>=8.1',
 'fastparquet>=0.7',
 'ipyleaflet>=0.17',
 'ipywidgets>=7.6',
 'metar>=1.8',
 'openap>=1.1',
 'paramiko>=2.7',
 'pyModeS>=2.14,<3.0',
 'pyOpenSSL>=22.0',
 'requests-pkcs12>=1.10',
 'requests>=2.27',
 'typing-extensions>=4.2']

extras_require = \
{':python_version < "3.11"': ['onnxruntime>=1.12'],
 'full': ['xarray>=0.18.2',
          'libarchive>=0.4.7,<1.0.0',
          'scikit-learn>=1.0',
          'textual>=0.1.17',
          'pyspark>=3.3.0'],
 'sdr': ['pyrtlsdr>=0.2.93,<0.3.0'],
 'web': ['textual>=0.1.17',
         'Flask>=2.1.1',
         'Flask-Cors>=3.0.10',
         'waitress>=2.1.1']}

entry_points = \
{'console_scripts': ['traffic = traffic.console:main'],
 'traffic.plugins': ['Bluesky = traffic.plugins.bluesky',
                     'CesiumJS = traffic.plugins.cesiumjs']}

setup_kwargs = {
    'name': 'traffic',
    'version': '2.8.1',
    'description': 'A toolbox for manipulating and analysing air traffic data',
    'long_description': "![A toolbox for processing and analysing air traffic data](./docs/_static/logo/logo_full.png)\n\n[![Documentation Status](https://github.com/xoolive/traffic/workflows/docs/badge.svg)](https://traffic-viz.github.io/) [![tests](https://github.com/xoolive/traffic/actions/workflows/run-tests.yml/badge.svg?branch=master&event=push)](https://github.com/xoolive/traffic/actions/workflows/run-tests.yml) [![Code Coverage](https://img.shields.io/codecov/c/github/xoolive/traffic.svg)](https://codecov.io/gh/xoolive/traffic) [![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](https://mypy.readthedocs.io/) [![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black) ![License](https://img.shields.io/pypi/l/traffic.svg)  \n[![Join the chat at https://gitter.im/xoolive/traffic](https://badges.gitter.im/xoolive/traffic.svg)](https://gitter.im/xoolive/traffic?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) ![PyPI version](https://img.shields.io/pypi/v/traffic) [![PyPI downloads](https://img.shields.io/pypi/dm/traffic)](https://pypi.org/project/traffic) ![Conda version](https://img.shields.io/conda/vn/conda-forge/traffic) [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/traffic.svg)](https://anaconda.org/conda-forge/traffic)  \n[![JOSS paper](http://joss.theoj.org/papers/10.21105/joss.01518/status.svg)](https://doi.org/10.21105/joss.01518) [![Google Scholar\nbadge](https://img.shields.io/endpoint?url=https%3A%2F%2Ftraffic-citations-y6ukblh4ymtb.runkit.sh)](https://scholar.google.com/scholar?cites=18420568209924139259&scisbd=1)\n\nThe traffic library helps to work with common sources of air traffic data.\n\nIts main purpose is to provide data analysis methods commonly applied to trajectories and airspaces. When a specific function is not provided, the access to the underlying structure is direct, through an attribute pointing to a pandas dataframe.\n\nThe library also offers facilities to parse and/or access traffic data from open sources of ADS-B traffic like the [OpenSky Network](https://opensky-network.org/) or Eurocontrol DDR files. It is designed to be easily extendable to other sources of data.\n\nStatic visualization (images) exports are accessible via Matplotlib/Cartopy. More dynamic visualization frameworks are easily accessible in Jupyter environments with [ipyleaflet](http://ipyleaflet.readthedocs.io/) and [altair](http://altair-viz.github.io/); or through exports to other formats, including CesiumJS or Google Earth.\n\n## Installation\n\n**Full installation instructions are to be found in the [documentation](https://traffic-viz.github.io/installation.html).**\n\n- If you are not familiar/comfortable with your Python environment, please install the latest `traffic` release in a new, fresh conda environment.\n\n  ```sh\n  conda create -n traffic -c conda-forge python=3.10 traffic\n  ```\n\n- Adjust the Python version you need (>=3.8) and append packages you need for working efficiently, such as Jupyter Lab, xarray, PyTorch or more.\n- Then activate the environment every time you need to use the `traffic` library:\n\n  ```sh\n  conda activate traffic\n  ```\n\n**Warning!** Dependency resolution may be tricky, esp. if you use an old conda environment where you overwrote `conda` libraries with `pip` installs. **Please only report installation issues in new, fresh conda environments.**\n\nIf conda fails to resolve an environment in a reasonable time, consider using a [Docker image](https://traffic-viz.github.io/user_guide/docker.html) with a working installation.\n\nFor troubleshooting, refer to the appropriate [documentation section](https://traffic-viz.github.io/troubleshooting/installation.html).\n\n## Credits\n\n[![JOSS\nbadge](http://joss.theoj.org/papers/10.21105/joss.01518/status.svg)](https://doi.org/10.21105/joss.01518) [![Google Scholar\nbadge](https://img.shields.io/endpoint?url=https%3A%2F%2Ftraffic-citations-y6ukblh4ymtb.runkit.sh)](https://scholar.google.com/scholar?cites=18420568209924139259&scisbd=1)\n\n- Like other researchers before, if you find this project useful for your research and use it in an academic work, you may cite it as:\n\n  ```bibtex\n  @article{olive2019traffic,\n      author={Xavier {Olive}},\n      journal={Journal of Open Source Software},\n      title={traffic, a toolbox for processing and analysing air traffic data},\n      year={2019},\n      volume={4},\n      pages={1518},\n      doi={10.21105/joss.01518},\n      issn={2475-9066},\n  }\n  ```\n\n- Additionally, you may consider adding a star to the repository. This token of appreciation is often interpreted as positive feedback and improves the visibility of the library.\n\n## Documentation\n\n[![Documentation Status](https://github.com/xoolive/traffic/workflows/docs/badge.svg)](https://traffic-viz.github.io/) [![Join the chat at https://gitter.im/xoolive/traffic](https://badges.gitter.im/xoolive/traffic.svg)](https://gitter.im/xoolive/traffic?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n\nDocumentation available at <https://traffic-viz.github.io/>  \nJoin the Gitter chat for assistance: https://gitter.im/xoolive/traffic\n\n## Tests and code quality\n\n[![tests](https://github.com/xoolive/traffic/actions/workflows/run-tests.yml/badge.svg?branch=master&event=push)](https://github.com/xoolive/traffic/actions/workflows/run-tests.yml) [![Code Coverage](https://img.shields.io/codecov/c/github/xoolive/traffic.svg)](https://codecov.io/gh/xoolive/traffic) [![Codacy Badge](https://img.shields.io/codacy/grade/eea673ed15304f1b93490726295d6de0)](https://www.codacy.com/manual/xoolive/traffic) [![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](https://mypy.readthedocs.io/)\n\nUnit and non-regression tests are written in the `tests/` directory. You may run `pytest` from the root directory.\n\nTests are checked on [Github Actions](https://github.com/xoolive/traffic/actions/workflows/run-tests.yml) platform upon each commit. Latest status and coverage are displayed with standard badges hereabove.\n\nIn addition to unit tests, code is checked against:\n\n- formatting with [black](https://black.readthedocs.io/), [isort](https://pycqa.github.io/isort/) and [flake8](https://flake8.pycqa.org/);\n- static typing with [mypy](https://mypy.readthedocs.io/)\n\n[pre-commit](https://pre-commit.com/) hooks are available in the repository.\n\n## Feedback and contribution\n\nAny input, feedback, bug report or contribution is welcome.\n\n- Should you encounter any [issue](https://github.com/xoolive/traffic/issues/new), you may want to file it in the [issue](https://github.com/xoolive/traffic/issues/new) section of this repository.\n- If you intend to [contribute to traffic](https://traffic-viz.github.io/installation.html#contribute-to-traffic) or file a pull request, the best way to ensure continuous integration does not break is to reproduce an environment with the same exact versions of all dependency libraries. Please follow the [appropriate section](https://traffic-viz.github.io/installation.html#contribute-to-traffic) in the documentation.\n\n  Let us know what you want to do just in case we're already working on an implementation of something similar. This way we can avoid any needless duplication of effort. Also, please don't forget to add tests for any new functions.\n",
    'author': 'Xavier Olive',
    'author_email': 'git@xoolive.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xoolive/traffic/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
