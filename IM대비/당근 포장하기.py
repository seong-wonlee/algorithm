T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ci = list(map(int, input().split()))

    small = []
    for i in range(N//3):
        small.append(ci[i])
    # print(small)

    medium = []
    a = (N - N//3)//2
    for i in range(N//3, N//3+a):
        medium.append(ci[i])


    large = []
    for i in range(N//3+a, N):
        large.append(ci[i])
    # print(large)

    while medium[0] == small[-1]:
        b = medium.pop(0)
        small.append(b)
        if len(medium) == 0:
            break

    while len(medium) != (N-len(small))//2:
        a = large.pop(0)
        medium.append(a)


    len_lst = []
    len_lst.append(len(small))
    len_lst.append(len(medium))
    len_lst.append(len(large))

    if len(small) > N//2 or len(medium) > N//2 or len(large) > N//2:
        ans = -1
    else:
        ans = max(len_lst) - min(len_lst)

    print(f'#{tc} {ans}')
