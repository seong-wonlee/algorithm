T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    i = 0   # 인덱스(커서)
    cnt = 0 # 카운트

    while i < len(a):
        # a안에 처음 커서부터 b길이 만큼의 값이 b와 같으면
        if a[i:i+len(b)] == b:
            cnt += 1
            i += len(b)
        # 같지 않으면
        else:
            i += 1
            cnt += 1
    print(f'#{tc} {cnt}')



