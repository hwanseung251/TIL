import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 폭발이 가장 큰 값을 저장할 변수
    max_value = 0
    for i in range(N):
        for j in range(M):
            # 폭발할 범위는 현재 지점의 폭탄값
            bomb_range = area[i][j]
            # 현재지점에서 폭발이 일어날 변수에 현재 지점 폭발 값 넣음
            total = bomb_range

            # 델타 탐색 + 폭발할 범위를 탐색
            for d in range(4):
                for p in range(1,bomb_range+1):
                    ni = i + di[d]*p
                    nj = j + dj[d]*p
                    if 0<=ni<N and 0<=nj<M:
                        total += area[ni][nj]
            # 가장 큰 폭발 값 갱신
            max_value = max(total, max_value)
    print(f"#{t} {max_value}")