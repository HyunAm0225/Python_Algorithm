octo = {
    "-": 0,
    "\\": 1,
    "(": 2,
    "@": 3,
    "?": 4,
    ">": 5,
    "&": 6,
    "%": 7,
    "/": -1
}
while True:
    data = list(input())
    if data[0] == "#":
        break
    data.reverse()
    # print(data)
    for i in range(len(data)):
        data[i] = octo[data[i]] * (8 ** i)
    print(sum(data))
