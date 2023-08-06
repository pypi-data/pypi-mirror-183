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
    'version': '0.0.8',
    'description': 'A chat client',
    'long_description': '# openai-kira\n\nOpenai GPT3 ChatBot 框架包，在未公开前快速实现类 ChatGPT接入（公开后就接入chatGPT），打包成依赖的玩具。提供 redis 和 文件数据库\n两个选择，非常好工作。\n\n## 使用\n\n`pip install -U openai-kira`\n\n**init**\n\n```python\nimport openai_kira\nopenai_kira.setting.redisSetting = RedisConfig()\nopenai_kira.setting.dbFile = "openai_msg.db"\nopenai_kira.setting.openaiApiKey = None\nopenai_kira.setting.proxyUrl = ""\nopenai_kira.setting.webServerUrlFilter = False\nopenai_kira.setting.webServerStopSentence = ["广告", "营销号"]\n```\n\n## 实例\n\n```python\nfrom openai_kira import Chat\n\nreceiver = Chat.Chatbot(\n    conversation_id=10086,\n    call_func=None,  # Api_keys.pop_api_key,\n    start_sequ=None,\n    restart_sequ=None,\n)\nresponse = await receiver.get_chat_response(model="text-davinci-003",\n                                            prompt="你好",\n                                            max_tokens=500,\n                                            role="你扮演...",\n                                            web_enhance_server={"time": ""}\n                                            )\n```\n\n```python\nimport openai_kira\n\nresponse = await openai_kira.Completion(call_func=None).create(\n    model="text-davinci-003",\n    prompt=str("你好"),\n    temperature=0.2,\n    frequency_penalty=1,\n    max_tokens=500\n)\n```\n\n## 结构\n\n```markdown\n.\n└── openai_kira\n├── api\n│ ├── api_url.json\n│ ├── api_utils.py\n│ ├── network.py\n├── Chat\n│ ├── __init__.py\n│ ├── module\n│ ├── Summer.py\n│ ├── test_module.py\n│ ├── text_analysis_tools\n│ └── vocab.json\n├── __init__.py\n├── requirements.txt\n├── resouce\n│ ├── completion.py\n│ ├── __init__.py\n└── utils\n├── data.py\n├── Network.py\n└── Talk.py\n```',
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
