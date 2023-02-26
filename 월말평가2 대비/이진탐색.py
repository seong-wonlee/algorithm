def f(i):
    if i < N+1:
        f(i*2)
        cnt.append(lst[i])
        f(i*2+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = []
    lst = [i for i in range(N+1)]
    f(1)
    for i in range(N):
        if cnt[i] == 1:
            ans = i+1
        elif cnt[i] == N//2:
            ans2 = i+1
    print(f'#{tc}', ans,ans2)