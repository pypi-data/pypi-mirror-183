# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['e_dnevnik_api']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'e-dnevnik-api',
    'version': '0.1.1',
    'description': 'Unofficial API for e-Dnevnik',
    'long_description': '# e-Dnevnik API\n\ne-Dnevnik API is an unofficial API for [e-Dnevnik](https://ocjene.skole.hr).\n\n## Installation\n\npip:\n```\npip install e-dnevnik-api\n```\n\n## Usage\n\n### Login\n\n```py\nfrom e_dnevnik_api import EDnevnik\n\nsession = EDnevnik()\nsession.login("username", "password")\n```\n\n### Get all courses\n\n```py\nsession.get_all_courses()\n```\n\n### Get course grades\n\n```py\nsession.get_course_grades(id)\n```\n\nFor more examples, check the documentation.\n\n## License\n\nThis project is licensed under the MIT license. For more information, check `LICENSE`.\n',
    'author': 'Ivan Paljetak',
    'author_email': 'ip@noreply.codeberg.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/ip/e-Dnevnik-API',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
