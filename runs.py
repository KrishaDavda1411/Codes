l = [4, 1, 0, 1]
run = int(input())
ball = int(input())
sum_r = 0
while ball > 0:
    for i in range(0, len(l)):
        sum_r += l[i]
        # print(ball)
        ball -= 1
# print(sum_r)
if sum_r>run:
    print(1)
else:print(0)