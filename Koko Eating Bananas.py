class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hours = sum((p + mid - 1) // mid for p in piles)
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1

        return left