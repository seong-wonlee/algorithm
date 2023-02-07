T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for k in range(0, N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        # cnt = 0
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    arr[i][j] += 1
                else:
                    arr[i][j] += 1
        # print(arr)
    cnt = 0
    for i in range(0, 10):
        for j in range(0, 10):
            if arr[i][j] == 2:
                cnt += 1
    # print(cnt)
    print(f'#{tc} {cnt}')






