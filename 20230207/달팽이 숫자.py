di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    # 방향 1 : 우 2: 하 3: 좌 4: 상
    k = 0
    # 초기위치
    i, j = 0, 0

    # 1부터 시작
    for r in range(1, n*n + 1):
        arr[i][j] = r
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            i = ni
            j = nj
        # 방향 틀기
        else:
            k = (k+1) % 4
            i = i + di[k]
            j = j + dj[k]
    print(f'#{tc}')
    # print(arr)
    for x in arr:
        print(*x)

