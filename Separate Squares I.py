class Solution(object):
    def separateSquares(self, s):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        l,r  = 0,2*1e9
        eps = 60

        while eps>0:
            mid = (l+r)/2.0
            areaA,areaB =0,0

            for square in s:
                b,slide = square[1],square[2]
                totalArea = slide * slide

                if mid <= b :
                    areaB += totalArea
                elif mid >=(slide+b):
                    areaA += totalArea
                else:
                    bottomarea = slide * (mid - b)
                    areaA += bottomarea
                    areaB += (totalArea - bottomarea)
            
            if areaA -areaB <0:
                l = mid
            else:
                r = mid
            eps -= 1
        
        return mid
