def f(i):
    if i > 0 and left[i] != '.' and right[i] != '.':
        f(left[i])
        f(right[i])
        cnt.append(lst2[i])
    return cnt

N = int(input())
left = [0] * (N+2)
right = [0] * (N+2)
cnt = []
for i in range(N):
    lst2 = []
    lst = list(input().split())
    lst2.append(lst[0])
    a, b = lst[1], lst[2]
    if left[a] == 0:
        left[a] = b
    else:
        right[a] = a
print(f(1))
