class Solution:
	def maxProduct(self,arr):
		if not arr:
		    return 0
		    
		max_pro=min_pro=result=arr[0]
		
		for i in range(1,len(arr)):
		    current=arr[i]
		    
		    if current<0:
		        max_pro,min_pro = min_pro,max_pro
		    
		    max_pro = max(current,max_pro*current)
		    min_pro = min(current,min_pro*current)
		    
		    result=max(result,max_pro)
	    return result
