T = int(input())
for tc in range(1, T+1):

    N= int(input())
    lst = list(map(int, input()))
    count = [0] * 10

    for i in range(0, N):
        count[lst[i]] += 1
    # print(count)
    maxv = 0
    for i in range(0, len(count)):
        if maxv <= count[i]:
            maxv = count[i]
            maxv_idx = i


    print(f'#{tc} {maxv_idx} {maxv}')
