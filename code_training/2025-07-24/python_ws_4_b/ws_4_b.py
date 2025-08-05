food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
for dic in food_list:
    종류, 이름 = dic.keys()
    if dic[이름] == '토마토':
        dic[종류] = '과일'
    elif dic[이름] == '자장면':
        print('자장면엔 고춧가루지')

    print(f"{dic[이름]} 은/는 {dic[종류]} (이)다.")

print(food_list)

n = 0
while n < 3:
    dic = food_list[n]
    종류, 이름 = dic.keys()
    if dic[이름] == '토마토':
        dic[종류] = '과일'
    elif dic[이름] == '자장면':
        print('자장면엔 고춧가루지')

    print(f"{dic[이름]} 은/는 {dic[종류]} (이)다.")
    n += 1
print(food_list)