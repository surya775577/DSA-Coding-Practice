    def rotateArr(self, arr, d):
        n=len(arr)
        d=d%n
        self.reverseArray(arr,0,d-1)
        self.reverseArray(arr,d,n-1)
        self.reverseArray(arr,0,n-1)
    def reverseArray(self,arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    n=int(input())
    arr=list(map(int,input().split()))
    d=int(input())  
    ob=Solution()
    ob.rotateArr(arr,d)
    