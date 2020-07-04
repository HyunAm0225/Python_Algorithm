N = int(input())
j = 0
k = N-1
for x in range(1,2*N-1,2):
    print(" "*k,end="")
    print('*'*x)
    k -= 1
for i in range(2*N-1,0,-2):
    print(" "*j,end="")
    print('*'*i)
    j += 1