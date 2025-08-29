import sys
sys.stdin = open("input.txt")
import heapq

T = 1

while True:
    N = int(input())
    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    INF = float("inf")
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = cave[0][0]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    pq = [(dist[0][0], 0, 0)]

    while pq:
        cost, i, j = heapq.heappop(pq)
        # 앞서 찾았던 경로가 더 최소일때
        if cost > dist[i][j]:
            continue

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                next_cost = cost + cave[ni][nj]
                if next_cost < dist[ni][nj]:
                    dist[ni][nj] = next_cost
                    heapq.heappush(pq, (next_cost, ni, nj))


    print(f"Problem {T}: {dist[N-1][N-1]}")

    T += 1