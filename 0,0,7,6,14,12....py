# 0,0,7,6,14,12,21,18,28...
l =[]
k,m=0,0
for i in range(0,30):
    if i==0:
        l.append(0)
    elif i ==1:
        l.append(0)
    elif i%2==0:
        k = k+7
        l.append(k)
    elif i%2!=0:
        m=m+6
        l.append(m)

print(l)
l =[]
k,m=1,1
for i in range(0,30):
    if i==0:
        l.append(1)
    elif i ==1:
        l.append(1)
    elif i%2==0:
        k = k*2
        l.append(k)
    elif i%2!=0:
        m=m*3
        l.append(m)

print(l)
