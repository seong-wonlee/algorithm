T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    sum = 0
    sum_lst = []
    for i in range(0, N-M+1):
        sum = 0
        for j in range(i,i+M):
            sum += lst[j]
        sum_lst.append(sum)

    maxv = 0
    for i in range(len(sum_lst)):
        if maxv < sum_lst[i]:
            maxv = sum_lst[i]


    minv = sum_lst[0]
    for i in range(len(sum_lst)):
        if minv > sum_lst[i]:
            minv = sum_lst[i]

    print(f'#{tc} {maxv - minv})