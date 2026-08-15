class Solution(object):
    def subarraySum(self, nums, k):
        
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        freq = {}
        ans = 0

        for p in prefix:
            ans += freq.get(p - k, 0)
            freq[p] = freq.get(p, 0) + 1

        return ans

    