N = int(input())

arr = [list(map(str, input())) for _ in range(8)]

ans = []
for i in range(8):
    for j in range(8-N+1):
        if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
           ans.append(arr[i][j:j+N])

arr2 = list(zip(*arr))
print(arr2)
for i in range(8):
    for j in range(8-N+1):
        if arr2[i][j:j+N] == arr2[i][j:j+N][::-1]:
            ans.append(arr2[i][j:j+N])
print(len(ans))