
for tc in range(1, 11):

    m = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    ans_lst = []
    # 가로확인
    for i in range(8):
        for j in range(8-m+1):
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                ans_lst.append(arr[i][j:j+m])

    # 세로확인
    columns_lst = []
    for j in range(8):
        columns = [i[j] for i in arr]
        columns_lst.append(columns)
    # print(columns_lst)
        for k in range(8-m+1):
            if columns_lst[j][k:k+m] == columns_lst[j][k:k+m][::-1]:
                ans_lst.append(columns_lst[j][k:k+m])


    print(f'#{tc} {len(ans_lst)}')
