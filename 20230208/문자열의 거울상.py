T = int(input())
for tc in range(1, T +1):
    lst = list(map(str, input()))

    for i in range(len(lst)):
        if lst[i] == 'q':
            lst[i] = 'p'
        elif lst[i] == 'p':
            lst[i] = 'q'
        elif lst[i] == 'd':
            lst[i] = 'b'
        else:
            lst[i] = 'd'

    ans = lst[::-1]

    print(f'#{tc}',''.join(ans))

