T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for i in range(N):
        a1, a2, b1, b2, c = map(int, input().split())
    # cnt = 0
        for i in range(a1, b1+1):
            for j in range(a2, b2+1):
                if c == 1:
                    arr[i][j] += 1
                else:
                    arr[i][j] += 1
        cnt = 0
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 2:
                    cnt += 1


    print(f'#{tc} {cnt}')
