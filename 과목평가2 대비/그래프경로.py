# T = int(input())

def dfs(S, G, N):
    visited = [0] * (N+1)
    stack = []
    v = S
    while True:
        if v == G:
            return 1

        visited[v] = 1
        for w in lst[v]:
            if visited[w] == 0:
                stack.append(v) # 현재 정점 푸시
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0


V, E = map(int, input().split())
lst = [[] for _ in range(V)]
for _ in range(E):
    v,w = map(int, input().split())
    lst[v].append(w)
S, G = map(int, input().split())
print(dfs(S,G,V))
