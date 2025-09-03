import sys
sys.stdin = open("input.txt")

T = int(input())

secret = {'0': '001101',
 '1': '010011',
 '2': '111011',
 '3': '110001',
 '4': '100011',
 '5': '110111',
 '6': '001011',
 '7': '111101',
 '8': '011001',
 '9': '101111'}

for t in range(1, T+1):
    hex_num = input()
    bin_num = ''.join(format(int(h, 16), '04b') for h in hex_num)
    print(f"#{t}", end=" ")
    i = 0
    while i < len(bin_num)-6:
        for k, v in secret.items():
            if bin_num[i:i+6] == v:
                print(k, end=" ")
                i += 6
                break
        else:
            i += 1

    print()