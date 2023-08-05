# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poltergeist']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'poltergeist',
    'version': '0.5.0',
    'description': 'Experimental Rust-like error handling in Python, with type-safety in mind.',
    'long_description': '# poltergeist\n\n[![pypi](https://img.shields.io/pypi/v/poltergeist.svg)](https://pypi.python.org/pypi/poltergeist)\n[![versions](https://img.shields.io/pypi/pyversions/poltergeist.svg)](https://github.com/alexandermalyga/poltergeist)\n\nExperimental Rust-like error handling in Python, with type-safety in mind.\n\n## Installation\n\n```\npip install poltergeist\n```\n\n## Examples\n\nUse the provided `@poltergeist` decorator on any function:\n\n```python\nfrom pathlib import Path\nfrom poltergeist import Err, Ok, Result, poltergeist\n\n# Wrap a function to handle a concrete exception type (Exception by default)\n@poltergeist(error=OSError)\ndef read_text(path: Path) -> str:\n    return path.read_text()\n\n# Now the function returns an object of type Result[str, OSError]\nresult = read_text(Path("test.txt"))\n```\n\nOr wrap errors manually:\n\n```python\ndef read_text(path: Path) -> Result[str, FileNotFoundError]:\n    try:\n        return Ok(path.read_text())\n    except FileNotFoundError as e:\n        return Err(e)\n```\n\nThen handle the result:\n\n```python\n# Get the contained Ok value or raise the contained Err exception\ncontent = result.unwrap()\n\n# Get the contained Ok value or a default value\ncontent = result.unwrap_or("default text")\ncontent = result.unwrap_or()  # default None\n\n# Get the contained Ok value or compute it from a callable\ncontent = result.unwrap_or_else(lambda e: f"The exception was: {e}")\n\n# Get the contained Err exception or None\nerr = result.err()\n\n# Handle errors using structural pattern matching\nmatch result:\n    case Ok(content):\n        print("File content in upper case:", content.upper())\n    case Err(e):\n        match e:\n            case FileNotFoundError():\n                print("File not found:", e.filename)\n            case PermissionError():\n                print("Permission error:", e.errno)\n            case _:\n                raise e\n```\n',
    'author': 'Alexander Malyga',
    'author_email': 'alexander@malyga.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alexandermalyga/poltergeist',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
