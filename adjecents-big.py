L = list(map(int,input().split()))
c = 0
for i in range(0,len(L)):
    if i==0:
        if L[i+1]>L[i]:
            c+=1
    elif i==len(L)-1:
        if L[i]<L[i-1]:
            c+=1
    elif L[i]<L[i-1] and L[i]<L[i+1]:
        c+=1

print(c)


