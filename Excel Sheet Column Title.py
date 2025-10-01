class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = []
        while columnNumber > 0:
            columnNumber -= 1   # shift because A=1, not 0
            remainder = columnNumber % 26
            res.append(chr(remainder + ord('A')))
            columnNumber //= 26

        return "".join(reversed(res))
        