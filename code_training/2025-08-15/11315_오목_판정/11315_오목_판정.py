import sys
sys.stdin = open("input.txt")

T = int(input())

def check_omok(arr):
    arr_90 = list(map(list, zip(*arr[::-1])))
    target = 'ooooo'

    for i in range(N):
        if target in "".join(arr[i]):
            return 'YES'
        elif target in "".join(arr_90[i]):
            return 'YES'

    for i in range(0, N-4):
        for j in range(0, N-4):
            my_str = ""
            for k in range(5):
                my_str += arr[i + k][j + k]
                if target in my_str:
                    return 'YES'
    for i in range(0, N-4):
        for j in range(4, N):
            my_str = ""
            for k in range(5):
                my_str += arr[i + k][j - k]
                if target in my_str:
                    return 'YES'

    return 'NO'

for t in range(1, T+1):
    N = int(input())

    board = [list(input()) for _ in range(N)]
    result = check_omok(board)

    print(f"#{t} {result}")