class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr

        # Case 1: Exclude last house
        case1 = rob_line(nums[:-1])

        # Case 2: Exclude first house
        case2 = rob_line(nums[1:])

        return max(case1, case2)

        ## At solving this problem you think about using the one external array fpr boolean value which indicate the usage of the 1's house and make then for the last dp element you have to make the logic for it like if the value of second last is true then use the Flase highest value + last house value and vice versa for other condition implement this if you checking it in futhure.
