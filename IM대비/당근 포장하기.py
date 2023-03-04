T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ci = list(map(int, input().split()))
    count = [0] * (31)
    for i in range(N):
        count[ci[i]] += 1

    ans = 1000      # 당근 개수 차이 최소값 초기화
    for i in range(1,30):
        for j in range(i+1, 31):
            small = sum(count[0:i+1])
            medium = sum(count[i+1:j+1])
            large = sum(count[j+1:31])

            if 0 < small <= N//2 and 0 < medium <= N//2 and  0 < large <= N//2:
                ans = min(ans, max(small, large, medium) - min(small, large, medium))
    if ans == 1000:
        ans = -1
    print(f'#{tc} {ans}')








