# 곱하기 혹은 더하기

from collections import deque

data = deque(input())
# data = deque(''.join(sorted(data)))
result = 0
for _ in range(len(data)):
    first = int(data.popleft())
    # print(first)
    if first <= 1 or result <=1:
        result += first
        # print(result)
    else:
        result *= first
        # print(result)


print(result)
