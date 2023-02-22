def f(i):
    global cnt
    if i > 0:
        cnt += 1
        f(left[i])
        f(right[i])
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(E):
        p, c = lst[i*2], lst[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    cnt = 0
    print(f'#{tc} {f(N)}')


