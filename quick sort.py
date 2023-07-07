def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left_arr=[i for i  in arr if i<pivot]
    right_arr=[i for i in arr if i>pivot]
    return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)
arr=[56,32,78,43,67,89]
answer=quick_sort(arr)
print("quick sort:",answer)
