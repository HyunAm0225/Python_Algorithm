import sys
from itertools import combinations_with_replacement as combi

N, M = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
ans_lst = list(combi(x,M))


for i in ans_lst:
    print(*i)