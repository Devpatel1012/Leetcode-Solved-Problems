class Solution:
    def romanToInt(self, num):

        if not (1 <= len(num) <= 15):
            raise ValueError("Input length must be between 1 and 15.")

        valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        if not set(num).issubset(valid_chars):
            raise ValueError(
                "Input must contain only valid Roman numeral characters: 'I', 'V', 'X', 'L', 'C', 'D', 'M'.")

        
        roman_to_value = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
            'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
            'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
        }

        i = 0
        number = 0
        while i < len(num):
            if i + 1 < len(num) and num[i:i + 2] in roman_to_value:
                number += roman_to_value[num[i:i + 2]]
                i += 2
            else:
                number += roman_to_value[num[i]]
                i += 1

        return number


soul = Solution()
x = "MCMXCIV"
print(soul.romanToInt(x))
