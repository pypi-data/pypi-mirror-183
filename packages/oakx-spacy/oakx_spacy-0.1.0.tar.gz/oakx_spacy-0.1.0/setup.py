# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['oakx_spacy']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'importlib>=1.0.4,<2.0.0',
 'oaklib>=0.1,<0.2',
 'scispacy>=0.5.1,<0.6.0',
 'setuptools>=65.0.1,<66.0.0',
 'spacy>=3.4.4,<4.0.0',
 'tox>=3.25.1,<4.0.0']

extras_require = \
{':extra == "docs"': ['sphinx[docs]>=5.3.0,<6.0.0',
                      'sphinx-rtd-theme[docs]>=1.0.0,<2.0.0',
                      'sphinx-autodoc-typehints[docs]>=1.19.4,<2.0.0',
                      'sphinx-click[docs]>=4.3.0,<5.0.0',
                      'myst-parser[docs]>=0.18.1,<0.19.0']}

entry_points = \
{'console_scripts': ['oxpacy = oakx_spacy.cli:main'],
 'oaklib.plugins': ['spacy = '
                    'oakx_spacy.spacy_implementation:SpacyImplementation']}

setup_kwargs = {
    'name': 'oakx-spacy',
    'version': '0.1.0',
    'description': 'oakx-spacy',
    'long_description': '# oakx-spacy\n\nSpacy plugin for OAK\n\n# Acknowledgements\n\nThis [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [oakx-plugin-cookiecutter](https://github.com/INCATools/oakx-plugin-cookiecutter) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).',
    'author': 'Harshad Hegde',
    'author_email': 'hhegde@lbl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
