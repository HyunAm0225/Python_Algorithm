import sys
input = sys.stdin.readline
N = int(input())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

x = sorted(x)
y = sorted(y,reverse=True)

_sum = 0

for i in range(N):
    _sum += (x[i] * y[i])
print(_sum)