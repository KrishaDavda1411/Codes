w = input()
D = {}
# print(type(D))
# print(w.count("a"))
for i in range(0,len(w)):
    if w[i] not in D.keys():
        D[w[i]]=w.count(w[i])
print(D)
str1 =''
for key, value in D.items():
        str1+=key+str(value)
print(str1)