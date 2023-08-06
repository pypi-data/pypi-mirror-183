# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['morph_ko']
setup_kwargs = {
    'name': 'morph-ko',
    'version': '0.1.0',
    'description': 'Utility for generating variations of Korean words',
    'long_description': '# Morph\n\nUtility for generating variations of Korean words.\n\nThis is intended to be used for matching words as they appear in the dictionary to tokens in text (어절).\nFor example, the sentence "우리는 오늘 동해로 간다" contains\n\n- "우리는" which is a combination of "우리" plus the particle "는"\n- "동해로" which is a combination of "동해" plus the particle "로"\n\n## Install\n- `pip install morph_po`\n\n## Usage\n\n- morph_noun() generates variations of nouns with particles applied based on whether the noun ends in a vowel or a consonent\n\n## See also\n\n- [KoParadigm](https://github.com/Kyubyong/KoParadigm) generates inflected forms of verbs\n',
    'author': 'Mat Moore',
    'author_email': 'matmoore@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MatMoore/morph',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
