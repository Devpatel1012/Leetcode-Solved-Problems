class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # opt 1
        ans = 0
        for i in range(1,len(nums)):
            first = sum(nums[:i])
            second = sum(nums[i:])
            if (abs(first-second)%2) == 0:
                ans+=1
        return ans

        #opt2
        if sum(nums) % 2 : return 0
        return len(nums)-1