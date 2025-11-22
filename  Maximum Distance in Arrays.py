class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mi = [float('inf'),-1]
        mi1 = [float('inf'),-1]
        ma = [float('-inf'),-1]
        ma1 = [float('-inf'),-1]
        
        for j,i in enumerate(arrays):
            first = i[0]
            last = i[-1]

            if mi[0]>first:
                mi1 = mi
                mi = [first,j]
            elif mi1[0]>first:
                mi1 = [first,j]
            
            if ma[0]<last:
                ma1 = ma
                ma = [last,j]
            elif ma1[0]<last:
                ma1 = [last,j]
        
        if mi[1] != ma[1]:
            return abs(mi[0]-ma[0])
        
        return max(abs(mi[0]-ma1[0]),abs(mi1[0]-ma[0]))