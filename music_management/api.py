import requests
import json
URL = "http://127.0.0.1:8000/songapi/"

def get_data(id = None):
    data = { }
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,data =json_data)
    print(r.json())

#get_data()
def post_data():
    data = {
        'id':'4',
        'song_title':'top class desi 4',
        'album':'punjabi',
        'artist': 'jimmi Kaler!',
        'audio':'',
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
#post_data()

def update_data():
    data = {
        'id':'2',
        'song_title':'top class desi 2',
        'album':'punjabi',
        'artist':'kaka2',
        #'audio':'',
    }
    json_data = json.dumps(data)
    r = requests.put(url =URL,data = json_data)
    print(r.json())
update_data()

def delete_data():
    data = {'id':'1'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data = json_data)
    print(r.json())

#delete_data()
