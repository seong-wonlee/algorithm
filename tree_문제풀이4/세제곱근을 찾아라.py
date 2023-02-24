T = int(input())

for tc in range(1, T+1):
    ans = -1
    N = int(input())
    for i in range(1, int(N**(1/3)+2)):
        if i ** 3 == N:
            ans = i

    print(f'#{tc} {round(ans)}')


# 이진탐색 방법
def binary_search(key):
    start = 1
    end = key

    while 1 < end - start:
        middle = (start + end) // 2
        if middle ** 3 > key:
            end = middle
        else:
            start = middle
    if start ** 3 == key:
        return start
    else:
        return -1