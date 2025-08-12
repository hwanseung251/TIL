import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    my_str = list(input())
    stack = []

    for s in my_str:
        # 스택에 값이 없으면 스택에 값 추가
        if len(stack) == 0:
            stack.append(s)
        else:
            # 스택 값이 있으면 pop하고 그 값을 변수에 저장해둠
            pop_item = stack.pop()
            # pop한 변수와 현재 검사하는 문자가 서로 다르면 다시 순서대로 스택에 다시 넣음
            # 만약 값이 같으면 중복을 제거하는 과정
            if pop_item != s:
                stack.extend((pop_item, s))
    print(f"#{t} {len(stack)}")

