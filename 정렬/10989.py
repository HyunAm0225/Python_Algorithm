import sys
input = sys.stdin.readline

n = int(input())
c = [0]*10001
for _ in range(n):
    c[int(input())] +=1
# print(c[:11])
for i in range(1,10001):
    for _ in range(c[i]):
        # print(f"i 값{i}, c[i] 값 {c[i]}")
        print(i)
