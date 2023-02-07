def consider(x,y):
    if x > y:
        return x
    else:
        return y



for tc in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        a, b, c, d, e = lst[i-2], lst[i-1], lst[i], lst[i+1], lst[i+2]
        h1 = consider(a,b)
        h2 = consider(d,e)
        h3 = consider(h1,h2)
        if h1 < c and h2 < c:
            answer += c - h3


    print(f'#{tc+1} {answer}')








