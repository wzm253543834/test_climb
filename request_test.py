import requests

response = requests.get('https://www.baidu.com', data=None, timeout=10)
print(response.headers)
