n = int(input())
def find_duration(n):
    time =0
    if n<=2000:
        time = 25
    elif n>=2001 and n<4000:
        time = 35
    elif n>=4000 and n<=7000:
        time =45
    else:
        return "invalid"
    return time

ans = find_duration(n)
print(ans)