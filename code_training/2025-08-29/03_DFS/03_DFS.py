import sys
sys.stdin = open("input.txt")

V, E = map(int, input().split())
data = list(map(int, input().split()))
visited = [False] * (V+1)
adj_lst = [[] for _ in range(V+1)]

for e in range(E):
    n1, n2 = data[e * 2], data[e * 2 + 1]
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

for i in range(1, V+1):
    adj_lst[i].sort(reverse=True)


def dfs(start):
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end="")

            for next_node in adj_lst[node]:
                if not visited[next_node]:
                    stack.append(next_node)


dfs(1)
