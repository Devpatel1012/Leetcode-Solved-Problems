
from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        inde = defaultdict(list)

        for i, val in enumerate(nums):
            inde[val].append(i)

        ans = [0] * len(nums)

        for key, val in inde.items():
            n = len(val)

            total = sum(val)   # compute once

            left_sum = 0

            for i in range(n):
                curr = val[i]

                # right sum = total - left_sum - curr
                right_sum_val = total - left_sum - curr

                left_count = i
                right_count = n - i - 1

                left = abs(left_sum - curr * left_count)
                right = abs(right_sum_val - curr * right_count)

                ans[curr] = left + right

                left_sum += curr   

        return ans