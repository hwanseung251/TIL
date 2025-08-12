import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    parentheses = list(input())
    stack = []
    # 하나씩 가져와서
    for p in parentheses:
        # 여는 괄호면 스택에 추가
        if p == '(':
            stack.append(p)
        # 닫는 괄호면 기존 스택에 값이 있는지 확인
        elif p == ')':
            # 스택에 값이 없으면 잘못된 괄호
            if len(stack) == 0:
                print(f"#{t} -1")
                break
            # 값이 있으면 짝이므로 pop해서 제외
            else:
                stack.pop()
    else:
        if len(stack) != 0:
            print(f"#{t} -1")
        else:
            print(f"#{t} 1")