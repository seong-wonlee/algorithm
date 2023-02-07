T = int(input())
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    p = 3
    lst = []
    for i in range(0, N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    lst.append(abs(arr[i][j] - arr[ni][nj]))
    print(f'#{tc} {sum(lst)}')

