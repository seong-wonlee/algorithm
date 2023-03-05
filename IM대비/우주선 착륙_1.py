T = int(input())
for tc in range(1, T+1):
    n,m,k,h= map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    didj = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            lst = []
            for k in range(8):
                ni = i + didj[k][0]
                nj = j + didj[k][1]
                if 0<= ni<n and 0<= nj <m:
                    lst.append(arr[ni][nj])
            if len(lst) == 8:
                if max(lst) - min(lst) <= k:
                    if arr[i][j] - min(lst) <= h and arr[i][j] >= min(lst) :
                        cnt += 1

    print(f'#{tc} {cnt}')