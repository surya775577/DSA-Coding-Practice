class Solution:    
def findMajority(self, arr):        
      n=len(arr)        
      freq={}        
      res=[]                
      for num in arr:            
            freq[num]=freq.get(num,0)+1                
      for num,count in freq.items():            
            if count>n//3:                
            res.append(num)        
      return sorted(res
