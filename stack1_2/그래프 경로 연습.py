def f1(S, G, N):
    visited = [0] * (N+1)     # 방문
    stack = []
    v = S
    while True:
        if v == G :
            return 1
        visited[v] = 1
        for k in lst[v]:
            if visited[k] == 0:
                stack.append(v)
                v = k
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V + 1)]
    for _ in range(E):s
        v, w = map(int, input().split())
        lst[v].append(w)
    S, G = map(int, input().split())

    print(f'#{tc} {f1(S,G,V)}')
