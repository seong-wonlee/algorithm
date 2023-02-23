
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0

    # heap에 인큐
    for i in range(N):
        enq(lst[i])

    # 조상노드 합 구하기
    n = len(heap)-1
    ans = 0
    while n > 0:
        ans += heap[n//2]
        n = n // 2
    print(f'#{tc} {ans}')
