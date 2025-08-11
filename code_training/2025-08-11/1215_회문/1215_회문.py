import sys
sys.stdin = open("input.txt")

T = 10

for t in range(1,T+1):
    N = int(input())

    arr = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                cnt += 1

            palindrome = ''
            for k in range(N):
                palindrome += arr[j+k][i]
            if palindrome == palindrome[::-1]:
                cnt += 1
    print(f"#{t} {cnt}")
