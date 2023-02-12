# T = int(input())
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(0, N):
    for j in range(0, N):
        sumv = arr[i][j]
        for k in range(0,M):
            sumv += arr

    maxv = 0
    if maxv <= sumv:
        maxv = sumv
    print(maxv)


