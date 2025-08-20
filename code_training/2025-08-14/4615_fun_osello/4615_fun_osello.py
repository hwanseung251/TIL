import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0] * (N+1) for _ in range(N+1)]
    mid = (N+1) // 2
    for i in range(mid, mid+2):
        for j in range(mid, mid+2):
            if i == j:
                board[i][j] = 2
            else:
                board[i][j] = 1

    di = [0, 0, 1, -1, 1, -1, -1, 1]
    dj = [1, -1, 0, 0, 1, -1, 1, -1]

    for _ in range(M):
        i, j, color = map(int, input().split())

        if board[i][j] != 0:
            continue

        # 주어진 좌표로 세로, 가로, 대각선 탐색하며 정점(본인의컬러) 발견하기
        # 발견하면 그 사이에 있는 돌은 모두 컬러 변경
        any_flipped = False
        for d in range(8):
            plus = 1
            change_lst = []
            while True:
                ni, nj = i + di[d]*plus, j + dj[d]*plus

                if not (1 <= ni <= N and 1 <= nj <= N):
                    change_lst = []
                    break

                next_color = board[ni][nj]
                if next_color == 0:
                    change_lst = []
                    break

                elif next_color != color:
                    change_lst.append((ni, nj))
                    plus += 1

                else:
                    if change_lst:
                        for r, c in change_lst:
                            board[r][c] = color
                        any_flipped = True

                    break

        if any_flipped:
            board[i][j] = color

    black = sum(row.count(1) for row in board)
    white = sum(row.count(2) for row in board)
    print(f"#{t} {black} {white}")