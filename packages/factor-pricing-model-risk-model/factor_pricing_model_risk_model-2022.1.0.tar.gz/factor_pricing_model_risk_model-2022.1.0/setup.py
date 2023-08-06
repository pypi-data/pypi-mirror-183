# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fpm_risk_model',
 'fpm_risk_model.accuracy',
 'fpm_risk_model.pipeline',
 'fpm_risk_model.regressor',
 'fpm_risk_model.statistical']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.5,<1.4.0', 'scikit-learn>=1.1.3,<2.0.0', 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{'docs': ['Sphinx>=5.0,<6.0',
          'insipid-sphinx-theme>=0.3.6,<0.4.0',
          'myst-parser>=0.18,<0.19']}

setup_kwargs = {
    'name': 'factor-pricing-model-risk-model',
    'version': '2022.1.0',
    'description': 'Package to build risk models for factor pricing model',
    'long_description': '# Factor Pricing Model Risk Model\n\n<p align="center">\n  <a href="https://github.com/factorpricingmodel/factor-pricing-model-risk-model/actions?query=workflow%3ACI">\n    <img src="https://github.com/factorpricingmodel/factor-pricing-model-risk-model/actions/workflows/ci.yml/badge.svg" alt="CI Status" >\n  </a>\n  <a href="https://factor-pricing-model-risk-model.readthedocs.io">\n    <img src="https://img.shields.io/readthedocs/factor-pricing-model-risk-model.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">\n  </a>\n  <a href="https://codecov.io/gh/factorpricingmodel/factor-pricing-model-risk-model">\n    <img src="https://img.shields.io/codecov/c/github/factorpricingmodel/factor-pricing-model-risk-model.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">\n  </a>\n</p>\n<p align="center">\n  <a href="https://python-poetry.org/">\n    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">\n  </a>\n  <a href="https://github.com/ambv/black">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">\n  </a>\n  <a href="https://github.com/pre-commit/pre-commit">\n    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">\n  </a>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/factor-pricing-model-risk-model/">\n    <img src="https://img.shields.io/pypi/v/factor-pricing-model-risk-model.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">\n  </a>\n  <img src="https://img.shields.io/pypi/pyversions/factor-pricing-model-risk-model.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">\n  <img src="https://img.shields.io/pypi/l/factor-pricing-model-risk-model.svg?style=flat-square" alt="License">\n</p>\n\nPackage to build risk model for factor pricing model. For further details, please refer\nto the [documentation](https://factor-pricing-model-risk-model.readthedocs.io/en/latest/)\n\n## Installation\n\nInstall this via pip (or your favourite package manager):\n\n`pip install factor-pricing-model-risk-model`\n\n## Usage\n\nThe library contains the pipelines to build the risk model. You can\nrun the pipelines interactively in Jupyter Notebook.\n\n```python\nimport fpm_risk_model\n```\n',
    'author': 'Factor Pricing Model',
    'author_email': 'factor.pricing.model@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/factorpricingmodel/factor-pricing-model-risk-model',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
