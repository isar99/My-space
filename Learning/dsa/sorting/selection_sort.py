def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        min_ind = i
        for j in range(i+1,arr_len):
             if arr[j] < arr[min_ind]:
                 min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    print(arr)

def selection_sort_des(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        max_ind = i
        for j in range(i+1,arr_len):
            if arr[j] > arr[max_ind]:
                max_ind = j
        arr[i], arr[max_ind] = arr[max_ind], arr[i]
    print(arr)



if __name__ == "__main__":
    arr = [7,2,4,5,7,9]
    # selection_sort(arr)
    selection_sort_des(arr)