# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     C_list = list(map(int, input().split()))
#     count = [0] * 10
#     count1 = [0] * 10
#     cnt = 0
#
#     for i in range(0, N):
#         count[C_list[i]] += i+1
#     print(count)
#
#     for j in range(1, 10):
#         if count[j] - count[j-1] == 1:
#             cnt += 1
#             count1[j] = 1
#
#     for j in range(1,N):
#         for k in range(1,N):
#             if (count1[j-1] == k) and (count1[j] == 1):
#                 count1[j] += count1[j-1]
#     print(count1)
#
#     maxv = 0
#     for m in range(0, 10):
#         if maxv < count1[m]:
#             maxv = count1[m]
#
#     print(maxv)
#     print(f'#{tc} {maxv+1}')





# T = int(input())
#
# for tc in range(1, T + 1):
N = int(input())
lst = list(map(int, input().split()))

rlt = 1
max_rlt = 1
for i in range(N - 1):
    if lst[i+1] > lst[i]:
        rlt += 1
        print(rlt)
    else:
        rlt = 1
        print(rlt)

    if rlt > max_rlt:
        max_rlt = rlt

# print(f'#{tc}', max_rlt)
