import os
import json
import random
import imghdr
import sys
import urllib.request
import urllib.parse

API_KEY = ''  # put your API key here
SEARCH_ENGINE_ID = ''  # you also have to generate a search engine token

if len(sys.argv) <= 1:
    print('Usage:')
    print('python fetch_google_image.py cat cute')
    exit()

q = ''

for arg in sys.argv[1:]:
    q += urllib.parse.quote(arg) + '+'

request = urllib.request.Request(
    'https://www.googleapis.com/customsearch/v1?key=' + API_KEY + '&cx=' +
    SEARCH_ENGINE_ID + '&q=' + q + '&searchType=image')

with urllib.request.urlopen(request) as f:
    data = f.read().decode('utf-8')
    
data = json.loads(data)
results = data['items']
url = random.choice(results)['link']
urllib.request.urlretrieve(url, './image')
imagetype = imghdr.what('./image')

if not type(imagetype) is None:
    os.rename('./image', './image.' + imagetype)
