# T = int(input())

word1 = list(map(str, input()))
word2 = list(map(str, input()))

for i in range(len(word1)):
    cnt = 0
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            cnt += 1
    maxv = 0
    if maxv < cnt:
        maxv = cnt
    print(maxv)

