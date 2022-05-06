D = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16}

# print(type(D))
s = input()
sl = [c for c in s]
sl = sl[::-1]
sum =0
c=0
for i in range(0,len(sl)):

    if sl[i]>="a" and sl[i]<"z":
      k = (ord(sl[i])-97+10) * 17**c
      c += 1
    elif sl[i]>="A" and sl[i]<"Z":
        k = (ord(sl[i]) - 65 + 10) * 17 ** c
        c += 1
    else:
        k = int(sl[i]) * 17**c
        c+=1
    sum+=k

print(sum)