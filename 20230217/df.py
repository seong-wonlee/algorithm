while True:
    lst = input()
    if lst == '.':
        break
    stack = []
    ans = 'yes'
    for i in lst:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    ans = 'no'
                    break
            else:  # 스텍이 비어있음
                ans = 'no'
                break
        if i == ']':
            if stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    ans = 'no'
                    break
            else:  # 스텍이 비어있음
                ans = 'no'
                break
        if len(stack) == 0:
            ans = 'yes'
        else:
            ans = 'no'
    print(ans)
