# import sys
# sys.stdin = open("input.txt")
import itertools
arr = list(range(10,0,-1))
for i in arr:
    for sub in list(itertools.combinations(arr, i)):
        if sum(sub) == 10:
            lst = list(sub)
            lst.sort()
            print(" ".join(map(str, lst)))
