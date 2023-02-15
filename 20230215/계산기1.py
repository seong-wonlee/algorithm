
T = 10
for tc in range(1, T+1):
    n = int(input())
    num = list(input())
    stack = []
    postfix = ''

    # 후위 표기식으로 바꾸기
    for i in num:
        # 숫자이면
        if i.isdigit():
            postfix += i
        else: # 연산자가 나오면
            if not stack:   # 스택이 비어있으면
                stack.append(i)
            else:   # 스택이 비어있지 않으면
                postfix += stack.pop()
                stack.append(i)
    while stack:    # 스택에 연산자가 남아있으면
        postfix += stack.pop()
    # print(postfix)

    # 후위 표기식 계산
    stack1 = []
    for i in postfix:
        if i.isdigit():
            stack1.append(int(i))
        else:
            b = stack1.pop()
            a = stack1.pop()
            stack1.append(b+a)
    print(f'#{tc} {stack1[-1]}')





