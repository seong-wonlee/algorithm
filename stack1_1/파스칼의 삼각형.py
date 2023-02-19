T = int(input())
for tc in range(1, T+1):
    N = int(input())

    count = [[0] * N for _ in range(N)]
    # print(count)
    cnt = 1
    for i in range(N):
        for j in range(i+1):
            if i == 0 and j == 0:
                count[i][j] = 1
                break
            else:
                count[i][j] = count[i-1][j-1] + count[i-1][j]
    print(f'#{tc}')

    arr = [[] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if count[i][j] > 0 :
                arr[i].append(count[i][j])

    for i in range(N):
        print(*arr[i])




