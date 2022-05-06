s = input()
sl = [c for c in s]
bs = [0]*len(sl)
fs = [0]*len(sl)
for i in range(0, len(sl)):
    # for backword
    if i == len(sl) - 1:
        bs[len(sl) - 1] = sl[0]
        print(i, "-", sl[i])
    else:
        bs[i] = sl[i + 1]
        print(i, "-", sl[i])

print(bs)

for i in range(0, len(sl)):
    # for forword
    if i == 0:
        fs[0] = sl[len(sl)-1]
        # print(i, "-", sl[i])
    else:
        fs[i] = sl[i - 1]
        # print(i, "-", sl[i])

print(fs)
if fs==bs:
    print(1)
else: print(0)
