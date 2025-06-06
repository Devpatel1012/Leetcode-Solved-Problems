class Solution(object):
    def __init__(self):
        self.lists = {}

    def create_multiple_lists(self, numRows):
        for i in range(1, numRows + 1):
            self.lists['list_{}'.format(i)] = []

    def convert(self, s, numRows):
        if numRows <= 0:
            return "Number of rows must be greater than 0."
        if numRows == 1:
            return s

        self.create_multiple_lists(numRows)
        direction = 1
        row = 1

        for char in s:
            self.lists['list_{}'.format(row)].append(char)
            if row == numRows:
                direction = -1
            elif row == 1:
                direction = 1
            row += direction

        result = ''.join([''.join(self.lists['list_{}'.format(i)]) for i in range(1, numRows + 1)])
        return result

soul = Solution()
result = soul.convert("PAYPALISHIRING", 4)
print(result)