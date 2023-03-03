T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)]     # 이 부분 중요
    arr[N//2][N//2] = 2
    arr[N//2+1][N//2] = 1
    arr[N//2][N//2+1] = 1
    arr[N//2+1][N//2+1] = 2
    # print(arr)
    dir = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]   # 상하좌우 대각선 방향

    for _ in range(M):
        a, b, c = map(int, input().split()) # c: 1이면 흑돌, 2이면 백돌
        arr[a][b] = c
        for k in range(8):
            ni, nj = a + dir[k][0], b + dir[k][1]   # 주위 확인
            lst = []
            while arr[ni][nj] != c and arr[ni][nj] != 0:
                lst.append((ni,nj))
                ni, nj = ni + dir[k][0], nj + dir[k][1]
            if arr[ni][nj] == c:
                for p,q in lst:
                    arr[p][q] = c


    cnt1 = 0 # 흑돌개수
    cnt2 = 0 # 백돌개수
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1

    print(f'#{tc} {cnt1} {cnt2}')



