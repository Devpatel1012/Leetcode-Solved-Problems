class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        ans = 1
        for i in range(1,len(complexity)):
            if complexity[i]<= complexity[0]:
                return 0
            ans = (ans*i)%(10**9+7)
        return ans
        

