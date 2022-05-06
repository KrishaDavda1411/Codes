from itertools import permutations
word = input()
# print(L)
def isPelindromPossible(word):
    L = [''.join(x) for x in permutations(word)]
    L = set(L)
    count =0
    for i in L:
            s = i
            # print(s)
            if s[::] == s[::-1]:
                count+=1
                note = s[::]
                print(note)
    if count>0:
        return True,note,count
    else:return False

print(isPelindromPossible(word))