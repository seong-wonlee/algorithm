
def bfs(i,j):
    visited = [[0] * N for _ in range(N)]
    didj = [(1, 0), (-1, 0), (0, 1), (0, -1)]   #하상우좌
    queue = [(i, j)]
    visited[i][j] = 1
    while queue: # 큐가 남아있을 때까지
        i, j = queue.pop(0)
        if arr[i][j] == 3:
            return visited[i][j] - 2    # 거처온 거리 출발, 도착 카운트 뺀거
        for k in range(4):
            ni, nj = i + didj[k][0], j + didj[k][1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                s, g = i, j     # 시작점 찾기
                break
    print(f'#{tc} {bfs(s, g)}')
