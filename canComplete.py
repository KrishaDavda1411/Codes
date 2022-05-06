# canComplete("buti","beautiful") -> true 0345
# canComplete("butlz","beautiful") -> false
# canComplete("tulb", "beautiful") -> false 4390

word = input()
sub = input()
wordL = [c for c in word]
subL = [c for c in sub]
print(wordL,subL)
# subL = subL[::-1]
def canComplete(subL,wordL):
    count =0
    ind = 0
    for i in range(0, len(subL)):
        print(subL[i])
        if subL[i] not in wordL:
            print("1")
            return False

        elif wordL.index(subL[i])>=ind:
            ind = wordL.index(subL[i])
            print("---->",ind)
            print("2")
            if len(subL)-1 == i:
                return True
        elif wordL.index(subL[i])<ind:
            print("---->",ind)
            print("3")
            return False
        else:
            print("4")
            return False

ans = canComplete(subL,wordL)
# L =[1,2,3,4,5]
# L.pop()
print(ans)

# print("i" in ["i","k"])