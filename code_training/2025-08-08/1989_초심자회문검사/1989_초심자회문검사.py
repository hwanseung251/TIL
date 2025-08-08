import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    vocab = list(input())

    if vocab == vocab[::-1]:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")