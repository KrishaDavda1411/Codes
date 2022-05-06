k = [''] * 101
k[0] = "zero"
k[1] = "one"
k[2] = "two"
k[3] = "three"
k[4] = "four"
k[5] = "five"
k[6] = "six"
k[7] = "seven"
k[8] = "eight"
k[9] = "nine"
k[10] = "ten"
k[11] = "eleven"
k[12] = "twelve"
k[13] = "thirteen"
k[14] = "fourteen"
k[15] = "fifteen"
k[20] = "twenty"
k[30] = "thirty"
k[40] = "forty"
k[50] = "fifty"
k[80] = "eighty"
k[100] = "hundred"


def vowel(s):
    sum = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            sum += 1
    return sum


def findword(a):
    if k[a] != "":
        return k[a]
    if a < 20 and a > 15:
        k[a] = k[a % 10] + "teen"
        return k[a]
    if a % 10 == 0:
        k[a] = k[(a // 10)] + "ty"
        return k[a]
    if a > 100:
        return "greater 100"

    k[a] = k[(a // 10) * 10] + "-" + k[a % 10]
    return k[a]

# d = findword(10)
# print(d)
sum1 = 0
sum2 = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    sum1 += vowel(findword(a[i]))

for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] + a[j] == sum1:
            sum2 += 1

print(findword(sum2))