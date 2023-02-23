T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N : 노드의 개수 M: 리프 노드의 개수 L: 값을 출력할 노드 번호
    tree = [0] * (N+1)  # 완전 이진트리
    for i in range(M):
        a, b = map(int, input().split())    # 리프노드에 저장하기
        tree[a] = b

    for i in range(N,0,-1): # 5부터 1까지 역순
        if i//2 > 0 :   # 부모에다가 자식 더하기
            tree[i//2] += tree[i]

    print(f'#{tc} {tree[L]}')


```
def post_order(i, N):
    if i <= N :
        if tree[i] == 0:
            r1 = post_order(i*2, N)    # 왼쪽 자식의 값 확인
            r2 = post_order(i*2+1, N)  # 오른쪽 자식의 값 확인
            tree[i] = r1+ r2    # post_order(i*2) + post_order(i*2+1)
        return tree[i]
    else:
        return 0
```