T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'NO'
    # 행 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
        if cnt >= 5:
            ans = 'YES'
            break

    # 열 확인

    for i in range(N):
        cnt2 = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt2 += 1

        if cnt2 >= 5:
            ans = 'YES'
            break


    # 대각선 확인
    cnt3 = 0
    cnt4 = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                if arr[i][j] == 'o':
                    cnt3 += 1

            if j == N-i-1:
                if arr[i][j] == 'o':
                    cnt4 += 1

    if cnt3 >= 5 or cnt4 >= 5:
        ans = 'YES'
    print(f'#{tc} {ans}')