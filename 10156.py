# 수학
# 사칙연산
data = list(map(int, input().split()))
if (data[0] * data[1])-data[2] >= 0:
    print((data[0] * data[1])-data[2])
else:
    print(0)
