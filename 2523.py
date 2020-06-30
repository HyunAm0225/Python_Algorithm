x = int(input())

for i in range (1,2*x-1):
    for j in range(i):
        if j < i:
            print("*",end="")
        else: