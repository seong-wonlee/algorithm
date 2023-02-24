def bfs(s,g,k):
    queue = []
    visited = [[0] * N for _ in range(N)]
    queue.append((s,g))     # 시작점 인큐
















# T = int(input())
N, M = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(N)]
for K in range(N+1, -1, -1):
    cost = K * K + (K-1) * (K-1)
    for i in range(N):
        for j in range(N):
            i, j = s, g

