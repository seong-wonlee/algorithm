
for i in range(0, 10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(0,100)]
    sum1_lst, sum2_lst, sum3_lst, sum4_lst = [] ,[], [], []
    ans = []
    # 행의 합의 최댓값
    for k in range(0, 100):
        sum1 = 0
        for j in range(0, 100):
            sum1 += arr[k][j]
        sum1_lst.append(sum1)
    sum1_lst.sort()
    ans.append(sum1_lst[-1])

    # 행의 합의 최댓값
    for k in range(0, 100):
        sum2 = 0
        for j in range(0, 100):
            sum2 += arr[j][k]
        sum2_lst.append(sum2)
    sum2_lst.sort()
    ans.append(sum2_lst[-1])

    sum3 = 0
    sum4 = 0
    # 대각선의 합의 최댓값
    for r in range(0,100):
        sum3 += arr[r][r]
        sum3_lst.append(sum3)
        sum4 += arr[r][99-r]
        sum4_lst.append(sum4)
    sum3_lst.sort()
    sum4_lst.sort()
    ans.append(sum3_lst[-1])
    ans.append(sum4_lst[-1])

    print(f'#{i+1} {max(ans)}')


