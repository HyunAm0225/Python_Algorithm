# 백준
# 절댓값 힙
import heapq
from functools import reduce
import sys
input = sys.stdin.readline
# 최소 힙 문제
n = int(input())
data = []
count = 0
heapq.heapify(data)
for _ in range(0, n):
    x = int(input())
    if x == 0:
        if data:
            print(reduce(lambda x, y: x*y, (heapq.heappop(data))))
        else:
            print(0)
    else:
        if x > 0:
            heapq.heappush(data, (abs(x), 1))
        else:
            heapq.heappush(data, (abs(x), -1))
