# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linkedin_auto_scraper', 'linkedin_auto_scraper.utils']

package_data = \
{'': ['*']}

install_requires = \
['alive-progress>=3.0.0,<4.0.0',
 'black>=22.12.0,<23.0.0',
 'fake-useragent>=1.1.1,<2.0.0',
 'isort>=5.11.4,<6.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'selenium>=4.7.2,<5.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'webdriver-manager>=3.8.5,<4.0.0',
 'xlsxwriter>=3.0.4,<4.0.0']

entry_points = \
{'console_scripts': ['linkedin-auto-scraper = linkedin_auto_scraper.main:app']}

setup_kwargs = {
    'name': 'linkedin-auto-scraper',
    'version': '0.1.6',
    'description': '',
    'long_description': '# linkedin-auto-scraper\n',
    'author': 'kenfelix',
    'author_email': 'Kmrapper.kf@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
