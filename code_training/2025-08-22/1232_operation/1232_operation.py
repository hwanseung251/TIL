import sys
sys.stdin = open("input.txt")

for t in range(1, 11):
    N = int(input())
    edge = [[0]]

    for _ in range(N):
        edge.append(list(input().split()))

    def tree(node):
        if len(edge[node]) == 2:
            return int(edge[node][1])

        left = tree(int(edge[node][2]))
        right = tree(int(edge[node][3]))
        if edge[node][1] == '+':
            return left + right
        if edge[node][1] == '-':
            return left - right
        if edge[node][1] == '*':
            return left * right
        if edge[node][1] == '/':
            return left // right


    print(f"#{t} {tree(1)}")