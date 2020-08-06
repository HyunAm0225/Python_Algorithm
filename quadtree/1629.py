import sys
input = sys.stdin.readline
x,y,z = map(int,input().split())

def power(x,y):
    if y == 1:
        return x % z
    save_power = power(x,y//2)
    if y%2==0:
        return save_power * save_power % z
    else:
        return x * save_power * save_power % z

print(power(x,y)%z)