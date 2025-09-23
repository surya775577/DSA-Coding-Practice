def move(arr):
    curr=0
    for num in nums:
        if num!=0:
            arr[curr]=num
            curr+=1
    while curr<len(arr):
        arr[curr]=0
        curr+=1
    return arr
n=int(input())
nums=list(map(int,input().split()))
print(move(nums))