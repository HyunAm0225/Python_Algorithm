N = int(input())
k = N-1
for i in range(1,N+1):
    print(" "*k,end="")
    print('*'*i)
    k -=1
k = 1
for j in range(N-1,0,-1):
    print(" "*k,end="")
    print('*'*j)
    k +=1