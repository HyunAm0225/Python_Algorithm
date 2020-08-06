N = int(input())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))
# print(matrix)
cnt_one = 0
cnt_zero = 0
cnt_minus_one = 0
def check(x,y,n):
    global cnt_zero, cnt_one, cnt_minus_one
    flag = True
    _color = matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if not flag:
                break
            else:
                if _color != matrix[i][j]:
                    flag = False
                    check(x,y,n//3)
                    check(x+n//3,y,n//3)
                    check(x+n//3+n//3,y,n//3)
                    check(x,y+n//3,n//3)
                    check(x+n//3,y+n//3,n//3)
                    check(x+n//3+n//3,y+n//3,n//3)
                    check(x,y+n//3+n//3,n//3)
                    check(x+n//3,y+n//3+n//3,n//3)
                    check(x+n//3+n//3,y+n//3+n//3,n//3)
                    break
    if flag:
        if _color == 0:
            cnt_zero +=1
        elif _color == 1:
            cnt_one +=1
        else:
            cnt_minus_one +=1

check(0,0,N)
print(cnt_minus_one)
print(cnt_zero)
print(cnt_one)
