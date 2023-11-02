l = [-2,1,-3,4,-1,2,1,-5,4]
ms,css = float('-inf'),0
for i in range(len(l)):
    css += l[i]
    ms = max(ms,css)
    css = max(css,0)
print(ms)