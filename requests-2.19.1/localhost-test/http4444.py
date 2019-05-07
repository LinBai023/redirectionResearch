import requests
r = requests.get('https://localhost:4443', auth=("hello","world"), verify = False)
print(r.headers)


# 'https://localhost:4443'