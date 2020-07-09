# 힙 정렬 
a = [16,14,10,8,7,9,3,2,4,1]
a = sorted(a)

# 위에 있는 배열을 트리로 바꾼다 index : 0 = root

# 부모 트리 i/2

# 왼쪽 트리 2i 오른쪽 트리 2i + 1

def heapify(unsorted, index, heap_size):
    print("unsorted : ",unsorted)
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    print("before max heap: ",unsorted)
    n = len(unsorted)
    for i in range(n//2-1,-1,-1):
        heapify(unsorted,i,n)
    print("after max heap",unsorted)
    for i in range(n-1,0,-1):
        unsorted[0],unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted,0,i)
    return unsorted
print(heap_sort(a))