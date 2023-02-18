n = int(input())
word = list(input())
alpha = [0] * n
for i in range(n):
    alpha[i] = int(input())
stack = []

for k in word:
    if k.isalpha():
        stack.append(alpha[ord(k) - ord('A')])
    else:   # 연산자이면
        a = stack.pop()
        b = stack.pop()
        if k == "*":
            ans = b * a
            stack.append(ans)
        if k == "+":
            ans = b + a
            stack.append(ans)
        if k == "-":
            ans = b - a
            stack.append(ans)
        if k == "/":
            ans = b / a
            stack.append(ans)

print('%.2f' %stack[-1])

