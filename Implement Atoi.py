class Solution:
    def myAtoi(self, s):
        i,n,sign,num = 0,len(s),1,0
        INT_MAX,INT_MIN = 2**31-1,-2**31
        
        while i<n and s[i] == ' ':
            i+=1
            
        if i<n and s[i] in '+-':
            sign =-1 if s[i]=='-' else 1
            i+=1
        while i<n and '0' <= s[i] <= '9':
            num = num*10 +(ord(s[i]) - ord('0'))
            if sign*num>INT_MAX:
                return INT_MAX
            if sign*num<INT_MIN:
                return INT_MIN
            i+=1
            
        return sign*num
            
