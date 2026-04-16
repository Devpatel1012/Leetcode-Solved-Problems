class Solution(object):
    def solveQueries(self, nums, queries):
        hashmap = {}

        for i, val in enumerate(nums):
            hashmap.setdefault(val, []).append(i)

        n = len(nums)
        ans = [-1] * len(queries)

        for i, q in enumerate(queries):
            indices = hashmap[nums[q]]

            if len(indices) == 1:
                continue

            pos = self.binary(q, indices)

            left = float('inf')
            right = float('inf')

            if pos > 0:
                d = abs(indices[pos] - indices[pos - 1])
                left = min(d, n - d)

            if pos < len(indices) - 1:
                d = abs(indices[pos] - indices[pos + 1])
                right = min(d, n - d)

            if pos == 0:
                d = abs(indices[pos] - indices[-1])
                left = min(d, n - d)

            if pos == len(indices) - 1:
                d = abs(indices[pos] - indices[0])
                right = min(d, n - d)

            ans[i] = min(left, right)

        return ans

    def binary(self, val, arr):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

        return -1