n = int(input())
m = int(input())
k = []
for i in range(0,m):
    col = []
    for j in range(0,n):
        m = int(input())
        col.append(m)
    k.append(col)
cl=[]
for row in k:
    print(row)
    c = row.count(1)
    cl.append(c)
    # print(cl)
print(cl.index(max(cl))+1)