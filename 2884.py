a, b = map(int, input().split())

if a<1 and b<45:
    if b<45:
        a = 23
        b = b+15
    else:
        a = 23
        b = b-45
else:
    if b<45:
        a = a-1
        b = b+15
    else:
        b = b-45
print(a,b)