import sys
stack = []
def bfs(i):
    global cnt
    stack.append(i)
    visited[i] = 0  # 1 방문했을 때 0으로 방문처리
    while stack:
        a = stack.pop()
        if visited[a] != -1:
            continue
        for k in lst[a]:
            if visited[k] == -1:
                visited[k] = visited[a] + 1
                stack.append(k)
    return

N, M, R = map(int, input().split())
lst = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
lst2 = [-1] * (N+1)
cnt = 0
for i in range(M):
    u,v = map(int, sys.stdin.readline().split())
    lst[u].append(v)
    lst[v].append(u)

for i in lst:
    i.sort(reverse=True)
print(lst)
bfs(R)
for i in range(1,N+1):
    print(visited[i])