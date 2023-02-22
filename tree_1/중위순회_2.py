def f(i):
    if i < N+1:
        f(i*2)
        cnt.append(lst2[i])
        f(i * 2 + 1)

for tc in range(1,11):
    lst2 = [[]]
    N = int(input())    # 노드 수
    for i in range(N):
        lst = list(input().split())
        lst2.append(lst[1])
    cnt = []
    f(1)
    print(f'#{tc} ', *cnt, sep = '')