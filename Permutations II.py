from typing import List

class Solution:
    def permuteUnique(self, nums: List[List[int]]) -> List[List[int]]:
        result = []
        current_permutation = []
        n = len(nums)
        nums.sort() 
        visited = [False] * n 

        def backtrack():
            if len(current_permutation) == n:
                result.append(current_permutation[:])
                return

            for i in range(n):
                if visited[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                
                current_permutation.append(nums[i])
                visited[i] = True

                backtrack()

                visited[i] = False
                current_permutation.pop()

        backtrack()
        return result