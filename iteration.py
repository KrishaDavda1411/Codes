num = int(input())


def sum(num):
    take = num
    count = 0
    while take>=10:
        sum = 0
        while num!=0:
            rem = num%10
            sum+=rem
            num = num//10
        count+=1
        print(take)
        take = sum
        num = sum
    return count

def multi(num):
    take = num
    count = 0
    while take>=10:
        mul = 1
        while num!=0:
            rem = num%10
            mul=mul*rem
            num = num//10
        count+=1
        print(take)
        take = mul
        num = mul
    return  count

sum_iteration = sum(num)
print("sum ",sum_iteration)
print("\t\tmulti")

multi_iteration = multi(num)
print("multiplication ",multi_iteration)
# while num!=0:
#     rem = num%10
#     num = num//10
#     print(rem)