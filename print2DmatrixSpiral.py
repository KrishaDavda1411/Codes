n = int(input())
m =  int(input())
rows,cols = n,m
arr =[]
for i in range(rows):
    col = []
    for j in range(cols):
        k = int(input())
        col.append(k)
    arr.append(col)
# print(arr)
print("initial------------------------------------")
for row in arr:
    print(row)

sr = 0
er = n
err=n-1

sc = 0
ec = n
ecc=n-1

i =0
while i<n*m:
    for j in range(sc,ec):
        print(arr[sr][j],end=" ")
        i+=1
    sr+=1
    if(i==n*m): break
    for j in range(sr,er):
        print(arr[j][ecc],end=" ")
        i+=1
    ec-=1
    if (i == n * m): break
    for j in reversed(range(ec,sc)):
        print(arr[err][j],end=" ")
        i+=1
    er-=1
    if (i == n * m): break

    for j in reversed(range(er,sr)):
        print(arr[j][sc],end=" ")
        i+=1
    sc+=1
    if (i == n * m): break




