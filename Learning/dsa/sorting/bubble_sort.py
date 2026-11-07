def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)



if __name__ == "__main__":
    arr = [7,2,7,5,4,9]
    bubble_sort(arr)