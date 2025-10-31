class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        dupes = []
        for num in nums:
            if num in seen:
                dupes.append(num)
            else:
                seen.add(num)
        return dupes

        # count = Counter(nums)
        # return [num for num, freq in count.items() if freq > 1]