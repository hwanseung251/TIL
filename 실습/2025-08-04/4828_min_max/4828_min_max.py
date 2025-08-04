import sys
sys.stdin = open('input.txt')

# 전체 케이스 변수
T = int(input())

for t in range(1, T + 1):
    # 각 케이스 변수들 할당
    N = int(input())
    ai = list(map(int, input().split()))

    # 최댓값과 최솟값 변수에 첫번째 값을 우선 넣어줌
    max_value = ai[0]
    min_value = ai[0]

    # 포문돌면서 값비교하고 최신화
    for i in range(1, N):
        if ai[i] > max_value:
            max_value = ai[i]
        elif ai[i] < min_value:
            min_value = ai[i]
    print(f"#{t} {(max_value - min_value)}")