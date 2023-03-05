T = int(input())
for tc in range(1, T+1):
    n , m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxv = 0
    for i in range(n):
        for j in range(n):
            sum = 0
            for r in range(m):
                for k in range(m):
                    if 0 <= i+r < n and 0 <= j+k < n:
                        sum += arr[i+r][j+k]
            if maxv < sum:
                maxv = sum
    print(f'#{tc} {maxv}')
