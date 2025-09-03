import sys
sys.stdin = open("input.txt")

bin_nums = input()

for i in range(0,len(bin_nums),7):
    bin_num = bin_nums[i:i+7]
    print(int(bin_num, 2), end=" ")