N = int(input())
matrix = []
cnt_black = 0
cnt_white = 0
for i in range(N):
    matrix.append(list(map(int,input().split())))
# print(matrix)
def check(x,y,n):
    global cnt_black, cnt_white
    _type = matrix[x][y]
    flag = True
    
    for i in range(x,x+n):
        if not flag:
            break
        for j in range(y,y+n):
            if _type != matrix[i][j]:
                flag = False
                check(x,y,n//2) #left-top
                check(x,y+n//2,n//2) #right-top
                check(x+n//2,y,n//2) #left-bottom
                check(x+n//2,y+n//2,n//2) #right-bottom
                break
    if flag:
        if _type:
            cnt_black +=1
        else:
            cnt_white +=1
check(0,0,N)
print(cnt_white)
print(cnt_black)
            


