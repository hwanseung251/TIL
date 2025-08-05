import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    number = input()

    counting_arr = [0] * 12

    for num in number:
        if int(num) == 0:
            counting_arr[10] += 1
        else:
            counting_arr[int(num)] += 1

    tri = run = 0
    i = 0
    while i < 12:
        if counting_arr[i] >= 3:
            counting_arr[i] -= 3
            tri += 1
            continue


        if (counting_arr[i] >= 1) and (counting_arr[i+1] >= 1) and (counting_arr[i+2] >= 1):
            counting_arr[i] -= 1
            counting_arr[i+1] -= 1
            counting_arr[i+2] -= 1
            run += 1
            continue
        i += 1
    if (tri + run) == 2:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
