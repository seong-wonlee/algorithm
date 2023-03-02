T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    didj = [(-1,0), (1,0), (0,1), (0,-1)]   # 위 아래 오 왼
    dir = [(-1,-1), (-1,1), (1,-1), (1,1)]  # 대각선

    maxv = 0
    for i in range(n):
        for j in range(n):
            sum = arr[i][j]
            for k in range(4):
                for r in range(1,m):
                    ni = i + didj[k][0] * r
                    nj = j + didj[k][1] * r
                    if 0<= ni<n and 0<= nj<n:
                        sum += arr[ni][nj]
                    else:
                        sum += 0
            if maxv < sum:
                maxv = sum


    maxv1 = 0
    for i in range(n):
        for j in range(n):
            sum1 = arr[i][j]
            for k in range(4):
                for r in range(1,m):
                    ni = i + dir[k][0] * r
                    nj = j + dir[k][1] * r
                    if 0<= ni<n and 0<= nj<n:
                        sum1 += arr[ni][nj]
                    else:
                        sum1 += 0
            if maxv1 < sum1:
                maxv1 = sum1

    if maxv > maxv1:
        ans = maxv
    else:
        ans = maxv1

    print(f'#{tc} {ans}')