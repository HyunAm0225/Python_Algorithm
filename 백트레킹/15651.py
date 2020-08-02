import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int,input().split())
x = [i for i in range(1,N+1)]
per_lst = list(combinations_with_replacement(x,M))

for i in per_lst:
    print(*i)
