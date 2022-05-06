'''
1 2 3    1 4 7        7 4 1
4 5 6 -> 2 5 8   ->   8 5 2
7 8 9    3 6 9        9 6 3
        transpose    rev each row'''

n = int(input())
rows,cols = n,n
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
#transpose
for i in range(0,n):
    for j in range(i,n):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
print("\ntranspose-------------------------------")
for row in arr:
    print(row)
#reverse rows
for i in range(0,n):
    s =0
    e =n-1
    while(s<=e):
        arr[i][s],arr[i][e] =arr[i][e],arr[i][s]
        s+=1
        e-=1
print("\nfinal--------------------------------------")
for row in arr:
    print(row)