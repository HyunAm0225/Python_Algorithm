def sumorsup(data):
    if data[1] == "+":
        return int(data[0]) + int(data[2])
    else:
        return int(data[0]) * int(data[2])


data = []
for _ in range(0, 3):
    data.append(input())
print(sumorsup(data))
