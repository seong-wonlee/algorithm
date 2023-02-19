# T = int(input())
lst = list(input().split())

stack = []
for i in lst:
    if i.isdigit():
        stack.append(int(i))
    if len(stack) >= 2:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif i == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b//a)
    elif i == '.':
        print(stack[-1])
        break
    else:
        print('error')





