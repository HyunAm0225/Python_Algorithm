x = [5,3,2,6,10,11,15,1,-1]

def selection(lst):
    length = len(lst)
    for i in range(0,length):
        min_index = i
        for j in range(i+1, length):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i],lst[min_index] = lst[min_index], lst[i]
    return lst

x = selection(x)
print(x)