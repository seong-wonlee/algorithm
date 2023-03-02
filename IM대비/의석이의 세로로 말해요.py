T = int(input())
for tc in range(1,T+1):
    lst2 = []
    word = [input() for _ in range(5)]

    for i in range(len(word)):
        lst2.append(len(word[i]))    # 단어 길이

    for i in range(len(word)):
        if len(word[i]) != max(lst2):
            word[i] = word[i] + '.' * (max(lst2)-len(word[i]))
    ans = []
    for i in range(max(lst2)):
        for j in range(5):
            if word[j][i] != '.':
                ans.append(word[j][i])
    print(f'#{tc} ', *ans, sep = '')