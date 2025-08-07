import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    for i in range(1, 1 << N): # 1<<N 은 2^N
        result = 0

        for j in range(N):
            if i & (1 << j):
                result += arr[j]

        if result == 0:
            print(f"#{t} 1")
            break

    else:
        print(f"#{t} 0")
