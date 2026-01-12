class Solution(object):
    def minTimeToVisitAllPoints(self, p):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(1,len(p)):
            x1,y1 = p[i-1]
            x2,y2 = p[i]
            ans += max(abs(x1-x2),abs(y1-y2))
        return ans
        