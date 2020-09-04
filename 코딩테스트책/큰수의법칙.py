# import sys
# input = sys.stdin.readline
N, M, K = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

first = data[-1]
second = data[-2]

result = 0

while True:
    result += first * K
    M -= K
    result += second
    M -= 1
    
    if M==0:
        break
print(result)

