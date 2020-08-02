import sys
input = sys.stdin.readline

N = int(input())
ans_lst = []
for _ in range(N):
    ans_lst.append(list(map(int,input().split())))

ans_lst.sort(key = lambda x : (x[1],x[0]))

for i in ans_lst:
    print(*i)