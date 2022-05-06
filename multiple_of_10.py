n = int(input())
l = list(map(int,input().split()))
newL=[]
for i in range(0,len(l)):
    if l[i]%10==0:
        k = l[i]
        newL.append(k)


for i in range(0,len(l)):
    if l[i] in newL:
        l[i] = "#"

for i in range(0,l.count('#')):
    l.remove("#")
    l.append(newL[i])

for i in l:
    print(i,end=" ")



