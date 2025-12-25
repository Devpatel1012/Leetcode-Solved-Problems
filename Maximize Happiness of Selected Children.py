class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse = True)
        ans = 0
        n = (len(happiness)-1)
       
        for i in range(k):
        
            ans+=happiness[i]
            if happiness[i]-i > 0:
                ans = ans-i
            else:
                ans-=happiness[i]
        
        return ans
      
