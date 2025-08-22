import sys
sys.stdin = open("input.txt")

for _ in range(10):
    t, N = map(int, input().split())
    data = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]

    for i in range(N):
        n1, n2 = data[i*2], data[i*2 + 1]
        adj_list[n1].append(n2)

    for i in range(100):
        adj_list[i].sort()

    def DFS(start):
        my_stack = [start]
        visited = [0] * 100
        visited[start] = 1

        while my_stack:
            current_node = my_stack.pop()
            if current_node == 99:
                return 1

            for next_node in adj_list[current_node]:
                if visited[next_node] == 0:
                    my_stack.append(next_node)
                    visited[next_node] = 1

        return 0

    print(f"#{t} {DFS(0)}")
