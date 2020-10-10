n = int(input())
data = list(map(int,input().split()))

data.sort()
# 1 1 2 3 6 7 30
target = 1
for i in data:
    if target<i:
        break
    target += i
    # print(target, end=" ")

print(target)

