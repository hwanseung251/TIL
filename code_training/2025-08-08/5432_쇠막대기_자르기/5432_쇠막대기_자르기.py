import sys

sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T + 1):
    lazer_stick = list(input())
    N = len(lazer_stick)

    # 레이저를 다른 기호로 구분해준다
    # "*"을 레이저로 사용하고
    # "x"로 대체한것은 무시한다
    for i in range(0, N - 1):
        if lazer_stick[i] == '(' and lazer_stick[i + 1] == ')':
            lazer_stick[i], lazer_stick[i + 1] = '*', 'x'

        # stack이라는 빈리스트를 만들어준다
        # 막대기 조각을 카운트할 변수를 생성한다
    stack = []
    cnt = 0

    # 괄호뭉치를 돌면서
    for p in lazer_stick:
        # 막대기 시작을 만나면 스택에 넣어준다
        if p == "(":
            stack.append(p)
        # 막대기 끝을 만나면 조각하나를 카운트해준다
        # 스택에서 하나를 pop해준다.
        elif p == ")":
            stack.pop()
            cnt += 1
        # '*'을 만나면 stack에 쌓인만큼 조각을 카운팅해준다.
        elif p == '*':
            cnt += len(stack)

    print(f"#{t} {cnt}")