# T = int(input())

n = int(input())
arr = [[0] * n for _ in range(n)]

di = [0,1,0,-1] # 우 하 좌 상
dj = [1,0,-1,0]
k = 0
i,j = 0, 0
for m in range(1, n*n+1):
    arr[i][j] = m
    ni = i + di[k]
    nj = j + dj[k]
    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj]==0:
        i = ni
        j = nj
    else:
        k = (k+1) % 4
        i = i + di[k]
        j = j + dj[k]
print(arr)


