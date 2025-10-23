class Solution(object):
    def triangleNumber(self, nums):
         # Brute-Force Approach
        # def is_valid_triangle(a, b, c):
        #     return (a + b > c) and (a + c > b) and (b + c > a)

        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if is_valid_triangle(nums[i], nums[j], nums[k]):
        #                 count += 1

        # return count

        # Optimized Version
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
        