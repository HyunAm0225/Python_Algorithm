# BFS 문제
# 푸는중
from collections import deque

n,k = map(int,input().split())

data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

q = deque([])
