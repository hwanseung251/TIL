import sys
sys.stdin = open("input.txt")

import itertools
T = int(input())

def is_run(arr):
    return arr[0]+1 == arr[1] and arr[1] == arr[2]-1


def is_triplet(arr):
    # return arr[0] == arr[1] == arr[2]
    # set를 활용한 트리플렛 검사!!
    return len(set(arr)) == 1

for t in range(1, T+1):
    numbers = list(map(int, input()))

    # 순열로 줄세우고 set로 중복 제거
    for p in set(itertools.permutations(numbers)):
        one = p[:3]
        another = p[3:]

        if (is_run(one) or is_triplet(another)) and (is_run(one) or is_triplet(another)):
            print(f"#{t} 1")
            break
    else:
        print(f"#{t} 0")