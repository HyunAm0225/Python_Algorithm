## 피보나치 문제

a = 10000
x = list(range(0,a+1))
# print(x)
for i in x:
    if(i<2):
        pass
    else:
        x[i] = x[i-2]+x[i-1]

x.remove(0)

T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    # print(x[0])
    print(f"Case #{i+1}: {x[a-1]%b}")