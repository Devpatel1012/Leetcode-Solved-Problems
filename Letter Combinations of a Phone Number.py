class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # Handle empty input immediately
        if not digits:
            return []

       
        number_pad = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        result = []

        def backtrack(current_combination, next_digit_index):
            if next_digit_index == len(digits):
                result.append(current_combination)
                return

            digit = digits[next_digit_index]
            
            letters = number_pad[digit]
            print(current_combination)

            for letter in letters:
                
                backtrack(current_combination + letter, next_digit_index + 1)
                
    
        backtrack("", 0)

        return result

sol = Solution()

# Example 1
digits1 = "23"
ans  = sol.letterCombinations(digits1)
print(ans)