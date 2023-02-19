lst = [55, 7, 78, 12, 42]
n = 5
# 오름차순
for i in range(n-1,-1, -1):
    for j in range(0,i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j + 1] = lst[j+1], lst[j]

# 내림차순
for i in range(n):
    for j in range(n-1, i, -1):
        if lst[j] > lst[j-1]:
            lst[j], lst[j - 1] = lst[j-1], lst[j]
print(lst)