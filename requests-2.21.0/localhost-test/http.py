import requests
# import requests.2.19.1
r = requests.get('https://localhost:4444', auth=('hello', 'world'), verify=False)
print(r.headers)
