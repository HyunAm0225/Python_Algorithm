N,T,C,P = map(int,input().split())
day = 1
price = 0
while(day<N):
    price += C*P
    day += T
    if day > N:
        price -= C*P
print(price)