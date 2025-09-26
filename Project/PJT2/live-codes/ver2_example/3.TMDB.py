import requests
from pprint import pprint
from dotenv import load_dotenv
import os

# 환경변수 파일을 읽어오겠다 (.env 파일을 자동으로 READ)
load_dotenv()

API_KEY = os.getenv('TMDB_API_KEY')

url = "https://api.themoviedb.org/3/movie/popular"

params = {
    'language': 'ko-KR',
    'page': 1
}

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers, params=params)

pprint(response.text)
