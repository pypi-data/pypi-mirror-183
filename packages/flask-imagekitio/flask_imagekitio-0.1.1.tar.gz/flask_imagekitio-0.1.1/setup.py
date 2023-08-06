# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flask_imagekitio']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.2.2,<3.0.0', 'imagekitio>=3.0.1,<4.0.0']

setup_kwargs = {
    'name': 'flask-imagekitio',
    'version': '0.1.1',
    'description': 'A simple interface to use ImageKiIO API with Flask.',
    'long_description': "# Flask-CKEditor-Manager\n\nFlask-ImageKitIO provides a simple interface to use ImageKitIO API with Flask.\n\n```{warning}\n🚧 This package is under heavy development..\n```\n\n## Installation\n\nInstall the extension with pip:\n\n```bash\npip install flask-imagekitio\n```\n\nInstall with poetry:\n\n```bash\npoetry add flask-imagekitio\n```\n\n## Configuration\n\nThis are some of the settings available\n\n| Config                  | Description                         | Type | Default |\n| ----------------------- | ----------------------------------- | ---- | ------- |\n| IMAGEKITIO_URL_ENDPOINT | The ImagekitIO account url endpoint | str  | `None`  |\n| IMAGEKITIO_PRIVATE_KEY  | The ImagekitIO Private Key          | str  | `None`  |\n| IMAGEKITIO_PUBLIC_KEY   | The ImagekitIO Public Key           | str  | `None`  |\n\n## Usage\n\nOnce installed ImagekitIO is easy to use. Let's walk through setting up a basic application. Also please note that this is a very basic guide: we will be taking shortcuts here that you should never take in a real application.\n\nTo begin we'll set up a Flask app:\n\n```python\nfrom flask import Flask\n\nfrom flask_imagekitio import ImagekitIO\n\napp = Flask(__name__)\n\nimagekitio = ImagekitIO()\nimagekitio.init_app(app)\n\nresult = imagekit.upload_file(data, file.filename)\nimg_url = imagekit.url({\n    'src': result.url,\n    'transformation': [\n        {\n            'width': '600',\n            'aspect_ratio': '5-3'\n        }\n    ]\n})\n```\n",
    'author': 'Sebastian Salinas',
    'author_email': 'seba.salinas.delrio@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
