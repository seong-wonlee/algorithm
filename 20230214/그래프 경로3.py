def f1(v, G):
    if v == G :
        return 1
    else:
        visited[v] = 1
        for w in adjL[v]:
            if visited[w] == 0:  # 인접하고 방문안한 w
                if f1(w,G):      # 목적지를 찾고 리턴하는 경우
                    return 1
        return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # v = 노드 수 E = 간선 수
    adjL = [[] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V+1)
    for _ in range(E):
        v, w = map(int, input().split())  # v1 출발, v2 도착(유향그래프)
        adjL[v].append(w)  # v1에 인접한 v2

    S, G = map(int, input().split())
    print(f'#{tc} {f1(S, G)}')