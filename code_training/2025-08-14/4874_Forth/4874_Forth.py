import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    postfix = input().split()
    stack = []

    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        elif token == '.':
            if len(stack) != 1:
                print(f"#{t} error")
                break
            print(f"#{t} {int(stack.pop())}")
            break
        else:
            if len(stack) < 2:
                print(f"#{t} error")
                break
            else:
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(left / right)
    else:
        print(f"#{t} error")
