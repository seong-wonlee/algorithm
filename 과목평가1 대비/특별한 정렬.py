# T = int(input())
N = int(input())
lst = list(map(int, input().split()))

count = [0] * (max(lst)+1)

for i in range(N):
    count[lst[i]] += 1

for i in range(1, len(count)):
    count[i] += count[i-1]

temp = [0] * N
for k in range(len(lst)-1, -1, -1):
    count[lst[k]] -= 1
    temp[count[lst[k]]] = lst[k]
temp[-1], temp[-1],temp[-1],temp[-1],temp[-1],temp[-1],temp[-1],temp[-1]

