# 10 이하의 소수 찾기
n = 10
pnumber = [1] * (n+1)
for i in range(2, n+1):
    if pnumber[i]:
        j = 2
        while i*j <= n:
            pnumber[i*j] = 0
            j += 1
print(pnumber)

for i in range(2, n+1):
    if pnumber[i]:
        print(i, end='')