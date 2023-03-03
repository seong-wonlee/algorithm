T = int(input())
for tc in range(1, T +1):
    N,M,K,H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    ans = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            lst = []
            for k in range(8):
                ni, nj = i + dir[k][0], j + dir[k][1]
                if 0 <= ni < N and 0 <= nj < M :
                    lst.append(arr[ni][nj])
            if len(lst) == 8:
                if max(lst) - min(lst) <= K:
                    if arr[i][j] - min(lst) <= H and arr[i][j] >= min(lst) :
                        cnt += 1
    print(f'#{tc} {cnt}')



