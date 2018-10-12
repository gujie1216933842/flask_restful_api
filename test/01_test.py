import  requests

import json
url = 'http://localhost:5000/v1/client/register'
payload = {'account':'aaaa','nickname':'xiaoming','email': 'data','password':'123456ssddds','type':101}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r)