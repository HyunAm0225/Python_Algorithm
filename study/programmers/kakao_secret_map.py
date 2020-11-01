n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

data = [bin(i|j)[2:].zfill(n).replace("1","#").replace("0"," ") for i,j in zip(arr1,arr2)]
print(data)