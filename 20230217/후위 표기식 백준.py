word = list(map(str, input()))

isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}

stack = []
postfix = ''
for i in word:
    # 알파벳일때
    if i != '(' and i != '+' and i != '-' and i != '*' and i != '/':
        postfix += i
    else:   # 연산자일때
        if i == ')':
            a = stack.pop()
            if a == '(':
                break
        else :  # 다른 연산자일 때 우선순위 따져서
            while stack and isp[stack[-1]] >= icp[i]:
                postfix += stack.pop()
            # 그게 아니면
            if i != '(' and i != ')':
                stack.append(i)


# 스택에 남아있는 애들 postfix 뒤에 붙이기
while stack:
    postfix += stack.pop()

print(postfix)




