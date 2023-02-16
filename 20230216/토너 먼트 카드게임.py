
def game(a,b):
    if abs(lst[a] - lst[b]) == 1:
        if lst[a] > lst[b]:
            return a
        else:
            return b
    if abs(lst[a] - lst[b]) == 2:
        if lst[a] > lst[b]:
            return a
        else:
            return b
    if abs(lst[a] - lst[b]) == 0:
        return a

def divide(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    first = nums[:mid]
    second = nums[mid:]
    first = divide(first)
    second = divide(second)
    return game(first[0], second[0])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    nums = list(range(N))
    print(divide(nums))