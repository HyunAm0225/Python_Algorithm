import sys
from itertools import combinations
input = sys.stdin.readline

def GCD(a, b):
    return GCD(b,a%b) if b else a # 3항연산자 b ? GCD(b,a%b)

N = int(input())

command = []
first_num = 0
_sum = 0
for _ in range(N):
    commend = input().strip().split()
    first_num = commend.pop(0)
    ans_lst = list(combinations(commend,2))
    for i in ans_lst:
        _sum += GCD(int(i[0]),int(i[1]))
    print(_sum)
    _sum = 0    