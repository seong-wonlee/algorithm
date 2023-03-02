T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    lst = []
    i = 0
    for r in range(n):
         lst.append(arr[i][n//2-r:n//2+r+1])
         i += 1
         if i > n//2:
             break

    sum = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            sum += lst[i][j]

    k = n-1
    lst2 = []
    for r in range(n):
         lst2.append(arr[k][n//2-r:n//2+r+1])
         k -= 1
         if k == n//2:
             break

    for i in range(len(lst2)):
        for j in range(len(lst2[i])):
            sum += lst2[i][j]

    # n이 1일 때
    if lst == lst2:
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                sum = lst[i][j]

    print(f'#{tc} {sum}')



