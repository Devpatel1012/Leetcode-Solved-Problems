class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        hFences.extend([1,m])
        vFences.extend([1,n])

        ans = 0
        dist  = set()
        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                dist.add(abs(hFences[j]-hFences[i]))

        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                val = abs(vFences[j]-vFences[i])
                if val in dist:
                    ans = max(ans,val)
        
        if ans == 0:
            return -1
        return (ans*ans)%(10**9+7)
            
           
  