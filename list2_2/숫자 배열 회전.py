
def rotate(a):
    b = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0,n):
            b[i][j] = a[n-1-j][i]
    return b

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    rotate_90 = rotate(arr)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)


    print(f'#{tc}')

    for i in range(n):

        print(*rotate_90[i], ' ',  *rotate_180[i], ' ', *rotate_270[i], sep='')

