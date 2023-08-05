# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_pointers',
 'pytest_pointers.tests',
 'pytest_pointers.tests.mock_structure']

package_data = \
{'': ['*']}

install_requires = \
['libcst>=0.3.15,<0.4.0', 'rich']

entry_points = \
{'console_scripts': ['format = poetry_deps_formatter:formatter'],
 'pytest11': ['plugin = pytest_pointers.plugin']}

setup_kwargs = {
    'name': 'pytest-pointers',
    'version': '0.3.1',
    'description': 'Pytest plugin to define functions you test with special marks for better navigation and reports',
    'long_description': '## Pytest Plugin to Show Unit Coverage\n\n**Code** coverage tools like\n[coverage.py](https://coverage.readthedocs.io/en/7.0.1/) show you the\ninstrumented code coverage of your tests, however it won\'t tell you if you\'ve\nwritten specific unit tests for each of your code\'s **units** (here unit meaning\nfunction).\n\nThis package implements a mechanism for measuring and reporting unit coverage.\nInstead of instrumenting your code you will need to mark tests with a\n**pointer** to the unit that it is covering.\n\nFor example if you have in your code this module `mypackage/widget.py`:\n\n``` python\ndef foo(in):\n    return in * 3\n```\n\nthen in your test suite you would write a unit test for this function and mark it as relating to that unit, e.g. in `tests/test_widget.py`:\n\n``` python\n\nfrom mypackage.widget import foo\n\n@pytest.mark.pointer(foo)\ndef test_foo():\n    assert foo(3) == 9\n```\n\nThis package works by collecting all of the pointed-to units during test\nexecution and persists these to the pytest cache (typically somewhere under\n`.pytest_cache`). Then in subsequent runs you need only report the results.\n\n### Invocation\n\nThis package adds a couple new options to the `pytest` CLI:\n\n`--pointers-collect=STR` (default `src`)\n\nThis explicitly indicates to collect unit coverage results. If not specified,\nbut `--pointers-report` is given results will be collected using the default.\n\n`--pointers-report` (default `False`)\n\nWhen this flag is given a textual report will be given at the end of the test\nrun. Note that even if this is not given the coverage checks will still be run.\n\n`--pointers-func-min-pass=INT` (default `2`)\n\nThis flag controls the number of unit test pointer marks are needed to get a\n"passing" unit. In the report units with 0 pointers are shown as red, passing\nnumbers are green, and anything in between is blue.\n\n`--pointers-fail-under=FLOAT` (default `0.0`)\n\nThis flag controls the percentage of passing units are needed for the entire\ncoverage check to pass. The percentage is always displayed even without\n`--pointers-report`. If this test is failed then the test process exits with\ncode 1, which is useful for things like CI.\n\n#### Example\n\nHere is an example with source code under the `src` folder, requiring 1 pointer\ntest per collected unit in the code, for all functions.\n\n```\npytest --pointers-report --pointers-collect=src --pointers-func-min-pass=1 --pointers-fail-under=100 tests\n```\n\n![](https://jaklimoff-misc.s3.eu-central-1.amazonaws.com/pytest-pointers/example_output.jpg)\n\n### Installation\n\n``` shell\npip install pytest_pointers\n```\n\n\n\n',
    'author': 'Jack Klimov',
    'author_email': 'jaklimoff@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jaklimoff/pytest-pointers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
