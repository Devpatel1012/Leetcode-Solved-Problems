class Solution(object):
    def getDescentPeriods(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        a = 1
        pre =0
        for i in p:
            if ((pre)-1 == i):
                a+=1
                ans += a
            else:
                a = 1
                ans += 1
            pre = i
        
        return ans
