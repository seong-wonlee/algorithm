T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(10) for _ in range(10)]

    didj = [(1,0),(-1,0),(0,-1),(0,1)]
    for i in range(N):
        r1, c1,r2, c2, c = map(int, input().split())
        for k in range(r1,r2+1):
            for j in range(c1,c2+1):
                arr[k][j] += c
                # 겹쳐있는 부분을 0 으로 변환
                if arr[k][j] == 3:
                    arr[k][j] = 0

    ans = 0
    for i in range(10):
        for j in range(10):
            cnt = 0
            # 색이 칠해진 칸에 주위 살펴서
            if arr[i][j] == 1 or arr[i][j] == 2:
                for k in range(4):
                    ni, nj = i + didj[k][0], j + didj[k][1]
                    if 0 <= ni < 10 and 0 <= nj < 10:
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
