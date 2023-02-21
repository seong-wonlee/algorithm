def bfs(v, G):
    visited = [0] * (V+1)   # 방문 생성
    queue = [v]     # 큐 생성, 시작점 인큐
    visited[v] = 1  # 시작점 방문
    while queue:    # 큐가 비어있지 않으면
        t = queue.pop(0)    # 디큐
        for i in adjL[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
    if visited[G] == 0:
        return 0
    else:
        return visited[G] -1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adjL[n1].append(n2)
        adjL[n2].append(n1)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S,G)}')

