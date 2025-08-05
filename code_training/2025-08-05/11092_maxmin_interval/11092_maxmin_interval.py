import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    # 문제에서 각 위치를 index+1을 요구하므로 편의상 0번인덱스는 사용하지 않는다
    ai = [0] + list(map(int, input().split()))

    # 인덱스1의 값과 인덱스 번호를 각각 최대최소값과 인덱스로 할당한다
    max_value, max_index = ai[1], 1
    min_value, min_index = ai[1], 1

    # 포문을 돌면서 각 최대최소값과 인덱스를 갱신한다.
    for i in range(2, N+1):
        # 최댓값은 값이 같으면 뒤에인덱스를 사용할것이므로 >= 사용
        if ai[i] >= max_value:
            max_value, max_index = ai[i], i
        # 최솟값은 값이 같으면 앞에인덱스를 사용할것이므로 < 사용
        elif ai[i] < min_value:
            min_value, min_index = ai[i], i

    print(f"#{t} {abs(max_index - min_index)}")