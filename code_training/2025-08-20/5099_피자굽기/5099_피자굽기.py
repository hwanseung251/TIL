import sys
sys.stdin = open("input.txt")

from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = [0] + list(map(int, input().split()))
    fire_pit = deque()

    # N개의 크기 화덕에 피자를 가득 채운다
    for i in range(1,N+1):
        fire_pit.append((i, pizzas[i]))
    # 현재 화덕에 들어가지 않은 피자 번호(가장 앞번호)
    current_pizza_num = N+1

    while len(fire_pit) > 1:
        # 피자를 꺼내 치즈 // 2 하기
        num, pizza = fire_pit.popleft()
        # 다 녹았으면
        if pizza // 2 == 0:
            # 새로운 피자추가(아직 새로운 피자가 있는 경우)
            if current_pizza_num < M+1:
                fire_pit.appendleft((current_pizza_num, pizzas[current_pizza_num]))
                current_pizza_num += 1
                # 화덕을 돌려준다
                fire_pit.rotate(-1)

        else:
            # 다 녹지 않았으면 다시 //2하여 넣어준다
            fire_pit.appendleft((num, pizza//2))
            # 화덕을 돌려준다
            fire_pit.rotate(-1)

    print(f"#{t} {fire_pit.popleft()[0]}")
