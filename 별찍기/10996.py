N = int(input())

if N == 1:
    print("*")

else:
    for i in range(0,N*2):
        if i%2==0:
            for j in range(N):
                if j%2==0:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        else:
            for j in range(N):
                if j%2==0:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()