# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bro_listen']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0',
 'pyttsx3>=2.90,<3.0',
 'rich>=12.6.0,<13.0.0',
 'sounddevice>=0.4.5,<0.5.0',
 'toml>=0.10.2,<0.11.0',
 'vosk>=0.3.45,<0.4.0']

entry_points = \
{'console_scripts': ['bro_listen = bro_listen.bro_listen:run']}

setup_kwargs = {
    'name': 'bro-listen',
    'version': '0.1.0',
    'description': 'Interact with openAI API with voice',
    'long_description': '# bro, listen 🤖\nTool that allows for voice interaction with OpenAI chat without need to type long, detailed requests. <br>\nIt\'s an terminal application that captures audio from microphone and queries chat with transcripted message.\n\n<p align="center">\n  <img src="https://github.com/mikkac/bro_listen/blob/master/demo/bro_demo.gif" alt="animated" />\n</p>\n\n\n---\n**Note:** Currently `text-davinci-003` model is used as a chat backend. Unfortunately API for chatGPT is not yet provided by OpenAI.\n\n\n## Installation\n\n`poetry` is required to install the package from the source code. You can get it [here](https://python-poetry.org/docs/)\n\nOnce `poetry` is enabled in the system, to install the project and its dependencies, execute following command:\n\n```bash\ngit clone https://github.com/mikkac/bro_listen.git && cd bro_listen && poetry install\n```\n\n## Configuration\n\nAfter installation, configuration file has to be provided.\nDefault location used by the application is `$HOME/.config/bro_listen/config.toml`. <br>\nOne can use the default [configuration file](https://github.com/mikkac/bro_listen/blob/master/src/bro_listen/config.toml). The only thing that needs to be provided is OpenAI API key that can be generated [here](https://beta.openai.com/account/api-keys).\n\n### Configuration details\n\nApplication supports several configuration parameters.\n* `voice_api` - Voice recognition API. Currently only `"vosk"` is supported, but it\'s planned to also enable usage of [Google Speech-To-Text](https://cloud.google.com/speech-to-text) and [Azure Speech to text](https://azure.microsoft.com/en-us/products/cognitive-services/speech-to-text/).\n* `language` - language used by `voice_api`. Currently available languages are listed in [Vosk\'s documentation](https://github.com/alphacep/vosk-api).\n* `enable_audio_response` - chat\'s responses are only written to console by default. However, it\'s possible to vocalize them by setting this parameter to `true`.\n* `device_id` - ID of recording device. It should be commented out or completely removed from configuration if default device shall be used.\n\n## Usage\n\nOnce configuration file has been provided, start the application with command:\n```bash\npoetry run bro_listen\n```\nor\n\n```bash\npoetry shell\nbro_listen\n```\n\n## License\n\nThis project is licensed under the LICENSE file that [can be found here](https://github.com/mikkac/bro_listen/blob/master/LICENSE.md)',
    'author': 'Mikolaj Kaczmarek',
    'author_email': 'm.kaczmarek9@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mikkac/bro_listen',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
