data = list(map(int,input().split()))
data = [str(i) for i in data]
data.sort(reverse=True, key = lambda x:x*3)
print(str(int(''.join(data))))