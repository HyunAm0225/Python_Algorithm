N = int(input())
count = 1
for i in range(N):
    for j in range(N-i-1):
        print("[{},{}]".format(i,j+i+1),end="")
    print()
