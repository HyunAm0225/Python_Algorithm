import sys
from itertools import combinations

N, M = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
ans_lst = list(combinations(x,M))


for i in ans_lst:
    print(*i)