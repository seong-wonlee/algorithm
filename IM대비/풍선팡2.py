T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    didj = [(-1,0),(1,0),(0,-1),(0,1)]  # 상하좌우
    maxv = 0
    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            for k in range(4):
                ni, nj = i + didj[k][0], j + didj[k][1]
                if 0 <= ni < N and 0 <= nj < M:
                    sum += arr[ni][nj]
            if maxv < sum:
                maxv = sum
    print(f'#{tc} {maxv}')
