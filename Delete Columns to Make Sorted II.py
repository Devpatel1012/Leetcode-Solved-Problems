class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        deletions = 0
        
        sorted_rows = [False] * (n - 1)
        
        for col in range(m):
            can_keep = True
            temp_sorted = sorted_rows[:]
            
            for row in range(n - 1):
                if not sorted_rows[row]:
                    if strs[row][col] > strs[row + 1][col]:
                        can_keep = False
                        break
                    elif strs[row][col] < strs[row + 1][col]:
                        temp_sorted[row] = True
            
            if not can_keep:
                deletions += 1
            else:
                sorted_rows = temp_sorted
        
        return deletions