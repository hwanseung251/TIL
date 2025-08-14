stack = [0] * 100
top = -1

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 밖에 있을때의 우선 순위 (클수록 높음)
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1} # 스택안에서의 우선 순위 ( " )

infix = '(6+5*(2-8)/2)'
postfix = ''

for token in infix:
    if token not in '(+-*/)':
        postfix += token
    elif token == ')': # 여는 괄호를 만날때까지 pop
        while top>-1 and stack[top] != '(':
            top -= 1
            postfix += stack[top+1]
        if top != -1:
            top -= 1  # '('  버림
    else:
        if top == -1 or isp[stack[top]] < icp[token]:
            top += 1
            stack[top] = token
        elif isp[stack[top]] >= icp[token]:
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = token
    print(postfix)