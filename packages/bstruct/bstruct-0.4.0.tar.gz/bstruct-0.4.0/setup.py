# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bstruct']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'bstruct',
    'version': '0.4.0',
    'description': 'Simple and efficient binary (de)serialization using regular type annotations.',
    'long_description': "# bstruct\n\n[![ci](https://github.com/flxbe/bstruct/actions/workflows/ci.yml/badge.svg)](https://github.com/flxbe/bstruct/actions/workflows/ci.yml)\n[![pypi](https://img.shields.io/pypi/v/bstruct)](https://pypi.org/project/bstruct/)\n\n<!-- start elevator-pitch -->\n\nSimple and efficient binary parsing using regular type annotations.\nSupports easy fallback to Python's built-in `struct` library for maximum performance.\n\n<!-- end elevator-pitch -->\n\n## ⚠️ DISCLAIMER\n\nThis project is still a work in progress. Use at your own risk.\n\n## Getting Started\n\n<!-- start quickstart -->\n\n```bash\npip install bstruct\n```\n\n```python\nfrom typing import Annotated\nimport bstruct\n\n\nclass Item(bstruct.Struct):\n    identifier: bstruct.u64  # shorthand for: Annotated[int, bstruct.Encodings.u64]\n    value: bstruct.i32       # shorthand for: Annotated[int, bstruct.Encodings.i32]\n\nclass Sequence(bstruct.Struct):\n    items: Annotated[list[Item], bstruct.Length(3)]\n\nsequence = Sequence(\n    items=[\n        Item(identifier=0, value=-1),\n        Item(identifier=1, value=0),\n        Item(identifier=2, value=1),\n    ]\n)\n\nencoded = bstruct.encode(sequence)\ndecoded = bstruct.decode(Sequence, encoded)\n\nassert decoded == sequence\n```\n\n<!-- end quickstart -->\n\nSee the [documentation](https://bstruct.readthedocs.io/) for more information.\n\n## Benchmarks\n\nPlease see the source of the benchmarks in the `benchmarks` directory.\nFeel free to create an issue or PR should there be a problem with the methodology.\nThe benchmarks where executed with\n[pyperf](https://github.com/psf/pyperf)\nusing Python 3.11.1 and\n[construct](https://pypi.org/project/construct/) 2.10.68\non a MacBook Pro 2018 with a 2.3GHz i5 processor.\n\n### `benchmarks/builtins.py`\n\n| Name                 | decode  | encode  |\n| -------------------- | ------- | ------- |\n| struct               | 0.56 us | 0.22 us |\n| bstruct              | 2.58 us | 1.68 us |\n| construct (compiled) | 9.31 us | 9.85 us |\n\n### `benchmarks/native_list.py`\n\n| Name                 | decode  | encode  |\n| -------------------- | ------- | ------- |\n| struct               | 0.16 us | 0.32 us |\n| bstruct              | 2.46 us | 0.97 us |\n| construct (compiled) | 4.02 us | 6.86 us |\n\n### `benchmarks/class_list.py`\n\n| Name                 | decode  | encode  |\n| -------------------- | ------- | ------- |\n| bstruct              | 8.54 us | 5.13 us |\n| construct (compiled) | 34.4 us | 38.6 us |\n\n### `benchmarks/nested.py`\n\n| Name                 | decode  | encode  |\n| -------------------- | ------- | ------- |\n| bstruct              | 6.30 us | 4.47 us |\n| construct (compiled) | 29.2 us | 29.2 us |\n",
    'author': 'flxbe',
    'author_email': 'flxbe@mailbox.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/flxbe/bstruct',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
