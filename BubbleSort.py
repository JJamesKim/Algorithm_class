def bubble_sort(arr):
    for i in range(0, len(arr)-1): 
        for j in range(len(arr)-i-1): #이중 for문 통해서, 가장 왼쪽부터 배열의 좌우값을 비교해 가장 큰 값을 우측 끝으로 이동시키고 배열의 크기를 하나씩 줄인다
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #우측 값이 좌측 값보다 커야하므로, 좌측 값이 우측 값보다 크거나 같으면 좌우측 값을 swap

b1 = [1, 11, 18, 10, 5, 3, 9, 7]
bubble_sort(b1)
print(b1)
