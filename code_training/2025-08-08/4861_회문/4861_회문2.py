import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    rotate_string = [list(input()) for _ in range(N)]
    found = False

    for i in range(N):
        for j in range(0, N-M+1):

            if rotate_string[i][j:j+M] == rotate_string[i][j:j+M][::-1]:
                print(f"#{t} {''.join(rotate_string[i][j:j+M])}")
                found = True

            if not found:
                my_str = []
                for k in range(M):
                    my_str.append(rotate_string[j+k][i])
                if my_str == my_str[::-1]:
                    print(f"#{t} {''.join(my_str)}")
                    found = True
