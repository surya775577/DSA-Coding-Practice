class Solution:
    def maxCircularSum(self, arr):
        # code here
        t=0
        max_ending = max_so_far = arr[0]
        min_ending = min_so_far = arr[0]
        
        for i, x in enumerate(arr):
            t+=x
            
            if i>0:
                max_ending = max(x,max_ending+x)
                max_so_far=max(max_so_far, max_ending)
                
                min_ending = min(x,min_ending+x)
                min_so_far=min(min_so_far, min_ending)
        if max_so_far < 0:
            return max_so_far
        return max(max_so_far, t-min_so_far)
