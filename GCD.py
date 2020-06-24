# 최대 공약수를 구하는 함수

def GCD(a, b):
    return GCD(b,a%b) if b else a # 3항연산자 b ? GCD(b,a%b)

x, y = map(int,input().split())

gcd = GCD(x,y)
print("최대공약수 : ",gcd)

lcm = int(x*y/gcd)
print("최소공배수 : ",lcm)