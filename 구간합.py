

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    maxV = 0
    minV = 1000000
    for i in range(N-M+1):
        s = 0
        for j in range(i, i+M):
            s += arr[j]

        if maxV < s:
            maxV = s
        if minV > s:
            minV = s

    print(f'#{tc} {maxV-minV}')








#
# N = 6
# a = [1,2,3,4,5,6]
#
# s = 0
# for i in range(0, N):
#     s += a[i]
# print(s)