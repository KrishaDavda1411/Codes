#A -> B -> C

n = int(input()) # no of node
pro_l = int(input()) #profit earned by last (leaf ) node
pro_pass = int(input()) #profit pass to supervisor in %

while(n!=1):
    pro_l = (pro_l * pro_pass)/100
    n-=1
    # print(int(pro_l))

print(int(pro_l))