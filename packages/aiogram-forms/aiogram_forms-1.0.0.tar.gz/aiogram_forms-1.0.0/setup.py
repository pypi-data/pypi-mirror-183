# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogram_forms', 'aiogram_forms.core', 'aiogram_forms.forms']

package_data = \
{'': ['*']}

install_requires = \
['aiogram>=3.0.0b5,<4.0.0']

setup_kwargs = {
    'name': 'aiogram-forms',
    'version': '1.0.0',
    'description': 'Forms for aiogram',
    'long_description': '# aiogram-forms\n![Project code coverage](https://img.shields.io/badge/coverage-96%25-green)\n![Project status](https://img.shields.io/pypi/status/aiogram-forms)\n![PyPI](https://img.shields.io/pypi/v/aiogram-forms)\n![GitHub](https://img.shields.io/github/license/13g10n/aiogram-forms)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/aiogram-forms?label=installs)\n\n## Introduction\n`aiogram-forms` is an addition for `aiogram` which allows you to create different forms and process user input step by step easily.\n\n## Installation\n```bash\npip install aiogram-forms\n```\n\n## Usage\nCreate form you need by subclassing `aiogram_forms.forms.Form`. Fields can be added from `aiogram_forms.forms.fields` subpackage.\n```python\nfrom aiogram_forms import dispatcher\nfrom aiogram_forms.forms import Form, fields, FormsManager\nfrom aiogram_forms.errors import ValidationError\n\ndef validate_username_format(value: str):\n    """Validate username starts with leading @."""\n    if not value.startswith(\'@\'):\n        raise ValidationError(\'Username should starts with "@".\', code=\'username_prefix\')\n\n@dispatcher.register(\'test-form\')\nclass TestForm(Form):\n    username = fields.TextField(\n        \'Username\', min_length=4, validators=[validate_username_format],\n        error_messages={\'min_length\': \'Username must contain at least 4 characters!\'}\n    )\n    email = fields.EmailField(\'Email\', help_text=\'We will send confirmation code.\')\n    phone = fields.PhoneNumberField(\'Phone number\', share_contact=True)\n    value = fields.TextField(\'Value\')\n\n    @classmethod\n    async def callback(cls, message: types.Message, forms: FormsManager, **data) -> None:\n        data = await forms.get_data(TestForm)  # Get form data from state\n        await message.answer(text=\'Thank you!\')\n\n@router.message(Command(commands=[\'start\']))\nasync def command_start(message: Message, forms: FormsManager) -> None:\n    await forms.show(\'test-form\')  # Start form processing\n\nasync def main():\n    bot = Bot(...)\n    dp = Dispatcher()\n\n    dispatcher.attach(dp)  # Attach aiogram to forms dispatcher \n\n    await dp.start_polling(bot)\n```\n\n## History\nAll notable changes to this project will be documented in [CHANGELOG](CHANGELOG.md) file.\n',
    'author': 'Ivan Borisenko',
    'author_email': 'i.13g10n@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://13g10n.com/docs/aiogram-forms',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
