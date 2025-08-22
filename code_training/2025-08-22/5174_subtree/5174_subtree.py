import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        parent, child = edge[i*2], edge[i*2+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    cnt = 0
    def preorder(node):
        global cnt
        if node != 0:
            cnt += 1
            preorder(left[node])
            preorder(right[node])

    preorder(N)

    print(f"#{t} {cnt}")
