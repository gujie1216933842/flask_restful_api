import  requests

import json
url = 'http://localhost:5000/v1/client/register'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r)