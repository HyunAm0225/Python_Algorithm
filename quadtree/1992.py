N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, str(input()))))

def quadcheck(x,y,n):
    check = matrix[x][y]
    flag = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if not flag:
                break
            if check != matrix[i][j]:
                print("(",end="")
                quadcheck(x,y,n//2) # left-top
                quadcheck(x,y+n//2,n//2) # left-bottom
                quadcheck(x+n//2,y,n//2) # right-top
                quadcheck(x+n//2,y+n//2,n//2) # right-bottom
                print(")",end="")
                flag = False
                break
    if flag:
        print(check,end="")
quadcheck(0,0,N)
                

