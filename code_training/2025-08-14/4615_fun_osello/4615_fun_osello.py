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
                board[i][j] = 'W'
            else:
                board[i][j] = 'B'
    print(board)

    color_dict = {
        1 : 'B',
        2 : 'W',
    }
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, 1, -1]

    for _ in range(M):
        i, j, color = map(int, input().split())
        board[i][j] = color_dict.get(color)

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            nni, nnj = i + di[d]*2, j + dj[d]*2
            if 0<=ni<N and 0<=nj<N and 0<=nni<N and 0<=nnj<N:
                if (
                    color == 1
                    and board[ni][nj] == color_dict.get(2)
                    and board[nni][nnj] == color_dict.get(color)
                ):
                    board[ni][nj] = not color_dict.get(color)

                elif color == 2 and board[ni][nj] == color_dict.get(1):
                    board[ni][nj] = color_dict.get(color)
    print(board)