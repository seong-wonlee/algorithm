for i in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    while True:
        if lst[-1] == 0:
            break
        for j in range(1, 6):
            a = lst.pop(0)
            if a-j <= 0:
                lst.append(0)
                break
            else:
                lst.append(a-j)
    print(f'#{n}', *lst)

