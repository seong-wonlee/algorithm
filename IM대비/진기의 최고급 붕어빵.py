# T = int(input())
N, M, K = map(int,input().split())    # N:손님 수 M초 들여서 K개 붕어빵 만들 수 있음
lst = list(map(int, input().split()))

per = [0] * 11111
for i in range(N):
    per[lst[i]] = 1
print(per)
for i in range(M,11112,M):
    per[i] = K
print(per)