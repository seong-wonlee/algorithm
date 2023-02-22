
# 중위 순회
def f(i):
    if i > 0 :
        f(left[i])
        cnt.append(lst2[i])
        f(right[i])
    return cnt

for tc in range(1,11):
    N = int(input())
    left = [0] * (N + 2)
    right = [0] * (N + 2)
    lst2 = [[]]
    for i in range(N):
        lst = list(input().split())
        lst2.append(lst[1])
        if len(lst) == 4:
            a, b, c = int(lst[0]), int(lst[2]), int(lst[3])
            left[a] = b
            right[a] = c
        elif len(lst) == 3:
            d, e = int(lst[0]), int(lst[2])
            left[d] = e
    cnt = []
    f(1)

    print(f'#{tc} ', *cnt, sep = '')
