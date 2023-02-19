def binarysearch(s,e, key):
    cnt = 0
    while s <= e : # 탐색 구간이 남아있으면
        m = int(s+e) // 2
        if m == key:
            return cnt
        elif m > key:
            e = m
        else:
            s = m
        cnt += 1

T= int(input())
for tc in range(1, T+1):
    P, pa, pb = map(int, input().split())
    cntA = binarysearch(1, P, pa)
    cntB = binarysearch(1, P, pb)
    if cntA == cntB:
        print(f'#{tc} 0')
    elif cntA < cntB:
        print(f'#{tc} A')
    else:
        print(f'#{tc} B')