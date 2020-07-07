N, M = map(int,input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))
coin = sorted(coin,reverse=True)
count = 0
for i in coin:
    count += M//i
    M %= i
print(count)


    

