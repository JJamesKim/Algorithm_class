def selection_sort(arr):
    for i in range(len(arr)):
        min = 999
        for j in range(i, len(arr)): #앞단부터 최소값을 집어넣으므로 첫 번째 for문의 round가 바뀔 때마다 두 번째 for문의 시작 순서가 달라져야 함 (최소값을 이중으로 찾지 않도록)
            if min > arr[j]:
                min = arr[j]
                ind = j
        print("최소값은 %d" %min)
        print("최소값의 index는 %d" %ind)

        
        """
        * 아래는 첫 번째 round for문의 최소값을 배열의 앞단으로 옮기는 코드
        * 앞단에서 대치되는 기존 값을 temp에 넣어두었다가 최소값의 위치로 이동시킨다 (swap)
        """
        
        temp = arr[i] 
        arr[i] = arr[ind] 
        arr[ind] = temp 
        print(arr)

selection_arr = [9,4,6,3,2,8,5]
selection_sort(selection_arr)
print(selection_arr)