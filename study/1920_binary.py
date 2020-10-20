# 이진 탐색 소스코드 구현하기(재귀 함수)
def binary_search(array, target, start, end):
    array.sort()
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n = int(input())
data = list(map(int,input().split()))
m = int(input())
data2 = list(map(int,input().split()))

for i in data2:
    # print(f"binary_search({data},{i})")
    if binary_search(data,i,0,n-1) == None:
        print(0)
    else:
        print(1)