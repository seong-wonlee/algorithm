
def count(arr):
    maxv = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
                if maxv < cnt:
                    maxv = cnt
            else:
                cnt = 0
    return maxv

T = int(input())
for tc in range(1,T +1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    ans = max(count(arr), count(arr_t))

    print(f'#{tc} {ans}')
