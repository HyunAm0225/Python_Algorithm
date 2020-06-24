a = int(input())

x = list(range(0,a+1))
# print(x)
for i in x:
    if(i<2):
        pass
    else:
        x[i] = x[i-2]+x[i-1]

print(x.pop()%1000000007)

