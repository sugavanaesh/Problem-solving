l = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(l)):
    for j in range(len(l)-1,-1,-1):
        print(l[j][i],end=" ")
    print()