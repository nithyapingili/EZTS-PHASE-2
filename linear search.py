arr=[5,6,7,8,9]
key=7
found=False
for index in range(len(arr)):
    if arr[index]==key:
        print("element found:",index)
        found=True
        break
if found==False:
    print("element is not found")
