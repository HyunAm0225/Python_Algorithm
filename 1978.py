# 소수 구하기 문제
N = int(input())
lst = list(map(int,input().split()))
chk = []
ans = 0
# print([i for i in range(2,2)])
def prime_number(num):
    size = int(num**0.5)+1
    if num != 1:
        for i in range(2,size):
            if num % i ==0:
                return False
    else:
        return False
    return True

for i in lst:
    chk.append(prime_number(i))
for j in chk:
    if j == True:
        ans +=1
print(ans)