T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    didj = [(-1,0),(1,0),(0,1),(0,-1)]
    maxv = 0
    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            for k in range(4):
                for r in range(1, arr[i][j]+1):
                    ni, nj = i + didj[k][0] *r, j + didj[k][1] *r
                    if 0 <= ni < N and 0 <= nj < M:
                        sum += arr[ni][nj]
            # print(sum)
            if maxv < sum:
                maxv = sum
    print(f'#{tc} {maxv}')


