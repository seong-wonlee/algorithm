n = int(input())

num = list(input())
stack = []
postfix = ''
print(num)
# 후위표기식으로 바꾸기
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
    while stack:
        postfix += stack.pop()
print(postfix)

# 후위 표기식 계산
stack1 = []
for i in postfix:
    if i != '+':
        stack1.append(int(i))
    else:
        b = stack1.pop()
        a = stack1.pop()
        stack1.append(b+a)
print(stack1.pop())





