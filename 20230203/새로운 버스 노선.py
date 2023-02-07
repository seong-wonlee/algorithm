T = int(input())

N = int(input())
count = [0] * 1000

for tc in range(1, T+1):
    for i in range(0, N):
        type, A, B = map(int, input().split())
        for j in range(A, B+1):

            # 일반 버스인 경우
            if type == 1:
                count[j] += 1


            # 급행 버스인 경우
            if type == 2:
                # A가 짝수인 경우
                if A % 2 == 0:
                    # 짝수 번호에 정차
                    if j % 2 == 0:
                        count[j] += 1

                # A가 홀수인 경우
                else:
                    # 홀수 번호에 정차
                    if j % 2 != 0:
                        count[j] += 1


            # 광역 급행 버스인 경우
            if type == 3:
                # A가 짝수인 경우
                if A % 2 == 0 :
                    # 4의 배수 번호에 정차
                    if j % 4 == 0:
                        count[j] += 1

                # A가 홀수인 경우
                else:
                    # 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차
                    if j % 3 == 0 and j % 10 != 0:
                        count[j] += 1

    maxv = 0
    for k in range(0, 1000):
        if maxv < count[k]:
            maxv = count[k]

    print(f'#{tc} {maxv}')









