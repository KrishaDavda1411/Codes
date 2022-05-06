n = int(input())

def roataion_forword(l):
    list1 = [0] * len(l)
    for i in range(0, len(l)):
        #forword
            if i == 0:
                list1[0] = l[len(l) - 1]
                # print(i, "-", l[i])
            else:
                list1[i] = l[i - 1]
                # print(i, "-", l[i])

    return list1
def roataion_backword(l):
    list1 = [0] * len(l)
    for i in range(0, len(l)):
        if i == len(l) - 1:
            list1[len(l) - 1] = l[0]
            # print(i, "-", l[i])
        else:
            list1[i] = l[i + 1]
            # print(i, "-", l[i])

    return list1
L = list(map(int, input().split()))
L2 = L
rotation_time = int(input())
while rotation_time!=0:
    ans = roataion_forword(L)
    ans2 = roataion_backword(L2)
    L = ans
    L2 =ans2
    rotation_time-=1

for i in ans:
    print(i,end=" ")
print("\n\tok next is backword:  ")
for i in ans2:
    print(i,end=" ")

