T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    minX = lst[0]
    for i in range(0, N+1):
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    result = ' '.join(map(str, lst))
    print(f'#{tc} {result}')


