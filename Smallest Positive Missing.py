class Solution:
    def missingNumber(self, arr):
        n=len(arr)
        
        i=0
        while i<n:
            c_i=arr[i]-1
            if 1<=arr[i] <= n and arr[i] != arr[c_i]:
                arr[i], arr[c_i] = arr[c_i], arr[i]
            else:
                i+=1
                
        for i in range(n):
            if arr[i] != i+1:
                return i+1
                
        return n+1
