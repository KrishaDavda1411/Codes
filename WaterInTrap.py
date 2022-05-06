L = list(map(int,input().split()))
print(L)
max = 0
maxL =[]
for i in range(0,len(L)):
    if(L[i]>max):
        max = L[i]
        maxL.append(L[i])
    else:
        maxL.append(max)
print(maxL)
max2 = 0
max2L = []
for i in reversed(range(0,len(L))):
    if(L[i]>max2):
        max2 = L[i]
        max2L.append(L[i])
    else:
        max2L.append(max2)
max2L.reverse()
print(max2L)

ans = 0

for i in range(0,len(L)):
    p = min(maxL[i],max2L[i])
    # print(p)
    ans = ans + (p-L[i])
print(ans)