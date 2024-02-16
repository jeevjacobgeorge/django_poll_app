import requests
import json
URL = 'http://127.0.0.1:8000/studapi/'

data = {
    'name': 'Rohith',
    'roll': '13',
    'city': 'Uganda'
}

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)

msg = r.json()
print("This is frontend speaking Status of submitting", msg)

