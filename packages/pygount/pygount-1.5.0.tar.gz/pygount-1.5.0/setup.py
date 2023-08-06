# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pygount']

package_data = \
{'': ['*']}

install_requires = \
['chardet>=5,<6', 'pygments>=2,<3', 'rich>=9,<13']

entry_points = \
{'console_scripts': ['pygount = pygount.command:main']}

setup_kwargs = {
    'name': 'pygount',
    'version': '1.5.0',
    'description': 'count source lines of code (SLOC) using pygments',
    'long_description': "[![PyPI](https://img.shields.io/pypi/v/pygount)](https://pypi.org/project/pygount/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/pygount.svg)](https://www.python.org/downloads/)\n[![Build Status](https://github.com/roskakori/pygount/actions/workflows/build.yml/badge.svg)](https://github.com/roskakori/pygount/actions/workflows/build.yml)\n[![Test Coverage](https://img.shields.io/coveralls/github/roskakori/pygount)](https://coveralls.io/r/roskakori/pygount?branch=master)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License](https://img.shields.io/github/license/roskakori/pygount)](https://opensource.org/licenses/BSD-3-Clause)\n\n# pygount\n\nPygount is a command line tool to scan folders for source code files and\ncount the number of source code lines in it. It is similar to tools like\n[sloccount](https://www.dwheeler.com/sloccount/) and\n[cloc](https://github.com/AlDanial/cloc) but uses the\n[pygments](https://pygments.org/)\npackage to analyze the source code and consequently can analyze any\n[programming language supported by pygments](https://pygments.org/languages/).\n\nThe name is a combination of pygments and count.\n\nPygount is open source and distributed under the\n[BSD license](https://opensource.org/licenses/BSD-3-Clause). The source\ncode is available from https://github.com/roskakori/pygount.\n\n## Quickstart\n\nFor installation run\n\n```bash\n$ pip install pygount\n```\n\nTo get a list of line counts for a projects stored in a certain folder run for\nexample:\n\n```bash\n$ pygount ~/projects/example\n```\n\nTo limit the analysis to certain file types identified by their suffix:\n\n```bash\n$ pygount --suffix=cfg,py,yml  ~/projects/example\n```\n\nTo get a summary of each programming language with sum counts and percentage:\n\n```bash\n$ pygount --format=summary ~/projects/example\n```\n\nAs an example here is the summary output for pygount's own source code:\n\n```\n    Language      Files    %     Code    %     Comment    %\n----------------  -----  ------  ----  ------  -------  ------\nPython               19   51.35  1924   72.99      322   86.10\nreStructuredText      7   18.92   332   12.59        7    1.87\nmarkdown              3    8.11   327   12.41        1    0.27\nBatchfile             1    2.70    24    0.91        1    0.27\nYAML                  1    2.70    11    0.42        2    0.53\nMakefile              1    2.70     9    0.34        7    1.87\nINI                   1    2.70     5    0.19        0    0.00\nTOML                  1    2.70     4    0.15        0    0.00\nText                  3    8.11     0    0.00       34    9.09\n----------------  -----  ------  ----  ------  -------  ------\nSum total            37          2636              374\n```\n\nPlenty of tools can post process SLOC information, for example the\n[SLOCCount plug-in](https://wiki.jenkins-ci.org/display/JENKINS/SLOCCount+Plugin)\nfor the [Jenkins](https://jenkins.io/) continuous integration server.\n\nA popular format for such tools is the XML format used by cloc, which pygount\nalso supports and can store in an output file:\n\n```bash\n$ pygount --format=cloc-xml --out=cloc.xml ~/projects/example\n```\n\nTo get a short description of all available command line options use:\n\n```bash\n$ pygount --help\n```\n\nFor more information and examples read the documentation chapter on\n[Usage](https://pygount.readthedocs.io/en/latest/usage.html).\n\n## Contributions\n\nTo report bugs, visit the\n[issue tracker](https://github.com/roskakori/pygount/issues).\n\nIn case you want to play with the source code or contribute improvements, see\n[CONTRIBUTING](https://pygount.readthedocs.io/en/latest/contributing.html).\n\n## Version history\n\nSee [CHANGES](https://pygount.readthedocs.io/en/latest/changes.html).\n",
    'author': 'Thomas Aglassinger',
    'author_email': 'roskakori@users.sourceforge.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/roskakori/pygount',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
