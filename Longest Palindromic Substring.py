class Solution(object):
    def longestPalindrome(self, s):
        ans = ""
        lens = len(s)

        for i in range(lens):
            for j in range(i, lens):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    if len(substring) > len(ans):
                        ans = substring

        return ans


soul = Solution()
s = "amscbbcbbcbhv"
print("Final ans: " + soul.longestPalindrome(s))