class Solution:
	def addBinary(self, s1, s2):
		i,j = len(s1)-1, len(s2)-1
		carry =0
		result = []
		
		while i>=0 or j>=0 or carry:
		    total = carry 
		    if i>=0:
		        total += int(s1[i])
		        i-=1
		    if j>=0:
		        total +=int(s2[j])
		        j-=1
		    result.append(str(total%2))
		    carry = total//2
	    while len(result) > 1 and result[-1]=='0':
	        result.pop()
	        
	    return ''.join(reversed(result))
