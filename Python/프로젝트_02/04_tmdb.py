# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# 8854669b886a6c07c12ea947bcc2311d

import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/1414'
# api_key 발급받아서 각자 키를 넣어주세요.
params = {
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'language': 'ko-KR'
}

response = requests.get(BASE_URL + path, params = params).json()
print(response)