# k = ord('a')
# print(k)

s = input()
sl = [c for c in s]
c = 0
for i in range(0,len(sl)):
    if(ord(sl[i])-97 == c or ord(sl[i])-65== c ):
        c+=1
    else:
        break
print(c)

