# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['epubclozer']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'ebooklib>=0.18,<0.19',
 'genanki>=0.13.0,<0.14.0',
 'spacy>=3.4.4,<4.0.0']

setup_kwargs = {
    'name': 'epubclozer',
    'version': '1.0.4',
    'description': 'Turn an epub into Anki flashcards',
    'long_description': '\n# Epub Clozer\n\nTurn an epub into Anki cloze flashcards\n\n## Description\n\nThis script will take every unique word in an epub and create a anki cloze flashcard using an example found in the book.\n\n\n## Requirements\n\nInstall [python 3.11](https://www.python.org/downloads/)\n\nInstall epubclozer\n\n```shell\npython -m pip install epubclozer\n```\n\n## How to use\n\nFrom the command line:\n\nCreate a close for each unique word in epub:\n\n```shell\npython -m epubclozer --lang "en" --path "C:/path/to/book.epub"\n```\n\nIgnore [stop words](https://en.wikipedia.org/wiki/Stop_word) such as "the, is, at, which" in English. Note this will only work effectively in you pass the target language `--lang` as well.\n\n```shell\npython -m epubclozer --lang "es" --path "C:/path/to/book.epub" --exclude-stop-words\n```\n\nSee `epubclozer --help` for all options\n\nYour Anki package will be put in the same location as the epub.\n',
    'author': 'Nelson',
    'author_email': 'nelson@truran.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nelsontkq/epubclozer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
