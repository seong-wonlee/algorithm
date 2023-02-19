T = 10

for tc in range(1, T +1):
    # 후위 표기식으로 변환
    def get_postfix(lst, n):    # lst : 변환전 n = 문자개수
        isp = {'+': 1, '*': 2}
        icp = {'+': 1, '*': 2}
        stack = []
        postfix = ' '
        for i in lst:
            if i.isdigit() :    # 피연산자이면
                postfix += i
            else:               # 연산자이면
                if i == ')':
                    char = stack.pop()
                    if char == '(':
                        break
                else:   # 다른 연산자이면
                    while stack and isp[stack[-1]] >= icp[i]:
                        postfix += stack.pop()
                    stack.append(i)
        while stack:    # 스택에 남아있으면 더하기
            postfix += stack.pop()

        return postfix

    # 후위 표기식 계산
    def cal_postfix(postfix):
        stack = []
        for i in postfix:
            if i.isdigit():
                stack.append(i)
            if i == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b*a)
            if i == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
        return stack[-1]

    N = int(input())
    word = list(input())
    ans = get_postfix(word, N)
    print(f'#{tc}',cal_postfix(ans))








