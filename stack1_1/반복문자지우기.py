T= int(input())

for tc in range(1,T+1):
    word = list(map(str, input()))
    stack = []
    for i in range(0,len(word)):
        # 스텍이 비어있으면
        if len(stack) == 0:
            stack.append(word[i])
        # 스텍이 비어있지 않을 때
        else:
            if stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])

    print(f'#{tc}', len(stack))

