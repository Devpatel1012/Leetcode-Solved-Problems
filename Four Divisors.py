
class Solution(object):
    def sumFourDivisors(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(n)):
            a = int(sqrt(n[i]))
            factor = set()
            for j in range(1,a+1):
                
                if n[i]%j == 0:
                    factor.add(j)
                    factor.add(n[i]//j)

                if len(factor)>4:
                    break
            
            if len(factor) == 4:
                ans += sum(factor)
        return ans
                       
    
