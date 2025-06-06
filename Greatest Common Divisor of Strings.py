class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Helper function to compute the GCD of two numbers
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        # Helper function to check if one string is a multiple of another
        def isMultiple(small, large):
            return large == small * (len(large) // len(small))
        
        # Compute GCD of lengths of the two strings
        len1, len2 = len(str1), len(str2)
        gcd_length = gcd(len1, len2)
        
        # Get the candidate substring which could be the GCD string
        candidate = str1[:gcd_length]
        
        # Check if the candidate is a divisor of both strings
        if isMultiple(candidate, str1) and isMultiple(candidate, str2):
            return candidate
        return ""