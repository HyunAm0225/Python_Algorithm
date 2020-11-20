import heapq
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
            print(heapq.heappop(data))
        else:
            print(0)
    else:
        heapq.heappush(data, x)
