
def bfs(i, j):
    visited = [[0] * 16 for _ in range(16)]
    queue = [(i,j)] # 출발점 인큐
    visited[i][j] = 1   # 출발점 방문
    didj = [(-1,0), (0,1), (1,0), (0, -1)] # 상우하좌
    while queue:    # 큐가 남아있을때까지
        i, j = queue.pop(0)
        if arr[i][j] == 3:
            return 1
        for k in range(4):
            ni, nj = i + didj[k][0], j + didj[k][1]
            if 0 <= ni <= 16 and 0 <= nj <= 16 and arr[ni][nj] != 1 and visited[ni][nj] ==0:
                queue.append((ni, nj))
                visited[ni][nj] = 1
    return 0



for i in range(10):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:  # 출발이면
                s, g = i, j
                break
    print(f'#{n} {bfs(s, g)}')