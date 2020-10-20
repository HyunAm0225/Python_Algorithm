n = int(input())
data = []
ans = []
for _ in range(n):
    data.append(input())

data.sort(key = lambda x:(len(x),x))
for x in data:
    if x not in ans:
        ans.append(x)
for i in ans:
    print(i)
