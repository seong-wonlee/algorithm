
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]


    ans = 0
    for lst in arr:
        cnt = 0
        for j in range(N+1):
            # 흰색 블럭인 경우
            if lst[j] == 1:
                cnt += 1

            else:
                if cnt == K :
                    ans += 1
                cnt = 0



    arr3 = list(map(list, zip(*arr)))
    ans2 = 0
    for lst in arr3:
        cnt = 0
        for j in range(N+1):
            # 흰색 블럭인 경우
            if lst[j] == 1:
                cnt += 1
            # 검은 색 블럭인 경우
            else:
                if cnt == K :
                    ans += 1
                cnt = 0

    print(f'#{tc} {ans+ans2}')
