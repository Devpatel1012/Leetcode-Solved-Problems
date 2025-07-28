class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = []
        stack = []

        # Precompute the minimum character from i to end
        min_char_from = [''] * n
        min_char_from[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_char_from[i] = min(s[i], min_char_from[i + 1])

        for i in range(n):
            stack.append(s[i])
            # While top of stack is <= smallest future character, pop and append
            while stack and (i == n - 1 or stack[-1] <= min_char_from[i + 1]):
                result.append(stack.pop())

        return "".join(result)
