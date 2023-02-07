# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     cnts = [0] * 5001
#     for i in range(N):
#         s, e = map(int, input().split())
#         for i in range(s, e+1):
#             cnts[i] += 1
#
#     P = int(input())
#     alst = []
#     for i in range(P):
#         p = int(input())
#         alst.append(cnts[p])


T = int(input())

for tc in range(1,T+1):

    N = int(input())
    count = [0] * 50001
    for i in range(0, N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            count[i] += 1
    # print(count)

    P = int(input())
    lst = []
    for j in range(0, P):
        busstop = int(input())
        lst.append(busstop)
    # print(lst)

    for i in range(0, len(lst)):
        lst[i] = count[lst[i]]
    # print(lst)

    print(f'#{tc}', *lst)






























