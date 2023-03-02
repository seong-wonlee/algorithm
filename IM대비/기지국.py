# T = int(input())
didj = [(1,0), (-1,0), (0,1), (0,-1)]

n = int(input())
arr = [input() for _ in range(n)]

cnt1 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'H':
            cnt1 += 1
# print(cnt1)
        cnt = 0
        for k in range(4):
            if arr[i][j] == 'A':
                ni = i + didj[k][0]
                nj = j + didj[k][1]
                if 0 <= ni <n and 0 <= nj <n:
                    if arr[ni][nj] == 'H':
                        cnt += 1
        if cnt == 4:
            cnt1 -= cnt
print(cnt1)





