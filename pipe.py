n,m,r = map(int,input().split())
# print(n,m,r)
incoming = list(map(int,input().split()))
outgoing = list(map(int,input().split()))
incoming = [x-r for x in incoming]
outgoing = [x-r for x in outgoing]
sum1,sum2 =sum(incoming),sum(outgoing)
print(incoming,outgoing)
print(sum1,sum2)

if(sum1>sum2):
    ans = (sum1-sum2)+r
    print("-{}".format(ans))
elif(sum2>sum1):
    ans=(sum2-sum1)+r
    print(ans)
else:print("BALANCED")

