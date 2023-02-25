T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dict = {'0001101' : 0,'0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001':5,
            '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                code = arr[i][j-55:j+1]
                break
    # print(code)
    mycode = []
    for i in range(0, 56, 7):   # 코드 분리
        mycode.append(code[i:i+7])
    # print(mycode)

    odd = 0     # 홀수
    even = 0    # 짝수
    for i in range(4):
        odd += dict[mycode[2*i]]
        even += dict[mycode[2*i+1]]

    if (odd * 3 + even) % 10 == 0:  # 올바른 암호코드이면
        ans = odd + even
    else:
        ans = 0
    print(f'#{tc} {ans}')