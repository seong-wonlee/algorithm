def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현

def win(a, b):
    if abs(lst[a] - lst[b]) == 1:
        if lst[a] > lst[b]:
            return a
        else:
            return b
    if abs(lst[a] - lst[b]) == 2:
        if lst[a] > lst[b]:
            return b
        else:
            return a
    if lst[a] == lst[b]:
        return a

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc}', f(0,N-1)+1)