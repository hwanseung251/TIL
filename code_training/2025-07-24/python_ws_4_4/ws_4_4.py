black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]
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


def create_user(lst):
    censored_user_list = {}
    for dic in lst:
        if censorship(dic['company'], dic['name']): # censorship검사로 True반환받으면
            censored_user_list[dic['company']] = [dic['name']] # 딕셔너리 추가해주고 반환
    return censored_user_list



def censorship(company, name): # 화사명과 이름을 인자로 받아서 블랙리스트에 있는 회사인지 비교하고
    if company in black_list:
        print(f"{company}소속의 {name} 은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다.') # 없으면 True 반환
        return True
    
result = create_user(dummy_data)
print(result)