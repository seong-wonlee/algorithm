
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    maxV = 0

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                cnt += 1

        if cnt > maxV:
            maxV = cnt

    print(f'#{tc} {maxV}')