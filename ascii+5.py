s1 = input()
s2 = input()
def asccii_encoding(s):
    sl = [c for c in s]
    ans =""
    for i in range(0,len(sl)):
        if sl[i]>="a" and sl[i]<="z":
          k = ord(sl[i])+5
          ans=ans+chr(k)
        elif sl[i]>="A" and sl[i]<="Z":
            k = ord(sl[i])+5
            ans = ans+chr(k)
        elif sl[i] == " " or (sl[i]>="0" and sl[i]<="9"):
            return "Invelid input"
        else:
            ans = ans + sl[i]

    return ans
def asccii_decoding(s):
    sl = [c for c in s]
    ans =""
    for i in range(0,len(sl)):
        if sl[i]>="a" and sl[i]<="z":
          k = ord(sl[i])-5
          ans=ans+chr(k)
        elif sl[i]>="A" and sl[i]<="Z":
            k = ord(sl[i])-5
            ans = ans+chr(k)
        elif sl[i]==" " or (sl[i]>="0" and sl[i]<="9"):
            return "Invelid input"
        else:
            ans = ans + sl[i]

    return ans

a1 = asccii_encoding(s1)
a2 = asccii_decoding(s2)
print("{} -> ".format(s1),a1)
print("{} -> ".format(s2),a2)



# print(ord("a"),ord("A")) //97 65