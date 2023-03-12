T = int(input())
for tc in range(1, T+1):
    N = int(input())
    word = ''
    for i in range(N):
        ci, ki = input().split()
        word += ci * int(ki)
        
    print(f'#{tc}')
    for i in range(0,len(word),10):
        print(word[i:i+10])

