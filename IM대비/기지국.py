T = int(input())
for tc in range(1,T+1):
    didj = [(1,0), (-1,0), (0,1), (0,-1)]

    n = int(input())
    arr = [input() for _ in range(n)]
    visited = [[0]*9 for _ in range(9)]
    cnt1 = 0        # 전체 집의 수
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt1 += 1
    # print(cnt1)


    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                for k in range(4):
                    ni = i + didj[k][0]
                    nj = j + didj[k][1]
                    if 0 <= ni <n and 0 <= nj <n and arr[ni][nj] == 'H' and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        cnt1 -= 1

            if arr[i][j] == 'B':
                for k in range(4):
                    for r in range(1,3):
                        ni = i + didj[k][0] * r
                        nj = j + didj[k][1] * r
                        if 0 <= ni <n and 0 <= nj <n and arr[ni][nj] == 'H' and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            cnt1 -= 1

            if arr[i][j] == 'C':
                for k in range(4):
                    for r in range(1,4):
                        ni = i + didj[k][0] * r
                        nj = j + didj[k][1] * r
                        if 0 <= ni <n and 0 <= nj <n and arr[ni][nj] == 'H' and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            cnt1 -= 1

    print(f'#{tc} {cnt1}')





