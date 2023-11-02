l = [7,1,5,3,6,4]
minpr = float('inf')
maxpr = 0
for i in range(len(l)):
    minpr = min(minpr,l[i])
    maxpr = max(maxpr,l[i]-minpr)

print(maxpr)