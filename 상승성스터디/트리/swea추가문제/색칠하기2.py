T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(11) for _ in range(11)]

    didj = [(1,0),(-1,0),(0,-1),(0,1)]
    for i in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                arr[i][j] += c

    # 겹쳐있는 부분을 0 으로 변환
    for i in range(11):
        for j in range(11):
            if arr[i][j] == 3:
                arr[i][j] = 0

    ans = 0
    for i in range(11):
        for j in range(11):
            cnt = 0
            # 색이 칠해진 칸에 주위 살펴서
            if arr[i][j] != 0:
                for k in range(4):
                    ni, nj = i + didj[k][0], j + didj[k][1]
                    if 0 <= ni < 11 and 0 <= nj < 11:
                        # 주위에 0이 몇개인지 확인
                        if arr[ni][nj] == 0:
                            cnt += 1
            if cnt == 2:
                ans += 2
            elif cnt == 1:
                ans += 1
            elif cnt == 3:
                ans += 3

    print(f'#{tc} {ans}')
