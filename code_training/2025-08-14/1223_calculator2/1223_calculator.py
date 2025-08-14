import sys
sys.stdin = open("input.txt")

def to_postfix(infix):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    stack = []
    result = []

    for token in infix:
        if token.isalnum():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while (stack
                and stack[-1] != '('
                and precedence.get(stack[-1], 0) >= precedence.get(token, 0)
            ):
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())
    return "".join(result)

T = 10

for t in range(1, T+1):
    N = int(input())
    infix = input()

    postfix = to_postfix(infix)
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '*':
                stack.append(left * right)

    print(f"#{t} {stack.pop()}")