T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]

    ans = 0
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0


    ans2 = 0
    for i in range(N+1):
        cnt1 = 0
        for j in range(N+1):
            if arr[j][i] == 1:
                cnt1 += 1
            else:
                if cnt1 == K:
                    ans2 += 1
                cnt1 = 0

    print(f'#{tc} {ans+ans2}')

