num = int(input())
temp = num
l =[]

for i in range(9,1,-1):
    while(num%i==0):
        print(num)
        num = num//i
        print("-->i ",i)
        l.append(i)

# print(l[::-1])

if len(l)>1:
    num = int(''.join(map(str, l[::-1])))
    print(num)
elif temp<10:
    print(temp+10)
else:
    print(-1)

