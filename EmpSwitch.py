n = int(input())
Ln = list(map(int,input().split()))
m = int(input())
Lm = list(map(int,input().split()))

switch =0
n = Ln[0]
m = Lm[0]
a = Ln[1:]
b = Lm[1:]

combined = Ln[1:]+Lm[1:]
print(combined)
combined.sort()
print(combined)
for i in range(0,len(combined)-1):
    if (combined[i] in a and combined[i+1] in a) or (combined[i] in b and combined[i+1] in b):
        pass
    else:
        switch+=1

print(switch)