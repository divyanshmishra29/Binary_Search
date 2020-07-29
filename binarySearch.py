def binarySearch(arr,x):
    low=0
    high = len(arr)-1
    while low<=high:
        mid=(low+high)//2
        guess=arr[mid]
        if guess==x:
            return mid
        elif guess>x:
            high = mid-1
        else:
            low = mid+1
    return None
print(binarySearch([1,2,3,45,67,90],67))

