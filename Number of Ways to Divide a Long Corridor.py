class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        mod = 10**9+7
        s = 0
        p = 0
        w = 1

        for ch in corridor:

            if ch == 'S':
                s += 1
                if s>2 and s%2 == 1:
                    w = (w*(p+1))%mod
                    p = 0
            else:
                if s>=2 and s%2 == 0:
                    p += 1
        
        if s < 2 or s % 2 != 0:
            return 0

        return w