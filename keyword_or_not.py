l = ["break","case","continue","default","defer","else","for","func","goto","if","map","range","retuen","struct","type","var"]
w = input()
if w not in l:
    print("{} is not a keyword ".format(w))
else:
    print("{} is a keyword ".format(w))