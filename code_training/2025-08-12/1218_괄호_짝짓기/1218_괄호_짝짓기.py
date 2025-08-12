import sys
sys.stdin = open("input.txt")

# 괄호 짝 딕셔너리 생성
my_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}

for t in range(1,11):
    N = int(input())
    parentheses = list(input())
    stack = []

    for p in parentheses:
        # 만약 딕셔너리 key에 해당하는 값이면(여는괄호이면) 스택에 추가
        if p in my_dict.keys():
            stack.append(p)
        # 만약 딕셔너리 value에 해당하는 값이면(닫는괄호면)
        elif p in my_dict.values():
            # 스택의 길이가 0이면 실패
            if len(stack) == 0:
                print(f"#{t} 0")
                break
            # 0이상이면 pop하고 짝꿍체크
            else:
                pop_item = stack.pop()
                if my_dict[pop_item] != p:
                    print(f"#{t} 0")
                    break
    else:
        if len(stack) == 0:
            print(f"#{t} 1")
        else:
            print(f"#{t} 0")