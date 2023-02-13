T = int(input())
for tc in range(1, T +1):

    txt = input()

    stack = [0] * 100   # 입력 100글자 이내
    top = -1
    ans = 1
    for x in txt :  # 한글자씩 가져오기
        if x == '(': # 여는 괄호 push
            top += 1
            stack[top] = x
        elif x == ')' : # 닫는 괄호인 경우
            if top > -1:    # 스텍에 여는 괄호가 있으면
                top -= 1    # pop
            else:       # 스텍에 여는 괄호가 없으면
                ans = 0     # 오류
        if x == '{':
            
    else:       # txt 끝
        if top > -1:    # 여는 괄호가 남아있으면
            ans = 0     # 오류
        # else:
        #     ans = 1     # 정상
    # print(ans)


    # print(ans1)
    if ans == 1 and ans1 == 1:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')
























