import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*(N+1) for _ in range(N+1)]

    # 가운데 w,b 돌 놓고 시작함
    mid = N//2
    board[mid][mid] = 2
    board[mid+1][mid+1] = 2
    board[mid+1][mid] = 1
    board[mid][mid+1] = 1

    di = [0, 0, 1, -1, 1, 1, -1, -1]
    dj = [1, -1, 0, 0, 1, -1, 1, -1]

    for _ in range(M):
        i, j, color = map(int, input().split())

        if board[i][j] != 0:
            continue
        # 돌을 놓았는지 못놓았는지 체크
        # 돌을 놓았으면 본인위치도 컬러변경해줄것임
        flip_check = False
        ## 8 방향모두 살펴보면서 돌을 놓을수 있으면 놓고 돌 변경
        for d in range(8):
            plus = 1
            flip_list = []
            while True:
                ni = i + di[d] * plus
                nj = j + dj[d] * plus
                if not (1<=ni<=N and 1<=nj<=N):
                    break
                # 옆이0인경우
                elif board[ni][nj] == 0:
                    break
                # 옆이 나랑 다른 컬러인 경우
                elif board[ni][nj] != color:
                    flip_list.append((ni, nj))
                    plus += 1
                # 나랑 같은 색상인 경우
                else:
                    # 바꿀게 있는 상황이면
                    if flip_list:
                        for r, c in flip_list:
                            board[r][c] = color
                            flip_check = True
                    break
        if flip_check:
            board[i][j] = color

    black = sum(row.count(1) for row in board)
    white = sum(row.count(2) for row in board)
    print(f"#{t} {black} {white}")