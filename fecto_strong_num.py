# 145 = 1!+4!+5! = 1 24+ 120 =145
k = int(input())
# l = int(input())
o = k
def fecto(num):
    if num==1:
        return 1
    else:
        return num*fecto(num-1)
sum1=0
while k!=0:
    m = k%10
    sum1+=fecto(m)
    k=k//10

# print(fecto(4))
print(sum1,o)
if sum1==o:
    print("Yes")
else:print("No")