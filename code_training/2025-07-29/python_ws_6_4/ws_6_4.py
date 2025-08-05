# 아래 함수를 수정하시오.
def get_keys_from_dict(dict):
    '''
    dict을 입력받고 key값을 list로 반환하는 함수
    '''
    result = []
    for key in dict.keys():
        result.append(key)
    return result
result = []
def get_all_keys_from_dict(dict):
    '''
    전역 변수로 리스트 result로 불러오고 dict 키 값을 result에 저장.
    만약 중첩된 딕셔너리가 있다면 재귀호출함
    '''
    global result
    for k in dict.keys():
        if type(k) == 'dict':
            return get_all_keys_from_dict(k)
        else:
            result.append(k)
    return result
my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']

