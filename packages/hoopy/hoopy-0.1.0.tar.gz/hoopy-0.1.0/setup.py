# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hoopy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hoopy',
    'version': '0.1.0',
    'description': '',
    'long_description': "# hoopy\n\n# This library is a stub. A working release is expected soon.\n\nHoopy extends the Python language, letting you write a subset of Haskell in your scripts!\n\n- `pip install hoopy` (not yet published)\n\n## Usage\n\n## Caveats\n\nHoopy is implemented entirely using Python (making maximal use of the builtin parser and tokenizer).\nGiven that static typing in Python is optional, Hoopy implements custom operators are using pure-Python\ndynamic dispatch. This adds some overhead to custom operators that wouldn't be present if they were a\nfirst-class language feature.\n\nHoopy does its best to ensure that code preprocessed by the library that's *not* using any of its features\nremains semantically equivalent to its unprocessed form. This is currently tracked via unit tests running Hoopy\nagainst selected modules within the Python standard library. Future plans include incorporating the builtin\n(`python3 -m test`) tests directly into a *fully* preprocessed copy of the standard library.\n\n## Development\n\nTo begin, install the dependencies and set up the development environment. Please run all the unit tests\nbefore submitting any code-related pull requests!\n\n```bash\n$ poetry install\n$ poetry run pre-commit install\n```\n\n(once implemented) Run the regression test suite on any significant code changes.\n\n```bash\n$ ./stdlib_test.sh\n```\n",
    'author': 'Olivia Palmu',
    'author_email': 'oliviaspalmu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
