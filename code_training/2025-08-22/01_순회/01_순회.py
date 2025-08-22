import sys
sys.stdin = open("input.txt")

V = int(input())
E = V-1
edge = list(map(int, input().split()))

left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(E):
    parent, child = edge[i*2], edge[i*2+1]
    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child

def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])

preorder(1)


