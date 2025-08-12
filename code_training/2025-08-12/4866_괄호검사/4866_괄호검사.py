import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    my_str = list(input())
    stack = []

    for s in my_str:
        # 여는 괄호면 스택에 추가
        if s in ['(', '{']:
            stack.append(s)
        # 닫는 괄호면 기존 스택에 값이 있는지 없는지 체크 ( 없으면 잘못된 괄호 )
        elif s in [')', '}']:
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            else:
                pop_item = stack.pop()
                # 스택에 값이 있으면 짝이 맞는 괄호인지 체크
                if s == ')':
                    if pop_item != '(':
                        print(f"#{t} 0")
                        break
                elif s == '}':
                    if pop_item != '{':
                        print(f"#{t} 0")
                        break
    else:
        if len(stack) == 0:
            print(f"#{t} 1")
        else:
            print(f"#{t} 0")
