a = [10,3,204,501,203,7,4,2,1,5]

n = len(a)
print(f"unsorted : {a}")
for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print(f"unsorted : {a}")

print(f"sorted : {a}")
