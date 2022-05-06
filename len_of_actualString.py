s = input()
sl = [c for c in s]
# print(sl)
num = ''
ch = ''
newL = sl
for i in range(0,len(sl)):
    if ord(sl[i])>=48 and ord(sl[i])<=57:
        num = num + sl[i]
    else:
        break

len_of_num = len(num)
if int(num) == (len(sl)-len_of_num):
    print("TRUE {}".format(num))
else:print("FALSE {}".format(len(sl)-len_of_num))