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
        # pop 이후에 방문처리
        if not visited[node]:
            visited[node] = True
            # 아직 방문하지 않은 노드이면 프린트
            print(node, end="")

            for next_node in adj_lst[node]:
                if not visited[next_node]:
                    stack.append(next_node)

# def dfs(start):
#     stack = [start]
#     visited[start] = True  # 스택에 넣을 때 방문 체크
#
#     while stack:
#         print(stack)
#         node = stack.pop()
#         print(node, end="")
#
#         for next_node in adj_lst[node]:
#             if not visited[next_node]:
#                 visited[next_node] = True  # 여기서 방문 체크
#                 stack.append(next_node)

"""
append하면서 방문처리를 하게되면
해당 예시에서 5번 노드는 2번 노드가 호출될때 stack에 먼저 들어가게됨.
그런데 6번 노드가 호출이 될 때 7,5 순서대로 stack에 들어가야하는데 5가 이미 방문처리 되어 있어서 7만들어감
즉 5가먼저 print되어야 하는데 7이 먼저 print 되게됨.(5는 아직 출력은 안됬으나 방문처리가 된 상태..)

그래서 pop함과 동시에 방문처리를 해주고 print 를 해주면 낮은 번호대로 print 될 수 있다. 
"""
dfs(1)