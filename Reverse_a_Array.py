def reverse(arr):
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
n=int(input())
arr=list(map(int,input().split()))
print(reverse(arr))
