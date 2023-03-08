import sys
stack = []
def bfs(i):
    global cnt
    stack.append(i)
    while stack:
        a = stack.pop()
        if visited[a]:
            continue
        cnt += 1
        visited[a] = cnt
        for k in lst[a]:
            if visited[k] == 0:
                stack.append(k)
    return

N, M, R = map(int, input().split())
lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)

cnt = 0
for i in range(M):
    u,v = map(int, sys.stdin.readline().split())
    lst[u].append(v)
    lst[v].append(u)

for i in lst:
    i.sort()

bfs(R)
for i in range(1,N+1):
    print(visited[i])