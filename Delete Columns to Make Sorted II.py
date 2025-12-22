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
    
# class Solution(object):
#     def minDeletionSize(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: int
#         """
#         # print('HI')
#         n = len(strs)
#         m = len(strs[0])

#         status = [False]*(n-1)
#         unresolved = n-1
#         deleted = 0

#         for col in range(m):
#             if unresolved == 0:
#                 break
            
#             deletion = False

#             for row in range(n-1):
#                 if not status[row] and strs[row][col]>strs[row+1][col]:
#                     deletion = True
#                     break
            
#             if deletion:
#                 deleted += 1
#                 continue
            
#             for row in range(n-1):
#                 if not status[row] and strs[row][col]<strs[row+1][col]:
#                     status[row] = True
#                     unresolved -=1
        
#         return deleted
    
    # class Solution(object):
    # def minDeletionSize(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: int
    #     """
    #     # print('HI')
    #     n = len(strs)
    #     ans=0
    #     status = [float("-inf")]*(n-1)
    #     for i in range(len(strs[0])):
    #         for j in range(1,n):
    #             if i == 0:
    #                 if strs[j-1][i]<strs[j][i]:
    #                     status[j-1] = 1
    #                 elif strs[j-1][i]==strs[j][i]:
    #                     status[j-1] = 0
    #                 else:
    #                     status[j-1] = -1
    #                     ans +=1
    #             else:
    #                 if status[j-1] == 1:
    #                     continue
    #                 else:
    #                     if strs[j-1][i]<strs[j][i]:
    #                         status[j-1] = 1
    #                     elif strs[j-1][i] == strs[j][i]:
    #                         status[j-1] = 0
    #                     else:
    #                         status[j-1] = -1
    #                         ans +=1
    #     return ans
