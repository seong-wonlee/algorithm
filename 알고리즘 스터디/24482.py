import sys
input = sys.stdin.readline
from collections import deque
stack = deque()
def dfs(a):
    stack.append([a,0])
    while stack:
        cur_node, depth = stack.pop()
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        node_depth[cur_node] = depth
        for i in lst[cur_node]:
            if not visited[i] :
                stack.append([i, depth+1])
    return

N,m,r = map(int, input().split())
visited = [False for _ in range(N+1)]
node_depth = [0 for _ in range(N+1)]
lst = [[] for _ in range(N+1)]
for _ in range(m):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
for i in lst:
    i.sort()    # [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
dfs(r)
for i in range(1,N+1):
    if i == r:
        print(0)
    elif visited[i] == 0:
        print(-1)
    else:
        print(node_depth[i])