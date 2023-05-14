#비효율적인 코드, 이미 정렬된 배열도 비교하는 과정이 비효율적
"""array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #두 번째 인덱스(1)부터 앞으로 비교하면서, 배열을 1씩 늘려간다
        print(j)
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else:
            break
            
print(array)"""


#최적화된 코드 
def insertion_sort(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i - 1] > arr[i]: #while문을 통해서 배열이 정렬되지 않은 인덱스까지만 접근, 배열이 정렬되었다면 앞선 인덱스는 정렬되었다고 가정하고 값을 비교하지 않는다
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
insertion_sort(array)
print(array)