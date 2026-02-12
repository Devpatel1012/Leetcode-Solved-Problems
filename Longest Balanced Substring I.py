class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length=0
        n=len(s)
        for left in range (n):
            freq=[0]*26
            
            distinct=0
            max_freq=0
            for right in range (left,n):
                x=ord(s[right])-ord("a")
                if freq[x]==0:
                    distinct+=1
                freq[x]+=1
                max_freq=max(max_freq,freq[x])
                
                length=right-left+1
                if length==distinct*max_freq:
                    max_length=max(max_length,length)
        return max_length
            
            
        