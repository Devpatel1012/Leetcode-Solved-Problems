class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        MOD = 10**9 + 7
  
        a,b = 6,6

        for i in range(1,n):
            na = (2*a + 2*b)%MOD
            nb = (2*a + 3*b)%MOD
            a,b = na,nb

        return (a+b)%MOD



