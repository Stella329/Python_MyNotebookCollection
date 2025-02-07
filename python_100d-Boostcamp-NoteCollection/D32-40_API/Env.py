# Environment Variables

import os
from dotenv import load_dotenv # 安装注意：pip install python-dotenv


# M1: USING OS
## TO SET -- TODO DELETE!!!!!!
os.environ['AMADUES_API_KEY'] = 'FE6RBsaH8IyD4Gl5UllMjc3vYGhKgAKs'
os.environ['AMADUES_API_SECRET'] = 'GsXi8DqElupzyiEB'

## TO GET
AMADEUS_API_KEY = os.environ.get('AMADUES_API_KEY')
AMADEUS_API_SECRET = os.environ.get('AMADUES_API_SECRET')

##NB
# 1. 如OOP，set需要在父目录（main.py)中储存，这样子目录才会继承（i.e. oop file 1)
# 2. 如要添加pycharm能用变量，需在 我的电脑 下添加（Hierarchy：system -> explorer桌面层级 -> pycharm）




# M2 不添加至系统环境, 而单独将Env储存至一个.env file

## ENV FILE: 必须后缀.env

# 文档
[PROJECT_1]
AMADEUS_API_KEY = 'FE6RBsaH8IyD4Gl5UllMjc3vYGhKgAKs'
AMADEUS_API_KEY = 'GsXi8DqElupzyiEB'

# Pycharm
load_dotenv('E:/Python/EnvironmentVariables/.env', verbose=True) ##读取
AMADEUS_API_KEY = os.getenv('AMADUES_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADUES_API_SECRET')
print(AMADEUS_API_KEY, AMADEUS_API_SECRET)


## 1. Ensure API credentials are loaded
if not self.AMADEUS_API_KEY or not self.AMADEUS_API_SECRET:
    print(self.AMADEUS_API_KEY, self.AMADEUS_API_SECRET)
    raise ValueError("API key and secret must be set in environment variables.")


## 2. 读取文档
load_dotenv('E:\Stella\PythonProjectFiles\EnvVar.env', verbose=True) ##verbose=自动搜索
#OR
load_dotenv('E:\Stella\PythonProjectFiles\.env', verbose=True)


#NB: env var are always STRINGS!!!