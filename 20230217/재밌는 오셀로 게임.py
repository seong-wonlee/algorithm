lst = list(map(str, input()))
print(lst)

stack = []
for i in lst:
    if i == '(' or i == '[':
        stack.append(i)
    if i == ')' or i == ']':
        stack.pop()




