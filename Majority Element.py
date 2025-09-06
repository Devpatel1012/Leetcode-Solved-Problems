# from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # element_counts = Counter(nums)
        # ans = element_counts.most_common(1)
        # return ans[0][0]
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        # return key with maximum value
        return max(count, key=count.get)