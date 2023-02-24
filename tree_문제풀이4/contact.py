def bfs(s):
    queue = []
    visited = [0] * 101
    queue.append(s)  # 초기 데이터 삽입
    visited[s] = 1   # 방문 표시

    while queue:
        c = queue.pop(0)    # 현재 위치
        for i in adj[c]:
            if visited[i] == 0:     # 방문하지 않은 정점이 있으면
                queue.append(i)     # 큐에 푸시
                visited[i] = visited[c] + 1     # 마지막에 연락 받은 사람 구하기 위해서
    maxv = 0
    for i in range(101):
        if maxv <= visited[i]:
            maxv = visited[i]
            maxv_id = i

    return maxv_id

for tc in range(1,11):
    N, S = map(int, input().split())    # N: 데이터 길이 S: 시작점
    lst = list(map(int, input().split()))   # from-to
    adj = [[] for _ in range(101)]

    for i in range(0,N,2):
        s, e = lst[i], lst[i+1]
        adj[s].append(e)  # 연결

    ans = bfs(S)
    print(f'#{tc} {ans}')

