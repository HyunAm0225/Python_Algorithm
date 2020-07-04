x = str(input())
# print(len(x))
a = []

for i in x:
    a.append(int(i))

def sel_sort(a):
    n = len(a)
    for i in range(0,n-1):
        max_idx = i
        for j in range(i+1,n):
            if a[j]>a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
        
sel_sort(a)
for l in a:
    print(l,end="")