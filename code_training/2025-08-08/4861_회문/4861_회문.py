import sys
sys.stdin = open("input.txt")

def row_check(i, j):
    # 검사할 i,j인덱스가 들어오면 M만큼 행검사
    my_str = str_arr[i][j:j+M]
    # 만약 뒤집은 결과가 같다면
    if my_str == my_str[::-1]:
        # True와 결괏값 반환
        return True, ''.join(my_str)
    # 그렇지 않으면 False와 빈문자열 반환
    return False, ""

def column_check(i, j):
    # 검사할 i,j인덱스가 들어오면
    # 열방향으로 M만큼 열검사
    my_str = [str_arr[p][j] for p in range(i, i+M)]
    if my_str == my_str[::-1]:
        return True, ''.join(my_str)
    return False, ""

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    str_arr = [list(input()) for _ in range(N)]

    found = False
    for i in range(N):
        for j in range(N - M + 1):
            result = row_check(i, j)
            if result[0]:
                print(f"#{t} {result[1]}")
                found = True
                break
            result = column_check(j, i)  # 세로 방향은 인덱스를 바꿔서 줘야함
            if result[0]:
                print(f"#{t} {result[1]}")
                found = True
                break
        if found:
            break