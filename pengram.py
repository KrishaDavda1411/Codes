#if string contain all alphabet a to z then its pengram
s = input()
s = s.lower()
s = s.replace(" ","")
slist = [c for c in s]
print(slist)
l = "abcdefghijklmnopqrstuvwxyz"

llist = [c for c in l]
llist.sort()

for k in llist:
    print(llist.count(k))
L = [0]*26
print(L.count(0))
m =0
for k in range(0,len(s)):
    c = slist[k]
    i = llist.index(c)
    # print(i)
    if(L[i]!=0):
        m+=1
        L[i]+=1
        # L.pop(-1)
    else:
        L[i]=1
        # L.pop(-1)

print(L.count(1))
print(L)
if 0 in L:
    print("NO")
else:
    print("yes")