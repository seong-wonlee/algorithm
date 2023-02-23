for tc in range(1,11):
    N = int(input())
    left = [0] * (N+2)
    right = [0] * (N+2)
    lst2 = [0] * (N+1)
    for i in range(1,N+1):
        lst = list(input().split())
        lst2[i] = lst[1]    # 정점 번호 인덱스에 정점 정보 받기
        if len(lst) == 4:
            a, b, c = int(lst[0]), int(lst[2]), int(lst[3])
            left[a] = b
            right[a] = c

    for i in range(N, 0, -1): # N부터 1까지 역순
        if lst2[i] == '+':
            lst2[i] = int(lst2[left[i]]) + int(lst2[right[i]])
        if lst2[i] == '*':
            lst2[i] = int(lst2[left[i]]) * int(lst2[right[i]])
        if lst2[i] == '-':
            lst2[i] = int(lst2[left[i]]) - int(lst2[right[i]])
        if lst2[i] == '/':
            lst2[i] = int(lst2[left[i]]) // int(lst2[right[i]])

    print(f'#{tc} {lst2[1]}')





