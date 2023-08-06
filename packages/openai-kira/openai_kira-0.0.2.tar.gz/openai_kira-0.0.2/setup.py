# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['openai_kira',
 'openai_kira.Chat',
 'openai_kira.Chat.module',
 'openai_kira.Chat.module.plugin',
 'openai_kira.Chat.text_analysis_tools',
 'openai_kira.Chat.text_analysis_tools.api.keyphrase',
 'openai_kira.Chat.text_analysis_tools.api.keywords',
 'openai_kira.Chat.text_analysis_tools.api.summarization',
 'openai_kira.Chat.text_analysis_tools.api.text_similarity',
 'openai_kira.api',
 'openai_kira.resouce',
 'openai_kira.utils']

package_data = \
{'': ['*'], 'openai_kira.Chat.text_analysis_tools': ['api/data/*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'elara>=0.5.4,<0.6.0',
 'httpx>=0.23.1,<0.24.0',
 'jieba>=0.42.1,<0.43.0',
 'loguru>=0.6.0,<0.7.0',
 'nltk>=3.8,<4.0',
 'openai-async>=0.0.2,<0.0.3',
 'pillow>=9.3.0,<10.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'redis>=4.4.0,<5.0.0',
 'transformers>=4.25.1,<5.0.0']

setup_kwargs = {
    'name': 'openai-kira',
    'version': '0.0.2',
    'description': 'A chat client',
    'long_description': '# openai-kira\n\nOpenai GPT3 ChatBot 框架包，在未公开前快速实现类 ChatGPT接入（公开后就接入chatGPT），打包成依赖的玩具。提供 redis 和 文件数据库\n两个选择，非常好工作。\n',
    'author': 'sudoskys',
    'author_email': 'coldlando@hotmail.com',
    'maintainer': 'sudoskys',
    'maintainer_email': 'coldlando@hotmail.com',
    'url': 'https://github.com/sudoskys/openai-kira',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
