T = int(input())

for tc in range(1,T+1):
    N = int(input())

    def rectangle(n):
        if n == 10:
            return 1
        elif n == 20:
            return 3
        else:
            return rectangle(n-10) + 2 * rectangle(n-20)

    print(f'#{tc} {rectangle(N)}')