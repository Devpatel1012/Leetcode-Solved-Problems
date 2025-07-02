class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0  # Edge case: empty needle is always found at index 0
        
        index = -1
        left = 0
        right = 0

        while left < len(haystack):
            if haystack[left] == needle[right]:
                if right == 0:
                    index = left  # Possible start index

                if right == len(needle) - 1:
                    return index  # Full needle matched

                left += 1
                right += 1
            else:
                if right > 0:
                    # If partial match failed, reset right and move left to index + 1
                    left = index + 1
                    index = -1
                    right = 0
                else:
                    left += 1

        return -1  # If not found
