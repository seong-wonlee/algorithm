def rotate(n, a):
    count = [[0] * n for _ in range(N)]
    for i in range(n):
        for j in range(n):
            count[i][j] = a[n - j - 1][i]
    return count

T = int(input())

for tc in range(1, T+1):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rotate_90 = rotate(N, arr)
    rotate_180 = rotate(N, rotate_90)
    rotate_270 = rotate(N, rotate_180)

    print(f'#{tc}')
    for i in range(N):
        print(*rotate_90[i],' ', *rotate_180[i], ' ', *rotate_270[i], sep = '')