def f1(S, G, N):  # S 출발, G 도착, N 마지막 정점 그래프 탐색, DFS
    visited = [0] * (N+1)   # 방문 표시
    stack = []  # 스택
    v = S
    while True:
        if v == G:      # 방문에서 목적지면
            return 1            # 성공 (1)
        visited[v] = 1  # 빙문
        for w in range(1, N+1):           # 인접하고 방문안한 w가 있으면
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)   # 현재 정점 push
                v = w
                break
        else:       # 더이상 갈곳이 없으면
            if stack:       # pop
                v = stack.pop()
            else:
                break            # 스택이 비어있으면
    return 0     # (1) v == G 인지검사한 경우

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split()) # v = 노드 수 E = 간선 수
    adjM = [[0] * (V+1) for _ in range(V + 1)]  # 인접리스트

    for _ in range(E):
        v,w = map(int,input().split()) # v1 출발, v2 도착(유향그래프)
        adjM[v][w] = 1    # v1에 인접한 v2
        # adjmM[v2][v1] # 무향그래프였다면
    # print(adjL)
    S, G = map(int, input().split())
    print(f'#{tc} {f1(S,G,V)}')

