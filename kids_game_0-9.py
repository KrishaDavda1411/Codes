n = input()
if int(n)<=1000000:
    nl = [c for c in n]
    print(nl)
    for i in range(0,len(nl)):
        nl[i] = str(9-int(nl[i]))
    print(nl)
    stra = "".join([x for x in nl])
    print(stra)
else:
    print("wrong input")

