def binary_search(arr,key,start,end):
    if start<=end:
        mid=(start+end)//2
        if key==arr[mid]:
            return mid
        elif key>arr[mid]:
            return binary_search(arr,key,mid+1,end)
        elif key<arr[mid]:
            return binary_search(arr,key,start,mid-1)
        else:
            return None
arr=[i for i in range(1,11)]
arr.sort()
key=7
res=binary_search(arr,key,0,len(arr)-1)
print(res)
