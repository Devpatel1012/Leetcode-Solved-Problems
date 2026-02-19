class Solution(object):
    def countBinarySubstrings(self, s):
        ans = prev = 0
        cur = 1
       
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                ans += min(prev,cur)
                prev = cur
                cur = 1
            else:
                cur += 1
        ans += min(prev,cur)
        return ans
