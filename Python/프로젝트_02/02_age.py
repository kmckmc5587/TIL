# http://api.agify.io?name=michael

import requests

URL = 'https://api.agify.io'
params = {
    'name' : 'minchan'
}
response = requests.get(URL, params = params).json()
print(response)