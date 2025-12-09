class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9+7
        ans = 0        
        freq = Counter(nums)
        lf = dict()
        for key in nums:
            tar = key*2
            freq[key] -= 1
            lc = lf.get(tar,0)
            rc = freq.get(tar,0)
            ans += lc*rc
            lf[key] = lf.get(key,0)+1
        return (ans)%mod
