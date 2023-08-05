# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_editorjs_field', 'django_editorjs_field.templatetags']

package_data = \
{'': ['*'],
 'django_editorjs_field': ['static/django_editorjs_field/css/*',
                           'static/django_editorjs_field/js/*',
                           'templates/django_editorjs_field/*',
                           'templates/django_editorjs_field/tools/*']}

install_requires = \
['django>=4.1.3,<5.0.0']

setup_kwargs = {
    'name': 'django-editorjs-field-next',
    'version': '0.1.1',
    'description': 'An EditorJS Field with dependency injection of tools support for Django >4.*',
    'long_description': '# Django EditorJS Field\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n> Django >4.* (Not tested in old versions)\n\nAn EditorJS Field with dependency injection of tools support for Django >4.*\n\n## Features\n\n- [x] Dependency injection for tools\n- [x] Templatetag support\n- [x] All EditorJS configuration supported\n- [x] Without custom backend\n- [x] Customized editor in admin\n- [x] [Debug support](#about-debug-support)\n\n## Installation and Usage\n\n### Installation\n> Some day it will be *django-editorjs-field*...\n\nInstall package via `pip`:\n\n```\npip install django-editorjs-field-next\n```\n\nAdd package to `INSTALLED_APPS`:\n\n```\nINSTALLED_APPS = [\n    ...\n    "django_editorjs_field"\n]\n```\n\n### Usage\n\n>**Note!**<br>If you will not provide configuration, you will have only default Paragraph Tool.\n\nExample of field configuration:\n\n```\nfrom django_editorjs_field.tool import EditorJSTool as Tool\n\n\nEditorJSField(\n    tools=[\n        Tool(name="Header", url="//cdn.jsdelivr.net/npm/@editorjs/header", template_name="tools/h.html"),\n        Tool(\n            name="Code",\n            url="https://cdn.jsdelivr.net/npm/@editorjs/code@2.8.0",\n            class_name="CodeTool",\n            template_name="tools/code.html"\n        )\n    ]\n)\n```\n\n**Any** kwargs that you add will pass to EditorJS configuration. For example, if you want `autofocus`, `placeholder` and `i18n`, you just add to field arguments:\n\n```\nautofocus=False,\nplaceholder="EditorJSPlaceholder",\ni18n={\n    "messages": {\n        "toolNames": {\n            "Heading": "Заголовок"\n        }\n    }\n}\n```\n\n**templatetag**\n\nExample of templatetag:\n\n```\n{% load editorjs %}\n\n{% for article in articles_list %}\n    <div>\n        <h3>{{ article.title }}</h3>\n        {% render article %}\n    </div>\n{% endfor %}\n```\n\n## Tools\n\nAll tools (plugins) are independent objects. Tool constructor define as:\n\n```\ndef __init__(self, name: str, url: str, template_name: str, class_name: str | None = None, **kwargs):\n    """\n        An EditorJSTool constructor\n\n        ...\n\n        Attributes\n        ==========\n        name : str\n            Must be unique!\n            A name of a Tool. Used as a type in EditorJS.\n        url : str\n            A URL or Path to JS-file of Tool.\n        template_name : str\n            A Path to template for output rendering.\n        class_name : str | None\n            Name attribute is used by default.\n            A class name of Tool, which JS need to call constructor for.\n    """\n```\n\n### Override Paragraph Tool\n\nIn order to override Paragraph Tool you need to pass it as a tool into field. Example:\n\n```\nfrom django_editorjs_field.tool import EditorJSTool as Tool\n\n\nEditorJSField(\n    tools=[\n        Tool(\n            name="paragraph",\n            url="//cdn.jsdelivr.net/npm/@editorjs/paragraph@2.0.2",\n            class_name="Paragraph",\n            template_name="tools/p.html"\n        )\n        Tool(name="Header", url="//cdn.jsdelivr.net/npm/@editorjs/header", template_name="tools/h.html"),\n    ],\n    ...\n)\n```\n\n## License\nMIT\n\n## Authors\nEvgeniy Gribanov\n\n## FAQ\n### About Debug support\nIf you run Django in DEBUG mode, your EditorJS inherit this mode too. It means that you will have usefull messages in your browser console about Editor Configuration and work.',
    'author': 'Evgeniy Gribanov',
    'author_email': 'evgeniy.therabbit@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eijawa/django-editorjs-field',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
