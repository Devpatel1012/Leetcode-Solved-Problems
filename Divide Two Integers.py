class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Edge case: overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        return -result if negative else result
