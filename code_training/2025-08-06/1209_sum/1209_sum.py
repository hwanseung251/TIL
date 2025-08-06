import sys
sys.stdin = open("input_1.txt")

# 행을 기준으로 최댓값을 반환하는 함수
def max_row(matrix):
    max_value = 0
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += matrix[i][j]
        max_value = max(max_value, sum_row)
    return max_value

# 열을 기준으로 최댓값을 반환하는 함수
def max_columns(matrix):
    max_value = 0
    for j in range(100):
        sum_column = 0
        for i in range(100):
            sum_column += matrix[i][j]
        max_value = max(max_value, sum_column)
    return max_value

# 대각선을 기준으로 최댓값을 반환하는 함수
def max_Diagonal(matrix):
    sum_right_diagonal = 0
    sum_left_diagonal = 0
    for i in range(100):
        sum_right_diagonal += matrix[i][i]
        sum_left_diagonal += matrix[i][99-i]
    return max(sum_right_diagonal, sum_left_diagonal)

for _ in range(10):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 세가지 함수의 반환값중에 가장 큰 값을 구한다
    result = max(max_row(matrix), max_columns(matrix), max_Diagonal(matrix))
    print(f"#{T} {result}")

