T = int(input())

for tc in range(1, T+1):
    word = list(map(str, input()))
    stack = []
    ans = 1
    for i in word:
        if i == "(" or i == '{':
            stack.append(i)
        elif i == ")" or i == "}":
            if not stack:
                ans = 0
            else:
                if i == ')' and stack.pop() != '(':
                    ans = 0
                if i == '}' and stack.pop() != '{':
                    ans = 0
    if stack:
        ans = 0
    print(f'#{tc} {ans}')


