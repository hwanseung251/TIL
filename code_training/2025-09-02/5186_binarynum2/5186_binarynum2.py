import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    decimal_num = float(input())
    bits = []
    # i = -1 … -12를 돌며 2⁻¹, 2⁻², …, 2⁻¹² 순서대로 검사
    # 남은 값이 그 자리값 이상이면 1을 찍고 그만큼 빼기, 아니면 0
    for i in range(-1, -13, -1):
        if decimal_num >= (2 ** i):
            bits.append('1')
            decimal_num -= (2 ** i)
        else:
            bits.append('0')

        if decimal_num == 0:
            result = "".join(bits)
            break
    else:
        result = "overflow"
    print(f"#{t} {result}")