import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(node, g):
    q = deque()
    visited = [False] * (N+1)

    visited[node] = True
    q.append(node)

    while q:
        current_node = q.popleft()

        for next_node in g[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

    return visited

T = int(input())

for t in range(1, T+1):
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    r_graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        r_graph[b].append(a)

    result = [0] * (N+1)
    for i in range(1, N+1):
        tall_list = bfs(i, graph)
        small_list = bfs(i, r_graph)

        for j in range(1, N+1):
            if tall_list[j] or small_list[j]:
                result[i] += 1

    print(f"#{t} {result.count(N)}")

