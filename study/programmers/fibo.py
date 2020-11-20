data = [0]*100001

def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


def fibo_dp(n):
    if n<=1:
        return n
    if data[n] != 0:
        return data[n]
    data[n] = fibo_dp(n-1) + fibo_dp(n-2)
    return data[n]

for i in range(0,100):
    print(fibo_dp(i))
