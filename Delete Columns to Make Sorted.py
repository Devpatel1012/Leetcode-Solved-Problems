class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs[0])
        ans = 0
        check = ['A']*n
        for i in range(n):
            for j in range(len(strs)):

                if check[i]<=strs[j][i]:
                    check[i] = strs[j][i]
                else:
                    ans+=1
                    break

     
        return ans
    
    # we can use zip to runa loop per columns like this :
    # for c in zip(*strs):
    #     print(c)
        