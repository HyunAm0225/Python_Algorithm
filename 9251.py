# 다이나믹 프로그래밍
# LCS문제
x = "0"+input()
y = "0"+input()
count = 0
data = [[0 for i in range(0, len(y))] for i in range(0, len(x))]
lcs = ""
for i in range(1, len(x)):  # (1~3)
    for j in range(1, len(y)):  # (1~2)
        if x[i] == y[j]:
            data[i][j] = data[i-1][j-1] + 1
        else:
            data[i][j] = max(data[i][j-1], data[i-1][j])


print((data.pop()).pop())
