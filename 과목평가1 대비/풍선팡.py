T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1] # 우 하 좌 상
    dj = [1, 0, -1, 0]
    lst = []
    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for m in range(1, arr[i][j] + 1):
                for k in range(4):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]
                        lst.append(total)
    # print(lst)
    maxv = 0
    for l in range(len(lst)):
        if lst[l] >= maxv:
            maxv = lst[l]
    print(f'#{tc} {maxv}')