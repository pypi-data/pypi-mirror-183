# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datamuse']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'python-datamuse',
    'version': '2.0.1',
    'description': 'Python wrapper for the Datamuse API',
    'long_description': '# python-datamuse\n\n[![PyPI](https://img.shields.io/pypi/v/python-datamuse)](https://pypi.org/project/python-datamuse/)\n[![PyPI - License](https://img.shields.io/pypi/l/python-datamuse)](https://github.com/gmarmstrong/python-datamuse/blob/main/LICENSE)\n[![CodeQL](https://github.com/gmarmstrong/python-datamuse/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/gmarmstrong/python-datamuse/actions/workflows/codeql-analysis.yml)\n\nPython wrapper and scripts for the [Datamuse API](http://datamuse.com/api/).\nAvailable on PyPI at <https://pypi.python.org/pypi/python-datamuse>. You can\ninstall this library with `pip3 install python-datamuse`.\n\n## Changelog\n\n### Version 2.0.* (2022-10-22)\n\n- require Python 3.7\n- add @margaret to authors\n- upgrade trove classifier "Development Status" from "3 - Alpha" to "5 - Production/Stable"\n- specify all dependency version requirements\n- rename default branch `main`\n- build tool changes, see <https://github.com/gmarmstrong/python-datamuse/releases/tag/v2.0.0>\n- **(2.0.1) (2022-12-29):** fix CI workflows\n\n### Version 1.3.* (2019-09-20)\n\n- Add optional arguments to `suggest` method\n- Document and test suggestion method\n- **(1.3.1):** Update README example\n- **(1.3.1):** Remove WORD_PARAMS\n- **(1.3.1):** Document `words` method\n- **(1.3.2) (2022-04-04):** Fix test_set_max bug \n\n### Version 1.2.* (2018-10-23)\n\n- Raise Python version to 3.6\n- Mock the Datamuse API for tests\n- Restructure project files\n- Set README as PyPI long description\n- **(1.2.1):** Fix README formatting on PyPI\n\n### Version 1.1.0 (2018-02-18)\n\n- Changed to Python 3\n- Uploaded to PyPI, added instructions for PyPI installation\n- Changed README example to reflect PyPI packaging\n- Set up Travis CI\n- Temporarily removed pandas\n- Changed mode of scripts to executable\n\n## Example\n\n```\n>>> from datamuse import Datamuse\n>>> api = Datamuse()\n>>> api.words(rel_rhy=\'ninth\', max=5)  # words that rhyme with "ninth"\n[]\n>>> api.words(rel_rhy=\'orange\', max=5)  # words that rhyme with "orange"\n[{\'word\': \'door hinge\', \'score\': 74, \'numSyllables\': 2}]\n>>> api.words(rel_jja=\'yellow\', max=5)  # things often described as "yellow"\n[{\'word\': \'fever\', \'score\': 1001}, {\'word\': \'color\', \'score\': 1000}, {\'word\': \'flowers\', \'score\': 999}, {\'word\': \'light\', \'score\': 998}, {\'word\': \'colour\', \'score\': 997}]\n>>> api.suggest(s=\'foo\', max_results=10)  # completion suggestions for "foo"\n[{\'word\': \'food\', \'score\': 3888}, {\'word\': \'foot\', \'score\': 3041}, {\'word\': \'fool\', \'score\': 1836}, {\'word\': \'football\', \'score\': 1424}, {\'word\': \'footage\', \'score\': 1328}, {\'word\': \'footprint\', \'score\': 1082}, {\'word\': \'foolish\', \'score\': 967}, {\'word\': \'foof\', \'score\': 930}, {\'word\': \'footing\', \'score\': 786}, {\'word\': \'foolproof\', \'score\': 697}]\n```\n\nNote that the default number of results is set to 100. You can set the default\n`max` to something else using the `set_max_default` method, e.g.\n`api.set_max_default(300)`. Datamuse only returns 1000 results max.\n',
    'author': 'Guthrie McAfee Armstrong',
    'author_email': 'git@gmarmstrong.dev',
    'maintainer': 'Guthrie McAfee Armstrong',
    'maintainer_email': 'git@gmarmstrong.dev',
    'url': 'https://github.com/gmarmstrong/python-datamuse',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
