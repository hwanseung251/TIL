import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    ts, tN = input().split()

    nums_dict = {
               "ZRO":0,
               "ONE":1,
               "TWO":2,
               "THR":3,
               "FOR":4,
               "FIV":5,
               "SIX":6,
               "SVN":7,
               "EGT":8,
               "NIN":9
    }
    nums_dict_reversed = {
        0: "ZRO",
        1: "ONE",
        2: "TWO",
        3: "THR",
        4: "FOR",
        5: "FIV",
        6: "SIX",
        7: "SVN",
        8: "EGT",
        9: "NIN"
    }
    input_nums = input().split()

    for i in range(int(tN)):
        input_nums[i] = nums_dict[input_nums[i]]

    input_nums.sort()

    for i in range(int(tN)):
        input_nums[i] = nums_dict_reversed[input_nums[i]]

    print(f"{ts} {' '.join(input_nums)}")