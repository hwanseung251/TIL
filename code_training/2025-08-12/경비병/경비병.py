import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            # 경비를 발견하면 탐색 시작
            if arr[i][j] == 2:
                for d in range(4):
                    # 기둥을 발견한 이후로는 그 방향으로 더이상 체크하지 않음
                    no_pillar = True
                    for k in range(1,N):
                        # 아직 기둥이 나오지 않았다면
                        if no_pillar:
                            ni = i + di[d]*k
                            nj = j + dj[d]*k
                            if 0<=ni<N and 0<=nj<N:
                                if arr[ni][nj] != 1:
                                    # 경비한테 발각되는 곳은 3으로 치환
                                    arr[ni][nj] = 3
                                else:
                                    # 기둥을 발견
                                    no_pillar = False
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f"#{t} {cnt}")