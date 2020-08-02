x = list(map(int,input().split()))
x = sorted(x)
item = int(input())
def binary_search(lst, value):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low+high)/2)
        guess = lst[mid]

        if guess == value:
            return mid
        elif guess > value:
            high = mid -1
        else:
            low = mid + 1
    return None

print(binary_search(x,item))