import requests
from pprint import pprint as print
dummy_data = []
for i in range(1,11):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}')
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])
print(dummy_data)