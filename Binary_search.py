def binary_search(arr,key):
    n=len(arr)
    low,high=0,n-1
    for i in range(low,high+1):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid 
        elif(arr[mid]<key):
            low=mid+1
        else:
            high=mid-1
    return -1
n=int(input())
arr=list(map(int,input().split()))
key=int(input())
print(binary_search(arr,key))