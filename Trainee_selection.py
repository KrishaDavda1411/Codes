arr=[]
for i in range(0,3):
    col=[]
    for j in range(0,3):
        col.append(int(input()))
    arr.append(col)

for row in arr:
    print(row)

avg_oxi=[]
for i in range(0,3):
    sum=0
    for j in range(0,3):
        sum+=arr[j][i]
    avg = sum/3
    avg_oxi.append(avg)

m1 = max(avg_oxi)

print(avg_oxi)
for i in range(0,len(avg_oxi)):
    if m1==avg_oxi[i]:
        print("Trainee number: {}".format(i+1))


