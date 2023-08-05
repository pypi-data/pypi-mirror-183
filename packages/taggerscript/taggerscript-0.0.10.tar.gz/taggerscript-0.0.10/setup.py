# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tagger', 'tagger.core', 'tagger.library', 'tagger.parser', 'tagger.visitor']

package_data = \
{'': ['*']}

install_requires = \
['lark>=1.1.5,<2.0.0']

setup_kwargs = {
    'name': 'taggerscript',
    'version': '0.0.10',
    'description': 'Scripting language written in Python for Discord bot',
    'long_description': '# Tagger\n\nTagger is a scripting language for Discord bot. It can be used from tag command to user automation moderation. It is simple but powerful. Users cannot run code that can harm your bot. You can add new function and class to it in a simple way.\n\n# Example\n\n```tagger\n{do\n    {msg.set("React with :heart: to claim this present")}\n    {msg.wait_for_reaction(":heart:")}\n    {msg.set("Just kidding there is no present")}\n}\n```\nCheck example for more\n\n# Install\n\n## PIP\n```\npip install taggerscript\n```\n\n## Poetry\n```\npoetry add taggerscript\n```\n\n## git clone\n```\ngit clone https://github.com/najis-poop/TaggerScript\n```\n\n# Documentation\n\ncoming soon\n\n# Feedback\n\nTagger still in development. Any bug should be reported quickly by creating issue in github issue.',
    'author': 'najis',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
