import sys
input = sys.stdin.readline

N = int(input())
ans_lst = []
for i in range(N):
    a, b = map(str,input().split())
    ans_lst.append([a,b,i])

ans_lst.sort(key = lambda x:(int(x[0]),x[2]))
    
for i in ans_lst:
    print(i[0],i[1])