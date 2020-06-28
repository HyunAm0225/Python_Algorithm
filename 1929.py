'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.


'''

def is_prime(x):
    prime = [True] * x
    size = int(x**0.5)
    for i in range(2,size+1):
        if prime[i] == True:
            for j in range(i+i,x,i):
                prime[j] = False
    return [i for i in range(2,x) if prime[i]==True]

M,N = map(int,input().split())

prime = is_prime(N+1)
# print(prime)
for i in prime:
    if i < M:
        pass
    else:
        print(i)
    
