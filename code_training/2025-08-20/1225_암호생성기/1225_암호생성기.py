import sys
sys.stdin = open("input.txt")

from collections import deque

for _ in range(10):
    t = int(input())

    numbers = deque(list(map(int, input().split())))

    switch = True
    while switch:
        for i in range(1,6):
            item = numbers.popleft()
            item -= i

            # 만약 0보다 작아지면 break
            if item <= 0:
                # 0으로 유지하고 뒤에 넘기면서 종료
                item = 0
                numbers.append(item)
                switch = False
                break

            numbers.append(item)

    print(f"#{t} {' '.join(map(str, numbers))}")