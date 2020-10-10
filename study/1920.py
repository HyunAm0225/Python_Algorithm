n = int(input())
data = list(map(int,input().split()))
m = int(input())
data2 = list(map(int,input().split()))

ans = []
for x in data2:
    if x in data:
        ans.append(1)
    else:
        ans.append(0)

for i in ans:
    print(i)