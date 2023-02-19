T = int(input())
for tc in range(1,T+1):
    N = int(input())


    lst = list(map(int, input().split()))

    minv = 1000001
    maxv = 0
    for i in range(N):
        if minv > lst[i]:
            minv = lst[i]
        if maxv < lst[i]:
            maxv = lst[i]
    print(f'#{tc} {maxv-minv}')