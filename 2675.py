import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    command = []
    command = input().strip().split()
    a = [i*int(command[0]) for i in command[1]]
    x = "".join(a)
    print(x)