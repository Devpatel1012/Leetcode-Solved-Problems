class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tar = nums[0]
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     tar = max(tar,curr)
        #     for j in range(i+1,len(nums)):
        #         curr *= nums[j]
        #         tar = max(tar,curr)
        # return tar
        
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            if n < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(n, max_prod * n)
            min_prod = min(n, min_prod * n)

            result = max(result, max_prod)

        return result
