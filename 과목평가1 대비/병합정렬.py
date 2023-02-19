def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    first_lst = lst[:mid]
    second_lst = lst[mid:]
    first_lst = merge_sort(first_lst)
    second_lst = merge_sort(second_lst)

    lst2 = []
    i, j = 0, 0
    while i < len(first_lst) and j < len(second_lst):
        if first_lst[i] > second_lst[j]:
            lst2.append(second_lst[j])
            j += 1
        else:
            lst2.append(first_lst[i])
            i += 1

    while j < len(second_lst):
        lst2.append(second_lst[j])
        j += 1

    while i < len(first_lst):
        lst2.append(first_lst[i])
        i += 1

    return lst2

N, K = map(int, input().split())
lst = list(map(int, input().split()))
print(merge_sort(lst))




