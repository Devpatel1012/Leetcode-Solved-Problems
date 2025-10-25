class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        days = n % 7

        total = 0
        # Sum for complete weeks
        for i in range(weeks):
            total += 28 + i * 7  # 28 is 1+2+3+4+5+6+7

        # Sum for remaining days
        start = 1 + weeks
        for i in range(days):
            total += start + i

        return total