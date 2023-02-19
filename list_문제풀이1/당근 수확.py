T = int(input())
for tc in range(1, T+1):
    N = int(input())

    carrot = list(map(int, input().split()))
    # print(carrot)

    sumi = 0
    sumj = 0
    sum_lst = []
    ans_lst = []

    for i in range(0, N):
        sumi += carrot[i]
        # sumj += carrot[i]

    for j in range(0,N):
        sumj += carrot[j]
        sum_lst.append(sumj)
    # print(sum_lst)

    for k in range(0, N):
        ans = sumi - sum_lst[k]
        ans_lst.append(ans)
    # print(ans_lst)

    minv = 100
    for m in range(0, N):
        ans_lst[m] = abs(ans_lst[m] - sum_lst[m])
        if minv > ans_lst[m]:
            minv = ans_lst[m]
            minv_index = m+1
    #
    # print(ans_lst)
    # print(minv)
    # print(minv_index)

    print(f'#{tc} {minv_index} {minv}')