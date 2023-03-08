import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().rstrip().split())   # 정점, 간선, 시작

lst = [[] for _ in range(n+1)]  # 연결 표시할 배열
visited = [False for _ in range(n+1)]   # 방문 배열
nodes_depth = [0 for _ in range(n+1)]   # 깊이 배열

# 간선 받아서 연결시킴 -> lst 완성
for _ in range(m):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    lst[tail].append(head)
    lst[head].append(tail)

# [[], [4, 2], [4, 3, 1], [4, 2], [3, 2, 1], []]
for i in range(n+1):
    lst[i].sort(reverse=True)
# print(lst)
stack = deque()
stack.append([r, 0])  # 스택에 시작점, 깊이 푸시 -> 시작점은 깊이가 무조건 0!
while stack:
    cur_node, depth = stack.pop()   # stack 마지막 값 pop
    if visited[cur_node]:   # 4에 방문이 찍혀있어서 while로 돌아가서 pop해줌
        continue
    visited[cur_node] = True        # 방문처리
    nodes_depth[cur_node] = depth   # 깊이 배열의 현재노드 인덱스에 깊이 푸시
    for i in lst[cur_node]:
        if not visited[i]:
            stack.append([i, depth+1])

for i in range(1, n+1):
    if i == r:
        print(0)
    elif nodes_depth[i] == 0:
        print(-1)
    else:
        print(nodes_depth[i])