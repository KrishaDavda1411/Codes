n = int(input())
sum = 0
while(n!=0):
    rem = n%10
    sum+=rem
    n=n//10

sum2 = 0
while(sum!=0):
    rem = sum%10
    sum2+=rem
    sum=sum//10

if(sum2==1):
    print("UNO")
else:print("NOT UNO")
print(sum2)
