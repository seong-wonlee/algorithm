import sys
input = sys.stdin.readline

def dfs(i):
    global cnt
    visited[i] = cnt
    for k in lst[i]:
        if visited[k] == 0:
            cnt += 1
            dfs(k)
    return

N, M, R = map(int, input().split())
lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)

cnt = 1
for i in range(M):
    u,v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
    lst[u].sort()

dfs(R)
for i in range(1,N+1):
    print(visited[i])

