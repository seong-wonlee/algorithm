T = int(input())
for tc in range(1,T+1):
    n,m = map(int, input().split())
    arr= [list(map(int,input().split())) for _ in range(n)]

    maxv = 0
    lst = []
    for i in range(n):
        for j in range(n):
            sumv = 0
            for k in range(m):
                for r in range(m):
                    if 0<= i+k < n and 0<= j+r < n:
                        sumv += arr[i+k][j+r]
            if maxv < sumv:
                maxv = sumv
    print(f'#{tc} {maxv}')

