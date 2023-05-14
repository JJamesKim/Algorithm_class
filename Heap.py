

arr1 = [7,5,4,6,2,3,10,1]

def heapify(arr):
    start = current = len(arr) - 1
    while start > 0:
        parent = (current - 1) // 2
        if arr[parent] >= arr[current]:
            arr[parent], arr[current] = arr[current], arr[parent]
            start -= 1
            current = parent
        else:
            break


heapify(arr1)
print(arr1)
