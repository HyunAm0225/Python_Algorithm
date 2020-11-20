from collections import deque

dartResult = input()

dartque = deque(dartResult)
point = []
def check_dart_point(dartque,point):
    index = -1
    while dartque:
        data = dartque.popleft()

        if data.isnumeric():
            if data =="0" and index== -1:
                point.append(int(data))
                index +=1
            elif data == "0":
                if point[index] == 1:
                    point[index] = 10
                else:
                    point.append(int(data))
                    index +=1
            else:
                point.append(int(data))
                index +=1
        else:
            if data == "S":
                point[index] **=1
            elif data == "D":
                point[index] **=2
            elif data == "T":
                point[index] **=3
            elif data == "#":
                point[index] *=(-1)
            else:
                if index == 0:
                    point[index] *=2
                else:
                    point[index-1] *=2
                    point[index] *=2
        print(point)
    return point
    
print(sum(check_dart_point(dartque,point)))


