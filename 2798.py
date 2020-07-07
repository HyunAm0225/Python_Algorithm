# 브루트포스 문제
from itertools import combinations
N, M = map(int,input().split())
lst = list(map(int,input().split()))
ans = []
# print(lst)
ans_lst = list(combinations(lst,3))
for i in ans_lst:
    if sum(i)<=M:
        ans.append(sum(i))
min_num = ans[0]
for j in ans:
    if abs(min_num-M) >= abs(j-M):
        min_num = j

print(min_num)