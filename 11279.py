# 백준
# 최대힙 문제
import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
heapq.heapify(data)

for _ in range(0, n):
    x = int(input())
    if x == 0:
        if data:
            print(-heapq.heappop(data))
        else:
            print(0)
    else:
        heapq.heappush(data, -x)
