T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    didj = [(0,1),(1,0),(1,-1),(1,1)]  # 오른쪽 하 왼하 오하 -> 방향 설정
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    ni = i + didj[k][0]
                    nj = j + didj[k][1]
                    cnt = 1
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] =='o':
                        cnt += 1
                        ni += didj[k][0]    # 그 방향으로 계속 탐색
                        nj += didj[k][1]
                    if cnt >= 5:
                        ans = 'YES'
    print(f'#{tc} {ans}')


