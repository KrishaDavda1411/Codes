n = int(input())
if n>=2:
     l = list(map(int,input().split()))
     # print(l)
     l.sort()
     if l.count(l[0])==len(l):
         print("Equal")
     else:
         print(l[0],l[1])
else:
    print("Invalid input")