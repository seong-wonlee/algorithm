k = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def f(arr, i):
    mid = len(arr)//2
    tree[i].append(arr[mid])
    if len(arr) == 1:
        return
    f(arr[:mid], i+1)
    f(arr[mid+1:], i+1)


f(lst,0)
for i in range(k):
    print(*tree[i])















