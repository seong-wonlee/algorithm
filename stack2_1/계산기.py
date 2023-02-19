'''
2+3*4/5
'''
nums = list(input())
oper = {'*': 2, '/': 2, '+': 1, '-': 1}
stack = [0]*len(nums)
postfix = ''
top = -1

for num in nums:
    if '0' <= num <='9':
        postfix += num
    elif num in oper:
        # 스택이 비어있거나 우선순위가 높으면
        if top == -1 or oper[stack[top]] < oper[num]:
            top += 1
            stack[top] = num
        else:
            # 스택에 남아있고 토큰의 우선순위가 높을 때 까지
            while top > -1 and oper[stack[top]] >= oper[num]:
                top -= 1    # pop
                postfix += stack[top+1]
            top += 1    # push
            stack[top] = num

# 스택에 연산자가 남아있으면
while top > -1 :
    top -= 1  # pop
    postfix += stack[top+1]
print(postfix)