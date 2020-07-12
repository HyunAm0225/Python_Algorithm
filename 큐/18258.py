import sys
from collections import deque
input = sys.stdin.readline
dq = deque([])
N = int(input())

def check_order(o):
    if(o[0]=="push"):
        dq.append(o[1])
    elif(o[0]=="front"):
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif(o[0]=="back"):
        if not dq:
            print(-1)
        else:
            print(dq[-1])
    elif(o[0]=="size"):
        print(len(dq))
    elif(o[0]=="empty"):
        if not dq:
            print(1)
        else:
            print(0)
    elif(o[0]=="pop"):
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
            

for i in range(N):
    commend = input().strip().split()
    check_order(commend)