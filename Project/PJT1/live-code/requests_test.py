import requests
from pprint import pprint

url = "https://fakestoreapi.com/carts"
data = requests.get(url).json()  # 조회 요청
pprint(data)  # 200: 정상 , 404: 그런 데이터는 우리 서버에 없다

import json

