from collections import deque
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
key_pad = ((1, 2, 3),(4, 5, 6),(7, 8, 9),("*", 0, "#"))
answer = []
hand = "left"
l_location = "*"
r_location = "#"

def check_distance(location,x):
    x1=0;y1=0;x2=0;y2=0
    for i in range(len(key_pad)):
        if location in key_pad[i]:
            x1 = i
            y1 = key_pad[i].index(location)
            break
    for i in range(len(key_pad)):
        if x in key_pad[i]:
            x2 = i
            y2 = key_pad[i].index(x)
            break
    return abs(x2-x1) + abs(y2-y1)
data = deque(data)

while data:
    x = data.popleft()
    if x%3==1:
        answer.append("L")
        l_location = x
    elif x%3==0 and x!=0:
        answer.append("R")
        r_location = x
    else:
        if check_distance(r_location,x) < check_distance(l_location,x):
            answer.append("R")
            r_location = x
        elif check_distance(r_location,x) > check_distance(l_location,x):
            answer.append("L")
            l_location = x
        else:
            # 거리가 같을 경우
            if hand == "right":
                answer.append("R")
                r_location = x
            else:
                answer.append("L")
                l_location = x

print(''.join(answer))