class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:  # If it's a closing bracket
                # If stack is empty, no matching opening bracket found
                if not stack:
                    return False
                
                # Pop the top element from the stack
                top_element = stack.pop()
                
                # Check if the popped element matches the corresponding opening bracket
                if mapping[char] != top_element:
                    return False
            # If the character is not a bracket (e.g., a letter or number),
            # the problem statement implies only brackets are in the string,
            # so we can ignore this case or handle it as an invalid character.
            # For this problem, we assume only the specified characters are present.
                    
        # After iterating through the entire string, the stack should be empty
        # if all opening brackets have been correctly closed.
        return not stack