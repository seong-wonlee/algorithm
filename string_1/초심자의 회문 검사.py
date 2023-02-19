T = int(input())

for tc in range(1, T+1):

    lst = list(map(str, input()))
    mid = len(lst) // 2
    lst1 = lst[:mid]
    lst2 = lst[mid:]

    cnt = 0
    for i in range(0, len(lst1)):
        if lst1[i] == lst2[-i-1]:
            cnt += 1

    if cnt == mid:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')
