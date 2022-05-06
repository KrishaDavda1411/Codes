# import array as arr
n = int(input())

# k = arr.array()

k=[]
for i in range(n):
    col=[]
    for j in range(n):
        inp = int(input())
        col.append(inp)
    k.append(col)
for row in k:
    print(row)

suml,sumr=0,0
i=0
j=0
while i!=n and j!=n:
    suml += k[i][j]
    i+=1
    j+=1

i =0
j = n-1
while(i!=n):
    sumr += k[i][j]
    i+=1
    j-=1

diff = abs(suml-sumr)
print(diff)
