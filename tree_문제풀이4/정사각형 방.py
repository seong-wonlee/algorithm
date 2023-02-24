
def f(s,g):
    didj = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    visited = [[0] * (N+1) for _ in range(N+1)] # 방문
    queue = []
    queue.append([s, g])
    visited[s][g] = 1   # 시작점 방문
    cnt = 1
    while queue:
        p, q = queue.pop(0)
        for k in range(4):
            ni, nj = p + didj[k][0], q + didj[k][1]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] - arr[p][q] == 1:
                queue.append([ni, nj])
                visited[ni][nj] = 1     # 방문찍구
                cnt += 1    # 다음 방으로 갈 때마다 카운트

    return arr[s][g], cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            s, g = i, j
            a, b = f(s,g)
            ans.append([a,b])
    ans.sort(key=lambda x : (-x[1],x[0]) )
    print(f'#{tc}', *ans[0])


