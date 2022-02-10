import requests
from config import Config

config = Config()

url = f'{config.base_url}instance{config.instance}/sendMessage?token={config.token}'

response = requests.request("POST", url, headers=config.headers, data=config.payload)
