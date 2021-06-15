import sys
# 안테나 문제
MIN = sys.maxsize
n = int(input())
x = list(map(int, input().split()))

x.sort()

print(x[n//2-1])
