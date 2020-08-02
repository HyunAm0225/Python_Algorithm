import sys
from itertools import combinations

N, M = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
ans_lst = sorted(set(list(combinations(x,M))))

for i in ans_lst:
    print(*i)