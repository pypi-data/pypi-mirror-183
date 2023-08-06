# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flake8_test_docs']
install_requires = \
['flake8>=6,<7']

extras_require = \
{':python_version < "3.10"': ['typing_extensions>=4,<5']}

entry_points = \
{'flake8.extension': ['TDO = flake8_test_docs:Plugin']}

setup_kwargs = {
    'name': 'flake8-test-docs',
    'version': '1.0.7',
    'description': 'A linter that checks test docstrings for the arrange/act/assert structure',
    'long_description': '# flake8-test-docs\n\nHave you ever needed to understand a new project and started reading the tests\nonly to find that you have no idea what the tests are doing? Good test\ndocumentation is critical during test definition and when reviewing tests\nwritten in the past or by someone else. This linter checks that the test\nfunction docstring includes a description of the test setup, execution and\nchecks.\n\n## Getting Started\n\n```shell\npython -m venv venv\nsource ./venv/bin/activate\npip install flake8 flake8-test-docs\nflake8 test_source.py\n```\n\nOn the following code:\n\n```Python\n# test_source.py\ndef test_foo():\n    value = foo()\n    assert value == "bar"\n```\n\nThis will produce warnings such as:\n\n```shell\nflake8 test_source.py\ntest_source.py:2:1: TDO001 Docstring not defined on test function, more information: https://github.com/jdkandersson/flake8-test-docs#fix-tdo001\n```\n\nThis can be resolved by changing the code to:\n\n```Python\n# test_source.py\ndef test_foo():\n    """\n    arrange: given foo that returns bar\n    act: when foo is called\n    assert: then bar is returned\n    """\n    value = foo()\n    assert value == "bar"\n```\n\n## Configuration\n\nThe plugin adds the following configurations to `flake8`:\n\n* `--test-docs-patter`: The pattern the test documentation should follow,\n  e.g., `given/when/then`. Defaults to `arrange/act/assert`.\n* `--test-docs-filename-pattern`: The filename pattern for test files. Defaults\n  to `test_.*\\.py`.\n* `--test-docs-function-pattern`: The function pattern for test functions.\n  Defaults to `test_.*`.\n\n\n## Rules\n\nA few rules have been defined to allow for selective suppression:\n\n* `TDO001`: checks that test functions have a docstring.\n* `TDO002`: checks that test function docstrings follow the documentation\n  pattern.\n\n### Fix TDO001\n\nThis linting rule is triggered by a test function in a test file without a\ndocstring. For example:\n\n```Python\n# test_source.py\ndef test_foo():\n    result = foo()\n    assert result == "bar"\n```\n\nThis example can be fixed by:\n\n```Python\n# test_source.py\ndef test_foo():\n    """\n    arrange: given foo that returns bar\n    act: when foo is called\n    assert: then bar is returned\n    """\n    result = foo()\n    assert result == "bar"\n```\n\n### Fix TDO002\n\nThis linting rule is triggered by a test function in a test file with a\ndocstring that doesn\'t follow the documentation pattern. For example:\n\n```Python\n# test_source.py\ndef test_foo():\n    """Test foo."""\n    result = foo()\n    assert result == "bar"\n```\n\nThis example can be fixed by:\n\n```Python\n# test_source.py\ndef test_foo():\n    """\n    arrange: given foo that returns bar\n    act: when foo is called\n    assert: then bar is returned\n    """\n    result = foo()\n    assert result == "bar"\n```\n\nThe message of the linting rule should give you the specific problem with the\ndocumentation. In general, the pattern is:\n\n* start on the second line with the same indentation is the start of the\n  docstring\n* the starting line should begin with `arrange:` (or whatever was set using\n  `--test-docs-patter`) followed by at least some words describing the test\n  setup\n* long test setup descriptions can be broken over multiple lines by indenting\n  the lines after the first by one level (e.g., 4 spaces by default)\n* this is followed by similar sections starting with `act:` describing the test\n  execution and `assert:` describing the checks\n* the last line should be indented the same as the start of the docstring\n\nBelow are some valid examples. Starting with a vanilla example:\n\n```Python\n# test_source.py\ndef test_foo():\n    """\n    arrange: given foo that returns bar\n    act: when foo is called\n    assert: then bar is returned\n    """\n    result = foo()\n    assert result == "bar"\n```\n\nHere is an example where the test function is in a nested scope:\n\n```Python\n# test_source.py\nclass TestSuite:\n\n    def test_foo():\n        """\n        arrange: given foo that returns bar\n        act: when foo is called\n        assert: then bar is returned\n        """\n        result = foo()\n        assert result == "bar"\n```\n\nHere is an example where each of the descriptions go over multiple lines:\n\n```Python\n# test_source.py\ndef test_foo():\n    """\n    arrange: given foo\n        that returns bar\n    act: when foo\n        is called\n    assert: then bar\n        is returned\n    """\n    result = foo()\n    assert result == "bar"\n```\n',
    'author': 'David Andersson',
    'author_email': 'david@jdkandersson.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
