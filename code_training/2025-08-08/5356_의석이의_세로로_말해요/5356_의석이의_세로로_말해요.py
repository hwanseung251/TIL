import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    print(f"#{t}", end = " ")
    board = [list(input()) for _ in range(5)]
    for j in range(15):
        for i in range(5):
            if 0<=j<len(board[i]):
                print(board[i][j], end ="")
    print()