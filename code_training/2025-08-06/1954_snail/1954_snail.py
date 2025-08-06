import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # 이미 지나간 배열을 체크해주는 체크박스 배열
    chk = [[False]*N for _ in range(N)]

    #달팽이는 우 하 좌 상 을 반복한다
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    #while 문의 종료 조건이면서 arr에 증가하는 숫자를 입력해주는 변수
    total_len = 0

    # 현재 배열의 위치 i,j
    i = 0
    j = 0

    # 방향 전환할 변수
    d = 0
    while total_len < (N*N):
        # total_len 을 증가시켜주면서 배열에 값을 넣어주고 chk박스에 체크해준다
        total_len += 1
        arr[i][j] = total_len
        chk[i][j] = True

        # 다음 이동할 곳을 이동해주고 다른 변수에 임의로 넣어놓는다
        # d가커지면서 리스트를 반복하도록 나머지를 활용해준다.
        ni = i + di[d%4]
        nj = j + dj[d%4]
        # 배열에 벗어나지 않고 아직 방문한 곳이 아니면
        if 0<=ni<N and 0<=nj<N and chk[ni][nj] == False:
            # 완전히 이동해준다
            i, j = ni, nj

        else:
            # 그렇지 않으면 방향을 전환해주고 그 방향으로 이동해준다
            d += 1
            ni = i + di[d % 4]
            nj = j + dj[d % 4]
            i, j = ni, nj

    print(f"#{t}")
    for i in range(N):
        print(" ".join(map(str, arr[i])))

