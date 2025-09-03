import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, hex_num = input().split()

    bin_num = "".join(format(int(h, 16), '04b') for h in hex_num)
    print(f"#{t} {bin_num}")

