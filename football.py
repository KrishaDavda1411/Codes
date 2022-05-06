n = int(input())
scoreD ={}
for i in range(n):

    t1,t2,scores = map(str,input().split(" "))
    if t1 not in scoreD.keys():
        scoreD[t1]=0
    if t2 not in scoreD.keys():
        scoreD[t2]=0
    # print(scores)
    s_t1,s_t2 = scores.split('-')
    s_t1 = int(s_t1)
    s_t2 = int(s_t2)
    if s_t1>s_t2:
        scoreD[t1] += 3
        scoreD[t2] += 0
    elif s_t1<s_t2:
        scoreD[t2] += 3
        scoreD[t1] += 0
    else:
        scoreD[t1] +=1
        scoreD[t2] +=1

print(scoreD)
m = max(scoreD.values())
for key,val in scoreD.items():
    if val == m:
        print(key)
        break

print(m)




