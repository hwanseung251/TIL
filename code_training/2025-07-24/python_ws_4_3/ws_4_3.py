import requests
from pprint import pprint as print
dummy_data = []
for i in range(1,11):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}')
    parsed_data = response.json()
    dic = {}

    if (-80 < float(parsed_data['address']['geo']['lat']) < 80) and (-80 < float(parsed_data['address']['geo']['lng']) < 80):
        dic['company'] = parsed_data['company']['name']
        dic['lat'] = parsed_data['address']['geo']['lat']
        dic['lng'] = parsed_data['address']['geo']['lng']
        dic['name'] = parsed_data['name']
        dummy_data.append(dic)
print(dummy_data)