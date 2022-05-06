l = int(input())
h = int(input())
coun = 0
for i in range(l,h+1):
    L =[]

    while i!=0:
        m = i%10
        if m not in L:
            L.append(m)
        else:
            break
        i=i//10
    if len(L) == len(str(l)):
        coun+=1


# n = 112
# print(len(str(n)))
print(coun)
