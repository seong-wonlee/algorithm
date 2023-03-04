T = 10
for tc in range(1, T +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]


    maxv = 0
    maxv1 = 0

    sum2 = 0
    sum3 = 0
    for i in range(100):
        sum = 0
        sum1 = 0
        for j in range(100):
            sum += arr[i][j]
            sum1 += arr[j][i]
            if maxv < sum:
                maxv = sum
            if maxv1 < sum1:
                maxv1 = sum1
            if i == j :
                sum2 += arr[i][j]
            if i == n - j -1:
                sum3 += arr[i][j]
    # print(maxv, maxv1, sum2, sum3)
    print(f'#{tc} {max(maxv, maxv1, sum2, sum3)}')