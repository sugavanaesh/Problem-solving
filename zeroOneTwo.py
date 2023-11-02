l = [0,2,1,2,0,1,2]
c0,c1,c2 = 0,0,0
for i in range(len(l)):
    if l[i]==0:
        c0+=1
    elif l[i]==1:
        c1+=1
    elif l[i]==2:
        c2+=1

for i in range(c0):
    l[i]=0
for i in range(c0,c0+c1):
    l[i]=1
for i in range(c0+c1,len(l)):
    l[i]=2
print(l)