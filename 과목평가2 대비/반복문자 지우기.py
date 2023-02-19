# T = int(input())
lst = list(map(str, input()))
# print(lst)

stack = []
for i in range(len(lst)):
    if not stack:
        stack.append(lst[i])
    elif stack:
        if lst[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(lst[i])

print(len(stack))
