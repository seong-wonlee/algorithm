
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    # 가로 확인하기
    lst = []
    for i in range(100):
        for m in range(2,100):
            for j in range(100-m+1):
                if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                    lst.append(len(arr[i][j:j+m]))


    # 세로 확인하기
    arr2 = list(zip(*arr))
    lst2 = []
    for i in range(100):
        for m in range(2,100):
            for j in range(100-m+1):
                if arr2[i][j:j+m] == arr2[i][j:j+m][::-1]:
                    lst2.append(len(arr2[i][j:j+m]))

    # 둘 중에 큰거 가져오기
    if max(lst) > max(lst2):
        ans = max(lst)
    else:
        ans = max(lst2)

    print(f'#{tc} {ans}')
