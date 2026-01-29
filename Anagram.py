class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
           return False
           
        freq = [0]*26
        
        for i in range(len(s1)):
            freq[ord(s1[i])-ord('a')]+=1
            freq[ord(s2[i])-ord('a')]-=1
            
        return all(count ==0 for count in freq)
