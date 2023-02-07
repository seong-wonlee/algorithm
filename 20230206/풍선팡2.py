


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    maxv = 0
    for i in range(0,N):
        for j in range(0,M):
            total = arr[i][j]
            for r in range(1, arr[i][j]+1):
                for k in range(4):
                    ni = i + di[k] * r
                    nj = j + dj[k] * r
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]
                if total >= maxv :
                    maxv = total
    print(f'#{tc} {maxv}')