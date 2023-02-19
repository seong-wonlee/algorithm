T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int,input().split())
    charge_list = list(map(int, input().split()))
    count = current = 0


    # error 인 경우
    for i in range(0, M-1):
        # charge_list 의 사이 간격이 k보다 큰경우 에러 -> 0 출력
        if charge_list[i+1] - charge_list[i] > K:
            print(f'#{tc} {0}')
            break
        # 첫번째 충전 정류장이 k보다 큰 경우 에러 -> 0 출력
        elif charge_list[0] > K :
            print(f'#{tc} {0}')
            break

    # error가 아닌 경우
    # 최대 거리 k 만큼 위치 이동
    else:
        while current < N:
            current += K
            if current >= N:
                break
            # k번째 이동한 버스위치에 충전 정류장이 존재하지 않는 경우 백스텝
            elif (current not in charge_list) and (current <= N):
                # 충전 정류장에 도달할때까지 반복
                while current not in charge_list:
                    current -= 1
                # 충전 정류장에 도달하였을 경우
                count += 1

            # k번째 이동한 버스위치에 정류장이 딱 존재하고 버스위치가 N노선 안에 존재할 경우
            else:
                if current > N:
                    break
                count += 1

        print(f'#{tc} {count}')




