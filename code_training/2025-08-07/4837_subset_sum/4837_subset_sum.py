import sys
sys.stdin = open('input.txt')
T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]

for t in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    for i in range(N):
        if N & (1 << i):
            result += A[i]

    if result == K:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")