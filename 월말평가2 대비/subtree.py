def f(i):
    global cnt
    if i > 0:
        cnt += 1
        f(left[i])
        f(right[i])


# T = int(input())
E, N = map(int, input().split())
lst = list(map(int, input().split()))
left = [0] * (E+2)
right = [0] * (E+2)
cnt = 0
for i in range(E):
    a, b = lst[i*2], lst[i*2+1]
    if left[a] == 0:
        left[a] = b
    else:
        right[a] = b
print(left,right)
f(N)
print(cnt)