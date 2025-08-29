import sys
sys.stdin = open("input.txt")


def dfs(i,j, engine_cost):
    global min_cost
    if i == N and j == N:
        min_cost = min(min_cost, engine_cost)
        return min_cost
    # 가지치기
    if min_cost < engine_cost:
        return

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 1<=ni<=N and 1<=nj<=N and visited[ni][nj] == False:
            # 내리막길
            if mountain[i][j] > mountain[ni][nj]:
                visited[ni][nj] = True
                dfs(ni,nj, engine_cost)
                visited[ni][nj] = False
            # 오르막길
            elif mountain[i][j] < mountain[ni][nj]:
                visited[ni][nj] = True
                plus = (mountain[ni][nj] - mountain[i][j])*2
                dfs(ni,nj, engine_cost+plus)
                visited[ni][nj] = False
            # 평지
            else:
                visited[ni][nj] = True
                dfs(ni, nj, engine_cost + 1)
                visited[ni][nj] = False

T = int(input())

for t in range(1, T+1):
    N = int(input())
    padding = [[0] * (N+1)]
    mountain = [[0] + list(map(int, input().split())) for _ in range(N)]
    mountain = padding + mountain

    visited = [[False] * (N+1) for _ in range(N+1)]

    min_cost = float("inf")
    visited[1][1] = True
    dfs(1,1,0)
    print(min_cost)