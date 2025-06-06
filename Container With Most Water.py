class Solution(object):
    def maxArea(self, height):
        lens = len(height)
        left = 0
        right = lens - 1
        area = 0

        while left < right:

            sample = (right - left) * min(height[left], height[right])
            print(sample)
            area = max(area, sample)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1


        print("area:", area)
        return area


soul = Solution()
a = [1,8,6,2,5,4,8,3,7]
print(soul.maxArea(a))



