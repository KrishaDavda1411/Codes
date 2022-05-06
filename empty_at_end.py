l = list(map(int,input().split()))

for i in range(0,len(l)):
    if l[i]==0:
        l.append(0)
        l.remove(0)


print(l)
# for i in range(0,len())