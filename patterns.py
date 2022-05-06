n = int(input())
# for i in range(0,n):
#     print("* * * *")
#
c=0
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(0,i):
        print("{} ".format(c),end="")
        c+=1
    print("")