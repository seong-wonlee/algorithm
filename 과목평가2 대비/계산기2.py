# 후위표기식 변환
T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = list(input())
    # print(lst)
    stack = []
    postfix = ''
    isp = {'(': 0, '*':2, '/':2, '+':1, '-':1}
    icp = {'(': 3, '*':2, '/':2, '+':1, '-':1}
    for i in lst:
        if i.isdigit():
            postfix += i
            # print(postfix)
        else: # 연산자이면
            # 스택에 연산자가 있으면
            while stack and isp[stack[-1]] >= icp[i]:
                postfix += stack.pop()
            stack.append(i)
    while stack:
        postfix += stack.pop()
    # print(postfix)

    # 후위 표현식 계산
    stack = []
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(b+a)
        elif i == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(b*a)
    print(f'#{tc} {stack[-1]}')












