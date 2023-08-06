# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_face_reddit',
 'kilroy_face_reddit.resources',
 'kilroy_face_reddit.scoring',
 'kilroy_face_reddit.scraping',
 'kilroy_face_reddit.scraping.frontpage']

package_data = \
{'': ['*']}

install_requires = \
['asyncpraw>=7.6,<8.0',
 'detoxify>=0.5,<0.6',
 'httpx>=0.23,<0.24',
 'kilroy-face-server-py-sdk>=0.9,<0.10',
 'numpy>=1.23,<2.0',
 'omegaconf>=2.2,<3.0',
 'platformdirs>=2.5,<3.0',
 'pydantic[dotenv]>=1.10,<2.0',
 'typer[all]>=0.6,<0.7']

entry_points = \
{'console_scripts': ['kilroy-face-reddit = kilroy_face_reddit.__main__:cli',
                     'kilroy-face-reddit-fetch-models = '
                     'kilroy_face_reddit.models:fetch_models']}

setup_kwargs = {
    'name': 'kilroy-face-reddit',
    'version': '0.1.0',
    'description': 'kilroy face for Reddit 🤖',
    'long_description': '<h1 align="center">kilroy-face-reddit</h1>\n\n<div align="center">\n\nkilroy face for Reddit 🤖\n\n[![Lint](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/lint.yaml)\n[![Multiplatform tests](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/test-multiplatform.yaml)\n[![Docker tests](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/test-docker.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/test-docker.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-reddit/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-face-reddit\n```\n\n## Usage\n\nTo run the face server, install the package and run the following command:\n\n```sh\nkilroy-face-reddit\n```\n\nThis will start the face server on port 10002 by default.\nThen you can communicate with the server, for example by using\n[this package](https://github.com/kilroybot/kilroy-face-client-py-sdk).\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-face-reddit',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
