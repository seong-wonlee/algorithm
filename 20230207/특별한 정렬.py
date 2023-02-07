def sort_array(array, n):
    for i in range(0, n-1):
        mindx = i
        for j in range(i+1, n):
            if array[mindx] > array[j]:
                mindx = j
        array[mindx], array[i] = array[i], array[mindx]
    return array[-1], array[0], array[-2], array[1], array[-3], array[2],array[-4],array[3], array[-5], array[4]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = sort_array(lst, N)
    print(f'#{tc}', *ans)


