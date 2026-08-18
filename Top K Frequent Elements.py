from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        occur = Counter(nums)

        sorted_data = sorted(
            occur.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [key for key, value in sorted_data[:k]]
