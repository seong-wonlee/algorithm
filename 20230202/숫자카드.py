T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    cnt = [0] * 10

    for i in range(0, len(lst)):
        cnt[lst[i]] += 1
    # print(cnt)
    maxV = 0

    for i in range(0, len(cnt)):
        if maxV <= cnt[i]:
            maxV = cnt[i]
            idx = i

    print("#{} {} {}".format(tc, idx, maxV))