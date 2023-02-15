def f(i, k):
    if i == k :
        print(bit)
        return
    else :
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0
        f(i+1, k)
        return

A = {1,2,3}
N = len(A)
bit = [0] * N

print(f(0,3))