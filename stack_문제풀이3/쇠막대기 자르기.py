# 쌓여있는 막대기 수 cnt
# '(' : cnt += 1
#         레이저 시작
# ')' : if st[i-1] == '(' -> 레이저
#         cnt -= 1, ans += cnt
#     else #')' 막대기 끝
#         cnt -= 1, ans += 1

T = int(input())
for tc in range(1, T +1 ):
    st = input()
    ans = 0 # 막대조각
    cnt = 0 # 쇠막대기
    for i in range(len(st)):
        if st[i] == '(': # 막대기 시작 또는 레이저
            cnt += 1
        else:   # ')'
            cnt -= 1
            if st[i-1] == '(': # 바로 앞에 있는 기호 확인해야함
                ans += cnt
            else: ans += 1
    print(f'#{tc} {ans}')


