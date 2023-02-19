T = int(input())
for tc in range(1, T +1):
    P, A, B = map(int, input().split())
    # a : 배열 N : 제일끝 개수
    def divide(N, key):
        cnt = 0
        start = 1
        end = N
        while start <= end:
            middle = (start + end) // 2
            if middle == key:
                return cnt
            elif middle > key:
                cnt += 1
                end = middle
            else:
                cnt += 1
                start = middle
        return cnt

    if divide(P, A) > divide(P,B):
        print(f'#{tc} B')
    elif divide(P, A) == divide(P,B):
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A')