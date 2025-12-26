class Solution(object):
    def bestClosingTime(self, c):
        """
        :type customers: str
        :rtype: int
        """
        ms,s,ans = 0,0,0
        for i,ch in enumerate(c):
            s+=1 if ch == 'Y' else -1
            if s>ms:
                ms,ans = s,i+1

        return ans