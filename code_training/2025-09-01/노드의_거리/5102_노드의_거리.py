import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(node):
    q = deque()
    visited = [False] * (V+1)

    q.append((0, node))
    visited[node] = True

    while q:
        idx, current_node = q.popleft()
        if current_node == finish:
            return idx

        for next_node in adj_list[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((idx+1, next_node))

    return 0

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    start, finish = map(int, input().split())
    print(f"#{t} {bfs(start)}")