# __import__("atexit").register(lambda: open("display_runtime.txt","w").write("0"))

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
        
#         memo = {}
    
#         s1 = word1
#         s2 = word2


#         def edit_distance(i, j):
#     # If s1 is exhausted, insert remaining chars of s2

#             if (i,j) in memo:
#                 return memo[(i,j)]

#             if i == len(s1):
#                 return len(s2) - j
#             # If s2 is exhausted, delete remaining chars of s1
#             if j == len(s2):
#                 return len(s1) - i

#             if s1[i] == s2[j]:
#                 memo[(i,j)] = edit_distance(i+1, j+1)
#             else:
#                 memo[(i,j)] = 1 + min(
#                     edit_distance(i+1, j),     # delete
#                     edit_distance(i, j+1),     # insert
#                     edit_distance(i+1, j+1)    # replace
#                 )

#             return memo[(i,j)]

        

#         return edit_distance(0,0)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        # Create a DP table with dimensions (len1 + 1) x (len2 + 1)
        # dp[i][j] will store the minimum edit distance between
        # word1[0...i-1] and word2[0...j-1]
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Base cases:
        # If word1 is empty, dp[0][j] = j (cost of inserting j characters into word2)
        for j in range(len2 + 1):
            dp[0][j] = j
        
        # If word2 is empty, dp[i][0] = i (cost of deleting i characters from word1)
        for i in range(len1 + 1):
            dp[i][0] = i

        # Fill the DP table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # If characters match, no operation needed for this pair
                # Cost is inherited from the diagonal (previous subproblem)
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # If characters don't match, consider 3 operations:
                    # 1. Insert: dp[i][j-1] + 1 (insert word2[j-1] into word1)
                    # 2. Delete: dp[i-1][j] + 1 (delete word1[i-1] from word1)
                    # 3. Replace: dp[i-1][j-1] + 1 (replace word1[i-1] with word2[j-1])
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        
        # The bottom-right cell contains the minimum edit distance
        return dp[len1][len2]