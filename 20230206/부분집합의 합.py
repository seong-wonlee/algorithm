T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    num = [int(i) for i in range(1, 13)]
    # print(num)
    new = []
    cnt = 0
    for i in range(1 << len(num)): # 1<<len(num) : 부분 집합의 개수
        lst = []
        for j in range(len(num)): # 원소의 수만큼 비트를 비교함
            if i & (1 << j):    # i의 j번 비트가 1인경우
                lst.append(num[j])
        if len(lst) == n and sum(lst) == k:
            cnt += 1

    print("#{} {}".format(tc, cnt))