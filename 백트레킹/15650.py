import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
x = [i for i in range(1,N+1)]
per_lst = list(combinations(x,M))

for i in per_lst:
    print(*i)
