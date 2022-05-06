p = int(input())
t = int(input())

bank=[]
for k in range(0,2):
    n = int(input())
    sum =0
    for i in range(0,n):
        yr,s = input().split()
        yr = int(yr)
        s = float(s)
        mi =0
        sq = pow((1+s),yr*12)
        emi = (p*s)/(1-1/sq)
        sum = sum+emi
    bank.append(sum)

if(bank[0]<bank[1]):
    print("bank A")
else:
    print("bank B")