#x+ p1-q + x + p2-q + x + p3-q +q = E -r
#3x + p1+p2+p3 -2q = E -r
# 3x = E - r + 2q - p1 -p2-p3
#3x = 345 - 43 + 2(14) - 30+26+28
#3x = 246
#x = 82

#no of candidate solved only 1st que
# x =126
p1 = int(input())
p2= int(input())
p3= int(input())
q= int(input())
e =int(input())
r= int(input())

#2nd

m = e-r + 2*q - p1 -p2-p3
x = m/3

first = x + p1-q + q +p3-q
print("first ans: ",first)
print("second ans: ",m )

# https://youtu.be/BygTMRAxZ4c