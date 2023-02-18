word = list(input())
# print(word)

isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}

stack = []
postfix = ''
for i in word:
    # 알파벳 일 때
    if i.isalpha():
        postfix += i
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while True:
            a = stack.pop()
            if a == '(':
                break
            postfix += a
    else:  # 다른 연산자일 때 우선순위 따져서 들어갈 연산자가 우선순위가 더 낮으면
        while stack and isp[stack[-1]] >= icp[i]:
            postfix += stack.pop()
        # 우선순위가 더 높으면
        stack.append(i)
    # 스택에 남아있는 애들 postfix 뒤에 붙이기
while stack:
    postfix += stack.pop()

print(postfix)




