from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all numbers to strings
        nums = list(map(str, nums))

        # Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join numbers
        result = "".join(nums)

        # Edge case: when all are zeros (e.g., [0,0])
        return "0" if result[0] == "0" else result
