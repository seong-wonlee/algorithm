T = int(input())
for tc in range(1,  T+1):
    str1 = list(map(str, input()))
    join_str1 = ''.join(str1)
    str2 = list(map(str, input()))
    join_str2 = ''.join(str2)

    if join_str1 in join_str2:
        a = 1
    else:
        a = 0

    print(f'#{tc} {a}')