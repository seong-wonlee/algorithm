T = int(input())
N = int(input())

arr = [[0] * (N) for _ in range(N)]
# print(arr)
for i in range(N):
    for j in range(N):
        if j == 0 or i == j :
            arr[i][j] = 1
        elif i > j:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


for lst in arr:
    for j in range(len(lst)):
        if lst[j] != 0)
            print(lst[j]
