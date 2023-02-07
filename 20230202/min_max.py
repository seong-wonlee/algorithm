# 1번쨰 방법
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = arr[0]
    minV = arr[0]

    for i in range(1, N):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]

    print(f'#{tc} {maxV-minV}')

# 2번쨰 방법
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 1
    minV = 1000000

    for i in range(1, N):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]

    print(f'#{tc} {maxV-minV}')

