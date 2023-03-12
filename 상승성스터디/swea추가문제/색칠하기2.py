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
    
    arr_padding = [[0] * 12] + [[0] + arr[i] + [0] for i in range(10)] + [[0] * 12]
    
    cnt = 0
    for i in range(1,11):
        for j in range(1,11):
            for k in range(4):
                ni, nj = i + didj[k][0], j + didj[k][1]
                if arr_padding[i][j] == 1:
                    # 주위에 0이 몇개인지 확인
                    if arr_padding[ni][nj] == 0 or arr_padding[ni][nj] == 2:
                        cnt += 1
                elif arr_padding[i][j] == 2:
                    if arr_padding[ni][nj] == 0 or arr_padding[ni][nj] == 1:
                        cnt += 1

    print(f'#{tc} {cnt}')
