N = int(input())

def GCD(a, b):
    return GCD(b,a%b) if b else a # 3항연산자 b ? GCD(b,a%b)

for _ in range(N):
    x, y = map(int,input().split())
    print(int((x*y)/GCD(x,y)))