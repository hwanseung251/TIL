import sys
sys.stdin = open("input.txt")

#인접 행렬 + 스택
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬(adgacency matrix) 생성: V+1 크기 (노드를 1부터 사용)
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보를 인접행렬에 기록 (양방향)
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

def DFS_stack(start):
    stack = [start]
    visited = [0] * (V+1)

    while stack:
        current_node = stack.pop()

        if visited[current_node] == 0:
            visited[current_node] = 1
            print(current_node, end = "")

            for next_node in range(V, 0, -1):
                if (adj_matrix[current_node][next_node] == 1) and (visited[next_node] == 0):
                    stack.append(next_node)

DFS_stack(1)