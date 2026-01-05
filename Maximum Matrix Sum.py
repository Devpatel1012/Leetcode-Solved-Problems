class Solution(object):
    def maxMatrixSum(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans  = 0
        neg  = 0
        small = float('inf')
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]<0:
                    neg+=1
                n = abs(m[i][j])
                ans += n
                if n<small:
                    small = n
                
        if neg%2 == 1:
            return (ans - (2*small))
        
        return ans