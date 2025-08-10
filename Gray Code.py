class Solution(object):
    def grayCode(self, n):
        
        res = []
        for i in range(1 << n):  # 1 << n is 2^n
            res.append(i ^ (i >> 1))
        return res
        
        