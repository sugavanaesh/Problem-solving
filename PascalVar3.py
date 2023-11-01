def ncr(n,r):
    res = 1

    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res
 
def pascal(n):
    val = []
    for i in range(1,n+1):
        tempList = []
        for j in range(1,i+1):
            tempList.append(ncr(i-1,j-1))
        val.append(tempList)
    return val
n = 24
ans = pascal(n)
for i in ans:
    for j in i:
        print(j,end=" ")
    print()