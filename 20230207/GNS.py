lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


T = int(input())
for tc in range(1, T+1):
    num = list(input().split())
    dict = {}
    key_lst = []
    for i in range(0,10):
        dict[i] = lst[i] # dict= {0:'zro', 1:'one' ...}
    for key in dict:
        key_lst.append(key)
    # print(key_lst)
    word = list(map(str, input().split()))
    for j in range(0,len(word)):
        for r in range(0, 10):
            if word[j] == dict[r]:
                word[j] = key_lst[r]

    word.sort()
    for k in range(0, len(word)):
        word[k] = dict[word[k]]

    print(f'#{tc}')
    print(*word)