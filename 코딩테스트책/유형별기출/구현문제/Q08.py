# 구현문제
# 문자열 재정의
from collections import deque
s = deque(input())
data = []
numeric_sum = 0
for _ in range(len(s)):
    x = s.popleft()
    if x.isalpha():
        data.append(x)
    else:
        numeric_sum += int(x)
data.sort()
a = ''.join(data)
print(a,end="")
print(numeric_sum)
