T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())    # N:손님 수 M초 들여서 K개 붕어빵 만들 수 있음
    lst = list(map(int, input().split()))
    lst.sort()

    for i in range(N):
        if (lst[i] // M) * K < i+1:     # 만들 수 있는 붕어빵 수 < 지금까지 온 손님의 숫자
            ans = 'Impossible'
            break
        else:
            ans = 'Possible'
    print(f'#{tc} {ans}')