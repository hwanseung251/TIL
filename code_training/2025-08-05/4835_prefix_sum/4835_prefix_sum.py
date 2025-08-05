import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # 구간 합의 최댓값과 최솟값을 저장할 변수를 생성해준다
    max_value = 0
    min_value = float('inf')

    # 구간 M 기준으로 왼쪽에서 M만큼 떨어진 부분부터 포문을 시작한다
    for i in range(M-1, N):
        prefix_sum = 0
        # 그리고 왼쪽으로 M만틈 떨어진 값들을 하나씩 더해서 현재의 구간합 prefix_sum을 구해준다
        for m in range(M):
            prefix_sum += ai[i-m]
        # 최댓값과 최소값을 갱신해준다
        max_value = max(max_value, prefix_sum)
        min_value = min(min_value, prefix_sum)
    print(f"#{t} {max_value-min_value}")