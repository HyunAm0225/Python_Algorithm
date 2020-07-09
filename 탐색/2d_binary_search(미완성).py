a = [
    [10,8,10,10],
    [14,13,12,11],
    [9,10,30,40],
    [15,9,11,21],
    [16,17,19,20],
]

mid = int(len(a)/2)-1

max_num = 0
for i in range(len(a)):
    if max_num < a[i][mid]:
        max_num = a[i][mid]

print(max(a))
