# 선형큐
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = [0] * 1000000
    front = -1
    rear = -1
    dough = N  # 오븐에 들어갈 차례인 피자 번호
    door = 0  # 입구로 돌아온 피자 번호
    for i in range(N):  # oven 채우기
        rear += 1
        oven[rear] = i  # 피자번호 - 1 (0번부터, 문제에서는 1번부터)

    while front != rear:  # oven이 비어있지 않으면
        front += 1
        door = oven[front]  # 입구로 돌아온 피자를 꺼내고
        pizza[door] //= 2  # 녹은 치즈 기록
        if pizza[door] > 0:  # 치즈가 남아있으면
            rear += 1
            oven[rear] = door  # 다시 투입
        else:  # 치즈가 모두 녹은 경우
            if dough < M:  # 구울 피자가 남아있으면
                rear += 1
                oven[rear] = dough  # 오븐에 투입
                dough += 1  # 다음에 투입할 피자
    print(f'#{tc} {door + 1}')