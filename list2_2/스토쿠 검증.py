
T = int(input())
for tc in range(1, T +1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    # 가로/세로 확인
    for i in range(9):
        num = [0] * 10
        num2 = [0] * 10
        for j in range(9):
            num[arr[i][j]] += 1
            num2[arr[j][i]] += 1

        for k in range(1, 10):
            if num[k] != 1:
                result = 0
                break
            if num2[k] != 1:
                result = 0
                break

    # 3x3 확인
    for i in range(3):
        for j in range(3):
            count = [0] * 10
            for k in range(3):
                for r in range(3):
                    count[arr[i * 3 + k][j * 3 + r]] += 1

            for l in range(1, 10):
                if count[l] != 1:
                    result = 0
                    break

    print(f'#{tc} {result}')


# set 써서 풀어보기