import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(i, j):
    q = deque()
    visited = [[False] * 16 for _ in range(16)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    q.append((i, j))

    while q:
        ci, cj = q.popleft()
        visited[ci][cj] = True

        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0<=ni<16 and 0<=nj<16:
                if not visited[ni][nj] and miro[ni][nj] == 0:
                    visited[ni][nj] = True
                    q.append((ni, nj))
                if miro[ni][nj] == 3:
                    return True
    return False


for _ in range(10):
    T = int(input())
    miro = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                if bfs(i,j):
                    print(f"#{T} 1")
                else:
                    print(f"#{T} 0")