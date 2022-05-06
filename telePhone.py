s = input()
sl = [c for c in s]
from itertools import permutations

x = ["".join(x) for x in permutations(s)]
# print(x)
ui = "abcdefgh"
ui = ui[:-2]
for i in range(0, len(x)):
    k = x[i]
    x[i] = k[:-2]
x = set(x)
c = 0
for i in x:
    c += 1
print(x)
x = list(x)


def canComplete(subL, wordL):
    ind = 0
    for i in range(0, len(subL)):

        if subL[i] not in wordL:
            print("1")
            return False

        elif wordL.index(subL[i]) >= ind:
            ind = wordL.index(subL[i])
            print("---->",ind)
            print("2")
            if len(subL) - 1 == i:
                return True
        elif wordL.index(subL[i]) < ind:
            if subL[i] in subL[i::]:
                pass
            else:
                print("---->",ind)
                print("3")
                return False
        else:
            print("4")
            return False


count = 0
t = []
for i in x:
    if canComplete(i, s):
        t.append(i)
        count += 1
    # break
print(count)
print(t)