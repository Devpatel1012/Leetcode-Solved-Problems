class Solution(object):
    def minimumDifference(self, nums, k):
   
        n = len(nums)
        if n == 1 or k == 1:
            return 0
        if n == 2 and k == 2:
            return abs(nums[0]-nums[1])
        nums.sort(reverse = True)
        ans = float("inf")
        for i in range(n-k+1):
            cur = nums[i:i+k]
            ans = min(ans,(cur[0]-cur[-1]))
        return ans

