def f(i, k):
    if i == k:
        print(n)

    else:
        for j in range(i, k):
            n[i], n[j] = n[j], n[i]
            f(i+1,k)
            n[i], n[j] = n[j], n[i]



n = [1, 2, 3]
k = len(n)
f(0,k)