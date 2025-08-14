import sys
sys.stdin = open("input.txt")

T = int(input())

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

for t in range(1, T+1):
    infix = input()
    print(f"#{t} {to_postfix(infix)}")