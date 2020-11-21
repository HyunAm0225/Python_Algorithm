# 다이나믹 프로그래밍
# LCS문제
x = "0"+input()
y = "0"+input()
count = 0
data = [[0 for i in range(0, len(y))] for i in range(0, len(x))]
lcs = []
for i in range(1, len(x)):
    for j in range(1, len(y)):
        if x[i] == y[j]:
            data[i][j] = data[i-1][j-1] + 1
        else:
            data[i][j] = max(data[i][j-1], data[i-1][j])
        # print(data[i][j], end=" ")
    # print()
index_y = len(x)-1
index_x = len(y)-1
while data[index_y][index_x] != 0:
    if data[index_y][index_x] == data[index_y][index_x-1]:
        index_x -= 1
    elif data[index_y][index_x] == data[index_y-1][index_x]:
        index_y -= 1
    else:
        lcs.append(x[index_y])
        index_x -= 1
        index_y -= 1

print(max([*map(max, data)]))

if lcs:
    print(''.join(reversed(lcs)))
