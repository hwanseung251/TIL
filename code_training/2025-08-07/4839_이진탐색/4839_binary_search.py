import sys
sys.stdin = open("input.txt")

def binary_search(P, target):
    start = 1
    end = P
    cnt = 0

    while start + 1 <= end:
        middle = (start + end)//2
        if middle == target:
            break
        elif target > middle:
            cnt += 1
            start = middle
        else:
            cnt += 1
            end = middle
    return cnt

T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())

    A_binary_search = binary_search(P, A)
    B_binary_search = binary_search(P, B)

    if A_binary_search > B_binary_search:
        print(f"#{t} B")
    elif A_binary_search < B_binary_search:
        print(f"#{t} A")
    else:
        print(f"#{t} 0")