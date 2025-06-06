class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        result = []
        for i in range(length):
            num1 = nums[i]
            for j in range(i + 1, length):
                num2 = nums[j]
                if (num1 + num2) == target:
                    return [i, j] 
        return result


numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(numbers, target))