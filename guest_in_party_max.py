n = int(input())
e = list(map(int,input().split()))
l = list(map(int,input().split()))
max_count=0
count =0

for i in range(0,len(e)):
    count += e[i]-l[i]
    if count>max_count:
        max_count=count
print(max_count)