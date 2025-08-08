import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    my_str = list(input())

    center = len(my_str)//2

    new_lst = my_str.copy()
    for i in range(center):
        new_lst[i], new_lst[-1-i] = my_str[-1-i], new_lst[i]


    if my_str == new_lst:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")