# infix : 중위 표기식 문자열
# n : 중위표기식 길이

def get_postfix(infix, n):
    # 결과로 나올 후위표기식
    postfix = ""
    stack = []
    # 스택 밖에 있을 때 연산자의 우선순위
    icp = {'+': 1, '*' : 2, '-' : 1, '/' : 2, '(': 3}
    # 스택 안에 있을 때 연산자의 우선순위
    isp = {'+': 1, '*': 2, '-': 1, '/': 2, '(': 0}

    # 문자열의 길이만큼 반복
    for i in range(n):
        if infix[i].isalpha():
            postfix += infix[i]
        else:
            if infix[i] == ")":
                char = stack.pop()
                if char == "(":
                    break
                postfix += char
            # 닫는 괄호가 아니라 기타 연산자
            else:
                # 현재 연산자의 우선순위보다 스택의 top에 있는 연산자의 우선순위가 같거나 높으면
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 그게 아니면 스택에 연산자 추가

                stack.append(infix[i])
    while stack:    # 남아있는 연산자는 모두 출력
        postfix += stack.pop()

    return postfix

n = int(input())
lst = input()
print(get_postfix(lst,n))