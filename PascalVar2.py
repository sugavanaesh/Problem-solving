def ncr(n,r):
    res = 1
    for i in range(r):
        res = res*(n-i)
        res = res // (i+1)
    return res

def pascal(n):
    for i in range(1,n+1):
        print(ncr(n-1,i-1),end=" ")
    print()

n = 10
pascal(n)