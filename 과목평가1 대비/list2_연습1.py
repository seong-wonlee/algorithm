# T = int(input())
di = [0, 1, 0, -1] # 오른쪽 아래 왼쪽 위
dj = [1, 0, -1, 0]

N = int(input())
arr = [list[map(int, input().split())] for _ in range(N)]

ans_lst = []
for i in range(N):
    for j in range(N):
        for k in range(4):
            ci = i + di[k]
            cj = j + dj[k]
            if 0 <= ci < N and 0 <= cj < N:
                ans_lst.append(abs(arr[i][j] - arr[ci][cj]))
print(ans_lst)
