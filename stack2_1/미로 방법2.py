
def f(i,j):
    di = [0,1,0,-1] # 우하좌상
    dj = [1,0,-1,0]
    visited = []
    stack = []
    while True:
        visited.append((i,j))
        if arr[i][j] == 3:  # 도착하면 성공
            return 1
        else:
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] != 1 and (ni,nj) not in visited:
                        stack.append((i,j)) # 현재위치 저장하고
                        i, j = ni, nj   # 움직여
                        break
            else: # 더이상 갈 곳이 없으면
                if stack:
                    i, j = stack.pop()
                else:   # 스택이 남아있지 않으면
                    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for m in range(N):
        for n in range(N):
            if arr[m][n] == 2:
                i, j = m, n

    print(f'#{tc}', f(i,j))



