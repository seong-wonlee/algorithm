# 카운팅 정렬
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lst = list(map(int, input().split()))

    count = [0] * (max(lst)+1)
    for i in range(N):
        count[lst[i]] += 1
    # print(count)
    for j in range(1,len(count)):
        count[j] += count[j-1]
    # print(count)
    temp = [0] * N
    for i in range(len(temp)-1, -1, -1):
        count[lst[i]] -= 1
        temp[count[lst[i]]] = lst[i]
    print(f'#{tc}', *temp)