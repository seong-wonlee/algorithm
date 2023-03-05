# T = int(input())
N, M = map(int, input().split())
arr = [[0] * (N+2) for _ in range(N+2)]
arr[N//2][N//2] = 2
arr[N//2+1][N//2] = 1
arr[N//2][N//2+1] = 1
arr[N//2+1][N//2+1] = 2
print(arr)
didj = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

for i in range(M):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    for j in range(8):
        lst = []
        ni, nj = a + didj[j][0], b + didj[j][1]
        while arr[ni][nj] != c and arr[ni][nj] != 0:
            lst.append((ni,nj))
            ni = ni + didj[j][0]
            nj = nj + didj[j][1]
        if arr[ni][nj] == c:
            for p,q in lst:
                arr[p][q] = c


print(arr)
cnt = 0
cnt1 = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            cnt +=1
        elif arr[i][j] == 2:
            cnt1 += 1
print(cnt,cnt1)

