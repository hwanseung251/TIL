import sys
sys.stdin = open("input.txt")

T = 10

for t in range(1, T+1):
    tc = int(input())

    arr = [list(input()) for _ in range(100)]

    max_len = 0
    switch = True
    if switch:
        for N in range(100, 0, -1):
            if switch:
                for i in range(100):
                    if switch:
                        for j in range(100 - N + 1):
                            if arr[i][j:j + N] == arr[i][j:j + N][::-1]:
                                max_len = N
                                switch = False
                            palindrome = ''
                            for k in range(N):
                                palindrome += arr[j + k][i]
                            if palindrome == palindrome[::-1]:
                                max_len = N
                                switch = False


    print(f"#{tc} {max_len}")