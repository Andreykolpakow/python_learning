import requests
from sys import path
response = requests.get('http://geekbrains.ru')
print(response) # <Response [200]>
