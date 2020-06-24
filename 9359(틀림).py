'''
자연수 N이 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 수 중에서 N과 서로소인 것의 개수를 구하는 프로그램을 작성하시오.

두 정수를 나눌 수 있는 양의 정수가 1밖에 없을 때, 두 정수를 서로소라고 한다.

즉, 두 수의 최대공약수가 1이면 서로소이다. 1은 모든 정수와 서로소이다.

'''

# 서로소 확인법 두개의 곱 = 최소공배수
# 최대 공약수가 1
import math

# def GCD(a, b):
#     return GCD(b,a%b) if b else a # 3항연산자 b ? GCD(b,a%b)
T = int(input())
count = 0
while T > 0:
    T -=1
    count +=1
    a, b, n = map(int,input().split())
    ans = 0
    x = list(range(a,b+1))
    for i in x:
        if math.gcd(i,n)==1:
            ans+=1
    print("Case #{}: {}".format(count,ans)) 
