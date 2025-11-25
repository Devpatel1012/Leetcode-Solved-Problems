class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k%2 == 0 and k%5 == 0:
            return -1
        
        remainder = 0
        for i in range(1,k+1):
            remainder = (remainder*10+1)%k
            if remainder == 0:
                return i
        return -1