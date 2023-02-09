# T = int(input())
arr = [list(map(int, input().split())) for _ in range(9)]
num = [0] * 10
count = [[0]*3 for _ in range(3)]

# 가로 확인
row_lst = []
for i in range(9):
    row_lst.append(arr[i][0:9])
for j in range(9):
    for k in range(9):
        num[row_lst[j][k]] += 1
print(num)






