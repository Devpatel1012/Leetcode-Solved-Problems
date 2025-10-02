class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen  = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digits)**2 for digits in str(n))
        
        return n == 1
        