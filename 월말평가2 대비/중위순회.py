def f(i):   # 중위순회
    if i < N+1:
        f(i*2)
        cnt.append(lst2[i])
        f(i*2+1)



cnt = []
N = int(input())
lst2 = [[]]
for i in range(N):
    lst = list(input().split())
    lst2.append(lst[1])
print(lst2)
f(1)
print(cnt)
