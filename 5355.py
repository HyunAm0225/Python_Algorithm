import sys
input = sys.stdin.readline

N = int(input())
number = 0
def check(n, sign):
    if sign == "@":
        n *=3
    elif sign == "%":
        n +=5
    else:
        n -=7
    return n

for _ in range(N):
    command = []
    command = input().strip().split()
    number = float(command.pop(0))
    for i in command:
        # print(number, i)
        number = check(number,str(i))
    print(format(number,"10.2f").lstrip())