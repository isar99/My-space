# def merge_sort(arr):

def merge_sorted_arr(arr1, arr2):
    print(f"merging {arr1}, {arr2}")
    arr_sort = []
    i,j = 0,0
    num1,num2 = len(arr1),len(arr2)
    while i < num1 and j < num2:
        if arr1[i] <= arr2[j]:
            arr_sort.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            arr_sort.append(arr2[j])
            j+=1
    if i < num1:
        while i<num1:
            arr_sort.append(arr1[i])
            i+=1
    if j < num2:
        while j<num2:
            arr_sort.append(arr2[j])
            j+=1
    return arr_sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    arr1_sort = merge_sort(arr1)
    arr2_sort = merge_sort(arr2)
    return merge_sorted_arr(arr1_sort,arr2_sort)


if __name__ == "__main__":
    arr = [7,2,7,5,4,9,3]
    # merge_sort(arr)
    # arr1 = [1,2,3,4]
    # arr2 = [1,1,3,4,5,6,7]
    # merge_sorted_arr(arr1, arr2)
    print(merge_sort(arr))