n,m = input().split()
# print(n,m)
l = len(m)
nL =[]
# if l==1:
for i in range(int(n),int(m)+1):
    o = l - len(str(i))
    s = ""
    if o == l:
        nL.append(str(i))
        break
    while o!=0:
        s = s+"0"
        o-=1
    s = s + str(i)
    nL.append(s)
# print(nL)
for i in range(0,len(nL)):
    print(nL[i],end=" ")
# else:
#     for i in range(int(n),int(m)+1):
#         print(i,end=" ")

