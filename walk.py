# print(10-20)
n = int(input())
c = "R"
inr = 10
x,y =0,0
while(n>0):
    if c=="R":
        x = x+inr
        inr+=10
        y=y
        c="U"
        n-=1
    elif c=="U":
        y = y+inr
        inr+=10
        x=x
        c="L"
        n-=1
    elif c=="L":
        x = x-inr
        y=y
        inr+=10
        c="D"
        n-=1
    elif c=="D":
        y = y-inr
        x=x
        inr+=10
        c="R"
        n-=1
print(x,y)