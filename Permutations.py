from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_permutation = []
        
        n = len(nums)

        def backtrack():
            if len(current_permutation) == n:
                result.append(current_permutation[:]) 
                return

            for num in nums:
                if num not in current_permutation:
                    current_permutation.append(num)
                    backtrack()
                    current_permutation.pop()

        backtrack()
        
        return result