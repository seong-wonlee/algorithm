T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'NO'
    didj = [(1,0),(0,1),(1,-1),(1,1)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    ni, nj = i + didj[k][0], j + didj[k][1]
                    while 0<= ni < N and 0<= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni, nj = ni + didj[k][0], nj + didj[k][1]
                        # print(cnt)
                    if cnt >= 5:
                        ans = 'YES'

    print(f'#{tc} {ans}')