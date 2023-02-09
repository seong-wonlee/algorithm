T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    # 가로 확인
    for i in range(N):
        for j in range(0,N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                ans = arr[i][j:j+M]

    # 세로 확인
    columns_lst = []
    for j in range(N):
        columns = [i[j] for i in arr]
        columns_lst.append(columns)
    for i in range(N):
        for j in range(0, N - M + 1):
            if columns_lst[i][j:j + M] == columns_lst[i][j:j + M][::-1]:
                ans = columns_lst[i][j:j + M]

    print(f'#{tc}',' ', *ans, sep='')










