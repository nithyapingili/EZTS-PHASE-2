arr=[56,32,78,43,67,39]
#insertion sort
for i in range(1,len(arr)):
    j=i
    while arr[j-1]>arr[j] and j>0:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)

#descending order sorting takes place
arr=[56,32,78,43,67,39]
#insertion sort
for i in range(1,len(arr)):
    j=i
    while arr[j-1]<arr[j] and j>0:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)
