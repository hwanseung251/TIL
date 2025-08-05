import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    # 문제에서 소수는 2,3,5,7,11 만 사용하므로 소수 리스트를 생성한다
    decimal_lst = [2, 3, 5, 7, 11]
    # a,b,c,d,e가 순서대로 저장될 result리스트를 생성한다
    result = []

    # 소수리스트를 활용해 포문을 돌면서
    for decimal_num in decimal_lst:
        cnt = 0
        # 주어진 소수로 N이 나눠질 수 있다면 계속해서 나눠준다
        while N % decimal_num == 0:
            # N은 소수로 한번 나눠진 후의 몫으로 계속 갱신해준다
            N //= decimal_num
            cnt += 1
        result.append(cnt)
    print(f"#{t} {' '.join(map(str, result))}")