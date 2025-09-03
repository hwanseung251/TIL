import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    # 0인 부분집합이 있는지 없는지 검사해줄 변수
    is_zero = False

    lst_len = len(lst)
    for i in range(1 << lst_len):
        subset = []
        for j in range(lst_len):
            if i & (1 << j):
                subset.append(lst[j])
        # 공집합이 아니고 합이 0인 부분집합이면
        if len(subset) and not sum(subset):
            # True로 변경
            is_zero = True

    if is_zero:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")