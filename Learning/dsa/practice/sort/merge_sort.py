def merge_sorted(arr1, arr2):
    new_arr = []
    i,j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i+=1
        else:
            new_arr.append(arr2[j])
            j+=1
    if i < len(arr1):
        new_arr.extend(arr1[i:])
    elif j < len(arr2):
        new_arr.extend(arr2[j:])
    return new_arr



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    left = merge_sort(arr1)
    right = merge_sort(arr2)
    return merge_sorted(left, right)




if __name__ == "__main__":
    arr = [54,33,73,89,54,21,90]
    print(merge_sort(arr))