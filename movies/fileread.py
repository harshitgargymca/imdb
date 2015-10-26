import json
import urllib2
import requests
from pprint import pprint

import requests
import json
with open('imdb.json') as json_file:
    json_data = json.load(json_file)
    pprint (json_data)

headers = {'Content-Type' : 'application/json'}

for x in json_data:
	r = requests.post('http://127.0.0.1:8000/api/v1/movies/', data=json.dumps(x), headers=headers)
	print r