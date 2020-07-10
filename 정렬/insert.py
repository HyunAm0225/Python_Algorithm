a = [10,3,204,501,203,7,4,2,1,5]

n = len(a)

print(f"unsorted : {a}")

for i in range(1,n):
    for j in range(i,0,-1):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
        else:
            print(f"unsorted : {a}")
            break
print(a)