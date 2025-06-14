class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] will store the number of ways to decode s[0...i-1]
        # dp array size will be n + 1
        dp = [0] * (n + 1)

        # Base Cases:
        # dp[0] = 1: Represents one way to decode an empty string (the starting point for valid decodings).
        dp[0] = 1

        # dp[1]: Ways to decode the first character s[0]
        # If s[0] is '0', it cannot be decoded alone, so 0 ways.
        # Otherwise, there's 1 way (as a single digit).
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        # Iterate from the second character (index 1 in s, which corresponds to dp[2])
        for i in range(2, n + 1):
            # Way 1: Decode s[i-1] as a single digit
            # Get the single digit at the current position (s[i-1])
            single_digit = int(s[i-1])

            # If the single digit is valid (between 1 and 9)
            if 1 <= single_digit <= 9:
                # Add the ways from the previous subproblem (excluding this single digit)
                dp[i] += dp[i-1]

            # Way 2: Decode s[i-2] and s[i-1] as a two-digit number
            # Get the two-digit number formed by s[i-2] and s[i-1]
            two_digits = int(s[i-2:i])

            # If the two-digit number is valid (between 10 and 26)
            if 10 <= two_digits <= 26:
                # Add the ways from the subproblem two steps back (excluding these two digits)
                dp[i] += dp[i-2]
        
        # The final answer is the number of ways to decode the entire string s
        return dp[n]