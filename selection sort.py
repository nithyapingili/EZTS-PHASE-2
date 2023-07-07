arr=[56,32,78,43,56,67,89]
for i in range(len(arr)):
    min_ind=i#initial value
    for j in range(i+1,len(arr)):
        arr[min_ind]>arr[j]
        min_ind=j#finding the min element index
    arr[i],arr[min_ind]=arr[min_ind],arr[i]#swapping the element with min element
print(arr)
