import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    ai = input()

    # 몇번 등장하는지 카운트하는 딕셔너리 생성하고 값저장
    cnt_dict = {}
    for num in ai:
        if num not in cnt_dict:
            cnt_dict[num] = 1
        else:
            cnt_dict[num] += 1

    # 중복 횟수 최댓값 변수 0으로 지정
    max_value = 0

    # 카운트 딕셔너리 포문 돌면서 최대 등장하는 숫자 갱신
    # 만약 중복으로 등장하면 숫자가 큰 값으로 갱신
    for k, v in cnt_dict.items():
        if max_value < int(v):
            max_value = int(v)
            max_key = k
        elif max_value == int(v):
            if int(max_key) < int(k):
                max_key = k
    print(f"#{t} {max_key} {max_value}")

