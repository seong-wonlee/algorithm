T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input()))

    count = [0] * N
    # count에 값 채우기
    for i in range(N):
        if lst[i] == 1:
            count[i] += 1


    # count에 연속한 값 누적해서 더하기
    for j in range(1,N):
        for k in range(1,N):
            if (count[j-1] == k) and (count[j] == 1):
                count[j] += count[j-1]
    # print(count)

    # count에서 최댓값 구하기
    maxv = 0
    for k in range(0,N):
        if maxv < count[k]:
            maxv = count[k]

    print(f'#{tc} {maxv}')

