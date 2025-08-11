import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    rusia = [list(input()) for _ in range(N)]

    min_paint = N * M

    # 화이트의 범위
    for i in range(0, N-2):
        # 블루의 최대 범위
        for j in range(i+1, N-1):
            paint = 0

            # 화이트 범위만큼 이중포문돌면서 페인트 횟수 카운팅
            for r in range(0, i+1):
                for c in range(M):
                    if rusia[r][c] != 'W':
                        paint += 1
            # 블루 범위만큼 이중포문돌면서 페인트 횟수 카운팅
            for r in range(i+1, j+1):
                for c in range(M):
                    if rusia[r][c] != 'B':
                        paint += 1
            # 레드 범위만큼 이중포문돌면서 페인트 횟수 카운팅
            for r in range(j+1, N):
                for c in range(M):
                    if rusia[r][c] != 'R':
                        paint += 1
            min_paint = min(min_paint, paint)
    print(f"#{t} {min_paint}")