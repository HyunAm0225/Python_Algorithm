import sys
from itertools import permutations

N, M = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
ans_lst = list(permutations(x,M))


for i in ans_lst:
    print(*i)