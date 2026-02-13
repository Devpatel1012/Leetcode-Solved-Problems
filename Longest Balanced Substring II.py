class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        n = len(s)
        
        for i in range(n):
            freq = [0] * 3
            freq[ord(s[i]) - ord('a')] += 1
            distinct = 1
            maxLen = max(maxLen, 1)
            for j in range(i + 1, n):
                ind = ord(s[j]) - ord('a')
                if freq[ind] == 0:
                    distinct+=1
                freq[ind] += 1
                val = set(freq)
                val.discard(0)
                
                if len(val) == 1:
                    maxLen = max(maxLen, sum(freq))
                    
        return maxLen