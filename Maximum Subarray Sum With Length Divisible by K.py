class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # ans = 0
        # sublen = (len(nums) - (len(nums)%k))
        # nums.sort()
        # for i in range(sublen):
        #     ans += nums[-1]
        #     nums.pop()
        # return ans

        # n = len(nums)
        # sublen = (n- (n%k))
        # ans = 0
        # startpoint = nums[0]
        # endpoint = nums[0]
        # prefixsum = []
        # for i in range(1,n):
        #     s = nums[i]+startpoint
        #     if i>(sublen-1 ):
        #         s = s-endpoint
        #         endpoint = nums[i-(sublen-1)]
        #     startpoint = s
        #     if i<(sublen-1):
        #         continue
        #     prefixsum.append(s)
        # return max(prefixsum)

        prefix = [float('inf')]*k
        prefix[0] = 0
        res = float('-inf')
        total = 0

        for i,n in enumerate(nums):
            total += n
            lenght = i+1
            prefix_len = lenght%k
            res = max(res,total - prefix[prefix_len])
            prefix[prefix_len] = min(prefix[prefix_len],total)
        return res
