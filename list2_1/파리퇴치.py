T = int(input())
for tc in range(1, T+1):
    N, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(0, N)]
    lst = []
    for i in range(0, N - m + 1):
        for j in range(0, N - m + 1):
            sum = 0
            for k in range(0,m):    # k-> i ~ i+M-1
                for l in range(0,m):    # l-> i ~ i+M-1
                    sum += arr[i+k][j+l]
                    lst.append(sum)
    lst.sort()
    print(f'#{tc} {lst[-1]}')


