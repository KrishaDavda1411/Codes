l = list(map(str,input().split(" ")))
# print(l)
len_w = []
for i in l:
    len_w.append(len(i))
print(max(len_w))