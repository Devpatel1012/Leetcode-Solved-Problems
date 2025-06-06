class Solution(object):
    def myAtoi(self, s):
        if not (0 <= len(s) <= 200):
            return 0

        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 +-.")
        if any(char not in valid_chars for char in s):
            return 0

        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        no = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = 0
        for char in s:
            if char not in [str(num) for num in no]:
                break
            result = result * 10 + int(char)

        result *= sign

        # Clamp the result within the 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result


# Example usage
soul = Solution()
s = "-04a2"
ans = soul.myAtoi(s)
print(ans)  # Output: -42
print(type(ans))  # Output: <class 'int'>
