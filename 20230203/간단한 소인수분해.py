# T = int(input())

# cnt_2 = 0
# cnt_3 = 0
# cnt_5 = 0
# cnt_7 = 0
# cnt_11 = 0
#
# N= int(input())
#
#
# def divide(x,y):
#     if x % y == 0:
#
#

T = int(input())

for tc in range(1, T+1):
    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    cnt_7 = 0
    cnt_11 = 0
    N = int(input())
    while True:
        if N % 2 == 0:
            cnt_2 += 1
            N = N / 2

        if N % 3 == 0:
            cnt_3 += 1
            N = N / 3

        if N % 5 == 0:
            cnt_5 += 1
            N = N / 5

        if N % 7 == 0:
            cnt_7 += 1
            N = N / 7

        if N % 11 == 0:
            cnt_11 += 1
            N = N / 11

        if N == 1:
            break


    print(f'#{tc} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}')


