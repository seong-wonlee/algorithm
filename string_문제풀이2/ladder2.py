
for tc in range(1, 11):
    n = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # print(arr)
    # 시작
    mn = 100*100
    for sj in range(1,101):
        si = 0
        if arr[si][sj] != 1:
            continue
        cnt = 0
        dj = 0
        # ci , cj 는 현재 위치
        ci, cj = si, sj
        while ci < 99:
            cnt += 1
            # 아래 방향일 때
            if dj == 0:
                # 오른쪽 방향
                if arr[ci][cj+1] == 1:
                    dj = 1
                    cj += 1
                # 왼쪽 방향
                elif arr[ci][cj-1] == 1:
                    dj = -1
                    cj -= 1
                # 아래 방향
                else:
                    dj = 0
                    ci += 1
            # 아래 방향일 떄
            else:
                # 오른쪽, 왼쪽
                if arr[ci][cj+dj] == 1:
                    cj += dj
                else:
                    dj = 0
                    ci += 1
        # 최솟값 구하기
        if mn >= cnt:
            mn = cnt
            ans = sj - 1
    print(f'#{tc} {ans}')





