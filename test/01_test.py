import requests

import json

url = 'http://localhost:5000/v1/client/register'
payload = {'nickname': 'xiaoming', 'email': 'data', 'password': '123456ssddds', 'type': 101}
# payload = {'account':'aaaa','nickname':'xiaoming'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r)
