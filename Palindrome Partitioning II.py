class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # results = []
        # n = len(s)

        # def isPalindrome(sub): 
        #     return sub == sub[::-1]

        # def backtrack(start_index, current_partition):
        #     if start_index == n:
        #         results.append(list(current_partition))
        #         return

        #     for i in range(start_index, n):
        #         substring = s[start_index : i + 1]
                
        #         if isPalindrome(substring):
        #             current_partition.append(substring)
        #             backtrack(i + 1, current_partition)
        #             current_partition.pop()

        # backtrack(0, [])
        
        # mini =  min(results, key=len)
        # l = len(mini)-1
        # return l
  
        n = len(s)
        dp = [i for i in range(n)]  # worst case: cut between every character

        for center in range(n):
            # Odd-length palindromes
            left, right = center, center
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left-1] + 1)
                left -= 1
                right += 1

            # Even-length palindromes
            left, right = center, center+1
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left-1] + 1)
                left -= 1
                right += 1
        print(dp)
        return dp[-1]



        