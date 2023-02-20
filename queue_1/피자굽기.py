T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = []
    # 화덕 채우기
    for i in range(N):
        oven.append(i)    # 피자번호
    last = N-1      # 화덕에 들어간 마지막 피자번호
    # 더 이상 피자가 없을 때까지 회전
    ans = 0     # 마지막으로 완성된 피자 번호
    while oven:
        num = oven.pop(0)      # 입구로 돌아온 피자 번호
        pizza[num] //= 2        # 한바퀴 돌면서 절반이 녹음
        if pizza[num] > 0:      # 완전히 녹지 않은 경우
            oven.append(num)
        else:   # 녹았으면
            ans = num       # 이후에 나오는 피자가 없으면 마지막 피자
            if last+1 < M:    # 아직 화덕에 들어가지 않은 피자가 있으면
                last += 1       # 추가로 화덕에 투입
                oven.append(last)
    print(f'#{tc} {ans+1}')





# 피자 배열에 치즈가 뿌려진 피자의 자료를 받음
pizza = list(map(int, input().split()))
# 화덕에 들어가는 피자 인덱스 정보를 받을 배열 오븐을 선언
oven = []
for i in range(n):
    oven.append(i)
# 오븐에 들어간 마지막 피자의 인덱스 값을 선언
last = n-1
ans = 0
# 화덕에 들어가있는 피자가 존재하는 동안 반복
while oven:
    # 맨 앞의 피자 인덱스를 임시변수에 저장
    tmp = oven.pop(0)
    # 임시변수 번째 피자의 치즈를 녹임
    pizza[tmp] //= 2
    # 해당 임시변수번째 피자의 치즈가 다 녹은 경우
    if pizza[tmp] == 0:
        # ans 에 임시변수의 인덱스를 할당
        ans = tmp
        # 배열이 m-1개까지 있기에 해당 구간까지 진행
        if last < m-1:
            # 피자가 오븐에 추가될때마다 갱신
            last += 1
            # 오븐에 새로운 피자를 넣어줌
            # 오븐에 새로 넣은 피자의 번호를 저장
            oven.append(last)
    # 아직 다 녹지 않았으면 인덱스를 오븐 배열의 맨 뒤로 넣어줌
    else:
        oven.append(tmp)
# 최종적으로 마지막으로 치즈를 녹인 피자의 번호를 출력
# 단 피자의 번호 시작을 0이 아닌 1부터 했기에 1을 더함
print(f'#{tc+1} {ans+1}')

