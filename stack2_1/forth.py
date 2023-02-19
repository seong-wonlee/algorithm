def forth():
    try:
        for num in nums:
            # 피연산자이면 스택에 푸시
            if num != '*' and num != '/' and num != '+' and num != '-':
                stack.append(num)
            # 연산자이면
            elif num == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b*a)
            elif num == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b+a)
            elif num == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            elif num == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b//a)
        if len(stack) == 1:
            return stack[-1]
        else:
            return 'error'
    except:
        return 'error'


T = int(input())
for tc in range(1, T+1):
    nums = list(input().split())
    nums.pop()
    stack = [] * len(nums)
    ans = forth()
    print(f'#{tc} {ans}')



