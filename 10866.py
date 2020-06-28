'''
덱 구현

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.


'''
import sys
input = sys.stdin.readline

T=int(input())
a = []
commend = []
def check_order(o):
    if(o[0]=="push_back"):
        a.append(o[1])
    elif(o[0]=="push_front"):
        a.insert(0,o[1])
    elif(o[0]=="front"):
        if(len(a)==0):
            print(-1)
        else:
            print(a[0])
    elif(o[0]=="back"):
        if(len(a)==0):
            print(-1)
        else:
            print(a[-1])
    elif(o[0]=="size"):
        print(len(a))
    elif(o[0]=="empty"):
        if(len(a)==0):
            print(1)
        else:
            print(0)
    elif(o[0]=="pop_front"):
        if(len(a)==0):
            print(-1)
        else:
            print(a.pop(0))
    elif(o[0]=="pop_back"):
        if(len(a)==0):
            print(-1)
        else:
            print(a.pop())
            

for i in range(T):
    commend = input().strip().split()
    check_order(commend)

# print(a)

