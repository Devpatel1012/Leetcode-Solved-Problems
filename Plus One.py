class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        PlusOne = False
        n = len(digits)
        for i in range(n):
            current_digit = digits[n - 1 - i]
            if i == 0:  # Last digit (rightmost)
                if current_digit == 9:
                    result.append(0)
                    PlusOne = True
                else:
                    result.append(current_digit + 1)
            else:
                if PlusOne:
                    if current_digit == 9:
                        result.append(0)
                    else:
                        result.append(current_digit + 1)
                        PlusOne = False
                else:
                    result.append(current_digit)
        if PlusOne:
            result.append(1)
        return result[::-1]


class Solution(object):
    def plusOne(self, d):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(d)-1

        while i>=0:
            if d[i]<9:
                d[i] += 1
                return d
            else:
                d[i] = 0
            i = i-1
        return [1]+d
