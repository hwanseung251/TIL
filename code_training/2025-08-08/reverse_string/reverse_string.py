import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    str_ = list(input())

    # 중심을 설정하고
    center = len(str_) // 2
    # 위치교환을 해준다
    for i in range(center):
        str_[i], str_[-1-i] = str_[-1-i], str_[i]

    print(f"#{t} {''.join(str_)}")