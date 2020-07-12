h, m, s = map(int,input().split())
time = int(input())

s += h*3600
s += m*60
s += time

def check(s):
    if s//3600 < 24:
        print(s//3600, (s%3600)//60, (s%3600)%60)
    else:
        s-=(3600*24)
        return check(s)

check(s)


