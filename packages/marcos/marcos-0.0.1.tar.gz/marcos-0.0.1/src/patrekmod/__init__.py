import os
try:
    import requests , user_agent , json
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
from .IG_info import IG_info