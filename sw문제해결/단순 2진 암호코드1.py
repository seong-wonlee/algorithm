T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
            '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                code = arr[i][j -55:j +1]
                break

    mycode = []
    for i in range(0,56,7):     # 코드 8개로 쪼개기
        mycode.append(code[i:i+7])
    print(mycode)

    num = [0] * 8
    for i in range(8):
        num[i] = dict[mycode[i]]    # 코드 8개 숫자로 변환


    sum = 0
    sum1 = 0
    for i in range(8):
        if i % 2 == 0:  # 홀수합
            sum += num[i]
        else:
            sum1 += num[i]  # 짝수합

    if (sum * 3 + sum1) % 10 == 0:
        ans = sum + sum1
    else:
        ans = 0

    print(f'#{tc} {ans}')



