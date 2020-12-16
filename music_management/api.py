import requests
import json
URL = "http://127.0.0.1:8000/songcreate/"

data = {
    'id':'2',
    'song_title':'top class desi 2',
    'album':'punjabi',
    'artist': 'jimmi Kaler',
    'audio_file':'',
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)