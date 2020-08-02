import sys
from itertools import product

N, M = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
ans_lst = sorted(set(list(product(x,repeat=M))))

for i in ans_lst:
    print(*i)