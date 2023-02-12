T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input()))

    cnt = 0
    cnt_lst = []
    for i in range(0,N):
        if lst[i] == 1 :
            cnt += 1
            cnt_lst.append(cnt)
        else:
            cnt = 0
            cnt_lst.append(cnt)

    maxv = 0
    for i in range(N):
        if maxv < cnt_lst[i]:
            maxv = cnt_lst[i]
    print(f'#{tc} {maxv}')