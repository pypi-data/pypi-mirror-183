# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['singledispatch_with_type_arg_support']
setup_kwargs = {
    'name': 'singledispatch-with-type-arg-support',
    'version': '0.1.0',
    'description': 'singledispatch with support for type/class arguments',
    'long_description': '# singledispatch-with-type-arg-support\n\nStandalone "preview" of https://github.com/python/cpython/pull/100624\n\nRequires a sufficiently recent Python 3.12 version (some tests fail with\nearlier 3.12 versions and versions older than 3.12, although the main\nfunctionality might still work - do your own testing).\n\n## Example\n\nSee `example.py`:\n\n```python\nfrom singledispatch_with_type_arg_support import singledispatch\n\n@singledispatch\ndef describe(x) -> str:\n  raise TypeError(f"no description for {repr(x)}")\n\n@describe.register\ndef describe(x: type[int]) -> str:\n  return "the integer type"\n\nprint(describe(int))  # should print: the integer type\n```\n\n## License\n\nSame as CPython (as 99% of it is copied from there), see `LICENSE` file.\n',
    'author': 'smheidrich',
    'author_email': 'smheidrich@weltenfunktion.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.12,<4.0',
}


setup(**setup_kwargs)
