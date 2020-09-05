# 이진 탐색 실전 문제
# 부품찾기
import sys
input = sys.stdin.readline

def search_binary(array,start,end,target):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

n = int(input())
store = list(map(int,input().split()))
store.sort()
m = int(input())
host = list(map(int,input().split()))

for product in host:
    # 해당 부품이 있는지 확인하기
    result = search_binary(store,0,n-1,product)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')