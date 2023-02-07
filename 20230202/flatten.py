# 834
# 42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34 74 65 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 2 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42




# for tc in range(1, 11):
dump = int(input())
height_list = list(map(int, input().split()))

while dump >= 0 :

    maxv = -1
    minv = 101

    for i in range(0, len(height_list)):
        if maxv < height_list[i]:
            maxv = height_list[i]
            max_index = i

        if minv > height_list[i]:
            minv = height_list[i]
            min_index = i
    # print(height_list[max_index])
    # print(height_list[min_index])
    if dump == 0:
        print(f'#{6} {height_list[max_index] - height_list[min_index]}')
    else :
        height_list[max_index] = height_list[max_index] - 1
        height_list[min_index] = height_list[min_index] + 1
    dump -= 1



