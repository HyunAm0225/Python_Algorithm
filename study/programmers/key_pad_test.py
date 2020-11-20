key_pad = [[1, 2, 3],[4, 5, 6],[7, 8, 9],["*", 0, "#"]]
answer = []
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
    print(f"({x1},{y1}),({x2},{y2})")
    return (x2-x1)**2+(y2-y1)**2

print(check_distance(9,5))
print(check_distance(5,5))