import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    # 큰 배열안에 작은배열을 순회하며 그 합중 최댓값을 구한다
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            cnt = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    cnt += arr[p][q]
            max_value = max(max_value, cnt)

    print(f"#{t} {max_value}")