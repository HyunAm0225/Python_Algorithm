import sys
from collections import deque

N, K = map(int,input().split())

x = deque([i for i in range(1,N+1)])
ans_lst = []
while len(x)>0:
    for _ in range(K-1):
        x.append(x.popleft())
    ans_lst.append(x.popleft())

print("<",end="")
for i in range(len(ans_lst)):
    if i == len(ans_lst)-1:
        print(ans_lst[i],end="")
    else:
        print(ans_lst[i],end=", ")
print(">")
    