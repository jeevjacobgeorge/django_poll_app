import requests
import json

URL = 'http://127.0.0.1:8000/studapi/'

def get_data(id_value = None):
    data = {}
    if id_value is not None:
        data = {'id':id_value}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    response = r.json()
    print(response)

# get_data()

def post_data():
    data = {
        'name': 'Akshay',
        'roll': '69',
        'city': 'tvm'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# post_data()
def update_data():
    data = {
        'id':'6',
        'name': 'Akshay',
        'roll': '6'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data(n):
    data = {
        'id':n
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

delete_data(8)