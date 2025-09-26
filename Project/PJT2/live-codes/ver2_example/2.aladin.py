import requests
from pprint import pprint
# python-dotenv: 환경변수를 관리해주는 패키지
from dotenv import load_dotenv
import os

# 환경변수 파일을 읽어오겠다 (.env 파일을 자동으로 READ)
load_dotenv()

API_KEY = os.getenv('ALADIN_API_KEY')

url = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'ttbkey': API_KEY,
    'Query': '싸피',
    'QueryType': 'Title',
    'MaxResults': 10,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': 20131101
}

response = requests.get(url, params=params).json()
pprint(response)
