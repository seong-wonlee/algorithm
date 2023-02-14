def dfs(s):
    # 방문 배열 만들기
    visited = [0] * 100
    # 스택
    stack = []
    # 시작 정점 방문 처리
    i = s
    visited[i] = 1

    # 스택이 될때까지 반복
    while True:
        # 현재 위치가 도착 지점 인지 체크
        if i == 99:
            return 1
        # 현재위치 i에서 방문할 수 있는 w를 확인하고 방문
        for w in range(100):
            if adj[i][w] == 1 and visited[w] == 0:
                # 방문 체크
                visited[w] = 1
                # 현재 위치를 스택에 저장
                stack.append(i)
                # 다음 위치로 이동
                i = w
                # 현재 위치에서 탐색을 중단하고 다음 위치로 이동
                break
        else:
            #스택에 정점이 남아있는 경우 되돌아가기
            if stack:
                i = stack.pop()
            else:
                break
    # 반복이 끝나고 여기까지 오면 현재위치 i가 한번도 99가 된적이 없다
    # 길이 없다는 뜻
    return 0


T = 10

for tc in range(1, T + 1 ):
    _, e = map(int, input().split())

    edges = list(map(int,input().split()))
    adj = [[0] * 100 for _ in range(100)]

    # 인접 행렬 만들기
    for i in range(e):
        # 간선의 개수 * 2 = 꼭지점 정보 개수
        adj[edges[i*2]][edges[i * 2 + 1]] = 1
    print(f'#{tc} {dfs(0)}')
