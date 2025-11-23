class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        if (total%3) == 0:
            return total

        # Groups of numbers by their remainder when divided by 3
        mod1 = []
        mod2 = []

        for num in nums:
            r = num % 3
            if r == 1:
                mod1.append(num)
            elif r == 2:
                mod2.append(num)

        # Sort so we can get smallest elements easily
        mod1.sort()
        mod2.sort()

        remainder = total % 3

        if remainder == 0:
            return total
        
        # Try removing smallest valid option
        remove_options = []

        if remainder == 1:
            # remove smallest mod1, OR remove two smallest mod2
            if len(mod1) >= 1:
                remove_options.append(mod1[0])
            if len(mod2) >= 2:
                remove_options.append(mod2[0] + mod2[1])

        elif remainder == 2:
            # remove smallest mod2, OR remove two smallest mod1
            if len(mod2) >= 1:
                remove_options.append(mod2[0])
            if len(mod1) >= 2:
                remove_options.append(mod1[0] + mod1[1])

        # If no valid removal possible → return 0
        if not remove_options:
            return 0

        return total - min(remove_options)