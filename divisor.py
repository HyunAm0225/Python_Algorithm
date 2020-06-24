# 빠른 약수 구하기 예제
'''
12의 약수

1 x 12, 2 x 6, 3 x 4

12 x 1, 6 x 2, 4 x 3

중복되는 값이 있으므로 루트 N만큼 진행(올림한다)

'''
import math

n = int(input())
ans = []
for i in range(1, int(n**0.5)+1):
    if n%i ==0:
        ans.append(i)
        if i!=n//i:
            ans.append(n//i)
print(sorted(ans))

