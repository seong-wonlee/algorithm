# 중위 순회

def f(i):
    if i < N+1:
        f(i*2)
        cnt.append(lst[i])
        print(cnt)
        f(i * 2 + 1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노드 수
    cnt = []
    lst = [i for i in range(N+1)]
    f(1)
    # print(cnt)
    for i in range(N):
        if cnt[i] == 1:
            ans = i+1
        if cnt[i] == N//2:
            ans2 = i+1

    print(f'#{tc}', ans, ans2)