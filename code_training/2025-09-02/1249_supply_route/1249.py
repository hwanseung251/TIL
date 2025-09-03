import sys
sys.stdin = open("input.txt")
import heapq

T = int(input())

for t in range(1, T+1):
    N = int(input())

    area = [list(map(int, input())) for _ in range(N)]
    inf = float("inf")
    dist = [[inf]*N for _ in range(N)]
    dist[0][0] = area[0][0]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    pq = [(0, 0, 0)]
    while pq:
        cost, x, y = heapq.heappop(pq)

        if cost > dist[x][y]:
            continue
        if x == N-1 and y == N-1:
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N:
                ncost = cost + area[nx][ny]
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(pq, (ncost, nx, ny))

    print(f"#{t} {dist[N-1][N-1]}")