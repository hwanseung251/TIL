import sys
sys.stdin = open("input.txt")

for t in range(1,11):
    N = int(input())
    edge = [[0]]

    for _ in range(N):
        edge.append(list(input().split()))

    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(1, N+1):
        parent = int(edge[i][0])
        if len(edge[i]) == 4:
            left[parent] = int(edge[i][2])
            right[parent] = int(edge[i][3])
        elif len(edge[i]) == 3:
            left[parent] = int(edge[i][2])


    def inorder(node):
        if node != 0:
            inorder(left[node])
            print(edge[node][1], end="")
            inorder(right[node])
    print()
    print(f"#{t} ", end="")
    inorder(1)
