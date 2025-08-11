import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T + 1):
    A, B = input().split()

    A_len = len(A)
    B_len = len(B)
    cnt = 0

    i = 0
    while i < (len(A)-B_len+1):
        if A[i:i+B_len] == B:
            cnt += 1
            i += B_len
        else:
            i += 1

    result = cnt + (A_len - B_len*cnt)
    print(f"#{t} {result}")
