data = [0]*10000001
n = int(input())
def fibo(n):
    if n<2:
        return n
    if data[n] != 0:
        return data[n]
    data[n] = fibo(n-2) + fibo(n-1)
    return data[n]

    
print(fibo(n)%1000000007)