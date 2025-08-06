import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 우, 하, 좌, 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 모든 지점에서 각각의 인접값들과 절대차를 모두 더해줄 변수
    total_sum = 0

    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                # 이동을 했을때 배열안에 있는 범위이면
                if 0<=ni<N and 0<=nj<N:
                    # abs사용 X -> 큰값에서 작은값을 뺀다
                    if arr[i][j] >= arr[ni][nj]:
                        total_sum += arr[i][j] - arr[ni][nj]
                    else:
                        total_sum += arr[ni][nj] - arr[i][j]

    print(f"#{t} {total_sum}")