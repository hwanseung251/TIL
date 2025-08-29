import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
island = [list(map(int, list(input()))) for _ in range(N)]
chk = [[False] * M for _ in range(N)]
cnt = 0


def dfs(r, c):
    stack = [(r, c)]
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, 1, -1]

    while stack:
        i, j = stack.pop()
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if island[ni][nj] == 1 and chk[ni][nj] == False:
                    chk[ni][nj] = True
                    stack.append((ni, nj))
    return 1


for i in range(N):
    for j in range(M):
        if island[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt += dfs(i, j)

print(cnt)