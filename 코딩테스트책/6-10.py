# 실전문제 - 2
# 위에서 아래로

N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data = sorted(data, reverse=True)
print(*data)