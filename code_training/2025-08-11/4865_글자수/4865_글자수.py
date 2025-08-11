import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    max_value = 0
    for s in str1:
        cnt = 0
        for ss in str2:
            if s == ss:
                cnt += 1
        max_value = max(max_value, cnt)

    print(f"#{t} {max_value}")
