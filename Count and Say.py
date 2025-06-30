class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        result = "1"
        for i in range(1, n):
            current = ""
            count = 1
            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    current += str(count) + result[j - 1]
                    count = 1
            current += str(count) + result[-1]  
            result = current
        return result
