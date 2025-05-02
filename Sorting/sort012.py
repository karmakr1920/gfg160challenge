def sort012(arr):
    # code here
    n = len(arr)
    low = 0
    high = n -1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        elif arr[mid] > 1:
            arr[high],arr[mid] = arr[mid],arr[high]
            high = high - 1
    return arr

print(sort012([0,1,2,2,1,1,0,0,0,0,2,2,1]))