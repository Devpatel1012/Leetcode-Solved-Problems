class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def binary(n):
            l = len(n)
            low = 0
            high = l-1
            neg = l
            while high>=low:
                mid = (low+high)//2
                if n[mid]<0:
                    neg = mid
                    high=mid-1
                else:
                    low= mid+1
            return l-neg
            


        ans = 0
        for i in grid:
            ans+=binary(i)
        return ans
