class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []

        for i in range(len(str(low)), len(str(high)) + 1):
            first = int(''.join(str(x) for x in range(1, i + 1)))
            add = int('1' * i)

            while first % 10 != 0:
                if low <= first <= high:
                    ans.append(first)
                first += add

        return ans