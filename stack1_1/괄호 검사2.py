def my_push(data):
    stack.append(data)

def my_pop():
    return stack.pop()

T = int(input())
for tc in range(1, T +1):
    txt = input()
    stack = []
    ans = 1
    for i in txt:
        if i == "(" or i == "{":
            my_push(i)
        elif i == ")" or i == "}":
            # 스텍에 여는 괄호가 없으면
            if len(stack) == 0:
                ans = 0
            # 스텍에 여는 괄호가 있으면
            else:
                if i == ")" and stack.pop() != "(":
                    ans = 0
                if i == "}" and stack.pop() != "{":
                    ans = 0
    # 여는 괄호가 남아있으면
    else:
        if len(stack):
            ans = 0
    print(f'#{tc} {ans}')



