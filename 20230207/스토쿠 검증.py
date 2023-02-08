# T = int(input())
arr = [list(map(int, input().split())) for _ in range(9)]
num = [0] * 10
count = [[0]*3 for _ in range(3)]
# 열 확인

for j in range(9):
    # num = [0] * 10
    num[arr[0][j]] = 1
    # print(num)
for k in range(1,10):
    if num[k] != 0:
        print(0)
    else:
        print(1)

# 행 확인

for i in range(9):
    num[arr[i][0]] = 1
    # print(num)
for k in range(1,10):
    if num[k] != 0:
        print(0)
    else:
        print(1)

3x3 확인
# lst = []
for i in range(9):
    n = i % 3
    if


