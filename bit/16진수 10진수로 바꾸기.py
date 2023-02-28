
arr = list(map(int, input()))
N = len(arr)
print(N, arr)
num = 0
for i in range(N):
    j = i % 7
    num += arr[i] * (2**(6-j))
    if j ==6:      # 7개 끊기
        print(num, end = ' ')
        num = 0
print()

arr = input()
for x in arr:
    print(int(x, 16))
    for j in range(3, -1, -1):
        bit = 1 if num&(1<<j) else 0
        print(bit, end = '')
    print(' ', end = '')