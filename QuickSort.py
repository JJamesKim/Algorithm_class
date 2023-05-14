array = [5, 7, 9, 11, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
            print("좌측 값 찾기")
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
            print("우측 값 찾기")
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            print("right와 pivot값 교체 발생")            
            array[right], array[pivot] = array[pivot], array[right]
            print(array)
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            print("left와 right값 교체 발생")
            array[left], array[right] = array[right], array[left]
            print(array)            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)