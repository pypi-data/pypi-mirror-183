# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['head_context']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'head-context',
    'version': '0.1.1',
    'description': '',
    'long_description': '# `head-context`\n\nEasily manage your assets in meta tags (scripts, css, preload etc.) from anywhere\nin the template code (and outside).\n\n## Why\n\nImagine a form widget, which requires a heavy image processing library that we want to include ONLY IF the widget itself was rendered. Thanks to `head-context` you can specify what resources you need locally (in template fragments, widgets and so on) yet load them in the `head` section of your page with ease.\n\n## What does it do?\n\n```html+jinja\n<!doctype html>\n<html>\n<head>\n    <title>My Title!</title>\n    <!-- this is where we want all our js/css rendered to be rendered -->\n    {{ head_placeholder() }}\n</head>\n<body>\n    {% include "my-cool-component.html" %}\n</body>\n</html>\n```\n\nAnd `my-cool-component.html`:\n\n```html+jinja\n<!-- we can call these from anywhere and they will be automatically rendered in the right place! -->\n{% do push_js(\'/static/cool-component.js\', mode="async") %}\n{% do push_css(\'/static/cool-component.css\') %}\n{% do push_preload(\'/static/some-image-we-need.png\', \'image\') %}\n<div class="my-cool-component">\n    <!-- ... --->\n</div>\n```\n\nAnd that\'s pretty much it. You can `push_js`/`push_css`/`push_preload` from anywhere in the template (and even outside of templates) and it will be automatically attached to the page being rendered.\n\n## Features\n\n* Supports scripts, styles and preload directives\n* Works with Jinja2\n* Can be used from Python code too\n  * simply use `head_context.push_js/push_css/push_preload` from Python code\n  * it needs to run during template rendering though (otherwise it wouldn\'t make sense)\n  * useful if you have form widget rendering written in Python for example\n  * or basically any kind of rendering written in Python\n\n\n## Installation and setup\n\nSimply install `head-context` package:\n\n```bash\npip install head-context\n# or with poetry\npoetry add head-context\n```\n\nAdd extension to the Jinja2 environment:\n\n```python\n\nfrom jinja2 import Environment\n\nenv = Environment()\nenv.add_extension("head_context.jinja_ext.HeadContextExtension")\n```\n\nand that\'s it! From now on you can use `push_css()`/`push_js()`/`push_preload()` and `head_placeholder()`.\n\n## Usage with Flask\n\nTo use this extension with `Flask` simply add it when configuring the app:\n\n```python\n\ndef create_app():\n    app = Flask("app", __name__)\n    app.jinja_env.add_extension("head_context.jinja_ext.HeadContextExtension")\n    app.jinja_env.add_extension("jinja2.ext.do")\n    \n    return app\n\n```\n\n## FAQ\n\n### Does this work with `asyncio`?\n\n`head-context` uses `contextvars` under the hood, which are compatible with `asyncio` but it integrates with `Jinja` in a way that won\'t work with templates which use `asyncio` rendering. If you have any good ideas how to make it work a PR would be welcome.\n\n',
    'author': 'Rafal Stozek',
    'author_email': 'rafal.stozek@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rafales/head-context',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
